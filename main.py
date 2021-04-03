# B = int(input("Please enter the lower bound B: "))
# n = int(input("Please enter the number n: "))
# summa = 0
# element = 0
# for i in range(1,(n+1)):
#   if i % 2 == 0:
#     p = 2**i + 1 
#   else:
#     p = 3**i + 1

#   element = p**(n-i)  
#   summa += element    

# #First, the brute-power search.
# T = 0
# num_guess = 0
# left_side = summa*T
# while left_side <= B:
#   T += 1
#   left_side = summa*T

# if T > 10000:
#   print(str(-1))  
# else:
#  print(str(T) + " = T")

# #Then, the bisection search
# minimum_value = 0
# maximum_value = 10000
# T = int((minimum_value + maximum_value)/2)
# left_side = summa*T
# while (left_side - B) >= summa or (left_side - B) <= 0:
#   if left_side < B:
#     minimum_value = T
#   elif left_side > B: 
#     maximum_value = T  
#   else: 
#     T += 1
#     print(T)
#     break
#   T = int((minimum_value + maximum_value)/2)
#   left_side = summa*T
    
# print(T)