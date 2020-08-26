final = []
for _ in range(int(input("Enter total no. of students: "))):
  lst =[]
  print("")
  name =input("enter your name: ")
  roll = input("enter your roll number: ")
  marks = float(input("enter your marks: "))
  print("")
  lst.append(name)
  lst.append(roll)
  lst.append(marks)
  final.append(lst)

print(final)
max = sorted(list(set([x[2] for x in final])))[-1]
print("Highest marks are")

for x in final:
  if x[2] == max:
    print("Name: " +str(x[0])+ "   Roll no: "+str(x[1])+ "   Marks: " +str(x[2]))

