class Suhu:
    def __init__(self,derajat):
        # celcius
        self.cf = (derajat*9/5)+32
        self.cr = derajat*4/5
        self.ck = derajat+273.15
        # fahrenheit
        self.fc = (derajat-32)*5/9
        self.fr = 4/9*(derajat-32)
        self.fk = (derajat-32)*5/9+273.15
        # reamur
        self.rc = (5/4)*derajat
        self.rf = (9/4*derajat)+32
        self.rk = (5/4*derajat)+273
        # kelvin
        self.kc = derajat-273.15
        self.kf = (derajat-273.15)*9/5+32
        self.kr = 4/5*(derajat-273)
while True:
    input_suhu = input("Masukkan suhu misal 30c, 30f, 30r, 30k: ")
    derajat = float(input_suhu[:-1])
    simbol = input_suhu[-1].lower()
    if simbol == 'c':
        simbol = Suhu(derajat)
        print(f"Celcius > Fahrenheit :{simbol.cf:.2f} F")
        print(f"Celcius > Reamur     :{simbol.cr:.2f} R")
        print(f"Celcius > Kelvin     :{simbol.ck:.2f} K")
    elif simbol == 'f':
        simbol = Suhu(derajat)
        print(f"Fahrenheit > Celcius :{simbol.fc:.2f} C")
        print(f"Fahrenheit > Reamur  :{simbol.fr:.2f} R")
        print(f"Fahrenheit > Kelvin  :{simbol.fk:.2f} K")
    elif simbol == 'r':
        simbol = Suhu(derajat)
        print(f"Reamur > Celcius     :{simbol.rc:.2f} C")
        print(f"Reamur > Fahrenheit  :{simbol.rf:.2f} F")
        print(f"Reamur > Kelvin      :{simbol.rk:.2f} K")
    elif simbol == 'k':
        simbol = Suhu(derajat)
        print(f"Kelvin > Celcius     :{simbol.kc:.2f} C")
        print(f"Kelvin > Fahrenheit  :{simbol.kf:.2f} F")
        print(f"Kelvin > Reamur      :{simbol.kr:.2f} R")
    else:
        print("INPUT TIDAK VALID !!!")
        continue
    while True:
        coba_lagi = input("Mau konversi lagi? (y/t): ").lower()
        if coba_lagi == 'y':
            break
        elif coba_lagi == 't':
            quit()
        else:
            print("INPUT TIDAK VALID !!!")
            continue