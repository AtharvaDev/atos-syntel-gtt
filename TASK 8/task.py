final ={}
for _ in range(int(input("Enter total no. of students: "))):
  marks = []
  name = input("name: ")
  mark1 = int(input("Enter maths-1 marks: "))
  marks.append(mark1)
  mark2 = int(input("Enter maths-2 marks: "))
  marks.append(mark2)
  mark3 = int(input("Enter maths-3 marks: "))
  marks.append(mark3)
  final[name] = marks

print(final)
