
from pathlib import Path
import pandas as pd
import click
from . import datasets as ds
from .plots import save_bar, save_barh, save_lines, save_heatmap_like
from .config import OUTPUT_DIR, EU

@click.group()
def cli():
    """Eurostat AI data CLI (Codespaces-ready)."""

@cli.command()
@click.option('--geo', default=EU, show_default=True)
@click.option('--years', multiple=True, type=int, default=[2023, 2024], show_default=True)
@click.option('--outdir', default=str(OUTPUT_DIR), show_default=True)
def timeseries(geo, years, outdir):
    outdir = Path(outdir); outdir.mkdir(exist_ok=True)
    df = ds.get_ai_overall_timeseries(geo=geo, years=list(years))
    df.to_csv(outdir / "eu_timeseries.csv", index=False)
    save_lines(df, x="year", y="value", group="geo_label",
               title=f"{geo}: enterprises using ≥1 AI (%, {min(years)}–{max(years)})",
               fname="eu_timeseries.png", output_dir=outdir)

@cli.command()
@click.option('--geo', default=EU, show_default=True)
@click.option('--year', default=2024, type=int, show_default=True)
@click.option('--outdir', default=str(OUTPUT_DIR), show_default=True)
def size(geo, year, outdir):
    outdir = Path(outdir); outdir.mkdir(exist_ok=True)
    df = ds.get_ai_by_size(geo=geo, year=year)
    df.to_csv(outdir / "eu_by_size_2024.csv", index=False)
    save_bar(df, x="size_emp_label", y="value",
             title=f"{geo}: AI adoption by size ({year})",
             fname="eu_by_size_2024.png", output_dir=outdir)

@cli.command()
@click.option('--geo', default=EU, show_default=True)
@click.option('--year', default=2024, type=int, show_default=True)
@click.option('--top-n', default=10, type=int, show_default=True)
@click.option('--outdir', default=str(OUTPUT_DIR), show_default=True)
def sector(geo, year, top_n, outdir):
    outdir = Path(outdir); outdir.mkdir(exist_ok=True)
    df = ds.get_ai_by_sector(geo=geo, year=year, top_n=top_n)
    df.to_csv(outdir / "eu_by_sector_top10_2024.csv", index=False)
    save_barh(df, x="value", y="nace_r2_label",
              title=f"{geo}: AI adoption by sector (Top {top_n}, {year})",
              fname="eu_by_sector_top10_2024.png", output_dir=outdir)

@cli.command()
@click.option('--year', default=2024, type=int, show_default=True)
@click.option('--top', default=12, type=int, show_default=True)
@click.option('--bottom', default=12, type=int, show_default=True)
@click.option('--outdir', default=str(OUTPUT_DIR), show_default=True)
def countries(year, top, bottom, outdir):
    outdir = Path(outdir); outdir.mkdir(exist_ok=True)
    top_df, bot_df = ds.get_ai_countries(year=year, top=top, bottom=bottom)
    top_df.to_csv(outdir / "countries_top_2024.csv", index=False)
    bot_df.to_csv(outdir / "countries_bottom_2024.csv", index=False)
    save_barh(top_df.sort_values("value"), x="value", y="geo_label",
              title=f"Countries: highest AI adoption ({year})",
              fname="countries_top_2024.png", output_dir=outdir)
    save_barh(bot_df, x="value", y="geo_label",
              title=f"Countries: lowest AI adoption ({year})",
              fname="countries_bottom_2024.png", output_dir=outdir)

@cli.command()
@click.option('--geo', default=EU, show_default=True)
@click.option('--year', default=2024, type=int, show_default=True)
@click.option('--outdir', default=str(OUTPUT_DIR), show_default=True)
def tech(geo, year, outdir):
    outdir = Path(outdir); outdir.mkdir(exist_ok=True)
    df = ds.get_ai_by_technology(geo=geo, year=year)
    df.to_csv(outdir / "eu_by_tech_2024.csv", index=False)
    save_bar(df, x="indic_is_label", y="value",
             title=f"{geo}: AI by technology ({year})",
             fname="eu_by_tech_2024.png", output_dir=outdir)

@cli.command()
@click.option('--geo', default=EU, show_default=True)
@click.option('--year', default=2024, type=int, show_default=True)
@click.option('--outdir', default=str(OUTPUT_DIR), show_default=True)
def purposes(geo, year, outdir):
    outdir = Path(outdir); outdir.mkdir(exist_ok=True)
    df = ds.get_ai_purpose_by_sector(geo=geo, year=year)
    df.to_csv(outdir / "eu_purposes_by_sector_2024.csv", index=False)
    save_heatmap_like(df, row="nace_r2_label",
                      title=f"Purposes × sector ({geo}, {year})",
                      fname="eu_purposes_by_sector_2024.png", output_dir=outdir)

@cli.command(name="lv-vs-eu")
@click.option('--years', multiple=True, type=int, default=[2023, 2024], show_default=True)
@click.option('--outdir', default=str(OUTPUT_DIR), show_default=True)
def lv_vs_eu(years, outdir):
    outdir = Path(outdir); outdir.mkdir(exist_ok=True)
    eu = ds.get_ai_overall_timeseries(geo="EU27_2020", years=list(years))
    lv = ds.get_ai_overall_timeseries(geo="LV", years=list(years))
    eu = eu.rename(columns={"geo_label":"region"}); eu["region"] = "EU-27"
    lv["region"] = "Latvia"
    import pandas as pd
    comp = pd.concat([eu[["year","value","region"]], lv[["year","value","region"]]], ignore_index=True)
    comp.to_csv(outdir / "lv_vs_eu_timeseries.csv", index=False)
    save_lines(comp, x="year", y="value", group="region",
               title=f"AI adoption: Latvia vs EU-27 ({min(years)}–{max(years)})",
               fname="lv_vs_eu_timeseries.png", output_dir=outdir)

if __name__ == "__main__":
    cli()
