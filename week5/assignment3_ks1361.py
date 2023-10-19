import locale

# Set locale to US English
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


# function to calculate compound interest
def compound_interest(P, r, n, t):
    p_prime = P * (1 + (r / n)) ** (n * t)
    return p_prime


# Getting input from user
print("Welcome to the Compound Interest Calculator.")
P = float(input("Please enter the initial amount of your investment: "))
r = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
t = int(input("Please enter the number of years for the investment: "))
n = int(input("Please enter the number of compoundings per year: "))

# Calculate compound interest
new_balance_after_t_years = compound_interest(P, r, n, t)

# Display the result
print(f"Original Investment: {locale.currency(P, grouping=True)}")
print(f"Interest Earned:\t {locale.currency((new_balance_after_t_years - P), grouping=True)}")
print(f"Final Balance:\t\t {locale.currency(new_balance_after_t_years, grouping=True)}")
