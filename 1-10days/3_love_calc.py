print("welcome to the love calculator")
name1 = input("what is your name ?")
name2 = input("what is their name ?")

combined_string = name1 + name2
lowercase = combined_string.lower()

t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")

true = t+r+u+e
love = l+o+v+e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your score is {love_score} and you are alright together")