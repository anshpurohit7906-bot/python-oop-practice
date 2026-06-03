import pandas as pd

data = {
    "Subject": ["Maths", "Physics", "CompSci"],
    "Marks": [85, 70, 98]
}

df = pd.DataFrame(data)
df.loc[3] = ["English", 95]
print(df.describe())
print(df)