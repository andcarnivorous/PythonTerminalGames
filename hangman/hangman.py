import random
import re


with open("english-nouns.txt", "r") as words:
    words = words.readlines()
    words = [x.rstrip() for x in words]
    


with open("hangman.txt", "r") as art:
    art = art.readlines()

class Session():

    status = 3
    word = [x for x in random.choice(words)]
    wordstatus = ["-"]*len(word)

    def __del__(self):
        pass
    
    def hangmanprinter(self):
        if self.status == 3:
            print("".join(art[0:10]))
            print("\t%s" % "".join(self.wordstatus))

        elif self.status == 2:
            print("".join(art[11:21]))
            print("\t%s" % "".join(self.wordstatus))
        elif self.status == 1:
            print("".join(art[22:32]))
            print("\t%s" % "".join(self.wordstatus))
        else:
            print("".join(art[33:]))
            print("\t%s" % "".join(self.wordstatus))
    def getguess(self):
        
        guess = input("Insert a letter:\n>>> ")

        return guess[0]
    
    def checkguess(self):
        guess = self.getguess()
        if guess in self.word:
            indxs = [x[0] for x in enumerate(self.word) if x[1] == guess]
             for x in indxs:
                self.wordstatus[x] = self.word[x]
        else:
            self.status -= 1
        
    def wordprinter(self):
        print(self.wordstatus)

session = Session()
#print(session.word)
while session.status > 0 and "-" in session.wordstatus:

    session.hangmanprinter()
    session.checkguess()

if "-" in session.wordstatus:
    print("You lost! The word was:\t%s" % "".join(session.word).upper())

else:
    print("You won!")
