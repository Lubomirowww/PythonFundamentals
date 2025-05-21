import re

text = "MItko is good Mitko"

result  = re.findall("Mitko", text, re.IGNORECASE)

print(result)
