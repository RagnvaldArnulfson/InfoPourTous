import random as r

l1=[r.randint(-10,10) for i in range(10**3)]

def recurs(l):
    n=len(l)
    
    if n==1:
        return l[0]
    
    k=(n//2)
    
    a1=recurs(l[0:k])
    a2=recurs(l[k:n])
    
    left_sum,right_sum = l[k-1],l[k]
    
    i0,j0=0,0
    
    s_g,s_d=0,0

    for i in range(k,n):
        s_d+=l[i]
        s_g+=l[n-i-1-(n%2)]
        if s_d < right_sum:
            right_sum = s_d
            j0 = i
        if s_g < left_sum:
            left_sum = s_g
            i0 = i
            
    
    return min(a1,a2,left_sum+right_sum)

def lineaire(l):
    c=l[0]
    m=l[0]
    for i in range(len(l)):
        c=min(c+l[i],l[i])
        m=min(m,c)
    return m
