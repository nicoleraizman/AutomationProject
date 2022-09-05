def prime_number(number: int):

    """A method that gets a number and
    returns if it's prime or not"""
    
    if number == 1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False

    return True

num = int(input("Enter number: "))
if prime_number(num):
    print("Prime number")
else:
    print("Not prime number")

help(prime_number)