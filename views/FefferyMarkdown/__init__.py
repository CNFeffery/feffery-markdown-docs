from dash.dependencies import Component
import feffery_markdown_components as fmc

from . import intro, demos
from components import doc_layout


def render() -> Component:
    return doc_layout.render(
        component=fmc.FefferyMarkdown,
        intro=intro.render(),
        demos=demos.render(component=fmc.FefferyMarkdown),
        catalog=demos.demos_config,
    )
