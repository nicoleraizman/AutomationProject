grade=int(input("enter grade: "))

# if grade>=90:
#     print("Very good!")
# else:
#     if grade>=80:
#         print("Good!")
#     else:
#         if grade>=70:
#             print("Okay!")
#         else:
#             print("Failed")
# else:
#     if grade>=80:
#         print("Good!") --- elif grade>=80:

if 0<=grade<=100:
    if grade >= 90:
        print("Very good!")
    elif grade >= 80:
        print("Good!")
    elif grade >= 70:
        print("Okay!")
    else:
        print("Failed")