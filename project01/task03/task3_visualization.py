import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('books_analysis.xlsx', sheet_name='Cleaned_Data')
df['Price_Clean'] = df['Price'].str.replace('£', '').astype(float)
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Numeric'] = df['Rating'].map(rating_map)
plt.style.use('dark_background')
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Books Data Analysis Dashboard', fontsize=20, fontweight='bold', color='white', y=1.02)
axes[0,0].hist(df['Price_Clean'], bins=20, color='#4ECDC4', edgecolor='white', alpha=0.8)
axes[0,0].set_title('Price Distribution', fontsize=14, color='white', fontweight='bold')
axes[0,0].set_xlabel('Price (£)', color='white')
axes[0,0].set_ylabel('Number of Books', color='white')
axes[0,0].axvline(df['Price_Clean'].mean(), color='#FF6B6B', linestyle='--', linewidth=2, label=f'Mean: £{df["Price_Clean"].mean():.2f}')
axes[0,0].legend(fontsize=10)
rating_counts = df['Rating'].value_counts()
bars = axes[0,1].bar(rating_counts.index, rating_counts.values, color=colors, edgecolor='white', alpha=0.9)
axes[0,1].set_title('Rating Distribution', fontsize=14, color='white', fontweight='bold')
axes[0,1].set_xlabel('Rating', color='white')
axes[0,1].set_ylabel('Number of Books', color='white')
for bar, val in zip(bars, rating_counts.values):
    axes[0,1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, str(val), ha='center', color='white', fontweight='bold')
scatter_colors = df['Rating_Numeric'].map({1:'#FF6B6B', 2:'#FFEAA7', 3:'#4ECDC4', 4:'#45B7D1', 5:'#96CEB4'})
axes[1,0].scatter(df['Rating_Numeric'], df['Price_Clean'], c=scatter_colors, alpha=0.6, s=30)
axes[1,0].set_title('Price vs Rating', fontsize=14, color='white', fontweight='bold')
axes[1,0].set_xlabel('Rating (1-5)', color='white')
axes[1,0].set_ylabel('Price (£)', color='white')
axes[1,0].set_xticks([1,2,3,4,5])
bp = axes[1,1].boxplot([df[df['Rating']==r]['Price_Clean'].values for r in ['One','Two','Three','Four','Five']],
                        labels=['One','Two','Three','Four','Five'],
                        patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)
axes[1,1].set_title('Price Range by Rating', fontsize=14, color='white', fontweight='bold')
axes[1,1].set_xlabel('Rating', color='white')
axes[1,1].set_ylabel('Price (£)', color='white')
plt.tight_layout()
plt.savefig('books_dashboard.png', dpi=150, bbox_inches='tight', facecolor='#1a1a2e')
plt.show()
print("Dashboard saved as books_dashboard.png!")