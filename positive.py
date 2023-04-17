n=int(input("Enter the number of terms in the list"))
list=[]
for i in range(n):
    a=int(input("Enter the list value:"))
    list.append(a)
print("The positive elements in the list are:")
for i in range(n):
    if list[i]>=0:
        print(list[i])
    else:
        pass