import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Mis redes sociales: "),
        link_button("X ",
                    "Mi perfil de X ",
                    "https://x.com/julianmillenn"),
        link_button("Linkedin ",
                    "Mi perfil profesional de linkdin ",
                    "https://www.linkedin.com/in/julianmillen/"),
        link_button("Github ",
                    "Mi Perfil en donde subo proyectos y practicas ",
                    "https://github.com/juliMillen"),
        width = "100%"
    )