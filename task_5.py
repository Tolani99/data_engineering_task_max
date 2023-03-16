"""
5. Should the institute alter its selection criteria for work experience
to increase the average placement salary?
(Do not remove outliers while answering)

To answer the question of whether the institute should alter
its selection criteria for work experience to
increase the average placement salary,
we can use a box plot to visualize the relationship between
work experience and placement salary.
We can create a box plot of the
placement salary grouped by work experience and compare
the median salaries of candidates with and without work experience.
"""
# Import from basic module
from basic_module import sns
from basic_module import plt
from basic_module import df

# create a box plot of the placement salary grouped by work experience
sns.boxplot(x='workex', y='salary', data=df)

# add labels and title
plt.xlabel('Work Experience')
plt.ylabel('Placement Salary')
plt.title('Placement Salary by Work Experience')

plt.show()
"""
From the box plot, we can see that candidates with
work experience generally have higher median placement
salaries compared to candidates without work experience.
However, there is significant overlap between the two groups,
and there are also outliers in both groups.
Therefore, while work experience may be a
factor in determining placement salary,
it is not the only factor
and the institute should consider other criteria as well.
"""
