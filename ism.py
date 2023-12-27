while True:
    ism=(input("Ismingini kiriting: "))
    x=1
    for i in range(len(ism)):
        print(ism[:x])
        x+=1