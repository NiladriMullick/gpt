import re

s = "aeroplane,ship,(mythology,indus,dog),(cat,crow),hog"

# Define a pattern to match text inside brackets
pattern = r'\((.*?)\)'

# Define a function to replace commas inside brackets with semicolons
def replace_commas(match):
    return match.group(0).replace(',', ';')

# Use re.sub() to replace commas inside brackets with semicolons
Afinal_s = re.sub(pattern, replace_commas, s)

print(Afinal_s)
