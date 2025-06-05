from aggregator import aggregate_worklogs


def test_aggregate_worklogs():
    logs = [
        {'day': '2025-06-02', 'charge': 'CN123', 'hours': 2},
        {'day': '2025-06-02', 'charge': 'CN123', 'hours': 1},
        {'day': '2025-06-03', 'charge': 'CN456', 'hours': 4}
    ]
    result = aggregate_worklogs(logs)
    assert ('2025-06-02', 'CN123', 3) in result
    assert ('2025-06-03', 'CN456', 4) in result
