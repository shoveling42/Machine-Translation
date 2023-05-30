from kiwipiepy import Kiwi

a = Kiwi()

print(a.tokenize("I like apple"))
print(a.tokenize("I bought a dining table from the home furniture section."))
print(a.tokenize("I also bought a lot of other products as well."))
print(a.tokenize("Let's set up the presentation date for BBB's FFF processed food product"))
print(a.tokenize("Would you mind if I go home now?"))
print(a.tokenize("What a nice day!"))