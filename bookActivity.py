import datetime

def bookActivity():
    name = input("Sinu nimi: ")
    action = input("Sinu tegevus: ")
    time = datetime.datetime.now()
    text = f"Date: {time}, Nimi: {name}, Oli selline tegevus: {action}\n"
    file = open("logs.txt","a", encoding="utf-8")
    file.write(text)
    file.close()
    print("Activity oli salvestatud edukalt")
