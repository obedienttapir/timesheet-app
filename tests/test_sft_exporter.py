from sft_exporter import export_to_sft


def test_export_to_sft(monkeypatch):
    rows = [{'day': '2025-06-02', 'charge': 'CN123', 'hours': 3}]
    # No actual network call will be made; route is stubbed in exporter
    assert export_to_sft(rows, 'https://example.com/sft/import')
