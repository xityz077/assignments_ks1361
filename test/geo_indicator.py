import re

def find_geographic_indicators(text):
    # Define a regular expression pattern to match geographic indicators
    # This is a basic example and can be expanded based on your specific needs
    pattern = r'\b(?:city|country|state|province|region|town)\b'

    # Find all matches in the text
    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    return matches

# Example usage
sample_text = "New York is a city in the United States. London is the capital of England."
geographic_indicators = find_geographic_indicators(sample_text)

print("Geographic Indicators found:")
for indicator in geographic_indicators:
    print(indicator)
