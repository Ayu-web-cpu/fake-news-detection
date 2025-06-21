import pandas as pd

# Load fake news data
fake_df = pd.read_csv('Fake.csv')
fake_df['label'] = 'FAKE'

# Generate dummy real news
true_df = pd.DataFrame({
    "title": [f"Real News Headline {i}" for i in range(len(fake_df))],
    "text": [f"This is a real news article content number {i}. It contains factual information." for i in range(len(fake_df))],
    "subject": ["News"] * len(fake_df),
    "date": pd.date_range(start="2022-01-01", periods=len(fake_df), freq="D").strftime('%B %d, %Y'),
    "label": ["REAL"] * len(fake_df)
})

# Combine and shuffle
combined_df = pd.concat([fake_df, true_df], ignore_index=True)
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Check basic info
print(combined_df['label'].value_counts())
print(combined_df.head())
