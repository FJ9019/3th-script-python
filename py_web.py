#coding: utf-8

age = 15

content = [
    ("Rockabye baby", "UNKNOW", 0),
    ("Eighties Baby", "Jammy Jams", 0),
    ("Babies go Beatles", "UNKNOW", 0),
    ("Le Voyage de Chihiro", "Hayao Miyazaki", 1),
    ("Le Roi Lion", "Roger Allers et Rob Minkoff", 1),
    ("Aladin", "John Musker et Ron Clements", 1),
    ("One Piece", "Eiichiro Oda", 2),
    ("Death Note", "Tsugumi Obba", 2),
    ("Fullmetal Alchemist", "Hiromu Arakawa", 2),
    ("OSS 117", "Michel Hazanavicius", 2),
    ("The Descent", "Neil Marshall", 2),
    ("La Ligne Rouge", "Terrence Malick", 4),
    ("Voyage au bout de l'enfer", "Michael Cimino", 4),
    ("Persuation", "Carrie Cracknell", 3),
    ("Book od Love", "Analeine Cal y Mayor", 3)
]

if 0<=age<=5: #Bébé 0
    print("Bienvenue dans l'interface Bébé !")
    for item in content:
        if item[2]<=0:
            print(f"{item[0]} de {item[1]}")
        else:
            print(f"{item[0]}")    
elif 6<=age<=12: #Enfant 1
    print("Bienvenue dans l'interface enfant !")
    for item in content:
        if item[2]<=1:
            print(f"{item[0]} de {item[1]}")
    
elif 13<=age<=18: #Adolescent 2
    print("Bienvenue dans l'interface adolescent !")
    for item in content:
        if item[2]<=2:
            print(f"{item[0]} de {item[1]}")

elif 19<=age<=50: #Adulte 4
    print("Bienvenue dans l'interface adulte !")
    for item in content:
        if item[2]<=4:
            print(f"{item[0]} de {item[1]}")

else: #Senior 3
    print("Bienvenue dans l'interface Senior !")
    for item in content:
        if item[2]<=3:
            print(f"{item[0]} de {item[1]}")