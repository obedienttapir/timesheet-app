from pathlib import Path
from jira_client import JiraClient
from aggregator import aggregate_worklogs
from main import WorklogApp


def test_ui_renders_rows():
    fixture = Path('tests/fixtures/worklogs_week24.json')
    client = JiraClient(fixture)
    rows = aggregate_worklogs(client.get_worklogs('2025-W24'))
    app = WorklogApp(rows, 'https://example.com')
    async def run():
        async with app.run_test() as pilot:
            await pilot.pause()
    import asyncio
    asyncio.run(run())
    assert len(rows) == 3
