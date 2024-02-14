# Function to apply additional 5% discount
def discc(payable):
    # Calculate the discount
    disc = payable * 0.05
    # Calculate the new payable amount after the additional discount
    amt = payable - disc
    # Display message indicating additional discount and total payable amount
    print("Lucky Day! You are Eligible for an additional 5% Discount.")
    print("Total Amount after additional discount:", amt)

# Function to calculate initial discount based on shopping amount
def shop(amt):
    if amt >= 500 and amt < 1000:
        print("Congratulations! You are Eligible for a 5% Discount.")
        disc = amt * 0.05
        payable = amt - disc
        print(f"You have received {disc} discount and total payable is {payable}")
        return payable
    elif amt >= 1000 and amt < 2000:
        print("Congratulations! You are Eligible for an 8% Discount.")
        disc = amt * 0.08
        payable = amt - disc
        print(f"You have received {disc} discount and total payable is {payable}")
        return payable
    elif amt > 2000:
        print("Congratulations! You are Eligible for a 10% Discount.")
        disc = amt * 0.1
        payable = amt - disc
        print(f"You have received {disc} discount and total payable is {payable}")
        return payable

# Main program
print("Welcome to Store")
amt = float(input("Enter the amount of shopping: "))
print("............................................................")

# Call shop function to calculate initial payable amount
payable = shop(amt)

# Ask if the customer is a member and apply additional discount if yes
ans = input("Are You a member of our Store? (Yes/No)").lower()
if ans == "yes":
    discc(payable)
else:
    print("Good day! Shop Again")
