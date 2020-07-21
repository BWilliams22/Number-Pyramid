length = int(input("How tall do you want the pyramid?"))
for i in range(1, length):
  for j in range(1, i+1):
   print(j, end =  " ")
  print() 