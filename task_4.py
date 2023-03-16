"""
4. Candidates with which undergraduate degree type have
   the highest mean MBA percentage?
To answer this question, we can create a bar chart
showing the average MBA percentage by degree_t.
"""
# Import from basic module
from basic_module import df
from basic_module import plt

# group the data by degree_t and calculate the mean MBA percentage
degree_mean_mba = df.groupby('degree_t')['mba_p'].mean()

# create a bar chart
degree_mean_mba.plot(kind='bar')
plt.title('Average MBA percentage by undergraduate degree type')
plt.xlabel('Undergraduate degree type')
plt.ylabel('Average MBA percentage')
plt.show()
"""
The resulting bar chart will shows that science
degree type has the highest mean MBA percentage.
"""
