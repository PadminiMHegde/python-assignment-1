
n1=int(input("Enter the first number :"))
n2=int(input("Enter the second number :"))
 
sum1=n1+n2
dif1=n1-n2
prd1=n1*n2
if n2!=0:
    div1=n1/n2
    div2=n1//n2
    rem1=n1%n2
else:
    div1="zero division error,"
    div2="zero division error,"
    rem1="zero division error,"
    
exp1=n1**n2
print(sum1,dif1,prd1,div1,div2,rem1,exp1)
