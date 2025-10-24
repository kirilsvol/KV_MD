
from eurostat_ai.datasets import (
    get_ai_overall_timeseries, get_ai_by_size, get_ai_by_sector,
    get_ai_countries, get_ai_by_technology, get_ai_purpose_by_sector
)
from eurostat_ai.plots import save_bar, save_barh, save_lines, save_heatmap_like
from eurostat_ai.config import OUTPUT_DIR, EU

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    ts = get_ai_overall_timeseries(geo=EU, years=[2023, 2024])
    ts.to_csv(OUTPUT_DIR / "eu_timeseries.csv", index=False)
    save_lines(ts, x="year", y="value", group="geo_label",
               title="EU-27: enterprises using ≥1 AI (%, 2023–2024)",
               fname="eu_timeseries.png")

    by_size = get_ai_by_size(geo=EU, year=2024)
    by_size.to_csv(OUTPUT_DIR / "eu_by_size_2024.csv", index=False)
    save_bar(by_size, x="size_emp_label", y="value",
             title="EU-27: AI adoption by size (2024)",
             fname="eu_by_size_2024.png")

    by_sector = get_ai_by_sector(geo=EU, year=2024, top_n=10)
    by_sector.to_csv(OUTPUT_DIR / "eu_by_sector_top10_2024.csv", index=False)
    save_barh(by_sector, x="value", y="nace_r2_label",
              title="EU-27: AI adoption by sector (Top 10, 2024)",
              fname="eu_by_sector_top10_2024.png")

    top_c, bottom_c = get_ai_countries(year=2024, top=12, bottom=12)
    top_c.to_csv(OUTPUT_DIR / "countries_top_2024.csv", index=False)
    bottom_c.to_csv(OUTPUT_DIR / "countries_bottom_2024.csv", index=False)
    save_barh(top_c.sort_values("value"), x="value", y="geo_label",
              title="Countries: highest AI adoption (2024)",
              fname="countries_top_2024.png")
    save_barh(bottom_c, x="value", y="geo_label",
              title="Countries: lowest AI adoption (2024)",
              fname="countries_bottom_2024.png")

    by_tech = get_ai_by_technology(geo=EU, year=2024)
    by_tech.to_csv(OUTPUT_DIR / "eu_by_tech_2024.csv", index=False)
    save_bar(by_tech, x="indic_is_label", y="value",
             title="EU-27: AI by technology (2024)",
             fname="eu_by_tech_2024.png")

    purp = get_ai_purpose_by_sector(geo=EU, year=2024)
    purp.to_csv(OUTPUT_DIR / "eu_purposes_by_sector_2024.csv", index=False)
    save_heatmap_like(purp, row="nace_r2_label",
                      title="Purposes × sector (EU-27, 2024)",
                      fname="eu_purposes_by_sector_2024.png")

if __name__ == "__main__":
    main()
