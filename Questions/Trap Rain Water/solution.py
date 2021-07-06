t=int(input())
for test in range(t):
    n=int(input())
    a = list(map(int,input().strip().split()))[:n]
    index=0
    count=0
    st=[]
    st.append(a[index])
    for i in range(1,n):
        if a[i]<a[index]: st.append(a[i])
        else :
            count+= a[index]*(i-index-1)
            while len(st)!=0:
                count-=st.pop()
            count+=a[index]
            st.append(a[i])
            index=i
    while len(st)!=0:
        index=st.pop()
        while len(st)!=0 and st[-1]<index:
            count+=index
            count-=st.pop()
    
    print(count)
            