import re
from html import escape

ANCHOR_RE = re.compile(
    r"^(?P<indent>[ \t]*)@anchor[ \t]+(?P<id>[A-Za-z][\w:.-]*)[ \t]*$",
    re.MULTILINE,
)


def on_page_markdown(markdown, page, config, files, **kwargs):
    def replace_anchor(match):
        indent = match.group("indent")
        anchor_id = escape(match.group("id"), quote=True)
        return f'{indent}<span id="{anchor_id}"></span>'

    return ANCHOR_RE.sub(replace_anchor, markdown)