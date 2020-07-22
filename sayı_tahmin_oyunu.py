import random
hak = int(input("Kaç denemede doğru sayıyı bulursun: "))
puan = 100
ceza = puan/hak
sayı=0
random = random.randint(1,100)
while hak > 0:
    sayı+=1
    hak-=1
    puan -= ceza
    tahmin = int(input("Tahmininiz: "))
    if tahmin < random:
        print("Artır!")
                
    elif tahmin > random:
        print("Azalt")
    else:
        print(f"Tebrikler *{sayı}* tekrarda buldunuz... Puanınız: ***{puan}***")
        break
    if hak == 0:
        print(f"{sayı} denemede bulamadınız. Tutulan sayı *{random}* Tekrar deneyin!")