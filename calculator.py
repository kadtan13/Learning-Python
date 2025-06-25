print ("Welcome to the calculator!\n\nThis calculator can perform the following operations:\n+, -, *, /, %, **, //\n")
a = float(input("Please input the first number:"))
b = float(input("Please input the second number:"))
op = input("Please input the operation you want to perform:")
if op == "+":
  print ("\nThe sum of", a, "and", b, "is:", float(a) + float(b))
if op == "-":
  print ("\nThe difference of", a, "and", b, "is:", float(a) - float(b))
if op == "*":
  print ("\nThe product of", a, "and", b, "is:", float(a) * float(b))
if op == "/":
  print ("\nThe quotient of", a, "divided", b, "is:", float(a) / float(b))
if op == "%":
  print ("\nThe remainder of", a, "divided", b, "is:", float(a) % float(b))
if op == "**":
  print ("\nThe exponential function of", a, "raised to the power of", b, "is:", float(a) ** float(b))
if op == "//":
  print ("\nThe floor division", a, "and", b, "is:", float(a) // float(b))
print ("\nThank you for using the calculator!")
