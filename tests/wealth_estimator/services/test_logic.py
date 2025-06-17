from pathlib import Path
from wealth_estimator.services.logic import find_top_matches
import json

def test_find_top_matches_happy_path():
    with open(Path('tests/test_data/warren_buffett.json'), "r") as expected_results: 
        warren_buffett_embedding = json.loads(expected_results.read())
        matches, estimated_wealth = find_top_matches(warren_buffett_embedding['warren_buffett']['embedding'], top_n_similar=2)
        expected_results = {
            "estimated_net_worth": 134964189446, # Weighted average of the net worths of the 2 matches below, weighted by similarity 
            "top_matches": [
                {"name": "warren_buffett", "similarity": 0.9351}, 
                {"name": "bill_gates", "similarity": 0.8679}
            ]
        }
        assert matches == expected_results['top_matches']
        assert estimated_wealth == expected_results['estimated_net_worth']

def test_find_top_matches_no_embedding():
    matches, estimated_wealth = find_top_matches([], top_n_similar=3)
    assert matches == []
    assert estimated_wealth is None