import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "millendev",
            height="40px"
        ),
        position="sticky",
        bg="blue",
        padding_X="16px",
        padding_Y="8px",
        z_index="999"
        )