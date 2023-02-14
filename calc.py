def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def subtract(a, b):
    return a-b
    
def modulus(a, b):
    return a%b

def main():
    number_1 = int(input("Enter number:"))
    number_2 = int(input("Enter number:"))
    op = input("Enter operator:")
    if op=="+":
        print(f"The sum of {number_1} and {number_2}:", add(number_1, number_2))
    elif op=="*":
        print(f"The product of {number_1} and {number_2}:", multiply(number_1, number_2))
    elif op=="/":
        print(f"The division of {number_1} and {number_2}:", divide(number_1, number_2))
    elif op=="/":
        print(f"The difference of {number_1} and {number_2}:", subtract(number_1, number_2))
    elif op=="%":
        print(f"The modulus of {number_1} and {number_2}:", modulus(number_1, number_2))
    else:
        print("operator not recognize")

if __name__=="__main__":
    main()
