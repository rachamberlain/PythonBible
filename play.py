import math

test = math.ceil(2.1)
print(test)

name = input("what is your name?: ")
print(name.strip())

x = len(name)
print(x)



# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....

test = word[7:20]

print(test)


answer = word[word.index("establishment"):word.index("ari")]
print(answer)