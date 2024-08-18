play = ["Orãção","Cotidiano","Vai passar","O que é o que é","Bebado e o equilibrista","Aquarela"]

"""Lista original"""
for musica in range(len(play)):
    print(play[musica])

play.append("A paz")

"""Lista apos adição"""
for musica in range(len(play)):
    print(play[musica])

play.remove("Aquarela")

"""Lista apos remoção"""
for musica in play:
    print(musica) 
