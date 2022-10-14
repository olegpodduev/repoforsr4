import random
n = int(input("Введите размерность массива: "))
arr=[]
for a in range(n):
    arr.append(random.random() * 100 - 50)
print(arr)
max=arr[0]
count=0
countmax=1
for b in arr:
    count+=1
    if b>max :
        max=b
        countmax=count

print(max)
print(countmax)

for a in range(countmax, n):
        arr[a]=0
print(arr)
        


   
