
"""
3.Is there a relationship between ssc_p and hsc_p for the candidates
who took Science or Commerce as streams for higher education?
To answer this question,
we can create a scatter plot showing the relationship
between ssc_p and hsc_p for the candidates who took
Science or Commerce as streams for higher education
"""
# Import from basic module
from basic_module import df
from basic_module import plt

# filter the data for Science and Commerce streams
df_science_commerce = df[df['hsc_s'].isin(['Science', 'Commerce'])]

# create a scatter plot
df_science_commerce.plot(kind='scatter', x='ssc_p', y='hsc_p')
plt.title('Relationship between ssc_p and hsc_p for Science/Commerce stream')
plt.xlabel('ssc_p')
plt.ylabel('hsc_p')
plt.show()
"""
The resulting scatter plot shows there is a relationship
between ssc_p and hsc_p for the candidates who took
Science or Commerce as streams for higher education.
The closer the data points come to forming a straight line when plotted,
the higher the correlation between the two variables,
or the stronger the relationship.
Since the data points make a straight line going
from near the origin out to high y-values,
the variables are said to have a positive correlation.
"""
