
import requests_mock
from eurostat_ai.api import fetch_jsonstat

def test_fetch_jsonstat_ok():
    with requests_mock.Mocker() as m:
        url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_eb_ai"
        m.get(url, json={"ok": True})
        res = fetch_jsonstat("isoc_eb_ai", {})
        assert res["ok"] is True
