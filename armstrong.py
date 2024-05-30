'''
num=int(input("enter the number:"))
n1=num
num1=str(num)
digits=len(num1)

sum=0

while num>0:

    q=num//10
    
    r=num%10

    power_dig=pow(r,digits)

    num=q

    sum=sum+power_dig

print(sum)

if sum==n1:
    print("Given number is Armstrong")

else:
    print("Given number is not Armstrong")

'''    

'''    
f1=0
f2=1
new=0

n=50
print(f1,"",f2,end=" ")
 
while f1+f2<n:
 
    
    new=f1+f2  
    f1=f2
    f2=new
    print(new, end= " ")

'''    
