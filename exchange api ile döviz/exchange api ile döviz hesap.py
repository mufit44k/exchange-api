import requests
import json
from datetime import datetime,date
class Döviz:
    def hesap(self,response,parabirimi1,parabirimi2,miktar):
        response = json.loads(response)
        response = response["rates"]
        print(json.dumps(response,indent=3,sort_keys=True).strip("{}"))
        para1 = float(response[parabirimi1])
        değer = miktar/para1
        para2 = float(response[parabirimi2])
        değer2 = değer*para2
        print(miktar,parabirimi1,"  ",değer2,parabirimi2)
        
    def döviz_hesap(self,parabirimi1,parabirimi2,miktar):
        url = "https://api.exchangeratesapi.io/latest?base="
        response = requests.get(url+str(parabirimi1)).text
        print("Anlık",parabirimi1,"karşısında diğer para birimleri")
        self.hesap(response,parabirimi1,parabirimi2,miktar)

    def tarih_doviz_hesap(self,tarih,parabirimi1,parabirimi2,miktar):
        url = "https://api.exchangeratesapi.io/"
        response = requests.get(url+str(tarih)+str("?base=")+str(parabirimi1)).text
        print(tarih,"tarihinde",parabirimi1,"karşısında diğer para birimleri")
        self.hesap(response,parabirimi1,parabirimi2,miktar)
    def sadece_fiyat_görüntüle(self,tarih,parabirimi):
        url = "https://api.exchangeratesapi.io/"
        response = requests.get(url+str(tarih)+str("?base=")+str(parabirimi)).text
        response = json.loads(response)
        response = response["rates"]
        print(tarih,"tarihinde",parabirimi,"karşısında diğer para birimleri")
        print(json.dumps(response,indent=3,sort_keys=True).strip("{}"))
    def parabirimleri(self,tarih):
        self.liste = []
        now = datetime.now().date()
        now = str(now)
        if now == tarih:
            url = "https://api.exchangeratesapi.io/latest"
            response = requests.get(url).text
            response = json.loads(response)
            rates = response["rates"]
            for i in rates:
                self.liste.append(i)
            self.liste.append(response["base"])
            return self.liste
        else:
            url = "https://api.exchangeratesapi.io/"
            response = requests.get(url+str(tarih)).text
            response = json.loads(response)
            rates = response["rates"]
            for i in rates:
                self.liste.append(i)
            self.liste.append(response["base"])
            return self.liste
while True:

    doviz = Döviz()
    print("""
    0-çıkış
    1-anlık olarak döviz çevirici
    2-belli bir tarihe göre döviz çevirici
    3-belli tarihteki döviz kurlarını görüntüleme
    """)
    işlem = input("işlem seçiniz:")
    if işlem == "0":

        cık = input("gerçekten çıkmak istiyormusunuz(E):")
        if cık == "E" or cık == "e":
            print("program sonlandı")
            break
        elif cık == "H" or "h":
            pass
        else:
            pass

    elif işlem == "1":
        print("kullanabileceğiniz para birimleri büyük küççük harf fark etmez")
        liste = doviz.parabirimleri(str(datetime.now().date()))
        print(liste)
        while True:
            
            parabirimi1 = input("elinizdeki para birimi:").upper()
            parabirimi2 = input("çevirmek istediğiniz para birimi:").upper()
            if parabirimi1 in liste and parabirimi2 in liste:
                break
            else: 
                print("parabirimleri hatalı")
        while True:
            try:
                miktar = float(input("miktar:"))
                doviz.döviz_hesap(parabirimi1,parabirimi2,miktar)
                break
            except ValueError:
                print("miktarı kontrol edin")
    elif işlem == "2":
        while True:
            tarih = input("tarihi giriniz min(1999-1-4):")
            try:
                a = tarih.split("-")
                yil = int(a[0])
                ay = int(a[1])
                gun = int(a[2])
                tar = date(yil,ay,gun)
                if yil == 1999 and ay == 1:
                    if gun >=4:

                        print("kullanabileceğiniz para birimleri büyük küççük harf fark etmez")
                        liste = doviz.parabirimleri(tarih)
                        print(liste)
                        break
                    else:
                        print("tarih hatalı min(1999-01-04)")
                elif yil >= 1999 and ay >= 1 and gun >=1:
                    print("kullanabileceğiniz para birimleri büyük küççük harf fark etmez")
                    liste = doviz.parabirimleri(tarih)
                    print(liste)
                    break
                else:
                    print("tarih hatalı min(1999-01-04)")



            except:
                print("tarih hatalı min(1999-01-04)")
        while True:
            parabirimi1 = input("elinizdeki parabirimi:").upper()
            parabirimi2 = input("çevirmek istediğiniz parabirimi:").upper()
            if parabirimi1 in liste and parabirimi2 in liste:
                break
            else:
                    print("para birimleri hatalı")
        while True:
            try:
               miktar = float(input("miktar:"))
               break
            except ValueError:
                print("sayısal değer olmalı")
        doviz.tarih_doviz_hesap(tarih,parabirimi1,parabirimi2,miktar)
            




    elif işlem == "3":
        while True:
            tarih = input("tarihi giriniz min(1999-1-4):")
            try:
                a = tarih.split("-")
                yil = int(a[0])
                ay = int(a[1])
                gun = int(a[2])
                tar = date(yil,ay,gun)
                if yil == 1999 and ay == 1:
                    if gun >=4:

                        print("kullanabileceğiniz para birimleri büyük küççük harf fark etmez")
                        liste = doviz.parabirimleri(tarih)
                        print(liste)
                        break
                    else:
                        print("tarih hatalı min(1999-01-04)")
                elif yil >= 1999 and ay >= 1 and gun >=1:
                    print("kullanabileceğiniz para birimleri büyük küççük harf fark etmez")
                    liste = doviz.parabirimleri(tarih)
                    print(liste)
                    break
                else:
                    print("tarih hatalı min(1999-01-04)")

            except:
                print("tarih hatalı min(1999-01-04)")
        while True:
            parabirimi1 = input("elinizdeki para birimi:").upper()
            if parabirimi1 in liste:
                break
            else:
                print("hatalı para birimi")
        doviz.sadece_fiyat_görüntüle(tarih,parabirimi1)
    else:
        print("geçersiz işlem")





