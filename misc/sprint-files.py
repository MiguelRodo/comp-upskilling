from pathlib import Path

file = Path("example.txt")
file.write_text("Hello, Python!", encoding="utf-8")

print(file.read_text(encoding="utf-8"))


# part a
file = Path("participants.csv")
file.write_text(
  "participant_id,age,response\n101,35,0.82\n102,42,0.65\n103,29,\n104,51,0.91\n",
  encoding = "utf-8"
)

print(file.read_text())

# part b
file.exists()
file.resolve()
len(file.read_text().splitlines())

# part d
import csv

with file.open("r", encoding="utf-8", newline="") as f:
  rows = list(csv.DictReader(f))

n_partcipant = len(rows)

age_list = []
response_list = []
for x in rows:
  age = x["age"]
  response = x["response"]
  if age is not None:
    age = int(age)
    age_list.append(age)
  else:
    age_list.append(None)
  
  if response is None or len(response) == 0:
    response_list.append(None)
  else:
    response_list.append(float(response))
