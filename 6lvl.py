def dlt(a,mx):
    counts={}
    result=[]
    for i in a:
        counts[i]=counts.get(i,0)+1
        if counts[i]<=mx:
            result.append(i)
    return result
list=[1,2,3,1,2,1,2,3]
limit=2
print(dlt(list,limit))
