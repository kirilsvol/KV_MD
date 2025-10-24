
from typing import Dict, List
import numpy as np
import pandas as pd

def jsonstat_to_dataframe(js: Dict) -> pd.DataFrame:
    ids: List[str] = js["id"]
    sizes: List[int] = js["size"]
    dims = js["dimension"]
    code_lists, label_maps = {}, {}
    for dim in ids:
        cat = dims[dim]["category"]
        index = cat.get("index", {})
        ordered = [k for k,_ in sorted(index.items(), key=lambda kv: kv[1])] if index else list(cat.get("label", {}).keys())
        code_lists[dim] = ordered
        label_maps[dim] = cat.get("label", {})
    N = int(np.prod(sizes))
    vals = np.full(N, np.nan, dtype=float)
    for k, v in js.get("value", {}).items():
        try: vals[int(k)] = float(v)
        except Exception: pass
    coords = np.unravel_index(np.arange(N), tuple(sizes), order="C")
    data = {}
    for i, dim in enumerate(ids):
        codes = code_lists[dim]; idx_arr = coords[i]
        data[dim] = [codes[j] if j < len(codes) else None for j in idx_arr]
        data[f"{dim}_label"] = [label_maps[dim].get(c, c) if c else None for c in data[dim]]
    df = pd.DataFrame(data)
    df["value"] = vals
    return df.dropna(subset=["value"]).reset_index(drop=True)
