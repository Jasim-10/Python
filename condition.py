# raining = True
# if raining == True:
#     print("take umbrella")



# raining = False
# if raining == True:
#     print("take umbrella")
# else:
#     print("dont take umbrella")

# number = int(input("Enter the number: "))
# if number >= 0:
#     print(f"{number} is positive")
# else:
#     print(f"{number} is negative")



# number = int(input("Enter the number: "))
# if number %2 == 0:
#     print(f"{number} is even")
# else:
#      print(f"{number} is odd")







# age = 10
# citizen=True
# if age>=18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("you cannot vote")
# else:
#     print("You are too young")



# marks = int(input("Enter the marks"))
# if marks > 100 or marks < 0:
#     print("Invalid Marks")
# elif marks >= 85:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 45:
#     print("Grade D")
# elif marks == 33:
#     print("Grade P")
# else:
#     print("Fail")


# eng_mark = int(input("Enter the marks of English: "))
# math_mark = int(input("Enter the marks of Math: "))

# if eng_mark >= 80 and math_mark >=80:
#     print("Grade A")
# elif eng_mark >= 80 or math_mark >=80:
#     print("Grade B")
# else:
#     print("Need to work hard")


# number = int(input("Enter the number: "))

# if number >= 1000 and number <= 9999:
#     print(f"{number} is four digit number")
# else:
#     print(f"{number} is not four digit number")


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1 == num2 == num3:
#     print("All number are equal")
# elif num1 >= num2 and num1 >= num3:
#     print(f"{num1} is greatest")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is greatest")
# else:
#     print(f"{num3} is greatest")




# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# n3 = int(input("Enter the third number: "))

# if n1 > n2 :
#     if n1 >n3:
#         print(f"{n1} is greatest")
#     else:
#         print(f"{n3} is greatest")
# else :
#     if n2 > n3:
#         print(f"{n2} is greater")
#     else:
#         print(f"{n3} is greater")


# number = int(input("Enter the number: "))
# if number % 15 == 0:
#     print(f"{number} is divisible by 15")
# else:
#     if number % 3 == 0 or number % 5 == 0:
#         print(f"{number} is not divisible by 15 but divisible by 5 or 3")
#     else:
#         print(f"{number} is neither divisible by 5 or 3")




#match case
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))


# operator = input("Enter Operator: ")

# match operator:
#     case "+":
#         print(f"Sum of {n1} + {n2} is {n1+n2}")
#     case "-":
#         print(f"Difference of {n1} + {n2} is {n1+n2}")
#     case "*":
#         print(f"Product of {n1} + {n2} is {n1+n2}")
#     case "/":
#         print(f"Division of {n1} + {n2} is {n1/n2}")
#     case _ :
#         print(f"Invalid Operator")



# Ternary operator

# age = 18
# result = "Adult" if age >= 18 else "Minor"
# print(result)


# num = int(input("Enter the number: "))
# result = "even" if num%2==0 else "odd"
# print(result)


# num = int(input("Enter the number: "))
# print("divisible by 5" if num%5==0 else "not divisible by 5")




# loop

# for i in range(5):
#     print(i," Hello")



# num = 7
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")


# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")


# print("even number between 2 to 99 ")
# for i in range(2,100,2):
#     print(i)



# fruits = ["apple","banana","mango","litchi","guava"]
# for fruit in fruits:
#     print(fruit)


# count = 0
# for i in range(2, 101): 
#     if i % 2 == 0:
#         count += 1
# print(f"Total even numbers between 2 and 100: {count}")



#while loop
# i = 0
# while i < 5:
#     print(i)
#     i += 1 


# i = 2
# while i <= 100:
#     print(i)
#     i+=2


# count = 0
# i = 2
# while i <= 100:
#     if i % 2 == 0:
#         count += 1
#     i += 1
# print(f"Total even numbers between 2 and 100: {count}")


# x = 4
# y = 0
# while x >= 0:
#     x -= 1
#     y += 1
#     if x==y:
#         continue
#     else:
#         print(x,y)



