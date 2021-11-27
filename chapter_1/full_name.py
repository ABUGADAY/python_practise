first_name = "ada"
last_name = "lovelace" 
## lower than 3.6
# full_name = f"{first_name} {last_name}"
## 3.6 and above
full_name = "{} {}".format(first_name, last_name)
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)