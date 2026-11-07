# GDS6000AOL - DATA SCIENCE FUNDAMENTALS - FALL TERM 2026 - Week 7 - Midterm Assessment

## Team

- Dimitrios Tsitouras
- Thodoris Dendrinos

## Project overview

This project analyses how inflation and interest rates relate to car prices and car sales between 2019 and 2023.
- Dataset Title: Car Prices, Inflation, and Interest Rates (2019–2023) (Kaggle) – 60 monthly observations with new car price, used car price, inflation rate, interest rate and units sold.
- Dataset URL: https://www.kaggle.com/datasets/abduulwasay/auto-prices-and-economic-trends-20192023/data?select=automobile_prices_economics_2019_2023.csv

## Main question: How do inflation and interest rates impact car prices and sales?
## Guiding Questions:
- Do increases in interest rates directly reduce car sales?
- Do used car prices react faster to economic conditions than new car prices?
- Can we model demand elasticity using this data?
- What kinds of forecasting models might work best on this dataset?


## Phases of Analysis
- Data cleaning: removed an empty row, converted dates, removed symbols (, and %) and converted all values to numeric types.
- Exploratory data analysis: correlation heatmap and time-series visualizations of sales, car prices, inflation and interest rates, used in order to analyze the given guiding questions.
- Modeling: linear regression, polynomial regression and k-NN, using interest rate, inflation rate and a time index as features and units sold as the target. Models were trained on 2019–2022 and tested on 2023, and evaluated with MAE, RMSE and R².
- Conclusions

## Repository structure
- Folder Name : week7
- Files:
- README.md                                   - ReadMe file explaining our work and method
- automobile_prices_economics_2019_2023.csv   - The csv file containing our dataset
- midterm_project.ipynb                       - The main body of our work and our full analysis

## How to reproduce
### 1. Environment setup
- Python 3.12 

Install the required packages:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

### 2. Run the analysis

1. Clone the repository.

2. Open week7/midterm_project.ipynb in Jupyter Notebook or VS Code.

3. Select Run All. The notebook runs from start to finish without errors.

## Summary of findings

Main question: we found no clear evidence that inflation or interest rates directly affect car sales or car prices within the period covered by our dataset. The number of cars sold shows an overall increasing trend that cannot be directly linked to changes in inflation or interest rates. New car prices remain relatively stable, while used car prices change without a consistent relationship with either economic indicator. The clearest relationship we found is between inflation and interest rates: interest rates follow inflation with an approximate delay of one year.

Guiding questions:

- Q1: no clear evidence that higher interest rates lead to lower car sales.
- Q2: used car prices do not appear to react faster than new car prices; both show price movements over similar periods.
- Q3: demand elasticity cannot be reliably estimated using the available data.
- Q4: linear regression is the most appropriate of the three models tested, although none of the models provides accurate predictions for 2023.

## Limitations

The dataset is small (60 monthly observations) and does not include other factors that may influence car prices and sales, such as production costs, supply chain conditions, consumer preferences and consumer income. Units sold are also not split between new and used cars.