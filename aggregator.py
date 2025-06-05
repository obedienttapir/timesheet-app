from collections import defaultdict
from typing import List, Dict, Tuple


def aggregate_worklogs(worklogs: List[Dict]) -> List[Tuple[str, str, float]]:
    """Aggregate worklogs by day and charge number."""
    totals = defaultdict(float)
    for wl in worklogs:
        key = (wl['day'], wl['charge'])
        totals[key] += wl['hours']
    return [(day, charge, hours) for (day, charge), hours in sorted(totals.items())]
