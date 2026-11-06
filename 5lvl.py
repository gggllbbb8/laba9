def mxs(list):
    mxnow=mxglob=0
    for i in list:
        mxnow=max(i,mxnow+i)
        if mxnow>mxglob:
            mxglob=mxnow
    return mxglob
sp=[-2,1,-3,4,-1,2,1,-5,4]
print(mxs(sp))