
from typing import Any, Dict
import requests
from .config import BASE_URL

def fetch_jsonstat(dataset: str, params: Dict[str, Any]) -> Dict[str, Any]:
    url = BASE_URL.format(dataset=dataset)
    params = {k: v for k, v in params.items() if v is not None}
    params.setdefault("lang", "EN")
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    return r.json()
