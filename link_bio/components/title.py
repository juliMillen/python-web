import reflex as rx
import link_bio.styles.styles as styles

def title(title:str) -> rx.Component:
    return rx.heading(
        title,
        size="md",
        style= styles.title_style
    )