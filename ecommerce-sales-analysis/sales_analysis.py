import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

FILE_NAME = "sales_data.csv"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data():
    """Load the raw sales dataset."""
    try:
        return pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        print(f"Error: {FILE_NAME} was not found.")
        raise SystemExit(1)


def clean_data(df):
    """Clean duplicates, dates, numeric fields, and missing values."""
    df = df.copy()

    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    print(f"\nDuplicate rows before cleaning: {df.duplicated().sum()}")

    df = df.drop_duplicates()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df = df.dropna(subset=["Order_Date"])

    numeric_columns = [
        "Quantity", "Unit_Price", "Discount", "Sales", "Profit"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df[column] = df[column].fillna(df[column].median())

    for column in ["Product", "Category", "Region", "Customer_ID"]:
        df[column] = df[column].fillna("Unknown")

    return df


def engineer_features(df):
    """Create date and profitability features."""
    df = df.copy()

    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.month
    df["Month_Name"] = df["Order_Date"].dt.strftime("%B")

    df["Profit_Margin"] = np.where(
        df["Sales"] != 0,
        (df["Profit"] / df["Sales"]) * 100,
        0
    )

    return df


def print_kpis(df):
    """Calculate and display business KPIs."""
    total_orders = df["Order_ID"].nunique()
    total_revenue = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_quantity = df["Quantity"].sum()
    average_order_value = (
        total_revenue / total_orders if total_orders else 0
    )
    average_margin = df["Profit_Margin"].mean()

    print("\n" + "=" * 60)
    print("SALES SUMMARY")
    print("=" * 60)
    print(f"Total Orders          : {total_orders:,}")
    print(f"Total Revenue         : ${total_revenue:,.2f}")
    print(f"Total Profit          : ${total_profit:,.2f}")
    print(f"Total Quantity        : {total_quantity:,}")
    print(f"Average Order Value   : ${average_order_value:,.2f}")
    print(f"Average Profit Margin : {average_margin:.2f}%")

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_quantity": total_quantity,
        "average_order_value": average_order_value,
        "average_margin": average_margin,
    }


def analyze(df):
    """Run product, category, regional, and monthly analysis."""
    top_products = (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    category_analysis = (
        df.groupby("Category")
        .agg(
            Revenue=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
        )
        .sort_values("Revenue", ascending=False)
    )

    region_analysis = (
        df.groupby("Region")
        .agg(
            Revenue=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order_ID", "nunique"),
        )
        .sort_values("Revenue", ascending=False)
    )

    monthly_sales = (
        df.groupby(["Year", "Month"])["Sales"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month"])
    )

    monthly_sales["Period"] = pd.to_datetime(
        monthly_sales["Year"].astype(str)
        + "-"
        + monthly_sales["Month"].astype(str)
        + "-01"
    )

    product_performance = (
        df.groupby("Product")
        .agg(
            Revenue=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
        )
    )

    high_sales_low_profit = product_performance[
        (product_performance["Revenue"] > product_performance["Revenue"].median())
        & (product_performance["Profit"] < product_performance["Profit"].median())
    ]

    return (
        top_products,
        category_analysis,
        region_analysis,
        monthly_sales,
        high_sales_low_profit,
    )


def create_visualizations(
    df, top_products, category_analysis, region_analysis, monthly_sales
):
    """Create and save analysis charts."""
    sns.set_theme(style="whitegrid")

    # Monthly revenue
    plt.figure(figsize=(12, 6))
    plt.plot(
        monthly_sales["Period"],
        monthly_sales["Sales"],
        marker="o",
    )
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/monthly_revenue.png", dpi=150)
    plt.close()

    # Revenue by category
    plt.figure(figsize=(10, 6))
    category_analysis["Revenue"].sort_values().plot(kind="barh")
    plt.title("Revenue by Category")
    plt.xlabel("Revenue")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/revenue_by_category.png", dpi=150)
    plt.close()

    # Profit by region
    plt.figure(figsize=(10, 6))
    region_analysis["Profit"].sort_values().plot(kind="bar")
    plt.title("Profit by Region")
    plt.xlabel("Region")
    plt.ylabel("Profit")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/profit_by_region.png", dpi=150)
    plt.close()

    # Top products
    plt.figure(figsize=(12, 6))
    top_products.sort_values().plot(kind="barh")
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_products.png", dpi=150)
    plt.close()

    # Sales vs profit
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x="Sales",
        y="Profit",
        hue="Category",
    )
    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/sales_vs_profit.png", dpi=150)
    plt.close()


def export_results(
    df, top_products, category_analysis, region_analysis
):
    """Export cleaned data and analysis tables."""
    df.to_csv(f"{OUTPUT_DIR}/cleaned_sales_data.csv", index=False)
    category_analysis.to_csv(f"{OUTPUT_DIR}/category_analysis.csv")
    region_analysis.to_csv(f"{OUTPUT_DIR}/region_analysis.csv")
    top_products.to_csv(f"{OUTPUT_DIR}/top_products.csv")


def main():
    print("Loading dataset...")
    df = load_data()

    print(f"Rows loaded: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    df = clean_data(df)
    df = engineer_features(df)

    print_kpis(df)

    (
        top_products,
        category_analysis,
        region_analysis,
        monthly_sales,
        high_sales_low_profit,
    ) = analyze(df)

    print("\n" + "=" * 60)
    print("TOP 10 PRODUCTS BY REVENUE")
    print("=" * 60)
    print(top_products)

    print("\n" + "=" * 60)
    print("CATEGORY PERFORMANCE")
    print("=" * 60)
    print(category_analysis)

    print("\n" + "=" * 60)
    print("REGIONAL PERFORMANCE")
    print("=" * 60)
    print(region_analysis)

    print("\n" + "=" * 60)
    print("HIGH SALES / LOW PROFIT PRODUCTS")
    print("=" * 60)
    print(high_sales_low_profit)

    create_visualizations(
        df,
        top_products,
        category_analysis,
        region_analysis,
        monthly_sales,
    )

    export_results(
        df,
        top_products,
        category_analysis,
        region_analysis,
    )

    print("\nAnalysis complete.")
    print(f"Results saved to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
