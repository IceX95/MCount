#!/bin/python3

from mark import *
import json
from time import localtime
import os

savefile_path = "savefile.json"

def err(message):
      print(Fore.RED+f"Ошибка! {message}.")
      print("Повторите ещё раз."+Fore.WHITE)

def main():
    # with open("savefile.json", "") as savefile:
    #     savelog = json.load(savefile)
    if not os.path.exists(savefile_path):
        with open(savefile_path, 'w') as f:
            json.dump({}, f)
    with open(savefile_path, 'r') as f:
        try:
            savelog = json.load(f)
        except json.JSONDecodeError:
            savelog = {}

    print("Добро пожаловать! Напишите 0 для выхода.")
    sum = 0
    inp = 1
    while True:
        try:
            inp = tuple(int(e) for e in input(f"({sum}) >>> ").split())
            if inp == (0, ):
                break
            current = Mark(*inp)
            print(current.info)
            sum += current.cost
        except ValueError:
            err("Получили строку вместо числа")
        except TypeError:
            err("Вы ничего не ввели")
    print("Итоги: ")
    print(f"Всего заработано {sum} сум. Ура!")

    try:
        id_for_savelog = str(int(list(savelog.keys())[-1])+1)
    except IndexError:
        id_for_savelog = 0
    savelog[id_for_savelog] = {
        "date": f"{localtime().tm_year}, {localtime().tm_mday} {["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"][localtime().tm_mon-1]}",
        "sum": sum
    }
    with open("savefile.json", "w+") as savefile:
        json.dump(savelog, savefile, indent=4)
    
if __name__ == "__main__":
    main()
