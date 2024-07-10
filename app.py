import os
from pathlib import Path
import re
import json
from typing import Dict
import datetime

with open('dictonary.json') as json_file:
    colors_dictonary = json.load(json_file)

def save_to_log(text:str) -> None :
    log.write('\n' + str(text))
    
def prGreen(skk) :
    print("\033[92m{}\033[00m" .format(skk))
    
def prYellow(skk) :
    print("\033[93m{}\033[00m" .format(skk))

def prCyan(skk) :
    print("\033[96m{}\033[00m" .format(skk))

def replace_var_values(line: str, text: str, vars: Dict) -> str:
    new_text = line.replace(text, vars[text])
    save_to_log(text + " -> " + vars[text])
    return new_text

def replace_variables_in_file(filename: str, var_dict: Dict) -> None:
    try:
        with open(filename, "r+") as fh:
            prCyan("Processing " + filename.name)
            save_to_log(input_dir + "/" + filename.name)

            replaced_count = 0
            
            content = fh.readlines()
            
            for i, line in enumerate(content):

                # parenthesis
                p_spaced_line = line.replace("(", "( ").replace(")", " )")

                words_array = re.split(':|;|,| ', p_spaced_line)

                for word in words_array :
                    if(word in var_dict) :
                        content[i] = replace_var_values(line, word, var_dict)
                        replaced_count += 1
            if(replaced_count == 0) :
                prCyan("No matching variable found in " + filename.name)
                save_to_log("No matching variable found in " + filename.name)
            else :
                prCyan("Replaced " + str(replaced_count) + " variables in " + filename.name)
                # saving empty line to log
                save_to_log("")
            fh.seek(0)
            fh.truncate()
            fh.writelines(content)
            
            fh.close()
            
    except Exception as e:
        raise FileExistsError(f"Error while processing file '{filename}' due to error: {e}") from None

def init(folder_path: str) -> None:
    mydir = Path(folder_path)

    if not os.path.exists(folder_path) :
        prYellow('Invalid directory path')
        return

    if len(os.listdir(folder_path)) == 0 :
        prYellow('No files found')
        return

    prGreen('\nStart')

    for file in mydir.glob('*.scss'):
        if 'color' in file.name.lower() :
            prYellow('Excluded color file: ' + file.name)
            continue
        
        replace_variables_in_file(file, colors_dictonary)  

    prGreen('End\n')
    # saving empty line to log
    save_to_log("\n")

log = open('log.txt', 'a')
log.write("[" + str(datetime.datetime.now()) + "]")

input_dir = '/Users/vishalbhojane/Documents/MyCode/nodejs/replace-from-dictionary/test'
# input_dir = input("Paste the directory path:")
init(input_dir)