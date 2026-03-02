'''
def info():
  print("Hello", end = "")
  print("!")


info()
info()
info()
'''
def info(word):
  print(word, end = "")
  print("!")

#info("Hi")

def suma(a, b):
  res = a + b
  #info(res)
  return res

res1 = suma(100, 1000)
res2 = suma(1.5, 10.1)
res3 = suma("hi", " world")
print(res1)
print(res2)
print(res3)

print(res1, res2, res3, sep = "\n")

#find min
num1 = [1, 5, 8, 10, 3, -10, 4, 6, 7, 9]
min1 = num1[0]
for i in num1:
  if i < min1:
    min1 = i

print(min1)

num2 = [1100, 5, 8, 10, 3, -100, 4, 6, 7, 80]
min2 = num2[0]
for i in num2:
  if i < min2:
    min2 = i

print(min2)


def find_min(l):
  min_num = l[0]
  for i in l:
    if i < min_num:
      min_num = i
  return min_num  


num1 = [1, 5, 8, 10, 3, -10, 4, 6, 7, 9]
res1 = find_min(num1)

num2 = [1100, 5, 8, 10, 3, -100, 4, 6, 7, 80]
res2 = find_min(num2)

if res1 < res2:
  print(res1)
else:
  print(res2)
