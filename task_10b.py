"""
10. What are the specialization and the graduation degree type of 
the majority of the top 10 candidates placed, based on salary?
To answer this question, we can use the same code 
as in the previous question to filter the data to
include only placed candidates and sort the data
by salaryin descending order. 
We can then select the top 10 candidates and count
the number of candidates with each 
specialization and graduation degree type.
"""
# Import Basic module
from basic_module import df
# select the top 10 candidates placed by salary, and group by their specialization and graduation degree type
top_10 = df[df["status"] == "Placed"].nlargest(10, "salary")
top_10_grouped = top_10.groupby(["specialisation", "degree_t"]).size().reset_index(name="count")

# find the majority specialization and graduation degree type
majority_specialization = top_10_grouped.loc[top_10_grouped["count"].idxmax()]["specialisation"]
majority_degree_type = top_10_grouped.loc[top_10_grouped["count"].idxmax()]["degree_t"]

# print the results
print("The majority specialization among the top 10 candidates placed is:", majority_specialization)
print("The majority graduation degree type among the top 10 candidates placed is:", majority_degree_type)
