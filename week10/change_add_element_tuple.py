# Change and add elements to the tuple
print("Change and add elements to the tuple:")
city = ("Texas", "New York", "New Jersey", "Utah")
print(f"Original city:\n{city}")
newcity = list(city)
newcity[1] = "Ohio"
city = tuple(newcity)
print(f"\nNew city:\n{city}")

print("\n------------------------------------------\n")

# Change and add elements to the tuple
print("\nChange and add elements to the tuple:")
city = ("Texas", "New York", "New Jersey", "Utah")
print(f"Original city:\n{city}")
newcity = list(city)
newcity.append("Arizona")
city = tuple(newcity)
print(f"\nNew city:\n{city}")

print("\n------------------------------------------\n")

# Change and add elements to the tuple
print("\nChange and add elements to the tuple:")
nested_tuple = ("Dallas", "Frisco", [2, 8, 9], ("Denton", "Plano"))
print(f"Original city:\n{nested_tuple}")
nested_tuple[2] [0] = 9
print(f"\n New nested_tuple:\n{nested_tuple}")
