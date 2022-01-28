print("1) Hány diák tanul az osztályban?")
print(f"{len(Tanulo.lista)} diák tanul az osztályban!")

print("2) Hány fiú tanul az osztályban?")
fiukszama = 0
for sor in f:  
    if(Tanulo.lista[sor].nem == "F"):
        fiukszama += 1
print(f"{fiukszama} fiú tanul az osztályba!")

print("3) Hány lány tanul az osztályban?")
lanyokszama = 0
for sor in f:  
    if(Tanulo.lista[sor].nem == "F"):
        lanyokszama += 1
print(f"{lanyokszama} lány tanul az osztályba!")