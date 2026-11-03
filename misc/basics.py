n = 100
p_threshold = 0.05
study_name = "study_A"
analysis_complete = False

print(type(n))
print(type(p_threshold))
print(type(study_name))
print(type(analysis_complete))

# additional exercise
x = list(range(5)) # [0, 1, 2, 3, 4] (is this a list? I can't remember. Do we do (0, 1, 2, 3, 4) for dictionaries,which are like named lists?)
y = x # y will point at x exactly in memory, right? or do we have a new copy?

x.append(5) # so, now, a list from 0 to 5
y = y + [6] # no, y is going to be eityher from 0 to 6 or 0 to 6 without 5, I cant remmerb

x.append(7)
print(x)
print(y)

from pathlib import Path
p = Path(".")


# aliasing and copying lists
original = [10, 20, 30]
independent = original.copy()
original[0] = 99
print(original)
print(independent)
original = [[1, 2], [3, 4]]
independent = original.copy() # this is a shallow copy, so the inner lists are still
original[0] = [99, 99]
print(original)
print(independent)


original = [[1, 2], [3, 4]]
independent = original.copy()
original[0] = 1
print(original)
print(independent)

original = [[1, 2], [3, 4]]
independent = original.copy()
original[0].append(99)
print(original)
print(independent)

original = [10, 20, 30]
alias = original
independent = original.copy()
alias[0] = 99
print(original) # first element 99, because it and alias are pointing at the same object in memory, and will until the names are assigned to objects that do not point at that same object
print(alias) # first element 99, of course
print(independent)
independent[2] = 50
print(original)
print(alias)
print(independent)

measurements = [12, 15, 18, 21, 24, 27, 30]

measurements[0]
measurements[-1]
measurements[2]
measurements[0:3]
measurements[2:5]
measurements[4:]
measurements[::2]

scores = [72, 81, 65]

new_scores = [90, 88]

# tuples
tuple_a1 = (10, 20, 30)
tuple_a2 = (10,)
list_a3 = [10]
tuple_a4 = ([10],)

# b: immutability
x = (10, 20, 30)
x[0] = 99
x.append(40)
y = x.append(40)

y = x + (40,)

# c
x = ([1, 2],) # tuple
y = x # points y at x

x[0].append(3) # x is now a tuple with first element [1, 2, 3]

print(x)
print(y) # same as x, as its first element was pointing at the same object as x

x[0] = [1]

# exercise 7: nested immutability
data = ([1, 2], (3, 4), 5.0)

data[0].append(10) # first element becomes a list with 10 at the end
data[1][1] = 0 # first element's second element becomes 0
data[0] = [7, 8] # error, as the tuple element cannot be assigned to a new object
data[0][1] = 50 # typle's first elmeent's second elmeenent becomes 50
data[2] = 6.0 # error, as we're now re-assiging a tple element

([1, 50, 10], (3, 4), 5.0)

data = ([1, 2], (3, 4), 5.0)
data[0].append(99)

# exercise 8
result = ("model_A", 0.85, 120)

## 1
model, accuracy, n = result
print(model)
y = type(model)
print(accuracy)
type(accuracy)
print(n)
type(n)
accuracy, n = n, accuracy

double_tuple = (("a", "b"), ("c", "d"))
t0, t1 = double_tuple

# exercise 9
x = [3, 1, 4, 1, 5]

# part a
type(x) # list, obviously
dir(x) # lists methods, not sure if it lists attributes
x.sort() # sorts
help(x.sort)
# can't remeber how to work out if its' callable, or what that means
callable(x.sort)

# b
x = [3, 1, 4, 1, 5]
id_orig = id(x)
x.sort()
id_sorted = id(x)
id_orig == id_sorted

x = [3, 1, 4, 1, 5]
y = x
x = sorted(x) # sorted in ascending order
# could also have done x.sorted(), 
# in which case y would have changed as well
id(x) == id(y)

# exercise 10
experiment = (
    "Trial_A",
    [0.12, 0.15, 0.11],
    3
)
name, measurements, n = experiment
type(name)
type(measurements)
type(n)
# is(measurements, experiment[1])
measurements is experiment[1]
measurements.append(0.14)
experiment # changed
n # not changed
# can chagne because object being referred to 
# has to be the same object but it itself can change

# part c
# bug, as that's changing what we're senidng the last elmeent to
updated_experiment = (name, measurements, len(measurements))
experiment is updated_experiment

updated_experiment[1] is experiment[1]

independent_experiment = (name, measurements.copy(), len(measurements))
independent_experiment[1].append(0.20)
print(experiment)
print(updated_experiment)
print(independent_experiment)
# only independnet has it because the measurements it has is a copy