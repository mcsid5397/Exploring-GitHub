double = lambda x : x*2
add = lambda x,y : x+y

num = int(input("Enter any number : "))
num1 = int(input("Enter first number : "))
num2 = int(input("Enter the second number : "))

result1 = double(num)
result2 = add(num1,num2)

print("Double of",num," is ",result1)
print("Sum of",num1," and ",num2," is ",result2)
