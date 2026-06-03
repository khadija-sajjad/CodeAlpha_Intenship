import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data load
df = pd.read_excel('books_analysis.xlsx', sheet_name='Cleaned_Data')
df['Price_Clean'] = df['Price'].str.replace('£', '').astype(float)

def get_sentiment(rating):
    if rating in ['Four', 'Five']:
        return 'Positive'
    elif rating == 'Three':
        return 'Neutral'
    else:
        return 'Negative'

df['Sentiment'] = df['Rating'].apply(get_sentiment)
sentiment_counts = df['Sentiment'].value_counts()

# Power BI Colors
colors = ['#1B3B5F', '#3498DB', '#27AE60']
bg_color = '#F2F4F5'
card_color = '#FFFFFF'
text_color = '#2C3E50'

fig = plt.figure(figsize=(18, 8), facecolor=bg_color)
fig.suptitle('Book Sentiment Analysis Dashboard',
             fontsize=22, fontweight='bold', color=text_color, y=1.01)

# Chart 1 - Donut
ax1 = fig.add_subplot(131)
ax1.set_facecolor(card_color)
wedges, texts, autotexts = ax1.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.75,
    wedgeprops=dict(width=0.6, edgecolor=bg_color, linewidth=3)
)
for text in texts:
    text.set_color(text_color)
    text.set_fontsize(12)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')
ax1.set_title('Sentiment Split', fontsize=14, color=text_color,
              fontweight='bold', pad=15)

# Chart 2 - Horizontal Bar
ax2 = fig.add_subplot(132)
ax2.set_facecolor(card_color)
sentiments = sentiment_counts.index.tolist()
values = sentiment_counts.values.tolist()
bars = ax2.barh(sentiments, values, color=colors,
                edgecolor='white', linewidth=0.5, height=0.5)
for bar, val in zip(bars, values):
    ax2.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f'{val} books', va='center', color=text_color,
             fontsize=12, fontweight='bold')
ax2.tick_params(colors=text_color, labelsize=12)
ax2.set_xlabel('Number of Books', color=text_color, fontsize=12)
ax2.set_title('Sentiment Count', fontsize=14, color=text_color,
              fontweight='bold', pad=15)
ax2.spines['bottom'].set_color('#BDC3C7')
ax2.spines['left'].set_color('#BDC3C7')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_xlim(0, max(values) + 80)

# Chart 3 - Box Plot
ax3 = fig.add_subplot(133)
ax3.set_facecolor(card_color)
sentiment_order = ['Positive', 'Neutral', 'Negative']
data_to_plot = [df[df['Sentiment']==s]['Price_Clean'].values for s in sentiment_order]
bp = ax3.boxplot(data_to_plot, labels=sentiment_order, patch_artist=True,
                 medianprops=dict(color='white', linewidth=2))
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.85)
ax3.tick_params(colors=text_color, labelsize=12)
ax3.set_ylabel('Price (£)', color=text_color, fontsize=12)
ax3.set_title('Price by Sentiment', fontsize=14, color=text_color,
              fontweight='bold', pad=15)
ax3.spines['bottom'].set_color('#BDC3C7')
ax3.spines['left'].set_color('#BDC3C7')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('sentiment_analysis.png', dpi=150,
            bbox_inches='tight', facecolor=bg_color)
plt.show()
print("Dashboard saved!")