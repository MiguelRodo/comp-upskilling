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

# exercise 20
i = 0

while i < 5:
  print(i)
  i += 2

# part a
n = 1
while n < 11:
  print(n)
  n += 1

# part b
measurements = [0.12, 0.15, 0.18, 0.95, 0.22, 0.30]

for x in measurements:
  print(x)
  if x > 0.8:
    break

# part c
for x in measurements:
  if x >= 0.3:
    continue
  print(x)

# part d
i = 0

while i < 5:
    i += 1

    if i == 2:
        continue

    if i == 4:
        break

    print(i)

# will print just 1 and 3
# skips 2 because of continue before print
# doesn't do 4 or 5 because the break check
# happens first

# part e 
statuses = [
    "success",
    "failed",
    "success",
    "failed",
    "failed",
    "success"
]

n_failure = 0

for index,status in enumerate(statuses):
  print("Processing")
  n_failure += 1 if status == "failed" else 0
  if index + 1 == len(statuses) or n_failure == 3:
    print("Encourated " + str(n_failure) + " failure" + ("s" if n_failure != 1 else ""))
    if n_failure == 3:
      break

# exercise 21
participants = [
  {"id": 101, "response": 0.82, "status": "complete"},
  {"id": 102, "response": 0.65, "status": "complete"},
  {"id": 103, "response": None, "status": "pending"},
  {"id": 104, "response": 0.91, "status": "complete"},
  {"id": 105, "response": 0.73, "status": "failed"},
  {"id": 106, "response": 0.88, "status": "complete"}
]

# part a
for x in participants:
  if x["status"] == "complete" and x["response"] > 0.8:
    print(str(x["id"]) + ": " + str(x["response"]))

# part a
for x in participants:
  if x["status"] == "complete" and x["response"] > 0.8:
    print(f'{x["id"]}' + ": " + f'{x["response"]}')


for x in participants[0:1]:
  print(x["id"])
  print(type(x["id"]))
  print(str(x["id"]))
  print(type(str(x["id"])))

# part b
count_dict = {
  "n_complete": 0, "n_pending":  0, "n_failed":  0, "n_complete_g08":  0
  }
for x in participants:
  if x["status"] == "complete":
    count_dict["n_complete"] += 1
    if x["response"] > 0.8:
      count_dict["n_complete_g08"] += 1
  elif x["status"] == "pending":
    count_dict["n_pending"] += 1
  elif x["status"] == "failed":
    count_dict["n_failed"] += 1
  else:
    print("error")

print(count_dict)

pid_idx = 0
complete_list = []
while pid_idx < (len(participants)):
  participants_curr = participants[pid_idx]
  if participants_curr["status"] == "complete" and participants_curr["response"] is not None:
    complete_list.append(participants_curr["response"])
  pid_idx += 1
print(complete_list)

for x in participants:
  status = x["status"]
  response = x["response"]
  if response is not None and status == "complete":
    if response > 0.8:
      x.__setitem__("high_response", True)
    else:
      x.__setitem__("high_response", False)
  else:
    x.__setitem__("high_response", None)


for x in participants:
  status = x["status"]
  response = x["response"]
  if response is not None and status == "complete":
    if response > 0.8:
      x["high_response"] = True
    else:
      x["high_response"] = False
  else:
    x["high_response"] = None

for x in participants:
  status = x["status"]
  response = x["response"]
  if response is not None and status == "complete":
    x["high_response"] = response > 0.8
  else:
    x["high_response"] = None


# 1. existing dictionary
# 2. yes
# 3. yes. Well, I'm not sure. Here we seem to be assigning it to a new obje ct
# okay, I just checked, and no, it does not. 
# so, [] is modification in place (for dictionaries, anyway)
# 4. I suppose because well, I'm not sure what would happen otherwie.map
# okay, I just get, and it says you can't copmapre between NoneType and flaot
# with > 

for x in participants:
  x = "a"

print(participants)

x = None
if x > 0.8:
  print("abc")
else:
  print("def")
