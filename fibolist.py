def getFibo(n):
    if n < 2:
        return n;
    
    a = 1
    b = 1
    c = 0
    for i in range(0, n-2):
        c = a+b
        b = a
        a = c
        
    return a
    

def getFiboLst(n):
    lst = []
    for i in range(n):
        lst.append(getFibo(i))
    return lst

print(getFiboLst(5))

assert getFiboLst(5) != []
assert len(getFiboLst(5)) == 5
assert getFiboLst(5)[0] == 0
assert getFiboLst(5)[1] == 1
assert getFiboLst(5)[2] == getFiboLst(5)[0] + getFiboLst(5)[1]

for i in range(10):
    assert len(getFiboLst(i)) == i
