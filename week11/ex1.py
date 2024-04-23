# Initialize empty dictionary to store pairs of values
university_colors = {}

# Ask for number of universities in advance
num_universities = int(input("Enter number of universities: "))

# Loop to input university-color pairs
for i in range(num_universities):
    university = input("Enter University: ")
    color = input("Enter Color: ")
    university_colors[university] =  color

# Print contents of dictionary
print("University-Color Dictionary:")
for university, color in university_colors.items():
    print(f"{university}:{color}")
