
import json
from eurostat_ai.jsonstat import jsonstat_to_dataframe

def test_jsonstat_parses_sparse_mapping():
    from pathlib import Path
    js = json.loads(Path('tests/fixtures/sample_isoc_eb_ai.json').read_text())
    df = jsonstat_to_dataframe(js)
    assert 'value' in df.columns
    assert df.shape[0] == 2
    assert set(df['time']) == {'2023','2024'}
