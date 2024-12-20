colors = ["orange", "green", "blue", "pink"]
print(colors)
print(colors[1])    #green

fruits = ["apple", "orange", "banana", "strawbery"]
#For-each loop
for item in fruits:
    print(item)
print("")

#For loop
for index in range(len(fruits)):   #range(0, len(friuts))
    print(fruits[index])
print("")

# lastfruit = fruits[len(fruits)-1]
lastfruit = fruits[-1]
print(lastfruit)
input()