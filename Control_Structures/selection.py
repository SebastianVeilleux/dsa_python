# Start an infinite loop to ensure valid input
while True:
    try:
        # Request grade input and convert it to a float
        grade = float(input("Enter your grade (0-100): "))
        
        # Check if the grade is within the valid range
        if 0 <= grade <= 100:
            break  # Exit loop if valid grade
        else:
            print("Grade must be between 0 and 100")
    
    # Handle invalid input (non-float values)
    except ValueError:
        print("Please enter valid float values.")

# Evaluate and print the result based on the grade
if grade >= 90:
    print("Excellent!")
elif grade >= 70:
    print("Approved")
else:
    print("Failed")
