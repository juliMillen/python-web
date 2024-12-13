import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Julian Millen",fallback="JM", size="xl"),
            rx.vstack(
                rx.heading("Julian Millen",
                           size="lg"),
                rx.text("@julianmillen",
                        margin_top="0px !import"
                        )
            )
        ),
        rx.text("""Soy Programador desde hace unos años. 
                Actualmente me encuentro terminando la carrera de programacion. 
                Ademas, estoy realizando cursos en internet sobre programacion
                Aqui veras una web creada en reflex. ¡BIENVENID@!"""),
        align_items="start"
    )