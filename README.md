
# eurostat-ai (Codespaces-ready)

Modular toolkit for loading, cleaning, and visualizing Eurostat AI adoption data (`isoc_eb_ai`, `isoc_eb_ain2`).

## Quickstart (GitHub Codespaces)
1. Create a GitHub repo from this folder (upload the ZIP).
2. Click **Code → Create codespace on main**.
3. In Codespaces terminal:
   ```bash
   make setup
   make test
   make run-all
   ```

## CLI examples
```bash
python -m eurostat_ai.cli timeseries --geo EU27_2020 --years 2023 2024
python -m eurostat_ai.cli size --geo EU27_2020 --year 2024
python -m eurostat_ai.cli sector --geo EU27_2020 --year 2024 --top-n 10
python -m eurostat_ai.cli countries --year 2024 --top 12 --bottom 12
python -m eurostat_ai.cli tech --geo EU27_2020 --year 2024
python -m eurostat_ai.cli purposes --geo EU27_2020 --year 2024
python -m eurostat_ai.cli lv-vs-eu --years 2023 2024
```
