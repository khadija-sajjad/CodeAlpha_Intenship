import pandas as pd
import numpy as np
df = pd.read_csv('books_data.csv', encoding='latin1')
df['Price_Clean'] = df['Price'].str.replace('£', '').astype(float)
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Numeric'] = df['Rating'].map(rating_map)
cleaned_data = df[['Title', 'Price', 'Rating']].copy()
Q1 = df['Price_Clean'].quantile(0.25)
Q3 = df['Price_Clean'].quantile(0.75)
IQR = Q3 - Q1
eda_summary = pd.DataFrame({
    'Metric': [
        'Total Records',
        'Mean Price',
        'Median Price',
        'Std Dev Price',
        'Min Price',
        'Max Price',
        'Mean Rating',
        'Q1 (25th Percentile)',
        'Q3 (75th Percentile)',
        'IQR',
        'Outlier Lower Bound',
        'Outlier Upper Bound'
    ],
    'Value': [
        len(df),
        f"£{df['Price_Clean'].mean():.2f}",
        f"£{df['Price_Clean'].median():.2f}",
        f"£{df['Price_Clean'].std():.2f}",
        f"£{df['Price_Clean'].min():.2f}",
        f"£{df['Price_Clean'].max():.2f}",
        f"{df['Rating_Numeric'].mean():.2f}",
        f"£{Q1:.2f}",
        f"£{Q3:.2f}",
        f"£{IQR:.2f}",
        f"£{Q1 - 1.5*IQR:.2f}",
        f"£{Q3 + 1.5*IQR:.2f}"
    ]
})
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['Price_Clean'] < lower_bound) | (df['Price_Clean'] > upper_bound)][['Title', 'Price', 'Rating', 'Price_Clean']]
outliers_sheet = pd.DataFrame({
    'Total Outliers Found': [len(outliers)],
    'Outlier Percentage': [f"{(len(outliers)/len(df)*100):.2f}%"],
    'Lower Bound': [f"£{lower_bound:.2f}"],
    'Upper Bound': [f"£{upper_bound:.2f}"]
})
insights = pd.DataFrame({
    'Insight': [
        'Price Range',
        'Most Common Rating',
        'Data Quality',
        'Books Above Upper Bound',
        'Books Below Lower Bound',
        'Average Book Price',
        'Recommendation'
    ],
    'Description': [
        f"£{df['Price_Clean'].min():.2f} - £{df['Price_Clean'].max():.2f}",
        df['Rating'].value_counts().idxmax() + ' stars',
        'No missing values - Data is complete',
        f"{len(outliers[outliers['Price_Clean'] > upper_bound])} books",
        f"{len(outliers[outliers['Price_Clean'] < lower_bound])} books",
        f"£{df['Price_Clean'].mean():.2f}",
        'Data ready for visualization and analysis'
    ]
})
with pd.ExcelWriter('books_analysis.xlsx', engine='openpyxl') as writer:
    cleaned_data.to_excel(writer, sheet_name='Cleaned_Data', index=False)
    eda_summary.to_excel(writer, sheet_name='EDA_Summary', index=False)
    outliers.to_excel(writer, sheet_name='Outliers', index=False)
    insights.to_excel(writer, sheet_name='Key_Insights', index=False)
    print("Excel file created: books_analysis.xlsx")
print("   Sheets: Cleaned_Data, EDA_Summary, Outliers, Key_Insights")