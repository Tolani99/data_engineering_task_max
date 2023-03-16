"""
7. What is the undergraduate degree type
of the majority of the candidates who are not
placed?
To determine the undergraduate degree type of the
majority of the candidates who are not placed,
we can create a bar plot of the count of candidates
by undergraduate degree type, grouped by placement status.
"""
# Import basic module
from basic_module import sns
from basic_module import plt
from basic_module import df

# create a bar plot of the count of candidates by
# undergraduate degree type, grouped by placement status
sns.countplot(x='degree_t', hue='status', data=df)

# add labels and title
plt.xlabel('Undergraduate Degree Type')
plt.ylabel('Count')
plt.title('Candidates by Undergraduate Degree Type and Placement Status')

plt.show()
"""
From the bar plot, we can see that the majority of candidates
who are not placed have an undergraduate degree type of Commerce.
"""
