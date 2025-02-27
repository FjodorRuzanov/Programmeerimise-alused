def zadanie():
    id1 = 1
    for i in  range(100):
        file = open("zadanie.txt", "a", encoding="utf-8")
        nimi = userInput = input("Sisesta nimi: ")
        vana = userInput = input("Sisesta vana: ")
        text = f"id = {id1},Nimi: {nimi}, Vana: {vana}\n"
        print(text)
        file.write(text)
        id1 += 1
        file.close()
        
        