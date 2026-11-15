class Participant:
  __slots__ = ("age", "group")
  
p = Participant()
p.age = 35
p.group = "Treatment"

print(p.age)
print(p.__slots__)
print(p.__dict__) # error

{
  name: getattr(p, name)
  for name in Participant.__slots__
  if hasattr(p, name)
}

{x: x**2 for x in [1, 2, 3]}

# {<it_key>: <function_to_run> (that accepts what as parameters?) for <it_key> (seems reudnant to speicfy it again?) in <some iteratble, I guess> <I don't get the if statement here)

{x: x + 10 for x in [1, 2, 3] if x >= 5}

{x % 2: x for x in [1, 2, 3, 4]}


# exercise 27

## part a

class Participant:
  study = "ACS"

p1 = Participant()
p2 = Participant()

p1.study = "Vaccine"
Participant.study = "Updated ACS"

print(p1.study)
print(p2.study)
print(Participant.study)
print(p1.__dict__)
print(p2.__dict__)


## part b

class Participant:
  visits = []

p1 = Participant()
p2 = Participant()

p1.visits.append(0)
p2.visits.append(28)

print(p1.visits)
print(p2.visits)
print(p1.visits is p2.visits)

## part c

class Measurement:
  unit = "pg/mL"

m1 = Measurement()
m2 = Measurement()

m1.value = 12.5
m2.value = 18.3

m1.unit = "ng/mL"
print(m1.unit)
print(m1.value)
print(m2.unit)
print(m2.value)

m1.__dict__
m2.__dict__

## part d

class Participant:
  pass

p1 = Participant()
p1.age = 35

p2 = Participant()
p2.age = 35

p3 = p1

print(p1 == p2) # same class and same instance attributes, so yes?
print(p1 is p2) # no, because if we modified p1, we woudlnt modify p2 (not even a shared class attribute)
print(p1 is p3) # yes
print(p1.age == p2.age) # yes

x = [1]
y = x
x is y
y = [1]
x is y

# exercise 28
class Participant:
    def __init__(self, participant_id, age):
        self.participant_id = participant_id
        self.age = age

p1 = Participant(101, 35)
p2 = Participant(102, 42)

p1.age = 40

print(p1.__dict__)
print(p2.__dict__)

# part b
class Participant:
  def __init__(self, participant_id, age, group_name, response=None):
    self.participant_id = participant_id
    self.age = age
    self.group_name = group_name
    self.response = response

p3 = Participant(
  participant_id=103,
  age=29,
  group_name="treatment"
)
p3.__dict__

# part d
class Participant:
    def __init__(self, participant_id, visits=[]):
        self.participant_id = participant_id
        self.visits = visits

p1 = Participant(101)
p2 = Participant(102)

p1.visits.append(0)
p2.visits.append(28)
Participant.visits.append(72)

print(p1.visits)
print(p2.visits)
print(p1.visits is p2.visits)

class Participant:
    def __init__(self, participant_id, visits=None):
        self.participant_id = participant_id
        # Complete this
        if visits is None:
          self.visits = []
        else:
          self.visits = visits

p1 = Participant(103)
p2 = Participant(104, [12])

# exercise 29

## part a

class Participant:
  def __init__(self, participant_id):
    self.participant_id = participant_id
    self.visits = []
  
  def add_visit(self, day):
    self.visits.append(day)

p1 = Participant(101)
p2 = Participant(102)

p1.add_visit(0)
p1.add_visit(28)
p2.add_visit(14)

print(p1.visits) # [0, 28]
print(p2.visits) # [14]
# different because a different list
# is created for each (in __init__),
# rather than passed as a default value
# to __init__,
# so when we mutate we're mutating in place
# but the initial objects are different.

## part b

class Participant:
  def __init__(self, participant_id):
    self.participant_id = participant_id
    self.visits = []
  
  def add_visit(self, day):
    self.visits.append(day)
  
  def number_of_visits(self):
    return len(self.visits)
  
  def last_visit(self):
    n_visits = self.number_of_visits()
    return None if n_visits == 0 else self.visits[n_visits - 1]


p1 = Participant(101)

p1.add_visit(0)
p1.add_visit(28)

print(p1.number_of_visits())  # 2
print(p1.last_visit())        # 28

p2 = Participant(102)

print(p2.number_of_visits())  # 0
print(p2.last_visit())        # None

# part c
p1.add_visit(56)

Participant.add_visit(p1, 56)

## A. Well, because you're calling a method from the Participant class. Now, if you were calling it from the instance itself, self woul dbe automaticaly supplied, but there is no "self", so you just pass an instanmce o that class yourself (you could pass anythign, but here we pass that because its' corect, but it' snot inripcinepl ruled out to pass something else). So, this makes the poitn that class methods are "generally available", and are avialble apart rom any instances in that class. 

## B. Error, because itw ill treat self as 84, and that lacks a visits attribute, so 84.visits fails. 

## c. Well, I'm not sure. I suppose perhaps the method would automaticaly pass "self", since it's from the instance? 

# exercise 30

## part a

class Participant:
  def __init__(self, participant_id, age):
    self.participant_id = participant_id
    self.age = age
  
  @classmethod
  def from_record(cls, record):
    return cls(record["participant_id"], record["age"])
  
  @staticmethod
  def valid_age(age):
    return age >= 0

record = {"participant_id": 101, "age": 35}

p1 = Participant.from_record(record)

print(p1.__dict__)
print(Participant.valid_age(-5))
print(p1.valid_age(35))

p1 = Participant(101, 35)

record = {"participant_id": 102, "age": 42}

p2 = p1.from_record(record)

print(p1.participant_id) # 101
print(p2.participant_id) # 102
print(p1 is p2) # false


## part B

class Participant:
  def __init__(self, participant_id, age):
    self.participant_id = participant_id
    self.age = age
  
  @classmethod
  def from_csv_row(cls, row):
    pid = int(row["participant_id"])
    age = int(row["age"])
    return cls(pid, age)

row = {
    "participant_id": "102",
    "age": "42"
}

p2 = Participant.from_csv_row(row)


print(p2.__dict__)


## part c

class Participant:
  def __init__(self, participant_id, age):
    self.participant_id = participant_id
    self.age = age
  
  @classmethod
  def from_csv_row(cls, row):
    pid = int(row["participant_id"])
    age = int(row["age"])
    return cls(pid, age)
  
  @staticmethod
  def is_adult(age):
    return age >= 18

Participant.is_adult(20)  # True
p3 = Participant(103, 25)
p3.is_adult(16)           # False


## part d

print(type(Participant.from_csv_row)) # function
print(type(Participant.is_adult)) # function
print(type(p3.from_csv_row)) # method
print(type(p3.is_adult)) # method

print(Participant.from_csv_row.__self__ is Participant) # True

# exercise 31

## part a

class Participant:
  def __init__(self, age):
    self._age = age
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, value):
    self._age = value

p = Participant(35)
p.age = 40

## part b

class Participant:
  def __init__(self, age):
    self.age = age
  
  @property
  def age(self):
    return self._age
  
  @staticmethod
  def valid_age(age):
    return age >= 0
  
  @age.setter
  def age(self, value):
    if not self.valid_age(value):
      raise ValueError("Age cannot be negative")
    else:
      self._age = value

p1 = Participant(30)
p1.age


p = Participant(35)

print(p.age)     # 35

p.age = 40

print(p.age)     # 40
print(p._age)    # 40
print(p.__dict__)

## part c
p = Participant(35) 
p.age = -5 # error
print(p.age) # 35

## part d
# just a straight error, p2 never is created

# exercise 31

class Participant:
  __slots__ = ("_age",)
  
  def __init__(self, age):
    self.age = age
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, value):
    if value < 0:
      raise ValueError("Age cannot be negative")
    self._age = value

## part a
p = Participant(35)

print(p.age) # 35
print(p._age) # 35

p.age = 40 
print(p.age) # 40

## part b

p.group = "treatment" # error
print(p.__dict__) # error a well, no dictionary as __slots__ doesn't allow attributes to be stored as dictionaries

## part c

### 1. because it's calling the property (well, is p.age even a "callable"? confusing, as when you run `type(p.age)` you get integer, same as p._age, which means it's operating on the output from the function age (proeprty age?), so I'm not quite sure how to get the proerpty age

### 2. _age is an attribute (is it still called an attribute, or is it now a slot?)

### 3. nothing

# exercise 32

class Participant:
  def __init__(self, participant_id):
    self.participant_id = participant_id
    self.visits = []
  
  def add_visit(self, day):
    self.visits.append(day)

class TrialParticipant(Participant):
  pass

p = TrialParticipant(101)
p.add_visit(0)
p.add_visit(28)

print(p.visits)

## part a

p1 = Participant(101)
p2 = TrialParticipant(102)

p2.add_visit(0)
p2.add_visit(28)

print(p2.__dict__) # {particpant_id: 102, visits: [0, 28]} (no slots so no error here)
print(type(p2) is Participant) # obviously False
isinstance(p2, Participant) # true
print(isinstance(p1, TrialParticipant)) # false

# type - its "final" class
# isinstance - is it that class or does it inherit from it

# part B
class TrialParticipant(Participant):
  def __init__(self, participant_id, treatment_arm):
    super().__init__(participant_id)
    self.treatment_arm = treatment_arm

p = TrialParticipant(103, "vaccine")

print(p.__dict__)
# {'participant_id': 103, 'visits': [], 'treatment_arm': 'vaccine'}

p.add_visit(0)
print(p.visits)  # [0]

## part c

class Participant:
  def __init__(self, participant_id):
    self.participant_id = participant_id
    self.visits = []
  
  def add_visit(self, day):
    self.visits.append(day)
  
  def summary(self):
    return f"Participant {self.participant_id}"

class TrialParticipant(Participant):
  def __init__(self, participant_id, treatment_arm):
    super().__init__(participant_id)
    self.treatment_arm = treatment_arm
  
  def summary(self):
    return super().summary() + " (" + self.treatment_arm + ")"

 
p = TrialParticipant(103, "vaccine")

print(p.summary())

## part d

class TrialParticipant(Participant):
    def __init__(self, participant_id, treatment_arm):
        self.treatment_arm = treatment_arm

p = TrialParticipant(104, "placebo")
p.add_visit(0)

### a: there is no visit attribute, as we never created one (either directly or by using __init__ from Participant)
### b: because you have to call its init fn
### c: 

class TrialParticipant(Participant):
  def __init__(self, participant_id, treatment_arm):
    super().__init__(participant_id)
    self.treatment_arm = treatment_arm

p = TrialParticipant(104, "placebo")
p.add_visit(0)