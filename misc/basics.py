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