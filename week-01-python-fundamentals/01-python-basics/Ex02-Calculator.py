#-------------------------------------
#      Calculator
#-------------------------------------

val1 = int(input("Enter the val1: "))
val2 = int(input("Enter the val2: "))

operation = input("Enter the operator(+, -, /, *, %): ")

#Addition
if operation=='+':
    add_val = val1 + val2
    print(add_val)

#Substraction    
elif operation=='-':
    sub_val = val1 - val2
    print(sub_val)

#Division        
elif operation=='/':
    if val2 == 0:
        print("Cannot divise be Zero!")
    else:
        div_val = val1 / val2
        print(div_val)

#Multiplication        
elif operation=='*':
    mul_val = val1 * val2
    print(mul_val)

#Modulus    
elif operation=='%':
    if val2==0:
        print("Cannot perform modulous by zero!")
    else:
        mod_val=val1 % val2
        print(mod_val)
else:
    print("Invalid Operator!")





