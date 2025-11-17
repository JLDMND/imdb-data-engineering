cat > README.md << 'EOF'
# IMDb Data Engineering Project

This repository contains a 12-week, end-to-end data engineering project built around the official IMDb datasets.

## Goal

Build a complete movie analytics pipeline, including:

- Extracting IMDb datasets
- Cleaning and transforming the data
- Modeling a star schema
- Storing data in Parquet files (data warehouse style)
- Running analytics with DuckDB and SQL
- Orchestrating workflows with Prefect
- Packaging and deployment with Docker

## Tech Stack

- Python 3.12 (with venv)
- Pandas
- DuckDB
- Parquet
- Prefect (for orchestration, later)
- Git + GitHub
- macOS (Apple Silicon) + VS Code

## Learning Journey

This project is structured as a 12-week curriculum:

1. Environment setup, Git, VS Code, venv  
2. Extract IMDb datasets, inspect, profile  
3. Transform and clean, create processed datasets  
4. SQL analytics with DuckDB  
5. Dimensional modeling (star schema)  
6. Build Parquet warehouse  
7. Intro to Prefect + first flow  
8. Incremental loads & data validation  
9. Scheduling, retries, logging  
10. Visualisation (plots, dashboards)  
11. Docker packaging & deployment  
12. Final documentation + portfolio polish  

This README will grow over time as the project evolves.
