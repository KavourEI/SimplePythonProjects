print("The Love Calculator is calculating your score...")
name1 = input("Enter the first name:")
name2 = input("Enter the second name:")

name1l = name1.lower()
name2l = name2.lower()

digit1 = 0
digit2 = 0

check_name = name1l+name2l

for char in check_name:
    if char in ('t','r','u','e'):
        digit1 = digit1 + 1

for char in check_name:
    if char in ('l','o','v','e'):
        digit2 = digit2 + 1

score = int(str(digit1) + str(digit2))

if (score<10) or (score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>=40) and (score<=50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")