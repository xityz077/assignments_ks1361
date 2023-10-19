# prime the loop
total = 0
count = 0
score = 0

# sum and count scores until sentinel is detected
while score >= 0:
    score = int(input("Enter score (-1 to end): "))
    if score >= 0:
        total += score
        count += 1


print(f"The average is, {total / count:.2f}")

print("The average is", format(total / count,".2f"))
