import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"©️ 2024-{datetime.date.today().year} Julian Millen.",
            href="https://www.linkedin.com/in/julianmillen/",
            is_external=True
            
        ),
        rx.text("Aprendiendo y creando software con ❤️ de Paraná hacia el mundo.")
    )