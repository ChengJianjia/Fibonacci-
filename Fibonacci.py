

def Fibnacci(n):
    result = [0,1]
    if n <= 1:
        return result[n]
    for i in range(2,n+1):
        result.append(result[i-1]+result[i-2])
    return result[n]

for j in range(1,201):
    print(j,': %d'%(Fibnacci(j)))
