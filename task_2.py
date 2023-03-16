"""
2. Which gender has the highest mean salary
for both placed and unplaced candidates combined?
To answer this question,
we can create a box plot showing the distribution of salary by gender.
"""
# Import from basic module
from basic_module import plt
from basic_module import df

# create a box plot
df.boxplot(column='salary', by='gender')
plt.title('Distribution of salary by gender')
plt.suptitle('')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.show()
"""
The resulting box plot shows which gender has
the highest mean salary for both placed and unplaced candidates combined.
"""
