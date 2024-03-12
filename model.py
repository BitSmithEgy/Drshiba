import pandas as pd

df = pd.read_csv('./ques1.csv')

filtered_df = df[df['course '] == 1]
print(filtered_df)

random_rows = filtered_df.sample(n=3)

# Print the result
print(random_rows)

values_list = random_rows.iloc[0, 1:3].tolist()

# Print the result
print(values_list)
