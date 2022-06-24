print("Welcome to Treasure Island.\nYour mission is to find the Teasure")
qns1=input("left or right: ")
if qns1=='right'.lower():
    print("game over")
else:
    qns2=input("swim or wait: ")
    if qns2=='swim'.lower():
        print("Game Over")
    else:
        qns3=input("which door: Red/Yellow/Blue? ")
        if qns3=='red'.lower() or qns3=='Blue'.lower():
            print("Game Over")
        else:
            print("you win")
