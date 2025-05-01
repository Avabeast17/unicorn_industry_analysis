# Unicorn Industry Analysis (2019–2021)

This project helps an investment firm identify the top-performing industries that produced the most unicorns (companies valued at $1B+) between 2019 and 2021.

## Objective

Analyze trends in unicorn creation by:
- Identifying the **top 3 industries** by number of unicorns
- Showing **how many unicorns** each industry produced per year
- Calculating their **average valuation (in billions)**

## Data Sources

Simulated from:
- `industries` table (company → industry)
- `dates` table (unicorn date)
- `funding` table (valuation)

## Final Output

A table sorted by:
- `industry`
- `year` (descending)
- `num_unicorns` (descending)

With these columns:
- `industry`
- `year`
- `num_unicorns`
- `average_valuation_billions`

## 📁 Files

- `unicorn_industry_analysis.py`: Python script that performs the full analysis

## 🚀 How to Run

```bash
pip install pandas
python unicorn_industry_analysis.py
