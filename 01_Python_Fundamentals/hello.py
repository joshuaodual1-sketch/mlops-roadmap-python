# method 1 for escaping characters
name = input("Whats your name? ")
print("Hello, \"", name, "\"!",sep="")
#method 2 for escaping characters
name = input("Whats your name? ")
print(f'Hello, "{name}"!')
#method 3 for escaping characters
name = input("Whats your name? ")
print('Hello, "', name, '"!', sep="")