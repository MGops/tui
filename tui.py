from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Label, Tree
from textual.widget import Widget
from textual.containers import Vertical, Container


class PtList(Tree):

    def compose(self):
        #yield Tree("Patients")
        tree: Tree[dict] = Tree("Patients")
        tree.root.expand()
        names = tree.root.add("Names", expand=True)
        names.add("John Doe")
        names.add("Jane Doe")
        yield tree


class Sidebar(Widget):

    CSS_PATH = 'tui.tcss'

    def compose(self):
        with Vertical():
            yield PtList("Patients")
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
        yield Static("Box1", classes="box", id='box1')
        yield Static("Box2", classes="box", id='box2')
        yield Static("Box3", classes="box", id='box3')
        yield Static("Box4", classes="box", id='box4')
        yield Static("Box5", classes="box", id='box5')
        yield Footer()
        

    def action_toggle_sidebar(self):
        self.query_one(Sidebar).toggle_class("-hidden")


if __name__ == '__main__':
    Dashboard().run()