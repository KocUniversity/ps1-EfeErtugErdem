n, B = list(map(int, input().strip().split()))
T = 0
summa = 0
element = 0
for i in range(1,(n+1)):
  if i % 2 == 0:
    p = 2**i + 1 
  else:
    p = 3**i + 1

  element = p**(n-i)  
  summa += element    

left_side = summa*T
while left_side <= B:
  T += 1
  left_side = summa*T
  if T > 10000:
    T = -1
    break 
 

print(T) 
 