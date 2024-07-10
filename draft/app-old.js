const fs = require('fs');
const variableRegex = /\$[a-zA-Z-0-9]+/;
const colors = require('./dictonary.json');
const SOURCE_FILE = "./source.txt";

function countOccurances(searchTerm, filePath) {
    let counter = 0;
    const content = fs.readFileSync(filePath);
    const linesArray = content.toString().split('\n');
    for (let i = 0; i < linesArray.length; i++) {
        const index = linesArray[i].indexOf(searchTerm);
        if (index !== -1) {
            counter++;

        }
    }
    return counter;
}

// async function getColors(url) {
//     const res = await fetch(url)
//     const json = await res.json()
//     return json;
// }

// const colors = getColors('./dictonary.json');
// console.log(typeof colors)

// let count = 0
// for (let color in colors){
//     count += 1
// }
// console.log(count)

// console.log(countOccurances('$border-blue11', "./source.txt"));

// for (let color in colors){
//     console.log(color)
// }

// console.log(countOccurances('$blue-lighter1', "./source.txt"))

Object.entries(colors).forEach((color)=>{
    
    replaceTextInFile(SOURCE_FILE, color[0], color[1]).then(() => {
        console.log("Done!");
      }).catch(error => {
        console.error(error.message);
      });
})


// function replaceColors(srcFile, srcColor, desColor) {
//     fs.readFileSync(srcFile, 'utf-8', (err, contents) => {
//         if (err) {
//             return console.error(err)
//         }

//         // Replace string occurrences
//         const updated = contents.replace(srcColor, desColor)

//         // Write back to file
//         fs.writeFileSync(srcFile, updated, 'utf-8', err2 => {
//             if (err2) {
//                 console.log(err2)
//             }
//         })
//     })
// }

// replaceColors(SOURCE_FILE, '$blue-lighter1', '#TEST');

// const fs = require('fs');
const path = require('path');

function replaceTextInFile(filename, searchString, replacementString) {
  // Read file content asynchronously
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

// replaceTextInFile(SOURCE_FILE, '$blue-lighter1', '#TEST').then(() => {
//     console.log("Done!");
//   }).catch(error => {
//     console.error(error.message);
//   });