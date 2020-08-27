
def funct(reply, score):
  reply = reply.upper()
  if score < 1:
    score = 0   
  if reply == "YES":
    score = score + 25
  else:
    score = score - 25
  # print(reply, score)
  return score


def funct1(reply, score):
  reply = reply.upper()
  if score < 1:
    score = 0 
  if reply == "YES":
    score = score - 25
  else:
    score = score + 25
  # print(reply, score)
  return score


final = 0
print("Answer the following questions in YES or NO ")
que1 = input("Are you at home?: ")
final = funct1(que1,final)
que2 = input("Do you have any abroad travel history?: ")
final = funct(que2,final)
que3 = input("Do you have any cough, cold symptoms?: ")
final = funct(que3,final)
que4 = input("Do you follow home qurantine?: ")
final = funct1(que4,final)

# print(final)

if final < 1:
  print("possibility of you getting infected with coronavirus is 0%")
else:
  print("possibility of you getting infected with coronavirus is "+str(final)+"%")


