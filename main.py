import requests
import json
import os
import time
from datetime import date, datetime


#get API_KEY from https://www.exchangerate-api.com/
api = '5b928b7d8567da03de2d4cda'



def main():
    v = 5
    pair = 'nie podany'
    data = 'n/a'
    kurs = 0.00

    while v !=0:
        os.system('cls')
        print("aktualna para:",pair,"\naktualny kurs: ",kurs,"\nwybierz opcję:\n    1. wybierz parę\n    2. oblicz kurs\n    3. odwróć parę\n    4. dane z api\n    0. wyjście", sep="")
        v = int(input())
        if v == 1:
            os.system('cls')
            wa = input('podaj walutę podstawową skrótem np. EUR: ').upper()
            wb = input('podaj walutę wymiany skrótem np. PLN: ').upper()
            pair = wa+'-'+wb
            url = 'https://v6.exchangerate-api.com/v6/'+api+'/pair/'+wa+'/'+wb
            response = requests.get(url)
            data = response.json()
            if data['result'] == "error":
                os.system('cls')
                print("nie poprawna para\n spróbuj ponownie.")
                time.sleep(2)
                pair = 'nie podany'
            else:
                kurs = data['conversion_rate']

        elif v == 2 and kurs == 0:
            os.system('cls')
            print("nie podałeś pary")
            time.sleep(2)
            continue
    
        elif v == 2 and kurs !=0:
            # Making our request
            os.system('cls')
            x = input('podaj kwotę: ')
            print("po wymiany kwota wynosi:", float(x) * kurs, str(wb), sep=" ")
            input("wciśnij dowolny przycisk, aby kontynuować...")
        
        elif v == 3:
            a = wa
            b = wb
            wa = b
            wb = a
            pair = wa+'-'+wb
            url = 'https://v6.exchangerate-api.com/v6/'+api+'/pair/'+wa+'/'+wb
            response = requests.get(url)
            data = response.json()
            kurs = data['conversion_rate']
            print("para została zamieniona")
            time.sleep(2)
        
        elif v == 4:
            spr()

        elif v == 0:
            break

        else:
            os.system('cls')
            print("nie poprawny wybór")
            time.sleep(2)
            

    os.system('cls')
    print("do zobaczenia")

def spr():
    url_dat = 'https://v6.exchangerate-api.com/v6/'+api+'/quota'
    response = requests.get(url_dat)
    data = response.json()
    ile = data['requests_remaining']
    poczat = data['plan_quota']
    odswiez = data['refresh_day_of_month']

    dzis = datetime.now()
    format = dzis.strftime("%d/%m/%Y %H:%M:%S")

    d0 = date(dzis.year, dzis.month, dzis.day)
    d1 = date(dzis.year, dzis.month + 1, odswiez)
    odl = d1 - d0

    os.system('cls')
    print("dzisiaj:", format)
    print("zostało", ile,"requestów")
    print("początkowo było", poczat, "requestów")
    print("data następnego resetu:",d1, sep=" ")
    print("zostało",odl.days,"dni do resetu liczbę requestów", sep=" ")
    input("wciśnij dowolny przycisk, aby kontynuować...")


if __name__ == '__main__':
    main()