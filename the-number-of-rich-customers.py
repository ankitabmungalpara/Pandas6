"""

Table: Store

+-------------+------+
| Column Name | Type |
+-------------+------+
| bill_id     | int  |
| customer_id | int  |
| amount      | int  |
+-------------+------+
bill_id is the primary key (column with unique values) for this table.
Each row contains information about the amount of one bill and the customer associated with it.
 

Write a solution to report the number of customers who had at least one bill with an amount strictly greater than 500.

The result format is in the following example.

 
Example 1:

Input: 
Store table:
+---------+-------------+--------+
| bill_id | customer_id | amount |
+---------+-------------+--------+
| 6       | 1           | 549    |
| 8       | 1           | 834    |
| 4       | 2           | 394    |
| 11      | 3           | 657    |
| 13      | 3           | 257    |
+---------+-------------+--------+
Output: 
+------------+
| rich_count |
+------------+
| 2          |
+------------+
Explanation: 
Customer 1 has two bills with amounts strictly greater than 500.
Customer 2 does not have any bills with an amount strictly greater than 500.
Customer 3 has one bill with an amount strictly greater than 500.

"""

# Approach:
# 1. Filter the 'store' DataFrame to include only rows where the 'amount' is greater than 500.
# 2. Count the number of unique 'customer_id' values in the filtered DataFrame.
# 3. Create a new DataFrame with the count and return it.

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:

    rich_customers = store[store['amount'] > 500]
    
    count = rich_customers['customer_id'].nunique()

    answer = pd.DataFrame({'rich_count': [count]})

    return answer
