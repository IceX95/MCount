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