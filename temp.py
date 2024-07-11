import os
import glob
from pathlib import Path
import json

with open('dictonary.json') as json_file:
    colors_dictonary = json.load(json_file)

var_prefix = ['$']
var_combinator = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9',
    '-','_'
    ]

def get_space_padding(text: str) -> str :
    return " " + text

def replace_variables_in_file(file: str) -> None :

    with open(file,'r+') as file:

        content = file.readlines()

        for i, line in enumerate(content): 

            detected_variable = ""
            var_building = False

            # for character in content[i] :
            #     if character in var_prefix :
            #         detected_variable += character

            #     if character in var_combinator :
            #         detected_variable += character
            #     else :
            #         if detected_variable in colors_dictonary :
            #             print(detected_variable + " -> " + colors_dictonary[detected_variable])
            #             detected_variable = ""
            
            for word in content[i] :
                if word in var_prefix :
                    detected_variable += word
                    var_building = not var_building

                if (word in var_combinator) and (var_building) :
                    detected_variable += word
                else :
                    is_in_dictionary = detected_variable in colors_dictonary
                    var_building = not var_building
                    if is_in_dictionary :
                        print(detected_variable + " -> " + colors_dictonary[detected_variable])
                        detected_variable = ""
            print("new line")

        file.seek(0)
        file.truncate()
        file.writelines(content)

def find_scss_files(directory):
    for path in Path(directory).rglob('*.scss'):
        if not str(path).endswith('.scssc'): # exclude compiled SASS (`.scssc`) files
            yield str(path)

for filename in find_scss_files('C:/Users/Vishal/Downloads/replace-from-dictionary/test'):
    if 'color' in filename.lower() :
        continue
    replace_variables_in_file(filename)