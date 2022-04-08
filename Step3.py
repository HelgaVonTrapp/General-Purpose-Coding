def calculate(operator, first_number, second_number):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "/":
        return first_number / second_number
    elif operator == "x":
        return first_number * second_number

with open("numbers2.txt", mode="r") as f:
    lines = f.read().splitlines()

    for line in lines:
        line_split = line.split()
        operator = line_split[1]
        first_number = int(line_split[2])
        second_number = int(line_split[3])
        print(line)
      
 