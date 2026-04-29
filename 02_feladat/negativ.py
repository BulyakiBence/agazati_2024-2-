import random

negativok = 0
def negativ(x):
    if x < 0:
        return True
    else:
        return False
    
for i in range(100):
    szam = random.randint(-50,50)
    if negativ(szam) == True:
        negativok += 1

print(f"A generált számok között {negativok} negatív szám szerepelt")    