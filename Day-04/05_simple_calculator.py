# Day 04 - Mini project 

a = float(input("Enter Your first number : ")) 
b = float(input("Enter Your second number : "))

op = input("Choose a operator(OP) + , - , * , / ") 

if op == "+" :
    print("Addition : ",a+b)
elif op == "-" :
    print("Subtraction : ",a-b)
elif op == "*" :
    print("Multiplication : ",a*b)
    
    
elif op == "/" :
    if b != 0 :
        print("Division : ", a/b)
    else :
        print("Cannot Divide by zero ! ")
        
else :
    print("Invalid operator ! ")