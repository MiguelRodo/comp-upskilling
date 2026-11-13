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

# exercise 24
x = 10

def calculate():
  y = 5
  return x + y

calculate()

def test(result = None):
  if result is None:
    result = []
  result.append(1)
  return result

test()


# part A

x = 10

def calculate():
    x = 20
    return x

y = calculate()

print(x) # 10
print(y) # 20

# part B

x = 10

def calculate():
  y = x + 5
  x = y + 2
  return x

calculate() # okay, I thought it would use x from the global scope, like x + y used x in the global scope in your example, but that's not what happened


# part c

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()

print(counter) # 2

# part d
results = [1, 2, 3]

def add_result():
    results.append(4)

add_result()
print(results) # [1, 2, 3, 4]

results = [1, 2, 3]

def add_result():
    results = results + [4]

add_result()

# exercise 25

## part a
def calculate_mean(*args):
  if not args:
    return None
  return sum(args) / len(args)

calculate_mean(2, 4, 6)
calculate_mean(10, 20)
calculate_mean()

## part b
def create_participant(id, **kwargs):
  participant = {"id": id}
  if kwargs is None or len(kwargs) == 0:
    return(participant)
  for key, value in kwargs.items():
    participant[key] = value
  return participant

create_participant(101)
create_participant(101, age = 35, response = 0.82, status = "complete")



# part c
def calculate(x, y, z):
  return x + y + z

values = [2, 3, 4]
parameters = {"x": 2, "y": 3, "z": 4}

# 9
# 9
# error (y and z not defined)
# either an error, because we're trying to unpack
# something that has names without acknowleding that it has names
# or no error because we're unpacking positionally
# ah, it passed just the keys!
# okay, I hadn't thought of that.
# if yuo loop  over a dictionary, it's also the 
# key rather than the value that's passed, right?


calculate(*values)
calculate(**parameters)
calculate(values)
calculate(*parameters)


for x in parameters:
  print(x)

for x in parameters.values():
  print(x)


# part d
def inspect(x, *args, **kwargs):
  print(x)
  print(args)
  print(kwargs)

inspect(10, 20, 30, name="study_A", alpha=0.05)
# x: 10
# args: (20, 30) (tuple)
# kwargs: {"name": "study_A", "alpha": 0.05}


# part e
# i would think the first is, because args is
# taking unnamed arguments, which is fine,
# so they can come before that with the default parameter
# value

# analyse(1, 2, 3): ((1, 2), 3) OR ((1, 2, 3), 0.05) (not sure).
# okay, it's the later, *args will suck up everything
# analyse(1, 2, threshold=0.01): ((1, 2), 0.01)
def analyse(*args, threshold=0.05):
    return args, threshold

analyse(1, 2, 3)
analyse(1, 2, threshold=0.01)


# you can never supply threshold as an ordinary positional argument


# exercise 26

participants = [
    {"id": 101, "response": 0.82, "status": "complete"},
    {"id": 102, "response": 0.65, "status": "complete"},
    {"id": 103, "response": None, "status": "pending"},
    {"id": 104, "response": 0.91, "status": "complete"},
    {"id": 105, "response": 0.73, "status": "failed"},
    {"id": 106, "response": 0.88, "status": "complete"}
]

# part a
def get_valid_responses(pid_list):
  resp_list = []
  for x in pid_list:
    if x["status"] == "complete" and x["response"] is not None:
      resp_list.append(x["response"])
  return resp_list

valid = get_valid_responses(participants)


## part b

### version 1
def summarise_responses(*args):
  if not args:
    return {"n": 0, "mean": None}
  return {"n": len(args), "mean": sum(args) / len(args)}

summarise_responses(*valid)
# {"n": 4, "mean": 0.815}

summarise_responses(*[])
# {"n": 0, "mean": None}


### version 2
def summarise_responses_ifelse(*args):
  n = len(args)
  return {"n": n, "mean": None if n == 0 else sum(args) / n}

summarise_responses_ifelse(*valid)
# {"n": 4, "mean": 0.815}

summarise_responses_ifelse(*[])
# {"n": 0, "mean": None}


### version 3
def summarise_responses_list(resp_list):
  n = len(resp_list)
  return {"n": n, "mean": None if n == 0 else sum(resp_list) / n}

summarise_responses_list(valid)
# {"n": 4, "mean": 0.815}

summarise_responses_list([])
# {"n": 0, "mean": None}


## part c

### version 1
def classify_responses(resp_list, threshold=0.8):
  gt_list = []
  if not resp_list:
    return gt_list
  for x in resp_list:
    gt_list.append(x > threshold)
  return gt_list

classify_responses(valid)
# [True, False, True, True]

classify_responses(valid, threshold=0.9)
# [False, False, True, False]

### version 2
def classify_responses_args(*args, threshold=0.8):
  gt_list = []
  if not args:
    return gt_list
  for x in args:
    gt_list.append(x > threshold)
  return gt_list

classify_responses_args(*valid)
# [True, False, True, True]

classify_responses_args(*valid, threshold=0.9)
# [False, False, True, False]

## part d

def add_flag(records):
    for record in records:
        record["reviewed"] = True
    return records

original = [{"id": 1}, {"id": 2}] # list, where each element is a dictionary
updated = add_flag(original) # okay, for each record, we are adding the reviewed key
 
# print(original):  [{"id": 1, "reviewed": True}, {"id": 2, "reviewed": True}] 
# print(updated): [{"id": 1, "reviewed": True}, {"id": 2, "reviewed": True}] 
# print(original is updated): True (we never created a new outer container)

print(original)
print(updated)
print(original is updated)

def add_flag(records):
    records_new = records.copy() # elements themselves point to the same objects
    for record in records_new:
        record_new = 
    return records


def add_flag_new(records):
  records_new = []
  for record in records:
    record_new = record.copy()
    record_new["reviewed"] = True
    records_new.append(record_new)
  return records_new

add_flag_new(original)


# part e
def get_valid_responses(pid_list):
  resp_list = []
  for x in pid_list:
    if x["status"] == "complete" and x["response"] is not None:
      resp_list.append(x["response"])
  return resp_list

def analyse_participants(pid_dict, *, threshold=0.8):
  valid = get_valid_responses(pid_dict)
  out_dict = summarise_responses_list(valid)
  out_dict["n_high"] = sum(classify_responses(valid, threshold=threshold))
  out_dict["threshold"] = threshold
  return out_dict

analyse_participants(participants)

  


analyse_participants(participants)
analyse_participants([])
analyse_participants(participants, threshold=0.9)

before = [p.copy() for p in participants]

result = analyse_participants(participants, threshold=0.9)

assert result["n_high"] == 1
assert participants == before


