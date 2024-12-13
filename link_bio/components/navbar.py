import reflex as rx
from link_bio.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "millendev"
        ),
        position="sticky",
        bg="lightgray",
        padding_X=Size.DEFAULT.value,
        padding_Y=Size.DEFAULT.value,
        z_index="999",
        top="0"
        )