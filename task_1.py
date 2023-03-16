"""
1. Which gender scored better in their MBA on average?
To answer this question,
we can calculate the mean MBA percentage by gender
and create a bar chart to visualize the results.
"""
# Import from basic module
from basic_module import df
from basic_module import plt

# Group the data by gender and calculate the mean MBA pecentage
gender_mean_mba = df.groupby('gender')['mba_p'].mean()

# Create a bar chart
gender_mean_mba.plot(kind='bar')
plt.title('Average MBA percentage by Gender')
plt.xlabel('Gender')
plt.ylabel('Average MBA percentage')
plt.show()
"""
The bar chart shows the mean MBA percentage for each gender.
We can see that on average,
male students scored slightly higher in their MBA than female students.
"""
