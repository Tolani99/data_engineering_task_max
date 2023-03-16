To analyze the data, you can use the following steps:

1. Import the necessary libraries and read the data into a pandas DataFrame.
2. Explore the data to get a better understanding of its structure and properties.
3. Clean the data by checking for missing or inconsistent values, and correcting or removing them if necessary.
4. Visualize the data to identify patterns and relationships between variables.
5. Perform statistical analyses, such as hypothesis testing or regression modeling, to answer the research questions posed by the senior board.

QUESTIONS AND LINES OF REASON
1. Which gender scored better in their MBA on average?
To determine this, we need to filter the dataset to only include placed candidates, then group the data by gender and calculate the mean MBA percentage. The gender with the higher mean MBA percentage will be the gender that scored better on average.

2. Which gender has the highest mean salary for both placed and unplaced candidates combined? Note that unplaced candidates have a salary of 0.
To determine this, we need to group the data by gender and calculate the mean salary for placed and unplaced candidates separately, then combine them to get the overall mean salary for each gender. The gender with the higher overall mean salary will be the gender with the highest mean salary for both placed and unplaced candidates combined.

3. Is there a relationship between ssc_p and hsc_p for the candidates who took Science or Commerce as streams for higher education?
To determine this, we need to filter the dataset to only include candidates who took Science or Commerce as their streams for higher education, then create a scatter plot with ssc_p on the x-axis and hsc_p on the y-axis. If there is a strong positive correlation between ssc_p and hsc_p, then there is a relationship between the two variables.
4. Candidates with which undergraduate degree type have the highest mean MBA percentage?
To determine this, we need to group the data by degree_t and calculate the mean MBA percentage for each degree type. The degree type with the higher mean MBA percentage will be the degree type with the highest mean MBA percentage.
Should the institute alter its selection criteria for work experience to increase the average placement salary? (Do not remove outliers while answering.)
To determine this, we need to compare the mean salary for candidates with work experience to the mean salary for candidates without work experience. If the mean salary for candidates with work experience is significantly higher than the mean salary for candidates without work experience, then it may be worth considering altering the selection criteria for work experience to increase the average placement salary.

5. What is the specialization of the majority of the candidates who are not placed?
To determine this, we need to filter the dataset to only include candidates who are not placed, then count the number of candidates in each specialization and identify the specialization with the highest count.

6. What is the undergraduate degree type of the majority of the candidates who are not placed?
To determine this, we need to filter the dataset to only include candidates who are not placed, then count the number of candidates in each undergraduate degree type and identify the degree type with the highest count.

7. Is the entire class properly spread in terms of the percentage marks scored in MBA? A class is properly spread if the percentage marks are normally distributed.
To determine this, we need to create a histogram of the MBA percentage and visually inspect the distribution. If the histogram is roughly bell-shaped and symmetrical, then the class is properly spread in terms of the percentage marks scored in MBA.

8. What is the average salary of the top 10 candidates placed from the Mkt&Fin specialization? The top 10 candidates are selected on the basis of the salary offered.
To determine this, we need to filter the dataset to only include placed candidates from the Mkt&Fin specialization, then sort the data by salary in descending order and select the top 10 candidates. Finally, we calculate the mean salary of the top 10 candidates.

9. What are the specialization and the graduation degree type of the majority of the top 10 candidates placed, based on salary?
To determine this, we need to filter the dataset to only include placed candidates, then sort the data by salary in descending

10. To answer this question using visualization tools, we can create a bar chart or a pie chart showing the distribution of the top 10 candidates placed by their specialization and graduation degree type.
