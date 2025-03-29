mot = input("entre des mot : ")


def accronyme(phrase):
    phrase = mot.strip().split(" ")
    tab = [x[0].title() for x in phrase]
    acronyme = "".join(tab)
    print(f"l'accronyme est : {acronyme}")


accronyme(mot)
