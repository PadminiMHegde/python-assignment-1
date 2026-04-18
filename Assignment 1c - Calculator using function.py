def calc2(a,b):
    list1=[]
    sum1=a+b
    diff1=a-b
    prd1=a*b
    if b!=0:
        div1=a/b
        div2=a//b
        rem1=a%b
    else:
        div1="Zero division error"
        div2="Zero division error"
        rem1="Zero division error"
    exp1=a**b
    

    list1.append(sum1)
    list1.append(diff1)
    list1.append(prd1)
    list1.append(div1)
    list1.append(div2)
    list1.append(rem1)
    list1.append(exp1)

    return list1

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

result=calc2(a,b)
print("Result:",result)