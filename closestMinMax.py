def closestMinMax(A):
    A_max=max(A)
    A_min=min(A)
    latestMinIndex=-1
    result=len(A)
    latestMaxIndex=-1
    for i in range(len(A)):
        if(A[i]==A_min):
            latestMinIndex=i
            if(latestMaxIndex>=0):
                result=min(result,i-latestMaxIndex+1)
    for i in range(len(A)):
        if(A[i]==A_max):
            latestMaxIndex=i
            if(latestMinIndex>=0):
                result=min(result,i-latestMinIndex+1)
    return result
A=list(map(int,input().split()))
print(closestMinMax(A))
