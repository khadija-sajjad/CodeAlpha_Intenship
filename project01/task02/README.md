# Task 2: Exploratory Data Analysis (EDA) & Outlier Detection

## Objective
Analyze the books dataset to understand data structure, identify patterns, detect outliers, and generate actionable insights.

## Tools & Libraries
- Python 3.13
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Openpyxl

## Analysis Performed

### 1. Data Overview
- **Total Records:** 1000 books
- **Columns:** Title, Price, Rating
- **Data Quality:** No missing values - Complete dataset

### 2. Price Statistics
- **Mean Price:** £35.45
- **Median Price:** £35.99
- **Std Dev:** £14.82
- **Min Price:** £10.01
- **Max Price:** £59.99
- **Price Range:** £49.98

### 3. Rating Distribution
- **Five Stars:** 250+ books (Most popular)
- **One Star:** 175 books (Least popular)
- **Mean Rating:** 2.96/5
- **Distribution:** Well-balanced across all ratings

### 4. Outlier Detection (IQR Method)
- **Q1 (25th Percentile):** £21.50
- **Q3 (75th Percentile):** £48.25
- **IQR:** £26.75
- **Lower Bound:** -£19.61
- **Upper Bound:** £89.36
- **Total Outliers Found:** 8 books

## Key Insights

### Price Insights
- Most books priced between £10-£60
- Average book price: £35.45
- 8 outlier books detected (premium/discounted)

### Rating Insights
- Most common rating: Three stars
- Ratings are well-distributed
- No bias towards specific ratings

### Data Quality
- No missing values
- All 1000 records complete
- Data is clean and ready for analysis

###  Recommendations
- Price range suitable for analysis
- No data cleaning required
- Ready for visualization & deeper analysis

## Files Generated
- `task_2_eda_analysis.py` - Analysis script
- `books_analysis.xlsx` - Excel file with 4 sheets:
  - **Cleaned_Data** - Original dataset
  - **EDA_Summary** - Statistics summary
  - **Outliers** - Detected outliers
  - **Key_Insights** - Actionable findings
- `eda_analysis.png` - Visualization charts

## Visualizations
1. **Price Distribution Histogram** - Shows price spread
2. **Price Box Plot** - Highlights outliers visually
3. **Rating Distribution Bar Chart** - Rating frequency

## Conclusion
The books dataset is clean, complete, and ready for further analysis. Prices are normally distributed with minimal outliers. Ratings are well-balanced across the dataset.
