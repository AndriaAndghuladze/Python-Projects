def add(x,y):
    return x + y

def Subtract(x,y):
    return x - y

def Multiply(x,y):
    return x * y

def Devide(x,y):
    return x / y

print('1:add')
print('2:Subtract')
print('3:Multiply')
print('4:Devide')


operator = input("Choise operator-> 1/2/3/4:")
num1 = float(input('enter num1:'))
num2 = float(input('enter num2:'))

if operator == '1':
    print(add(num1,num2))

elif operator == '2':
    print(Subtract(num1,num2))

elif operator == '3':
    print(Multiply(num1,num2))

elif operator == '4':
    print(Devide(num1,num2))

else:
    print('Eror!!!')