filename = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as file:
    contents = file.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as file:
    for line in file:
        print(line.rstrip())

print("\n--- Storing the lines in a list:") 
with open(filename) as file:    
    lines = file.readlines()

for line in lines:
    print(line.rstrip())