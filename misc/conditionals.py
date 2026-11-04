x = 10

if x > 10:
  print("High")
elif x == 10:
  print("Equal")
else:
  print("Low")

p_value = 0.03
alpha = 0.05

if p_value < alpha:
  print("Statistically significant")
else:
  print("Not statistically significant")

p_value = 0.008

if p_value < 0.01:
  print("Strong evidence")
elif p_value < 0.05:
  print("Moderate evidence")
else:
  print("Weak evidence")

# part c:prints 10
x = 15

if x > 10:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")