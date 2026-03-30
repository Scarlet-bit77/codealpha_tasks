# eda.py - Complete EDA + Visualizations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Load CSV with proper encoding ---
df = pd.read_csv("books.csv", encoding="utf-8-sig")

# --- Step 2: Initial Exploration ---
print("----- First 5 rows -----")
print(df.head())

print("\n----- Data Info -----")
print(df.info())

# --- Step 3: Clean Price column ---
df['Price'] = df['Price'].str.replace(r'[^0-9.]', '', regex=True).astype(float)

print("\n----- After Cleaning Price -----")
print(df.head())

# --- Step 4: Summary Statistics ---
print("\n----- Summary Statistics -----")
print(df.describe())

# --- Step 5: Max, Min, Average Price ---
print("\nMost expensive book:", df['Price'].max())
print("Cheapest book:", df['Price'].min())
print("Average price:", df['Price'].mean())

# --- Step 6: Missing Values and Duplicates ---
print("\nMissing values per column:\n", df.isnull().sum())
print("Duplicate titles:", df.duplicated(subset=['Title']).sum())

# --- Step 7: Visualizations ---

# 1️⃣ Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=10, color='#FFA500',  # brighter orange
             kde=True,  # adds a smooth curve over bars
             edgecolor='black')  # adds black edges for clarity
plt.title("Distribution of Book Prices", fontsize=16, fontweight='bold')
plt.xlabel("Price (£)", fontsize=12)
plt.ylabel("Number of Books", fontsize=12)
plt.grid(alpha=0.3)  # subtle grid lines
plt.show()

# 2️⃣ Top 10 Most Expensive Books
top_books = df.sort_values(by='Price', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x='Price', y='Title', data=top_books, palette='magma')
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.show()

# 3️⃣ Boxplot to see Price Outliers
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Price'], color='#FFD700', linewidth=2)  # golden color, thicker lines
plt.title("Book Price Boxplot", fontsize=16, fontweight='bold')
plt.xlabel("Price (£)", fontsize=12)
plt.grid(alpha=0.3)
plt.show()