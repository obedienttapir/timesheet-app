from pathlib import Path
from jira_client import JiraClient


def test_jira_client_parses_worklogs():
    fixture = Path('tests/fixtures/worklogs_week24.json')
    client = JiraClient(fixture)
    logs = client.get_worklogs('2025-W24')
    assert len(logs) == 3
    days = {log['day'] for log in logs}
    assert '2025-06-02' in days
