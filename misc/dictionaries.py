participant = {
  "id": 101,
  "age": 35,
  "response": 0.82
}
participant["age"]

test_dict = {
  1: "a",
  "b": 31
}

participant["age"] = 46

del participant["response"]

study = {
  "name": "TB_study",
  "n_participants": 150,
  "alpha": 0.05,
  "completed": False
}
study["name"]
study["n_participants"]
type(study)
dir(study)
study.__len__()
len(study)
study.__setitem__(key = "response", value = 0.25)

study.__setitem__("response", 0.25)
study["n_participants"] = 175
study["country"] = "South Africa"

# exercise 12
study.keys()
study.values()
study # all key-value pairs?
study.__getitem__("name")
study.items() # all key-value pairs?
study.__getitem__("missing_key")

y = study.get("missing_key")
type(y)

z = study.get("missing_key", "Not available")
type(z)
z

# exercise 13
participant = {
    "id": 101,
    "age": 35
}
participant["age"] # 35
participant["response"] # error
participant.get("response") # NoneType
participant.get("response", 0) # 0
"response" in participant # False

# exercise 14
participant = {
    "id": 101,
    "measurements": [0.12, 0.15, 0.11],
    "n": 3
}
participant["measurements"].append(0.14)
participant["n"] = len(participant["measurements"])
participant_copy = participant.copy()
participant_copy["measurements"].append(0.2)
# I predict that they wll be different
participant["measurements"]
participant_copy["measurements"]
# ah, they're the same! Okay, 
# I've not quite understood shallow clone versus deep clone.
# it looks to me here lik eshallow clone
# (with a list that isn't nested)
# is the same as assingnment (e.g. participant_copy = participant)
# obviousyl what's happneed with participant.copy is that the individual elements point to the same things in memroy
id(participant)
id(participant_copy)

# exercise 16

participants = {
  101: {"age": 35, "response": 0.82},
  102: {"age": 42, "response": 0.65},
  103: {"age": 29, "response": 0.91}
}

## part a
participants[102]["age"]
participants[101]["response"] = 0.85
participants[104] = {"age": 38, "response": 0.73}
len(participants)

# part b

participants.pop(103)
participants.__contains__(103)
103 in participants

# part c
# integers
# error
# yes, because pointing to same leemnt in emmeory, no t a deep copy

# exercise 16
api_response = {
    "status": "success",
    "data": {
        "participant_id": 105,
        "visits": [
            {"day": 0, "response": 0.12},
            {"day": 28, "response": 0.35},
            {"day": 56, "response": 0.48}
        ]
    }
}

api_response["status"]
api_response["data"]["participant_id"]
api_response["data"]["visits"]
api_response["data"]["visits"][1]["response"]
api_response["data"]["visits"].append(
  {"day": 84, "response": 0.52}
)
len(api_response["data"]["visits"])
