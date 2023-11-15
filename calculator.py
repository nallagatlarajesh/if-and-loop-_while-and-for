#program to craete a simple  four function calculator +-*/
result=0
val1=float(input("enetr val1 :"))
val2=float(input("enter value2:"))
op=input("enetr any one pf the operator (+-*/)")
if op=="+":
    result=val1+val2
elif op=="-":
    if val1>vakl2:
        result=val1-val2
    else:
        result=val2-val1
elif op=="*":
    result=val1*val2
elif op=="/":
    if val2==0:
        print("Error !,Division by zero is not allowed ,program terminated")
    else:
        result=val1/val2
        
else:
    print("wrong input program terminated")
print("result is",result)
            
        
