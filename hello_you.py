# Ask user for name
name = input("What is your name?: ").strip().capitalize()

# Ask user for their age
age = input("How old are you?: ")

# Ask user where they live
live = input("Where do you live?: ").strip().capitalize()

# Ask user what they enjoy
hobbys = input("Whats your fave thing to do?: ").strip().capitalize()

# Create output text

string = "Your name is {}, you are {} years old, you live in {} and you love {}."
output = string.format(name, age, live, hobbys)

# Print output to screen

print(output)


