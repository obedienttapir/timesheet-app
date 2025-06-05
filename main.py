import argparse
import configparser
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.reactive import reactive
from textual.containers import Container
from rich.table import Table
from rich.live import Live
from rich.console import Console
from jira_client import JiraClient
from aggregator import aggregate_worklogs
from sft_exporter import export_to_sft

CONFIG_FILE = Path("config.txt")


def load_config() -> configparser.ConfigParser:
    parser = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        parser.read(CONFIG_FILE)
    return parser


class WorklogApp(App):
    CSS_PATH = None
    rows = reactive([])

    def __init__(self, rows, webhook):
        super().__init__()
        self.rows = rows
        self.webhook = webhook

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container()
        yield Footer()

    def on_mount(self) -> None:
        self.refresh_table()

    def refresh_table(self):
        table = Table()
        table.add_column("Day", style="cyan")
        table.add_column("Charge #", style="yellow")
        table.add_column("Hours", justify="right")
        daily_total = 0
        for day, charge, hours in self.rows:
            table.add_row(day, charge, f"{hours:.2f}")
            daily_total += hours
        table.add_row("--", "Total", f"{daily_total:.2f}")
        console = Console()
        console.clear()
        with Live(table, refresh_per_second=4):
            pass

    def key_e(self):
        export_to_sft([{'day': d, 'charge': c, 'hours': h} for d, c, h in self.rows], self.webhook)

    def key_w(self):
        self.key_e()

    def key_r(self):
        self.refresh_table()

    def key_q(self):
        self.exit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--week', default='current')
    args = parser.parse_args()

    config = load_config()
    fixture = Path('tests/fixtures/worklogs_week24.json')
    client = JiraClient(fixture)
    worklogs = client.get_worklogs(args.week)
    rows = aggregate_worklogs(worklogs)
    webhook = config.get('sft', 'webhook', fallback='https://sft.example.com')
    app = WorklogApp(rows, webhook)
    app.run()


if __name__ == '__main__':
    main()
