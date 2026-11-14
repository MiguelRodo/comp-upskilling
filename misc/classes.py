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