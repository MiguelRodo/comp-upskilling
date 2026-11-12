def calculate_mean(x):
  return sum(x) / len(x)

measurements = [0.12, 0.15, 0.11, 0.20]

calculate_mean(measurements)

import numpy as np

x = np.array([0.12, 0.15, 0.11, 0.20])

x * 2
x.mean()
x.sum()
x.len()
len(x)
x.__len__()

def classify_response(x):
  return None if x is None else ("High" if x > 0.8 else "Low")

classify_response(0.91)   # "High"
classify_response(0.65)   # "Low"
classify_response(0.8)    # "Low"
y = classify_response(None)   # None
type(y)


def modify_value(x):
    x = x + 10
    return x

a = 5
b = modify_value(a)

print(a) # 5
print(b) # 15
# 3. I hope not, else life is confusing! I would think we're passing the value of a, not a itself, assigned to x.
# 4. rebindiing a name, I'm not sure if you mean just assigning a new object to a name, or if you mean taking its value and putting that value under another name (as a copy, I guess; I'm not sure what would happen if a were, like, a list)


def add_measurement(values):
    values.append(0.5)

measurements = [0.1, 0.2]
result = add_measurement(measurements)

print(measurements)
print(result)

# 1. 0.1, 0.2 and 0.5)
# 2. same
# 3. They shouldn't be! Oh, shucks, we didn't return result. What if we di? 


def add_measurement_return(values):
    return values.append(0.5)

result_return = add_measurement_return(measurements)
print(result_return)

# okay, so we didn't return it even then!


def add_measurement_return_object(values):
    values.append(0.5)
    return values

result_return_object = add_measurement_return_object(measurements)
print(result_return_object)

def standardise(x, mean = 0, sd = 1):
  return (x - mean) / sd
standardise(0.5)
standardise(5, 2, 3)
standardise(5, sd = 2)
standardise(x = 5, sd = 2, mean = 1)


def calculate(x, y=10):
    return x + y

calculate(5) # 15
calculate(5, 20) # 25 
calculate(y=20, x=5) # 25
calculate(x=5, 20) # error (position after keyword argument)
calculate(5, x=10) # 15

# 1. well, I am not sure, but I know you *want* keywords after position
# 2. If it does, because o fht eabove
# 3
def calculate(y, x=10):
  return y + x

# 4
calculate(5)

# part d
def add_result(value, results=[]):
  results.append(value)
  return results

a = add_result(10)
b = add_result(20)

print(a) # [10]
print(b) # [10]
print(a is b) # False
# yes, a new empty lsit is created eachtime


def collect(x, values=None):
    if values is None:
        values = []
    values.append(x)
    return values

a = collect(1) # [1]
b = collect(2, a) # [1, 2]
c = collect(3) # [3]

print(a)
print(b)
print(c)
print(a is b) # false
