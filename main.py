# file = open("myFile.txt","w")
# file.write("myText")
# file.close()

import bookCreator2 as bookCreator2
import bookActivity as bookActivity
import fileReader as reader
import zadanie as zadanie

def main():
    print("1- külalisteraamat")
    print("2 - tegevusraamat")
    print("3 - Lugeda faili: ")
    print("4 - zadanie: ")
    userInput = input("Sinu valik: ")
    if userInput == "1":
        bookCreator2.guestBook()
    elif userInput == "2":
        bookActivity.bookActivity()
    elif userInput == "3":
         userFile = input("milline file sa tahad lugeda?")
         reader.readFile(userFile)
    elif userInput =="4":
        zadanie.zadanie()
        
    
    else:
        print("vale valik")
    
main()
