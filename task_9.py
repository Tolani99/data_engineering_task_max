"""
9. What is the average salary of the top 10 candidates placed from the Mkt&Fin specialization? The top 10 candidates are selected on the basis of the salary offered
We can filter the data to include only candidates who are placed and have a specialization of "Mkt&Fin", then sort the data by the "salary" column in descending order and select the top 10 rows. We can then calculate the mean of the "salary" column for the selected rows.
"""
# Import basic module
from basic_module import df
from basic_module import plt

# filter data to include only placed candidates with Mkt&Fin specialization
filtered = df[(df['status'] == 'Placed') & (df['specialisation'] == 'Mkt&Fin')]

# sort data by salary in descending order and select top 10 rows
top_10 = filtered.sort_values('salary', ascending=False).head(10)

# calculate mean salary of top 10 candidates
avg_salary = top_10['salary'].mean()

print('The average salary of the top 10 candidates placed from the Mkt&Fin specialization is:', avg_salary)

