import numpy as np

random = np.random.default_rng(seed=1)

marks = (random.integers(low =40 , high = 100 , size = 10))
print(marks)
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(marks[marks>75])
print(np.where(marks>50 , marks , 0))
random.shuffle(marks)
print(marks)