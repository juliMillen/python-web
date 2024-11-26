import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("X","https://x.com/julianmillenn"),
        link_button("Linkedin","https://www.linkedin.com/in/julianmillen/"),
        link_button("Github","https://github.com/juliMillen"),
    )