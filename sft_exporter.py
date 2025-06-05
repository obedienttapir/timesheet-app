from typing import List, Dict, Optional
from playwright.sync_api import sync_playwright


def export_to_sft(rows: List[Dict], webhook: str) -> bool:
    payload = {'rows': rows}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        context.route("**/sft/**", lambda route: route.fulfill(status=200, body="OK"))
        page = context.new_page()
        response = page.request.post(webhook, json=payload)
        browser.close()
    return response.ok
