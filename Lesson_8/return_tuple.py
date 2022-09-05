def calc(num1,num2):
    sum1 = num1+num2
    diff=num1-num2
    mult=num1*num2
    div=num1/num2

    return sum1,diff,mult,div

num1=10
num2=4

result = calc(num1,num2)
print(result,type(result))