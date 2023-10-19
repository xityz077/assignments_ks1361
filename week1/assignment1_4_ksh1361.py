
def calculate_tip(total_amount, tip_percentage):
    tip_amount = total_amount*(tip_percentage/100)
    return tip_amount

def main():
    try:
        total_amount = float(input("Enter the total amount:$"))
        tip_percentage = float(input("Enter the tip percentage:"))

        tip_amount = calculate_tip(total_amount,tip_percentage)
        total_with_tip = total_amount + tip_amount

        print(f"Tip amount:${tip_amount:.2f}")
        print(f"Tip amount with tip:${total_with_tip:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()







# print('Frisco, TX 75035')


name1 = "star1"
name2 = 12
type(name1)
type(name2)

#Get the user's first name
# first_name = input("Enter your first name: ")
# print(first_name)

# age = int(first_name)
