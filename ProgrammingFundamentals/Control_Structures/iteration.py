# Loop through numbers from 0 to 9 and print each
for i in range (10):
    print(i)
print("\n")  
  
# Create a range object from 0 to 4 and iterate through it
x = range(5)
for i in x:
    print(i)
print("\n")

# Create a range object from 3 to 5 (inclusive of 3, exclusive of 6)
# Iterate through and print each number in the range
x = range(3, 6) # first num is inclusive, second is exclusive
for i in x:
    print(i)
print("\n")

# Loop through numbers from 10 down to 1 in steps of -1
# Python doesn't assume the range is descending; you must specify -1 as the step
for i in range(10, 0, -1):
    print(i)
print("\n")  

# Loop through numbers from 0 to 9 in steps of 2
# 0, 2, 4, 8
for i in range(0, 10, 2):
    print(i)
print("\n") 


answer = 0
# Continuously prompt the user to guess the number until they guess correctly
while(answer != 50):
    # Prompt the user to guess a number and convert the input to an integer
    answer = int(input("Guess the number between 49 and 51: "))
    # Check if the guess is incorrect
    if(answer != 50):
        print("wrong number")

# If the loop exits, the correct number has been guessed
print("You guessed the number!")