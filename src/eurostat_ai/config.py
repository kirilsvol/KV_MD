
from pathlib import Path
BASE_URL = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{dataset}"
OUTPUT_DIR = Path("output"); OUTPUT_DIR.mkdir(exist_ok=True)
EU = "EU27_2020"
UNIT = "PC_ENT"
SIZE_ALL = "GE10"
DEFAULT_YEARS = [2023, 2024]
TECH_CODES = ["E_AI_TTM","E_AI_TSR","E_AI_TNLG","E_AI_TIR","E_AI_TML","E_AI_TPA","E_AI_TAR"]
PURPOSE_CODES = ["E_AI_PMS","E_AI_PPP","E_AI_PBAM","E_AI_PLOG","E_AI_PITS","E_AI_PFIN","E_AI_PRDI"]
