#!/bin/python3

from mark import *
import json
from time import localtime
import os

# from lang import lang_info
# if lang_info.current is not None:
#     try:
#         exec(f"from lang import {lang_info.current}")
#         labels = lang_info.current
#     except ImportError:
#         labels = lang_info.current = "en"
# else:
#     from lang import en
#     print(en.start)
#     print(lang_info.available)
#     while True:
#         choice = input(">>> ")
#         if choice in lang_info.available:
#             exec(f"from lang import {choice}")
#             break
#         else:
#             print(en.try_one_more_time)

import importlib
from lang import lang_info

def load_language_module(lang_code):
    try:
        return importlib.import_module(f"lang.{lang_code}")
    except ImportError:
        return None

with open("lang/current") as current_lang_file:
    current_lang = current_lang_file.read()
if current_lang != '':
    module = load_language_module(current_lang)
    if module:
        labels = module
    else:
        labels = load_language_module(lang_info.default)
        current_lang = lang_info.default
else:
    labels = load_language_module(lang_info.default)
    print(labels.start)
    print(labels.available_languages, lang_info.available)
    
    while True:
        choice = input(">>> ").strip().lower()
        if choice in lang_info.available:
            selected_lang = load_language_module(choice)
            if selected_lang:
                current_lang = choice
                with open("lang/current", "w", encoding="utf-8") as f:
                    f.write(current_lang)
                labels = selected_lang
                break
            else:
                print(labels.language_not_found)
        else:
            print(labels.try_one_more_time)

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
        "date": f"{localtime().tm_year}, {localtime().tm_mday} {["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"][localtime().tm_mon-1]}",
        "sum": sum
    }
    with open("savefile.json", "w+") as savefile:
        json.dump(savelog, savefile, indent=4)
    
if __name__ == "__main__":
    main()
