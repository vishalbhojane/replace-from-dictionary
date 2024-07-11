import os
from typing import Dict

import json
with open('dictonary.json') as json_file:
    colors_dictonary = json.load(json_file)

def replace_var_values(text: str, vars: Dict) -> str:
    for key, value in vars.items():
        text = text.replace(key, value)
    
    return text

def replace_variables_in_file(filename: str, var_dict: Dict) -> None:
    try:
        with open(filename, "r+") as fh:
            content = fh.readlines()
            
            for i, line in enumerate(content):
                content[i] = replace_var_values(line, var_dict)
                
            fh.seek(0)
            fh.truncate()
            fh.writelines(content)
            
            fh.close()
            
    except Exception as e:
        raise FileExistsError(f"Error while processing file '{filename}' due to error: {e}") from None

# replace_variables_in_file('t2.scss', colors_dictonary)

from pathlib import Path

working_dir = '/Users/vishalbhojane/Documents/MyCode/nodejs/test'

# root_dir = '/Users'

import pwd

mydir = Path(working_dir)

for file in mydir.glob('*.scss'):

    if 'color' in file.name.lower() :
        print('excluded the file: ' + file.name)
        continue

    replace_variables_in_file(file, colors_dictonary)  

# print(pwd.getpwuid(os.getuid())[0])
