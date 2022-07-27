x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add(1, "Vicki")
print(sampleSet)

def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)

x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)

a = 4
b = 11
print(a | b)
print(a >> 2)

l = [None] * 10
print(len(l))

aList = [5, 10, 15, 25]
print(aList[::-2])

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)