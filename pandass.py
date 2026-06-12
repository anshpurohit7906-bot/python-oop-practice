import pandas as pd

#print(pd.__version__)

'''  Series  '''

#Using Lists

# data = [1,2,3,4,5]

# series = pd.Series(data, index = ["A","B","C","D","E"])#A Series stores data along with labels/indexes and datatype information.
#                                                        # index customizes the labels of the elements
# series.loc["C"] = 67 # updates the value having label/index = "C"

# print(series)
# print(series.loc["A"])#Returns the element having the label 'A'
# print(series.iloc[4]) # returns the element having the integer location "4"
#print(series[series>2]) # returns the series satisfying the condition

#Using dictionaries

# marks = {"Maths": 85 , "Physics": 56 , "CompSci": 98 , "English" : 95 , "Chemistry": 27}

# series = pd.Series(marks)# no need to mention index while using dictionary 
# series.loc["Physics"] += 14# updates the  marks in physics by adding 14

# print(series)
# print(series.loc["Maths"])
# print(series.loc["Physics"])
# print(series[series>50])