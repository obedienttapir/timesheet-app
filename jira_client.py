import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict


class JiraClient:
    def __init__(self, fixture_path: Path):
        self.fixture_path = fixture_path

    def get_worklogs(self, week: str) -> List[Dict]:
        """Return list of {'day': date, 'charge': str, 'hours': float}"""
        data = json.loads(self.fixture_path.read_text())
        worklogs = []
        for issue in data['issues']:
            for wl in issue['fields']['worklog']['worklogs']:
                started = datetime.fromisoformat(wl['started'].replace('Z', '+00:00'))
                day = started.date().isoformat()
                charge = issue['fields'].get('customfield_charge', 'UNKNOWN')
                hours = wl['timeSpentSeconds'] / 3600
                worklogs.append({'day': day, 'charge': charge, 'hours': hours})
        return worklogs
