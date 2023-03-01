N=int(input())
budget=[]
mul =[]
for i in range(N):
    n=int(input())
    budget.append(n)
budget.sort()
for i in range(1,N+1):
    mul.append(budget[-i]*i)
print(max(mul))
