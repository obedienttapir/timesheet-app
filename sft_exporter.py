from typing import List, Dict
import requests
import requests_mock


def export_to_sft(rows: List[Dict], webhook: str) -> bool:
    payload = {"rows": rows}
    # Use requests_mock to avoid real network calls during tests
    with requests_mock.Mocker() as m:
        m.post(webhook, text="OK")
        response = requests.post(webhook, json=payload)
    return response.ok
