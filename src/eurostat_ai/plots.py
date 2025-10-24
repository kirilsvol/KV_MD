
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from .config import OUTPUT_DIR

def save_bar(df: pd.DataFrame, x: str, y: str, title: str, fname: str, output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(exist_ok=True)
    plt.figure(figsize=(8,5))
    plt.bar(df[x], df[y])
    plt.xticks(rotation=30, ha="right")
    plt.title(title); plt.ylabel(y)
    plt.tight_layout(); plt.savefig(output_dir / fname, dpi=200); plt.close()

def save_barh(df: pd.DataFrame, x: str, y: str, title: str, fname: str, output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(exist_ok=True)
    plt.figure(figsize=(9,6))
    plt.barh(df[y], df[x])
    plt.gca().invert_yaxis()
    plt.title(title); plt.xlabel(x)
    plt.tight_layout(); plt.savefig(output_dir / fname, dpi=200); plt.close()

def save_lines(df: pd.DataFrame, x: str, y: str, group: str, title: str, fname: str, output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(exist_ok=True)
    plt.figure(figsize=(8,5))
    for key, g in df.groupby(group):
        plt.plot(g[x], g[y], marker="o", label=str(key))
    plt.title(title); plt.xlabel(x); plt.ylabel(y); plt.legend()
    plt.tight_layout(); plt.savefig(output_dir / fname, dpi=200); plt.close()

def save_heatmap_like(df_wide: pd.DataFrame, row: str, title: str, fname: str, output_dir: Path = OUTPUT_DIR):
    output_dir.mkdir(exist_ok=True)
    rows = df_wide[row].tolist()
    vals = df_wide.drop(columns=[row]).to_numpy(dtype=float)
    plt.figure(figsize=(max(8, len(rows)*0.3), 8))
    plt.imshow(vals, aspect="auto")
    plt.colorbar(label="Percentage of enterprises")
    plt.yticks(ticks=np.arange(len(rows)), labels=rows)
    plt.xticks(ticks=np.arange(df_wide.shape[1]-1), labels=df_wide.columns[1:], rotation=30, ha="right")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_dir / fname, dpi=220)
    plt.close()
