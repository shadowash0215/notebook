import os
import re
import logging

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files

from utils.env_renderer import MathenvRenderer
from utils.markdown_utils import (
    replace_indented_block_start_with_options,
    get_indentation_level,
)

enabled = os.getenv("TIKZ", "1") == "1" or os.getenv("FULL", "0") == "true"
logger = logging.getLogger("mkdocs.hooks.mathenv")

if enabled:
    logger.info("hook - mathenv is loaded and enabled")
else:
    logger.info("hook - mathenv is disabled")

CACHE = True


def on_page_markdown(
    markdown: str, page: Page, config: MkDocsConfig, files: Files, **kwargs
) -> str:
    if not enabled:
        return markdown

    def _replace_mathenv(matched: re.Match) -> str:
        options = matched.group("options")
        contents = matched.group("contents")
        zoom = matched.group("zoom")
        first_line_indentation_level = get_indentation_level(matched.group("contents"))

        # print(first_line_indentation_level)

        contents = [i for i in contents.splitlines()]

        contents_remain = []

        for idx, i in enumerate(contents):
            if get_indentation_level(i) < first_line_indentation_level:
                contents_remain = contents[idx:]
                contents = contents[:idx]
                break

        contents = "\n".join(contents)
        mathenv = MathenvRenderer(options, contents)

        # The string should not be splitted into lines, since markdown parser won't recognize it
        svg_str = "".join(
            mathenv.write_to_svg(CACHE)
            .replace("<?xml version='1.0' encoding='UTF-8'?>", "")
            .splitlines()
        )

        # bolden the stroke
        svg_str = svg_str.replace("stroke-width='0.6'", "stroke-width='0.7'")
        svg_str = svg_str.replace("stroke='none'", "stroke='#000' stroke-width='0.2'")

        return (
            matched.group("leading")
            + f'<div style="text-align: center; zoom: {zoom if zoom else "1.5"};">{svg_str}</div>'
            + "\n"
            + "\n".join(contents_remain)
        )

    markdown = replace_indented_block_start_with_options(
        r"(?<!\\)\\tikzcd", _replace_mathenv, markdown
    )
    markdown = re.sub(r"\\\\tikzcd", r"\\tikzcd", markdown)

    return markdown