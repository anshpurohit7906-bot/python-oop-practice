import numpy as np

'''multidimentional array'''
# num = np.array([1,2,3,4])
# num *=2
# print(num)
# print(num.ndim) #Tells about the dimension of the array


# num = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                #  [[10,11,12],[13,14,15],[16,17,18]],
                #   [[19,20,21],[22,23,24],[25,26,27]]])

# print(num.shape)#gives the shape of the array in the form of(depth,row,column)
# print(num[1,0,2])#multidimensional indexing it gives the the element at the given index
#                  in the form (depth,row,column)

# sum = num[0,0,0] + num[1,0,2] + num[2,0,1]
# print(sum)


'''Slicing'''

num = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

#print(num) #num[start:end:step]

'''  for rows  '''
#print(num[1])
# print(num[0:4:2])
# print(num[-1])
# print(num[:3])
# print(num[::2])
#print(num[::-2])

'''   for columns  '''
# print(num[0,0])# this print the first column in the first row 
# print(num[:,0])
# print(num[1:,0:2])
# print(num[:,-1])
# print(num[:,::2])
# print(num[::2,::-2])

'''   arithmetics  '''

#Scalar arithmetics

# num = np.array([1.01,2.25,3.8])

# print(num +1)
# print(num - 2)
# print(num  * 3)
# print(num / 4)
# print(num **5)

#Vectorized Math functions

# print(np.sqrt(num))
# print(np.round(num))
# print(np.floor(num))
# print(np.ceil(num))
# print(np.pi)

''' Element-wise Arithmetic'''

# num1 = np.array([1,2,3])
# num2 = np.array([4,5,6])

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 ** num2)

'''  Comparison Operators'''

# num = np.array([54,26,84,69,14,9,78,95,32,0])

# print(num == 0)
# print(num>= 60)

# num[num<33] = 0
# print(num)

'''     Broadcasting   '''

# num1 = np.array([[1,2,3,4],
#                  [5,6,7,8],
#                  [9,10,11,12],
#                  [13,14,15,16]])
# num2 = np.array([[1],[2],[3],[4]])

# print(num1.shape)
# print(num2.shape)

# print(num1 * num2)#broadcasting only works when the dimensions of both the 
#                   #array are same or if one of them has a single row or column  
                  
'''Aggregrate Functions'''

# num = np.array([[1,2,3,4,5],
#                 [6,7,8,9,10],
#                 [11,12,13,14,15]])

# print(np.sum(num))
# print(np.diff(num))# subtracts the [a+1]index with the [a] index, like num[2]-num[1]
# print(np.mean(num))# provides the average or mean of all the elements in the array
# print(np.std(num))# standard deviation
# print(np.var(num))#variance
# print(np.max(num))# maximum value in the array 
# print(np.min(num))# minimum value in the array 
# print(np.argmax(num))# gives the index of the maximum value in the array 
# print(np.argmin(num))# gives the index of the minimum value in the array 

# print(np.sum(num , axis= 0))# adds all the columns with each other(vertical)
# print(np.sum(num, axis=1))# adds all the rows with each other(horizontal)

''' Filtering'''

# ages = np.array([[17,48,65,36,94,22,23],
#                 [23,67,15,6,9,78,14]])

# teenagers = ages[(ages<18) & (ages>=12)]
# child = ages[ages<12]
# adult = ages[((ages>18) & (ages<=60))]
# seniors = ages[ages>65]
# a = np.where(ages>=18,ages,0 )#retains the shape as in "ages", where = (condition ,[x,y], change the value of others )
# print(a)

''' Random numbers'''

##For integers

# random = np.random.default_rng(seed=1)#seed will give the same program output everytime 

# print(random.integers(low=1 , high = 67))#generates a random no. between 1 and 67 (excluding 67)
# print(random.integers(low=1 , high = 67, size=3)) # set the size to 3 no.s 
# print(random.integers(low=1 , high = 67, size=(3,3)))# now the size is set for a 3X3 matrix


##For floating - point numbers

# np.random.seed(seed=1)

# print(np.random.uniform(low=-1 , high=1 ,size = (3,2)))


##Shuffling an array

#random = np.random.default_rng()

# num = np.array([5,4,3,2,1])
# random.shuffle(num)
# print(num)

# fruits = np.array(["Apple" , "Banana","Coconut","Pear","Grapes","Mango"])
# random.shuffle(fruits)
# fruit = random.choice(fruits, size = (3,3 ))
# print(fruits)
# print(fruit)
