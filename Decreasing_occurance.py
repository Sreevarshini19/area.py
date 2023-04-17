def occur(a): 
    l=len(a)
    dict={}
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in range(0,l):
        max=i
        for j in range(0,l):
            if(dict[a[max]]<dict[a[j]]):
                max=j
        if(dict[a[max]]!=0):
            print(a[max],"=",dict[a[max]])
            dict[a[max]]=0              
a=input("Enter a string")
occur(a)