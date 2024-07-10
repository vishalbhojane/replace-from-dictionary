const fs = require('fs');
const variableRegex = /\$[a-zA-Z-0-9]+/;
const colors = require('./dictonary.json');
const SOURCE_FILE = "./source.txt";

function replaceTextInFile(filename, searchString, replacementString) {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      }
      const result = data.split(searchString).join(replacementString);
      
      fs.writeFile(filename, result, err => {
        if (err) {
          reject(err);
        }
        resolve();
      });
    });
  });
}

Object.entries(colors).forEach((color)=>{
  replaceTextInFile(SOURCE_FILE, color[0], color[1]).then(() => {
      console.log("Done!");
    }).catch(error => {
      console.error(error.message);
    });
})