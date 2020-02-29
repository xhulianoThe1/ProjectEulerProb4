arr = []
triNum = 0
for i in range(1, 40):
  k = 1 
  d = 1
  while k < triNum: 
    if triNum % k == 0: 
      d += 1 
    k+=1 
  arr.append([triNum, d])
  if d > 500: 
    print(triNum)
    break 
  triNum += i
  
print(arr)

# print("i", i)
# print(triNum)
