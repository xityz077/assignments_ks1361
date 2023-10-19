
def miles_to_kilometers(miles):
    kilometers = miles*1.60934
    print("in miles_to_kilometers")
    return kilometers

def main():
    print("main.......")
    try:
        miles = float(input("Enter the number of miles in the road trip: "))
        kilometers = miles_to_kilometers(miles)

        print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")
    except ValueError:
        print("Invalid input. Please enter a valid number of miles.")

if __name__ == "__main__":
    print("__name__")
    main()
    print("end __name__")







# print('Frisco, TX 75035')


name1 = "star1"
name2 = 12
type(name1)
type(name2)

#Get the user's first name
# first_name = input("Enter your first name: ")
# print(first_name)

# age = int(first_name)
