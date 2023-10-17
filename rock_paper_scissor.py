import random

user_choice = int(input("Type 1 for Rock, 2 for Paper and 3 for scissors."))
computer_choice =  random.randint(1,3)

print("Computer Choice:")
print(computer_choice)

if user_choice == computer_choice:
    print ("It's a tie")
    
elif user_choice == 1 and computer_choice == 2:
    print ('Computer wins ')

elif user_choice == 1 and computer_choice == 3:
    print("User wins")

elif user_choice == 2 and computer_choice == 3:
    print("Computer wins")

elif user_choice == 3 and computer_choice == 2:
    print("User wins")

elif user_choice == 2 and computer_choice == 1:
    print("User wins")

elif user_choice == 3 and computer_choice == 1:
    print("Computer wins")

else:
    print("Invalid input.Please select the number beween 1 to 3")