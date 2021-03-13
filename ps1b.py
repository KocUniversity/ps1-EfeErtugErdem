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

minimum_value = 0
maximum_value = 10000
T = int((minimum_value + maximum_value)/2)
left_side = summa*T
while (left_side - B) > summa or (left_side - B) <= 0:
  if left_side < B:
    minimum_value = T
  elif left_side > B: 
    maximum_value = T  
  else: 
    T += 1
    break
  T = int((minimum_value + maximum_value)/2)
  left_side = summa*T
  if T == 9999 and left_side < B:
    T = -1
    break
    
print(T)