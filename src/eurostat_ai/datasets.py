
from typing import List, Tuple
import pandas as pd
from .api import fetch_jsonstat
from .jsonstat import jsonstat_to_dataframe
from .config import EU, UNIT, SIZE_ALL, TECH_CODES, PURPOSE_CODES

def get_ai_overall_timeseries(geo: str = EU, years: List[int] = (2023, 2024)) -> pd.DataFrame:
    js = fetch_jsonstat("isoc_eb_ai", {"indic_is":"E_AI_TANY","size_emp":SIZE_ALL,"unit":UNIT,"geo":geo,"time":list(years)})
    df = jsonstat_to_dataframe(js).rename(columns={"time":"year"})
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    return df[["geo","geo_label","year","value"]].sort_values(["geo","year"])

def get_ai_by_size(geo: str = EU, year: int = 2024) -> pd.DataFrame:
    js = fetch_jsonstat("isoc_eb_ai", {"indic_is":"E_AI_TANY","size_emp":["10-49","50-249","GE250"],"unit":UNIT,"geo":geo,"time":year})
    df = jsonstat_to_dataframe(js)
    df["year"] = pd.to_numeric(df["time"], errors="coerce")
    return df[["geo","geo_label","size_emp","size_emp_label","year","value"]].sort_values("value", ascending=False)

def get_ai_by_sector(geo: str = EU, year: int = 2024, top_n: int = 10) -> pd.DataFrame:
    js = fetch_jsonstat("isoc_eb_ain2", {"indic_is":"E_AI_TANY","size_emp":SIZE_ALL,"unit":UNIT,"geo":geo,"time":year})
    df = jsonstat_to_dataframe(js)
    if "nace_r2_label" in df.columns:
        df = df[~df["nace_r2_label"].str.contains("All activities", na=False)]
    return df[["nace_r2","nace_r2_label","value"]].sort_values("value", ascending=False).head(top_n)

def get_ai_countries(year: int = 2024, top: int = 12, bottom: int = 12):
    js = fetch_jsonstat("isoc_eb_ai", {"indic_is":"E_AI_TANY","size_emp":SIZE_ALL,"unit":UNIT,"time":year,"geoLevel":"country"})
    df = jsonstat_to_dataframe(js)
    df = df[~df["geo"].isin(["EU27_2020","EA"])]
    rank = df.sort_values("value", ascending=False).reset_index(drop=True)
    return rank.head(top), rank.tail(bottom)

def get_ai_by_technology(geo: str = EU, year: int = 2024) -> pd.DataFrame:
    js = fetch_jsonstat("isoc_eb_ai", {"indic_is":TECH_CODES,"size_emp":SIZE_ALL,"unit":UNIT,"geo":geo,"time":year})
    df = jsonstat_to_dataframe(js)
    return df[["indic_is","indic_is_label","value"]].sort_values("value", ascending=False)

def get_ai_purpose_by_sector(geo: str = EU, year: int = 2024) -> pd.DataFrame:
    js = fetch_jsonstat("isoc_eb_ain2", {"indic_is":PURPOSE_CODES,"size_emp":SIZE_ALL,"unit":UNIT,"geo":geo,"time":year})
    df = jsonstat_to_dataframe(js)
    wid = (df[["nace_r2_label","indic_is_label","value"]].pivot_table(index="nace_r2_label", columns="indic_is_label", values="value").sort_index()).reset_index()
    return wid
