import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer

class State(rx.State):         #clase State maneja los estados
    pass

def index() -> rx.components:                #Definicion de componente
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )


app = rx.App()
app.add_page(index)
app._compile()