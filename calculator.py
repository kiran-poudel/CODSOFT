
x = float(input('Enter first number: '))
y = float(input('Enter second number: '))

print("Select Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

select = input("Enter 1/2/3/4 for operation: ")

if select in ('1','2','3','4'):
    if select == '1':
       result = add(x,y)
    elif select =='2':
        result = subtract(x,y)
    elif select =='3':
        result = multiply(x,y)
    elif select =='4':
        result = divide(x,y)
    
    print(f"The result is: {result}")
else:
    print("Invalid input.Please select a valid operation (1/2/3/4).")