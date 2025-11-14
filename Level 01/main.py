operator = input("Choise --- (+ -  *  /) :")
num1 = int(input("enter the num1 :"))
num2 = int(input("enter the num2 :"))

if operator =="+":
    result = num1 + num2
    print(round(result))

elif operator =="-":
    result = num1 - num2
    print(round(result))

elif operator =="*":
    result = num1 * num2
    print(round(result))

elif operator =="/":
    result = num1 / num2
    print(round(result))



