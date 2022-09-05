# def f():
#     try:
#         num = int(input("enter number: "))
#     except:
#         print("Invalid number")
#         num=None
#     return num

while True:
    try:
        num = int(input("enter number: "))
        num2 = int(input("enter number: "))
        print(num/num2)
        break
    except ValueError:
        print("Invalid number")
    except ZeroDivisionError:
        print("Dividing by zero")
print(num)
