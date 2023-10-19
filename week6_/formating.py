total = 0
count = 0

for i in range(5):
    prompt = "Enter score for test " +str(i) + ":"
    score = int(input(prompt))
    total += score
    count += 1


print(f"The average is, {total / count:.2f}")

print("The average is", format(total / count,".2f"))
