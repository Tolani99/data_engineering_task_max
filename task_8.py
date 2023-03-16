"""
8.Is the entire class properly spread in terms of the percentage marks scored in MBA? A class is properly spread if the percentage marks are normally distributed.
We can create a histogram of the "mba_p" column to visualize the distribution of percentage marks scored in MBA. If the histogram is roughly bell-shaped, with most of the data points clustered around the mean, then the data is normally distributed.
"""
# Import basic module
from basic_module import df
from basic_module import plt

# create histogram of percentage marks scored in MBA
plt.hist(df['mba_p'], bins=20)
plt.xlabel('Percentage marks scored in MBA')
plt.ylabel('Number of candidates')
plt.show()

"""
This displays a histogram of the percentage marks scored in MBA. Sincethe histogram is roughly bell-shaped, then the class is properly spread in terms of the percentage marks.
"""
