"""
To determine whether the institute should alter its selection criteria 
for work experience to increase the average placement salary, 
we can analyze the relationship between work experience and salary.

We can start by comparing the average salaries of candidates with
and without work experience. To do this, we can group the data by 
the "workex" column and calculate the mean of the "salary" column for each group.
"""
from basic_module import df
import pandas as pd

# group data by work experience and calculate mean salary
grouped = df.groupby('workex')['salary'].mean()

print(grouped)


"""
This outputs the mean salary for candidates with and without work experience
If the average salary of candidates with work experience
is significantly higher than the average salary of candidates
without work experience, it may be worth considering 
altering the selection criteria for work experience.

However, it is important to note that outliers should not be
removed when making this analysis. Outliers may skew the results 
and make it difficult to determine whether there is a significant
difference in salary between candidates with and without work experience. 
Therefore,considering the entire
range of data when making this analysis,
while work experience may be a factor in determining placement salary, it is not the only factor and the institute should consider other criteria as well.
"""
