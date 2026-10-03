# 📊 E-Commerce Sales Analysis

A Python-based data analysis project that analyzes e-commerce transaction data to uncover **sales trends, product performance, profitability, and regional patterns**.

The project demonstrates a complete data analysis workflow — from **raw data cleaning and preprocessing to exploratory data analysis, visualization, and business insights**.

---

## 📌 Project Overview

E-commerce businesses generate large amounts of transactional data. Analyzing this data can help identify which products generate the most revenue, which regions perform well, how sales change over time, and which products have strong sales but relatively low profitability.

This project uses Python to analyze an e-commerce sales dataset and answer questions such as:

- What is the total revenue generated?
- How much profit was generated?
- Which products generate the most revenue?
- Which categories perform the best?
- Which regions generate the highest revenue and profit?
- How do sales change over time?
- Which products have high sales but low profit?
- What is the average order value?
- How does sales volume relate to profitability?

---

## 🎯 Objectives

The main objectives of this project are:

1. Clean and preprocess raw sales data.
2. Handle missing and duplicate records.
3. Convert and extract useful date information.
4. Calculate important business KPIs.
5. Perform exploratory data analysis (EDA).
6. Analyze product, category, and regional performance.
7. Identify monthly sales trends.
8. Analyze the relationship between sales and profit.
9. Generate meaningful visualizations.
10. Export cleaned data and analysis results for further use.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data cleaning, transformation, and analysis |
| **NumPy** | Numerical calculations |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical visualization |
| **CSV** | Input and output data format |

---

## 📂 Project Structure

```text
ecommerce-sales-analysis/
│
├── sales_analysis.py
├── sales_data.csv
├── requirements.txt
├── README.md
│
└── output/
    ├── cleaned_sales_data.csv
    ├── category_analysis.csv
    ├── region_analysis.csv
    ├── top_products.csv
    │
    ├── monthly_revenue.png
    ├── revenue_by_category.png
    ├── profit_by_region.png
    ├── top_products.png
    └── sales_vs_profit.png
```

---

## 📊 Dataset

The dataset contains transactional e-commerce sales information.

### Dataset Columns

| Column | Description |
|---|---|
| `Order_ID` | Unique identifier for each order |
| `Order_Date` | Date on which the order was placed |
| `Customer_ID` | Unique customer identifier |
| `Product` | Product purchased |
| `Category` | Product category |
| `Region` | Sales region |
| `Quantity` | Number of units purchased |
| `Unit_Price` | Price per unit |
| `Discount` | Discount applied to the order |
| `Sales` | Total sales/revenue |
| `Profit` | Profit generated from the order |

---

# 🔄 Analysis Workflow

The project follows a structured data analysis pipeline.

```text
Raw Dataset
     │
     ▼
Data Loading
     │
     ▼
Data Inspection
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
KPI Calculation
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Data Visualization
     │
     ▼
Business Insights
     │
     ▼
Export Results
```

---

# 🧹 1. Data Cleaning

The first step is to inspect and clean the raw dataset.

The project checks for:

- Missing values
- Duplicate records
- Invalid dates
- Incorrect numerical values
- Missing categorical values

### Cleaning operations include:

- Removing duplicate rows
- Converting `Order_Date` into a datetime format
- Handling invalid dates
- Filling missing numerical values using median values
- Filling missing categorical values with `"Unknown"`

This ensures that the dataset is suitable for further analysis.

---

# ⚙️ 2. Feature Engineering

Additional features are created from the existing data to make the analysis more useful.

### Date Features

From `Order_Date`, the project extracts:

- Year
- Month
- Month name

Example:

```text
Order_Date → 2025-03-15

Year       → 2025
Month      → 3
Month_Name → March
```

### Profit Margin

The project also calculates profit margin:

```text
Profit Margin = (Profit / Sales) × 100
```

This helps compare profitability across different products and categories.

---

# 📈 3. Key Performance Indicators

The project calculates several important business KPIs.

### Total Orders

Number of unique orders:

```text
Total Orders = Unique Order IDs
```

### Total Revenue

```text
Total Revenue = Sum of Sales
```

### Total Profit

```text
Total Profit = Sum of Profit
```

### Average Order Value

```text
Average Order Value =
Total Revenue / Total Orders
```

### Average Profit Margin

The average profit margin is calculated across transactions.

These metrics provide a high-level overview of the business.

---

# 🔍 4. Exploratory Data Analysis

The project performs analysis across multiple dimensions.

## Product Analysis

Products are grouped and ranked based on:

- Revenue
- Profit
- Quantity sold

The project identifies the **top 10 products by revenue**.

---

## Category Analysis

Each product category is analyzed using:

- Total revenue
- Total profit
- Total quantity sold

Example output:

```text
Category       Revenue       Profit       Quantity
--------------------------------------------------
Electronics    XXXXX         XXXXX        XXXX
Accessories    XXXXX         XXXXX        XXXX
```

---

## Regional Analysis

Sales regions are compared based on:

- Revenue
- Profit
- Number of orders

This helps identify differences in regional performance.

---

## Monthly Sales Analysis

Sales are grouped by:

- Year
- Month
- Month name

This allows the project to identify changes in revenue over time.

---

# 📊 5. Data Visualization

The project generates several visualizations.

## Monthly Revenue Trend

Shows how revenue changes over time.

**File:**

```text
monthly_revenue.png
```

Useful for identifying:

- Growth trends
- Declining periods
- Seasonal patterns
- High-performing months

---

## Revenue by Category

Compares total revenue across product categories.

**File:**

```text
revenue_by_category.png
```

---

## Profit by Region

Shows how profitable each sales region is.

**File:**

```text
profit_by_region.png
```

---

## Top 10 Products

Displays the top products ranked by revenue.

**File:**

```text
top_products.png
```

---

## Sales vs Profit

A scatter plot is used to analyze the relationship between sales and profit.

**File:**

```text
sales_vs_profit.png
```

This can help identify products or transactions with:

- High sales and high profit
- High sales but low profit
- Low sales and low profit

---

# 💡 6. Business Insights

The analysis can be used to identify insights such as:

- Products generating the highest revenue
- Categories contributing the most to overall sales
- Regions generating the highest profit
- Months with unusually high or low revenue
- Products with high sales but relatively low profitability
- Relationships between sales volume and profit

These insights could help a business make decisions regarding:

- Product strategy
- Regional sales strategy
- Pricing
- Discounts
- Inventory planning
- Marketing priorities

---

# 📤 7. Output Files

The project automatically exports analysis results to the `output/` directory.

### Cleaned Dataset

```text
cleaned_sales_data.csv
```

Contains the processed dataset with additional calculated features.

### Category Analysis

```text
category_analysis.csv
```

Contains revenue, profit, and quantity statistics by category.

### Regional Analysis

```text
region_analysis.csv
```

Contains revenue, profit, and order statistics by region.

### Top Products

```text
top_products.csv
```

Contains the highest-revenue products.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd ecommerce-sales-analysis
```

---

## 2. Install dependencies

Make sure Python is installed.

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pandas numpy matplotlib seaborn
```

---

# ▶️ Running the Project

Make sure `sales_data.csv` is in the same directory as `sales_analysis.py`.

Run:

```bash
python sales_analysis.py
```

The program will:

1. Load the dataset.
2. Inspect the data.
3. Clean the dataset.
4. Calculate KPIs.
5. Perform exploratory analysis.
6. Generate visualizations.
7. Export analysis results.

The generated files will be saved inside:

```text
output/
```

---

# 📋 Example Console Output

```text
============================================================
SALES SUMMARY
============================================================

Total Orders         : 9,842
Total Revenue        : $1,284,521.00
Total Profit         : $182,430.00
Total Quantity       : 25,621
Average Order Value  : $130.50
Average Profit Margin: 14.20%
```

Example product analysis:

```text
============================================================
TOP 10 PRODUCTS BY REVENUE
============================================================

Laptop              XXXXX
Monitor             XXXXX
Headphones          XXXXX
Keyboard            XXXXX
Mouse               XXXXX
```

---

# 🧠 Skills Demonstrated

This project demonstrates practical knowledge of:

### Python

- File handling
- Exception handling
- Functions and control flow
- Data processing

### Pandas

- DataFrames
- GroupBy
- Aggregation
- Filtering
- Sorting
- Missing-value handling
- Date manipulation

### NumPy

- Numerical operations
- Conditional calculations
- Feature creation

### Data Analysis

- Data cleaning
- Exploratory Data Analysis
- KPI calculation
- Trend analysis
- Product analysis
- Regional analysis
- Profitability analysis

### Data Visualization

- Line charts
- Bar charts
- Horizontal bar charts
- Scatter plots

---

# 🔮 Future Improvements

Possible improvements for future versions include:

- [ ] Add an interactive **Power BI dashboard**
- [ ] Add automated monthly sales reports
- [ ] Add customer segmentation
- [ ] Add sales forecasting
- [ ] Add year-over-year growth analysis
- [ ] Add correlation analysis
- [ ] Add interactive Plotly visualizations
- [ ] Build a Streamlit web dashboard
- [ ] Connect the project to a SQL database

---

# 📌 Future Architecture

The project can eventually be expanded into:

```text
CSV / SQL Database
        │
        ▼
Data Cleaning
        │
        ▼
Python Analysis
        │
        ├───────────────┐
        ▼               ▼
   Statistical       KPI
    Analysis       Calculation
        │               │
        └───────┬───────┘
                ▼
        Interactive Dashboard
                │
                ▼
        Business Insights
```

---

# 👨‍💻 Author
Harsh Vardhan Anand

This project was created as a portfolio project to demonstrate practical skills in Python, data analysis, data cleaning, exploratory data analysis, and visualization.

---

## ⭐ Project Highlights

- End-to-end data analysis workflow
- Real-world business-oriented analysis
- Automated data cleaning
- KPI calculation
- Product and regional performance analysis
- Multiple data visualizations
- Exportable analysis results
- Extensible architecture for Power BI or dashboard integration
