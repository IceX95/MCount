#!/bin/python3

from mark import *
import json
from time import localtime
import os
from lang.labels import labels

savefile_path = "savefile.json"

def err(message):
      print(Fore.RED + message)
      print(labels.try_one_more_time + Fore.WHITE)

def main():
    if not os.path.exists(savefile_path):
        with open(savefile_path, 'w') as f:
            json.dump({}, f)
    with open(savefile_path, 'r') as f:
        try:
            savelog = json.load(f)
        except json.JSONDecodeError:
            savelog = {}

    print(labels.welcome)
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
            err(labels.string_instead_of_number)
        except TypeError:
            err(labels.nothing_entered)
    print(labels.results, sum, labels.sums)

    try:
        id_for_savelog = str(int(list(savelog.keys())[-1])+1)
    except IndexError:
        id_for_savelog = 0
    savelog[id_for_savelog] = {
        "date": [localtime().tm_year, localtime().tm_mon, localtime().tm_mday],
        "sum": sum
    }
    with open("savefile.json", "w+") as savefile:
        json.dump(savelog, savefile, indent=4)
    
if __name__ == "__main__":
    main()
