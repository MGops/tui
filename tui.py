from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label
from textual.widget import Widget
from textual.containers import Vertical
from textual.events import Key

class Sidebar(Widget):


    CSS_PATH = 'tui.tcss'


    def compose(self):
        with Vertical():
            yield Label ('Main Menu')
            yield Button("Patient List")
            yield Button("Medications")


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