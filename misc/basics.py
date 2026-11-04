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
scores.append(75)
scores.append(new_scores)
scores = [71, 81, 65]
scores.extend(new_scores)
print(scores) # now, we're "binding" the list on, rather than adding the list as an additional element
