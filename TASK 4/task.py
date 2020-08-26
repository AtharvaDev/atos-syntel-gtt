num = int(input("ENTER NUMBER\n"))

if (num % 2 == 0):
  print("Number Entered is Even.")
  print("Square of this number is " + str(num*num))
else:
  print("Number Entered is Odd.")
  print("Cube of this number is " + str(num*num*num))
