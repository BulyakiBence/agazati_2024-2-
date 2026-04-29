szelesseg = float(input("Add meg a szoba szélességét: "))
hosszusag = float(input("Add meg as szoba hosszúságát: "))
csomag = int(input("Hány csomag parkettád van: "))

terület = szelesseg*hosszusag
print(f"A szoba területe: {terület:.2f} négyzetméter")

if terület > csomag*2:
    print("Szükséges még parkettát vásárolni!")
else:
    print("Van elegendő parketta!")