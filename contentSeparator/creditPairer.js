const fs = require('fs');
const dir = "/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Thematic Displays"

const creditFile = `${dir}/....txt`
const orderFile = `${dir}/....txt`

const orderedGNums = fs.readFileSync(orderFile, 'utf8')
  .split("\r")

const creditCollection = fs.readFileSync(creditFile, 'utf8')
  .split('\r')  
  .map(line => line.trim())
  .map(line => line.split('\t'))
  .reduce((collection, item) => {
    Object.assign(collection, 
      { [item[0]] : item[1] }
    )
    return collection
}, {})

const orderedCreds = orderedGNums
  .map(gNum => creditCollection[gNum])
  .join("; ")

fs.writeFileSync(`${dir}/creditList.txt`, newCreds.join("; "), 'utf-8')
