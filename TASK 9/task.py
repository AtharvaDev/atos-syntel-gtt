final = []
for _ in range(int(input("Enter total no. of students: "))):
  lst =[]
  print("")
  name =input("enter your name: ")
  roll = input("enter your roll number: ")
  marks = int(input("enter your marks: "))
  print("")
  lst.append(name)
  lst.append(roll)
  lst.append(marks)
  final.append(lst)


for x in final:
  print("hello "+x[1]+ "your marks are less than 35 so you get 5 more grace marks.\n")
  if x[2] < 35:
    abc = x[2] + 5
    x[2] = abc
  
print(final)
