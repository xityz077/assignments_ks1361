try:
    answer = 'y'
    while answer == 'y':
        # Initialize empty dictionary to store pairs of values
        university_colors = {}

        # Ask for number of universities in advance
        num_universities = int(input("Enter number of universities: "))

        # Loop to input university-color pairs
        for i in range(num_universities):
            university = input("Enter University: ")
            color = input("Enter Color: ")
            university_colors[university] = color

        # Prompt specific university name
        prompt_university = input("which university's pair of university-color to print: ")

        # Print contents of dictionary
        print("University-Color Dictionary:")

        if prompt_university in university_colors.keys():
            print(f"{university}:{color}")
            answer = input("continue...(y/n)?").lower()
        else:
            print("Given university is not found!")
            answer = input("continue...(y/n)?").lower()
    print("Thank you for playing.")
except ValueError:
    print("Please! Enter only integer. Try again!")
