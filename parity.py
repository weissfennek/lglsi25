def nombres_paire(arry):
    n=len(arry)
    k=0
    for i in range(n):
        if(arry[i]%2==0):
            k+=1
    return(k)
def nombres_impaire(arry):
    n=len(arry)
    k=0
    for i in range(n):
        if(arry[i]%2!=0):
            k+=1
    return(k)
