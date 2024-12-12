path = "C:\\Users\\earlo\\OneDrive\\Desktop\\python\\writing.txt"
text = "Hello, World! Meow Meow"

with open(path, 'w') as file:
    file.write(text)
with open(path, "r") as file:
    print(file.read())

