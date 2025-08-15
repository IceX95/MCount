#!/bin/python3

from mark import *

def err(message):
      print(Fore.RED+f"Ошибка! {message}.")
      print("Повторите ещё раз."+Fore.WHITE)

def main():
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
    
if __name__ == "__main__":
    main()
