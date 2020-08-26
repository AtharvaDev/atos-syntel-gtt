name = input('What is your name?\n')
print('Enter 5 subject marks.')
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))

print('Hi, %s.' % name)
avg = (sub1+sub2+sub3+sub4+sub5)/5
print('your avg marks are %s.' %avg)
print(name+" you got "+str(avg)+"% in exams")
