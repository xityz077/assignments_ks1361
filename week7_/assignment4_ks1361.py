#  Babylonian Method to solve for the square root of x

def babylonian_square_root(x):
    # Step 1: epsilon value: solution close to actual square root, four decimal places
    epsilon = 0.0001

    # Step 2: initial estimate is e
    e = x

    while True:

        # evaluating estimate
        # Step 3: x/e
        # Step 5: (x/e + e) /2; here, x/e become new average of (x/e and e)
        estimate = (x / e + e) / 2

        # Step 4:
        if estimate > e:
            # rare vase x/e == e
            if (estimate - e) < epsilon:
                break
        else:
            if (e - estimate) < epsilon:
                break

        # Step 5: revise estimate
        e = estimate

    return e


# Program starts here
while True:
    try:
        num = int(input("Enter a positive integer value: "))
        if num > 0:
            result = babylonian_square_root(num)
            print("Value \t Square Root")
            print(f"{num} \t\t {result:.3f}\n")
        else:
            print("Your number must be a positive integer. Please try again.\n")

    except ValueError:
        print("Exception captured: Entered number is not positive number\n")
