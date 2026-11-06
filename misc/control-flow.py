p_value = 0.03
sample_size = 120
converged = True

if p_value < 0.05 and sample_size >= 100 and converged:
  print("Acceptable result")
else:
  print("Review required")

status = "pending"

if status == "pending" or status == "failed":
  print("Not complete")
else:
  print("Complete")

if ("pending", "failed").__contains__(status):
  print("Not complete")
else:
  print("Complete")

if status in ("pending", "failed"):
  print("Not complete")
else:
  print("Complete")


x = 0

if x != 0 and 10 / x > 2:
    print("A")
else:
    print("B") # obviously B because x is 0. ZeroDivisionError only if it's not lazy in its evaluation, but I'm sure it is lazy


True and False # False
True or False # Trye
not True # False
0 or 5 # 5
3 and 7 # 7

1 and 0
0 or 1

# exercise 19
measurements = [0.12, 0.15, 0.11, 0.2]
for x in measurements:
  print(x * 100)

participants = ["Alice", "Bob", "Charlie"]
for i in enumerate(participants):
  print(str(i[0]) + " " + i[1])
  print(i[0], i[1])
  #print(i)
  #print(i[0])
  #print(i[1])

for i in enumerate(participants):
  print(i * 2)

for index, name in enumerate(participants):
  print(index, name)

# parts c-e
responses = {
  101: 0.82,
  102: 0.65,
  103: 0.91
}

for x in responses.items():
  id, response = x
  print(id, response)

for pid, response in responses.items():
  print(pid, response)

n_g08 = 0
for response in responses.values():
  if response > 0.8:
    n_g08 += 1

print(n_g08)

values = [2, -1, 5]

for x in values:
    x = x * 2

print(values)

for tpl in enumerate(values):
  values[tpl[0]] = 2 * tpl[1]
  # values[i] = 2 * values[i]
print(values)

for i, val in enumerate(values):
  values[i] = 2 * val

for i in range(len(values)):
  values[i] *= 2
