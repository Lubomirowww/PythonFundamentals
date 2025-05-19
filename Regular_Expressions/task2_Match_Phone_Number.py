import re

number = input()

matches = re.findall(r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}", number)

print(" ".join(matches))

#maybe not work true