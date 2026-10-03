# E-Commerce Sales Analysis

A Python-based data analysis project that explores e-commerce transaction data to identify revenue trends, product performance, profitability, and regional sales patterns.

## Project Overview

This project demonstrates an end-to-end data analysis workflow:

**Raw Data → Data Cleaning → Feature Engineering → KPI Calculation → EDA → Visualization → Exported Results**

The dataset contains order, customer, product, category, region, quantity, pricing, discount, sales, and profit information.

## Objectives

- Clean and preprocess transactional sales data
- Handle duplicate and missing records
- Create useful date and profitability features
- Calculate business KPIs
- Analyze product and category performance
- Compare regional revenue and profit
- Identify monthly sales trends
- Find high-sales / low-profit products
- Generate reusable visualizations
- Export cleaned data and summary tables

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset

The included `sales_data.csv` contains 1,008 rows before cleaning, including a small number of intentional duplicate and missing-value records so that the cleaning workflow can be demonstrated.

Columns:

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Order date |
| Customer_ID | Customer identifier |
| Product | Product purchased |
| Category | Product category |
| Region | Sales region |
| Quantity | Units purchased |
| Unit_Price | Price per unit |
| Discount | Discount applied |
| Sales | Revenue generated |
| Profit | Profit generated |

## Project Structure

```text
ecommerce-sales-analysis/
├── README.md
├── sales_analysis.py
├── sales_data.csv
├── requirements.txt
└── output/
    ├── .gitkeep
    └── screenshots/
```

When the script runs, the `output/` directory is populated with analysis tables and charts.

## Key Metrics

The script calculates:

- Total orders
- Total revenue
- Total profit
- Total quantity sold
- Average order value
- Average profit margin

### Average Order Value

```text
Average Order Value = Total Revenue / Total Orders
```

### Profit Margin

```text
Profit Margin = (Profit / Sales) × 100
```

## Analysis Performed

### 1. Data Cleaning

The script:

- Removes duplicate rows
- Converts order dates to datetime
- Handles invalid dates
- Converts numeric columns
- Fills missing numeric values using medians
- Fills missing categorical values with `Unknown`

### 2. Feature Engineering

Additional fields are generated:

- Year
- Month
- Month Name
- Profit Margin

### 3. Product Analysis

Products are ranked by:

- Revenue
- Profit
- Quantity sold

The top 10 products by revenue are exported.

### 4. Category Analysis

Categories are compared using:

- Revenue
- Profit
- Quantity

### 5. Regional Analysis

Regions are compared using:

- Revenue
- Profit
- Number of orders

### 6. Monthly Trend Analysis

Revenue is grouped by month to identify changes in sales performance throughout the year.

### 7. Sales vs Profit

A scatter plot is used to explore the relationship between sales and profit and identify potentially unusual transactions.

### 8. High Sales / Low Profit Analysis

The project identifies products whose revenue is above the median while their total profit is below the median. This can highlight products that generate substantial sales but may need profitability investigation.

## Visualizations

The script generates:

- `monthly_revenue.png` — monthly revenue trend
- `revenue_by_category.png` — revenue by category
- `profit_by_region.png` — profit by region
- `top_products.png` — top 10 products by revenue
- `sales_vs_profit.png` — sales versus profit relationship

## Output Files

The script also exports:

- `cleaned_sales_data.csv`
- `category_analysis.csv`
- `region_analysis.csv`
- `top_products.csv`

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ecommerce-sales-analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

Make sure `sales_data.csv` is in the project root, then run:

```bash
python sales_analysis.py
```

The console will display KPI summaries and analysis results. Charts and CSV reports will be created in the `output/` directory.

## Example Workflow

```text
sales_data.csv
      |
      v
Load Dataset
      |
      v
Inspect Missing Values & Duplicates
      |
      v
Clean Data
      |
      v
Create Features
      |
      v
Calculate KPIs
      |
      v
Perform EDA
      |
      v
Generate Visualizations
      |
      v
Export Results
```

## Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Data aggregation with Pandas
- Feature engineering
- Business KPI calculation
- GroupBy and statistical summaries
- Time-series aggregation
- Data visualization
- Basic profitability analysis
- Exporting analytical results

## Future Improvements

Possible extensions:

- Build an interactive Power BI dashboard
- Add customer segmentation
- Add sales forecasting
- Add year-over-year growth analysis
- Add correlation analysis
- Add a Streamlit dashboard
- Connect the analysis to a SQL database
- Automate periodic sales reports

## Disclaimer

The included dataset is synthetic and intended for educational and portfolio purposes.
