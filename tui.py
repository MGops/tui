from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, Input, Static
from textual.widget import Widget
from textual.containers import Vertical, Container


class Sidebar(Widget):


    CSS_PATH = 'tui.tcss'


    def compose(self):
        with Vertical():
            yield Label ('Main Menu')
            #yield Input(placeholder="Initials")
            yield Button("Patient List")
            yield Button("Medications")
            yield Button("MHA")


class Dashboard(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("s", "toggle_sidebar", "Toggle sidebar")
    ]

    CSS_PATH = 'tui.tcss'

    def compose(self):
        yield Sidebar(classes='-hidden')
        yield Header(show_clock=True)
        yield Static("Box1", classes="box", id="box1")
        yield Footer()
        

    def action_toggle_sidebar(self):
        self.query_one(Sidebar).toggle_class("-hidden")


if __name__ == '__main__':
    Dashboard().run()