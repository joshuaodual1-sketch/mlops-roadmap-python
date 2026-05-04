# 4 Ways to buide a string
# MEthod 1 concatenation with +
name = input("What's your name?")
print("Hello, " + name)
# Method 2 Multiple arguments (COMMA)
print("Hello,", name) # auto inserts a space
#Method 3 Named Parameters (End/Sep)
print("Hello, ", end="")
print(name)
#Method 4 F- strings (higly recommended)
print(f"Hello, {name}")
