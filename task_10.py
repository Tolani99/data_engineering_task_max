"10.What are the specialization and the graduation degree type of the majority of the top 10 candidates placed, based on salary?
To answer this question using visualization tools, we can create a bar chart or a pie chart showing the distribution of the top 10 candidates placed by their specialization and graduation degree type.
"""
# Import basic module
from basic_module import df
from basic_module import plt
from basic_module import sns

# Select the top 10 placed candidates based on salary
top_10 = df[df['status']=='Placed'].nlargest(10, 'salary')

# Create a countplot of the top 10 candidates' specialization
sns.countplot(data=top_10, x='specialisation')
plt.title('Specialization of top 10 placed candidates')
plt.show()

# Create a countplot of the top 10 candidates' graduation degree type
sns.countplot(data=top_10, x='degree_t')
plt.title('Graduation degree type of top 10 placed candidates')
plt.show()
"""
This code creates two plots showing the distribution
of the top 10 placed candidates by their
specialization and graduation degree type.
The first plot is a countplot showing the number of
candidates in each specialization,
and the second plot is a countplot showing the
number of candidates in each graduation degree type.
"""
