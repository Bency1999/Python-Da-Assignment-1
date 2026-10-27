import numpy as np

# Step 1: Create a 1D NumPy array
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print("Week 1 temperatures:", temperatures_w1)

# Step 2: Inspection and Properties
print("Shape:", temperatures_w1.shape)
print("Data type:", temperatures_w1.dtype)
print("Number of elements:", temperatures_w1.size)

# Step 3: Array Operations
temperatures_f = (temperatures_w1 * 9/5) + 32
print("Temperatures in Fahrenheit:", temperatures_f)

print("Maximum:", np.max(temperatures_w1))
print("Minimum:", np.min(temperatures_w1))
print("Mean:", np.mean(temperatures_w1))

# Step 4: Array Slicing and Indexing
print("First three days:", temperatures_w1[:3])
print("Weekend (last two days):", temperatures_w1[-2:])
print("Middle three days:", temperatures_w1[2:5])

# Step 5: Create a 2D array
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],  # Week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]   # Week 2
])
print("2D temperatures array:")
print(temperatures)

# Step 6: Inspect and slice the 2D array
print("Shape:", temperatures.shape)
print("Data type:", temperatures.dtype)
print("Total number of elements:", temperatures.size)

print("Week 1:", temperatures[0])
print("Week 2:", temperatures[1])
print("Weekend, Week 1:", temperatures[0, -2:])
print("Weekend, Week 2:", temperatures[1, -2:])
print("Weekends, both weeks:")
print(temperatures[:, -2:])

import pandas as pd

# Pandas Series - Step 1: Create a Series with custom indices
marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
)
print("Marks Series:")
print(marks)

# step 2: Indexing and Slicing
print("Mark of 1st rank (integer position):", marks.iloc[0])
print("Top 3 ranks using loc:")
print(marks.loc[['Rank1', 'Rank2', 'Rank3']])
print("Mark of 3rd rank using iloc:", marks.iloc[2])
print("Marks greater than 90:")
print(marks[marks > 90])

# Pandas Series - Step 3: Manipulating Series
# Modify the mark of the 1st rank student to 100
marks.loc['Rank1'] = 100
print("After modifying Rank1:")
print(marks)

# Remove the entry of the last rank
marks = marks.drop('Rank5')
print("After removing the last rank:")
print(marks)

# Compute CGPA by dividing each mark by 10
cgpa = marks / 10
print("CGPA:")
print(cgpa)

# Pandas DataFrame - Step 1: Create the DataFrame
transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing',
                        'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West',
               'North', 'East', 'West', 'South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})
print("Transactions DataFrame:")
print(transactions)

# Pandas DataFrame - Step 2: Data Exploration
print("Head:")
print(transactions.head())
print("Tail:")
print(transactions.tail())
print("Shape:", transactions.shape)
print("Column names:", list(transactions.columns))
print("Data types:")
print(transactions.dtypes)

print("ProductCategory and Amount only:")
print(transactions[['ProductCategory', 'Amount']])

print("Last 3 columns using iloc:")
print(transactions.iloc[:, -3:])

print("North region with Amount greater than 200:")
print(transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)])

print("Value counts for ProductCategory:")
print(transactions['ProductCategory'].value_counts())

print("Unique values in Region:")
print(transactions['Region'].unique())

print("Mean amount for each region:")
print(transactions.groupby('Region')['Amount'].mean())

# Pandas DataFrame - Step 3: Manipulating the DataFrame
# Modify the Amount for TransactionID 102 to 165
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
print("After modifying TransactionID 102:")
print(transactions)

# Add a new column 'Discount' (10% of Amount)
transactions['Discount'] = transactions['Amount'] * 0.10
print("After adding Discount column:")
print(transactions)

# Remove the row with TransactionID 109
transactions = transactions[transactions['TransactionID'] != 109]
print("After removing TransactionID 109:")
print(transactions)

# Delete the 'Discount' column
transactions = transactions.drop(columns='Discount')
print("After deleting Discount column:")
print(transactions)