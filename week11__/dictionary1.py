# Creating Dictionaries

d1 = {}
print(f"d1: {d1}")
print(type(d1))

d2 = {1: "Welcome", 2: "to", 3:"Python", 4: "tutorial"}
print(f"d2: {d2}")

d3 = {"name": "Sam", "age": 22, "profession": "student"}
print(f"d3: {d3}")

d4 = dict({"name": "Sam", "age": 22, "profession": "student"})
print(f"d4: {d4}")

d5 = dict([("name", "Sam"), ("age", 22), ("profession", "student")])
print(f"d5: {d5}")
print("--------d6 START--------")
d6 = dict([("name", (("first_name", "Sam"), ("last_name", "crew"))), ("age", 22), ("profession", "student")])
print(f"d6: {d6}")
d6[0] = "Welcome"
print(f"d6: {d6}")
print(f"d6: {d6['name']}")
print(f"d6: {d6.get(0)}")
print(f"d6: {d6.pop(0)}")
print(f"d6: {d6}")
print(f"d6: {d6.pop('name')}")
print(f"d6: {d6}")

print(f"d6: {d6.popitem()}") # popitem removes last (key,value) from dictionary

print(f"d6 value: {d6.values()}")
print(f"d6 info: {d6['age']}")

try:
    print(f"d6 info: {d6['name']}")
except KeyError:
    print(f"d6 info: d6['name'] is not PRESENT")
    print(KeyError)

d6.clear()
print(f"d6 after clear: {d6}")
print("--------d6 END--------")
