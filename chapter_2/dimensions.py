dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 250

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)   

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)