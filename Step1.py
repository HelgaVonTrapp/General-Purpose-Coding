# Get the input first
operator = input("Operator Please: ")
first_number = int(input("Number 1 Please: "))
second_number = int(input("Number 2 Please: "))


# Do the calculation

# Decide which operator we have
if operator == "+":
  print(first_number + second_number)
elif operator == "-":
  print(first_number - second_number)
elif operator == "/":
  print(first_number / second_number)
elif operator == "x":
  print(first_number * second_number)