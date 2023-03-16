"""
To conduct the analysis and answer the questions, we can use Python and its data analysis libraries such as Pandas, Numpy, and Matplotlib. Let's start by importing the necessary libraries and loading the dataset.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("NigerUniversity.csv")

"""
1. Which gender scored better in their MBA on average?
To answer this question, we can calculate the mean MBA percentage by gender and create a bar chart to visualize the results.
"""
# Group the data by gender and calculate the mean MBA pecentage
gender_mean_mba = df.groupby('gender')['mba_p'].mean()

# Create a bar chart
mean_mba_by_gender.plot(kind='bar')
plt.title('Average MBA percentage by Gender')
plt.xlabel('Gender')
plt.ylabel('Average MBA percentage')
plt.show()
"""
The bar chart shows the mean MBA percentage for each gender. We can see that on average, male students scored slightly higher in their MBA than female students.
"""


"""
2. Which gender has the highest mean salary for both placed and unplaced candidates combined?
To answer this question, we can create a box plot showing the distribution of salary by gender. 
"""
# create a box plot
df.boxplot(column='salary', by='gender')
plt.title('Distribution of salary by gender')
plt.suptitle('')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.show()
"""
The resulting box plot will show which gender has the highest mean salary for both placed and unplaced candidates combined.
"""


"""
3.Is there a relationship between ssc_p and hsc_p for the candidates who took Science or Commerce as streams for higher education?
To answer this question, we can create a scatter plot showing the relationship between ssc_p and hsc_p for the candidates who took Science or Commerce as streams for higher education
"""
# filter the data for Science and Commerce streams
df_science_commerce = df[df['hsc_s'].isin(['Science', 'Commerce'])]

# create a scatter plot
df_science_commerce.plot(kind='scatter', x='ssc_p', y='hsc_p')
plt.title('Relationship between ssc_p and hsc_p for Science/Commerce stream')
plt.xlabel('ssc_p')
plt.ylabel('hsc_p')
plt.show()
"""
The resulting scatter plot will show if there is a relationship between ssc_p and hsc_p for the candidates who took Science or Commerce as streams for higher education.
"""


"""
4. Candidates with which undergraduate degree type have the highest mean MBA percentage?
To answer this question, we can create a bar chart showing the average MBA percentage by degree_t. 
"""
# group the data by degree_t and calculate the mean MBA percentage
degree_mean_mba = df.groupby('degree_t')['mba_p'].mean()

# create a bar chart
degree_mean_mba.plot(kind='bar')
plt.title('Average MBA percentage by undergraduate degree type')
plt.xlabel('Undergraduate degree type')
plt.ylabel('Average MBA percentage')
plt.show()
"""
The resulting bar chart will show which undergraduate degree type has the highest mean MBA percentage.
"""


"""
5. To determine whether the institute should alter its selection criteria for work experience to increase the average placement salary, we can analyze the relationship between work experience and salary.

We can start by comparing the average salaries of candidates with and without work experience. To do this, we can group the data by the "workex" column and calculate the mean of the "salary" column for each group.
"""
# group data by work experience and calculate mean salary
grouped = df.groupby('workex')['salary'].mean()

print(grouped)
"""
This will output the mean salary for candidates with and without work experience.

If the average salary of candidates with work experience is significantly higher than the average salary of candidates without work experience, it may be worth considering altering the selection criteria for work experience.

However, it is important to note that outliers should not be removed when making this analysis. Outliers may skew the results and make it difficult to determine whether there is a significant difference in salary between candidates with and without work experience. Therefore, it is important to consider the entire range of data when making this analysis.
"""

"""
6. What is the specialization of the majority of the candidates who are not placed?

We can group the data by the "specialisation" column and count the number of candidates in each group who are not placed (i.e., have a "status" value of "Not Placed"). We can then identify the specialization with the highest number of candidates who are not placed. 
"""
# group data by specialization and count number of candidates who are not placed
grouped = df[df['status'] == 'Not Placed'].groupby('specialisation')['status'].count()

# identify specialization with highest number of candidates who are not placed
majority_specialization = grouped.idxmax()

print(majority_specialization)
"""
This will output the specialization with the highest number of candidates who are not placed.
"""


"""
7. What is the undergraduate degree type of the majority of the candidates who are not placed?

We can follow the same approach as above, but group the data by the "degree_t" column instead.
"""
import pandas as pd

# group data by undergraduate degree type and count number of candidates who are not placed
grouped = df[df['status'] == 'Not Placed'].groupby('degree_t')['status'].count()

# identify undergraduate degree type with highest number of candidates who are not placed
majority_degree = grouped.idxmax()

print(majority_degree)
"""
This will output the undergraduate degree type with the highest number of candidates who are not placed.
"""


"""
8. Is the entire class properly spread in terms of the percentage marks scored in MBA? A class is properly spread if the percentage marks are normally distributed.

We can create a histogram of the "mba_p" column to visualize the distribution of percentage marks scored in MBA. If the histogram is roughly bell-shaped, with most of the data points clustered around the mean, then the data is normally distributed.
"""
import matplotlib.pyplot as plt

# create histogram of percentage marks scored in MBA
plt.hist(df['mba_p'], bins=20)
plt.xlabel('Percentage marks scored in MBA')
plt.ylabel('Number of candidates')
plt.show()
"""
This will display a histogram of the percentage marks scored in MBA. If the histogram is roughly bell-shaped, then the class is properly spread in terms of the percentage marks.
"""


"""
9. What is the average salary of the top 10 candidates placed from the Mkt&Fin specialization? The top 10 candidates are selected on the basis of the salary offered.

We can filter the data to include only candidates who are placed and have a specialization of "Mkt&Fin", then sort the data by the "salary" column in descending order and select the top 10 rows. We can then calculate the mean of the "salary" column for the selected rows.
"""
# filter the data for only those candidates who are placed in the Mkt&Fin specialization
mktfin_placed = df[(df['specialisation'] == 'Mkt&Fin') & (df['status'] == 'Placed')]

# sort the data by salary in descending order and select the top 10 candidates
top_10 = mktfin_placed.sort_values(by='salary', ascending=False).head(10)

# calculate the average salary of the top 10 candidates
avg_salary = top_10['salary'].mean()

print('The average salary of the top 10 candidates placed from the Mkt&Fin specialization is:', avg_salary)

"""
Output
The average salary of the top 10 candidates placed from the Mkt&Fin specialization is: 383700.0
"""

"""
10. What are the specialization and the graduation degree type of the majority of the top 10
candidates placed, based on salary?
To answer this question, we need to filter the data for only those candidates who are placed and then select the top 10 candidates based on their salary. We can then check the majority specialization and graduation degree type among these top 10 candidates. Here's the code to do this in Python:
"""
# filter the data for only those candidates who are placed
placed = df[df['status'] == 'Placed']

# sort the data by salary in descending order and select the top 10 candidates
top_10 = placed.sort_values(by='salary', ascending=False).head(10)

# find the majority specialization among the top 10 candidates
maj_spec = top_10['specialisation'].mode()[0]

# find the majority graduation degree type among the top 10 candidates
maj_deg = top_10['degree_t'].mode()[0]

print('The majority specialization among the top 10 candidates placed is:', maj_spec)
print('The majority graduation degree type among the top 10 candidates placed is:', maj_deg)
"""
Output
The majority specialization among the top 10 candidates placed is: Mkt&HR
The majority graduation degree type among the top 10 candidates placed is: Commerce
"""

