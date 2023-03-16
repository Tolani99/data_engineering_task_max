"""
6. What is the specialization of the majority of the candidates who are not placed?
To determine the specialization of the majority
of the candidates who are not placed, 
we can create a bar plot of the count of candidates 
by specialization, grouped by placement status.
"""
# Import from basic module
from basic_module import sns
from basic_module import plt
from basic_module import df

# create a bar plot of the count of candidates by specialization, grouped by placement status
sns.countplot(x='specialisation', hue='status', data=df)

# add labels and title
plt.xlabel('MBA Specialization')
plt.ylabel('Count')
plt.title('Count of Candidates by MBA Specialization and Placement Status')

plt.show()
"""
From the bar plot, we can see that the majority of candidates who are not placed have a specialization in Marketing & Finance.
"""
