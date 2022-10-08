print("Permainan Gunting Batu Kertas")
print()
print("G : Gunting")
print("B : Batu")
print("K : Kertas")
print()
print("Pilih (G, B, atau K)")
print()

skorPlayer1 = 0
skorPlayer2 = 0

while True:
    player1 = input("Player 1 > ")
    player2 = input("Player 2 > ")
    print()
    if player1 == "G":
        if player2 == "G":
            print("Draw")
        elif player2 == "B":
            print("Player 2 Menang")
            skorPlayer2 += 1
        elif player2 == "K":
            print("Player 1 Menang")
            skorPlayer1 += 1
        else:
            print("Player 2 Invalid")
    elif player1 == "B":
        if player2 == "B":
            print("Draw")
        elif player2 == "K":
            print("Player 2 Menang")
            skorPlayer2 += 1
        elif player2 == "G":
            print("Player 1 Menang")
            skorPlayer1 += 1
        else:
            print("Player 2 Invalid")
    elif player1 == "K":
        if player2 == "K":
            print("Draw")
        elif player2 == "G":
            print("Player 2 Menang")
            skorPlayer2 += 1
        elif player2 == "B":
            print("Player 1 Menang")
            skorPlayer1 += 1
        else:
            print("Player 2 Invalid")
    else: 
        print("Player 1 Invalid")
    print()
    print("Skor = ", skorPlayer1, " : ", skorPlayer2)
    if skorPlayer1 == 3 or skorPlayer2 == 3:
        print("Terimakasih sudah bermain!")
        exit()
    else:
        print()
        continue