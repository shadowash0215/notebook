import html
import re


STATEMENT_RE = re.compile(
    r'^(?P<indent>[ \t]*)!!!(?:[ \t]+numbered-|[ \t]+\+|\+)[ \t]*'
    r'(?P<kind>theorem|lemma|corollary|definition|remark)'
    r'(?:[ \t]+"(?P<title>[^"]*)")?'
    r'(?:[ \t]+\{#(?P<label>[^}\n]+)\})?[ \t]*$',
    re.MULTILINE,
)

REFERENCE_RE = re.compile(r"\\adref\{(?P<label>[^}\n]+)\}")

LABELS = {
    "theorem": "定理",
    "lemma": "引理",
    "corollary": "推论",
    "definition": "定义",
    "remark": "注",
}

ADMONITION_TYPES = {
    "theorem": "note",
    "lemma": "success",
    "corollary": "success",
    "definition": "info",
    "remark": "tip",
}


def normalize_label(label):
    label = re.sub(r"\s+", "-", label.strip())
    label = re.sub(r"[^A-Za-z0-9_.:-]+", "-", label)
    return label.strip("-")


def on_page_markdown(markdown, page, config, files, **kwargs):
    counters = {kind: 0 for kind in LABELS}
    references = {}

    def replace_statement(match):
        kind = match.group("kind")
        counters[kind] += 1

        indent = match.group("indent")
        label = LABELS[kind]
        title = html.escape(match.group("title") or label, quote=True)
        number = counters[kind]
        raw_label = match.group("label")
        raw_label = raw_label.strip() if raw_label else None
        label_suffix = normalize_label(raw_label) if raw_label else str(number)
        anchor = f"{kind}-{label_suffix}"
        heading = f"{label} {number}" if title == label else f"{label} {number}：{title}"

        reference = raw_label or anchor
        reference_value = (anchor, f"{label} {number}")
        references[reference] = reference_value
        if raw_label:
            references[normalize_label(raw_label)] = reference_value

        return (
            f'{indent}<span id="{anchor}"></span>\n'
            f'{indent}!!! {ADMONITION_TYPES[kind]} "{heading}"'
        )

    markdown = STATEMENT_RE.sub(replace_statement, markdown)

    def replace_reference(match):
        label = match.group("label").strip()
        reference = references.get(label)
        if reference is None:
            reference = references.get(normalize_label(label))
        if reference is None:
            return match.group(0)
        anchor, text = reference
        return f'<a href="#{html.escape(anchor, quote=True)}">{text}</a>'

    return REFERENCE_RE.sub(replace_reference, markdown)
