import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Julian Millen",fallback="JM", size="4"),
        rx.text("@julianmillen"),
        rx.text("HOLA 👋🏻 MI NOMBRE ES JULIAN MILLEN"),
        rx.text("""Soy Programador desde hace unos años. 
                Actualmente me encuentro terminando la carrera de programacion. 
                Ademas, estoy realizando cursos en internet sobre programacion
                Aqui veras una web creada en reflex. ¡BIENVENID@!"""),

    )