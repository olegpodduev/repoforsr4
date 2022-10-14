import random
n1 = int(input("Введите размерность массива X: "))
n2 = int(input("Введите размерность массива R: "))
X=[]
R=[]

for c in range(n1):
    X.append(round(random.random() * 10 - 5))
for c in range(n2):
    R.append(round(random.random() * 10 - 5))    
print(X)
print(R)
b=0
for c in range(1, n1):
    for j in range(1, n2):
             if X[c]==R[j]:
                 print(X[c])   
