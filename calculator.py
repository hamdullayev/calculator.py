print("""

***1:Toplama emeli ucun 1 daxil edin :
***2:Cixma emeli ucun 2 daxil edin :
***3:Bolme emeli ucun 3 daxil edin :
***4:Vurma emeli ucun 4 daxil edin :

""")
a = int(input("Seciminizi daxil edin : "))

if a == 1:
    toplama1 = int(input("Birinci ededi daxil edin : "))
    toplama2 = int(input("Ikinci ededi daxil edin : "))
    toplama = toplama1 + toplama2
    print(toplama)
elif a == 2:
    cixma1 = int(input("Birinci ededi daxil edin : "))
    cixma2 = int(input("Ikinci ededi daxil edin : "))
    cixma = cixma1 - cixma2
    print(cixma)
elif a == 3:
    bolme1 = int(input("Birinci ededi daxil edin : "))
    bolme2 = int(input("Ikinci ededi daxil edin : "))
    bolme = bolme1 / bolme2
    print(bolme)
elif a == 4:
    vurma1 = int(input("Birinci ededi daxil edin : "))
    vurma2 = int(input("Ikinci ededi daxil edin : "))
    vurma = vurma1*vurma2
    print(vurma)
else:
    print("Opps!...Ne ise ters getdi...")
    
print(input("Press any key to exit..."))