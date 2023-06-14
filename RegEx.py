import re

txt = "The rain in Spain"

# https://regex101.com/
# https://www.w3schools.com/python/python_regex.asp

# find start with rain, end with Spain
x = re.search("^The.*Spain$", txt)
print(x)
