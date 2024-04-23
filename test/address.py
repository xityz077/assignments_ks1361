import re

def find_addresses(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Define a regular expression pattern for matching addresses
    address_pattern = r'\d+\s+\w+\s+\w+,\s+\w+,\s+\w.*?(\d{5}|\d{6})'

    # Find all matches of addresses in the data
    addresses = re.findall(address_pattern, data)

    return addresses

# Replace 'file.txt' with the actual path of your file
file_path = 'census-first-names.txt'
addresses = find_addresses(file_path)

if addresses:
    print("Addresses found:")
    for address in addresses:
        print(address)
else:
    print("No addresses found in the file.")
