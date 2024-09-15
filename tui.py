from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button
from textual.containers import Container
from textual.events import Key

class Sidebar(Container):
    pass


class Dashboard(App):

    BINDINGS = [
        ('Q', 'quit', 'Quit'),
        ("ctrl+s", "toggle_sidebar", "Toggle sidebar")
    ]

    CSS_PATH = 'tui.tcss'

    def compose(self):
        yield Header(show_clock=True)
        yield Sidebar(classes='-hidden')
        #yield Button("Medications")
        yield Footer()

    def action_toggle_sidebar(self):
        self.query_one(Sidebar).toggle_class("-hidden")

if __name__ == '__main__':
    Dashboard().run()