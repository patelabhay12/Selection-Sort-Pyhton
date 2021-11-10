A=[]
n=int(input("Enter Size of the list :"))
for i in range(n):
    val=int(input("Enter your number :"))
    A.append(val)
def Selection_Sort(A):
    l=len(A)
    min=0
    for i in range(0,l-1):
        for j in range(i+1,n):
            if(A[j]<A[i]):
                A[j],A[i]=A[i],A[j]

Selection_Sort(A)
print(A)

