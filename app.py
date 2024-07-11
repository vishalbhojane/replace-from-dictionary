import os
from pathlib import Path
import re
import json
from typing import Dict
import datetime

var_combinator = [
    'a)','b)','c)','d)','e)','f)','g)','h)','i)','j)','k)','l)','m)','n)','o)','p)','q)','r)','s)','t)','u)','v)','w)','x)','y)','z)',
    'A)','B)','C)','D)','E)','F)','G)','H)','I)','J)','K)','L)','M)','N)','O)','P)','Q)','R)','S)','T)','U)','V)','W)','X)','Y)','Z)',
    '0)','1)','2)','3)','4)','5)','6)','7)','8)','9)',
    '_)']

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

            # creating space between ()
            for i, line in enumerate(content):
                p_spaced_line = content[i].replace("($", "( $")
                content[i] = p_spaced_line                
            
            fh.seek(0)
            fh.truncate()
            fh.writelines(content)

            for j, line in enumerate(content):
                closing_paranthesis = line.count(')')
                # print("outerloop => " +line)
                if closing_paranthesis > 0 :
                    for jj in range (closing_paranthesis) :
                        temp = jj
                        for vc in var_combinator :
                            if vc in content[j] :
                                new_character = vc[:1] + " " + vc[1:]
                                # print(new_character)
                                p_spaced_line_2 = content[j].replace(vc, new_character)
                                content[j] = p_spaced_line_2 
            fh.seek(0)
            fh.truncate()
            fh.writelines(content)
            
            for k, line in enumerate(content):
                words_array = re.split(':|;|,| ', content[k])
                for word in words_array :
                    if(word in var_dict) :
                        content[k] = replace_var_values(content[k], word, var_dict)
                        replaced_count += 1
            fh.seek(0)
            fh.truncate()
            fh.writelines(content)
            fh.close()

            if(replaced_count == 0) :
                prCyan("No matching variable found in " + filename.name)
                save_to_log("No matching variable found in " + filename.name)
            else :
                prCyan("Replaced " + str(replaced_count) + " variables in " + filename.name)
                # saving empty line to log
                save_to_log("")
            
    except Exception as e:
        raise FileExistsError(f"Error while processing file '{filename}' due to error: {e}") from None

def init(folder_path: str) :
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

# input_dir = 'C:/Users/Vishal/Downloads/replace-from-dictionary/test'
# input_dir = '/Users/vishalbhojane/Downloads/replace-from-dictionary-11july/test'
input_dir = input("Paste the directory path:")
init(input_dir)