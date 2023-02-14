import time

question = int(input("Choisir un chiffre entre 1 et 32: "))


def countdown(question,number):
    while number:
        for i in question:
            print(i, end= '\n')
            time.sleep(2)
            number -= 1

while question >32 or question <1:
    question=int(input("error! entre 1 et 32 j'ai dit: "))

else:
    print("super!")
    enigme_1= ['multiplie par 2','ajoute 20','divise par 2','retire ton nombre de départ']
    countdown(enigme_1,len(enigme_1))
    reponse =input("c'est bon pour toi? Répondre par oui ou non: ")

    while reponse == "non":
        print("on reprend alors")
        enigme_1= ['multiplie par 2','ajoute 20','divise par 2','retire ton nombre de départ']
        countdown(enigme_1,len(enigme_1))
        reponse =input("c'est bon pour toi? Répondre par oui ou non: ")

    if reponse == "oui":
        print("on continue!")
        question2 = ['je connais ton chiffre!','il était pas dur en vrai','haha', 'alors ton chiffre est: ', 'tun!tun!']
        countdown(question2, len(question2))
        print("bah c'est: 10 evidemment!")
        time.sleep(5)
        print(" \nnullard ...")


