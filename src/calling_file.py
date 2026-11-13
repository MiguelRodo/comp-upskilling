import statistics_utils
import numpy as np

x = np.array([10, 12, 15, 13, 11])

cv = statistics_utils.coefficient_of_variation(x)

print(cv)
