filename = "learning_python.txt"

with open(filename) as f:
    for line in f:
        new_line = line.replace('Python','C')
        print(new_line.rstrip())