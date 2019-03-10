#txt2csv
Simple command-line tool to convert `txt` files to `csv` (comma-separated values) file.

`txt2csv` treats each "chunk" of data (separated by an empty newline) as 1 row and each line within the chunk as 1 column.

For example:  
```
17916
5 Azurite
Bisbee, Arizona, USA
 
18285
12 Shattuckite with bisbeeite
Shattuck Mine, Bisbee, Arizona, USA
```

Will be converted to:  
```
17916 | 5 Azurite                     | Bisbee, Arizona, USA
18285 | 12 Shattuckite with bisbeeite | Shattuck Mine, Bisbee, Arizona, USA
```

## Installation
Best to place executable file (`txt2csv`) in `~/bin`. Remember to add `~/bin` to `$PATH`.

## Text formatting
`txt2csv` takes in any UTF-8-encoded text file. This means that any character that can be represented with Unicode *should* be supported, including diacritics. 

Subscripts and superscripts will work if they're not "fake" (ie. if they're Unicode sub/superscripts, not rich-text-formatted sub/superscripts). In Word, sub/superscripts accessed through the sub/superscript buttons tend to not be real Unicode characters, so any formatting will be lost when converted to a `txt` file. If possible, those should be converted to Unicode characters prior to saving as a `txt` file, or they can be surrounded by `<sub></sub>` or `<super></super>` tags.

[More information on Unicode sub/superscripts](https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts).

## Basic Usage
`txt2csv path/to/file.txt`

For instance, `txt2csv artifacts1.txt` will convert a text file called `artifacts1.txt` inside of the current directory. Alternatively, `txt2csv ~/Desktop/new_artifacts.txt` will convert a text file called `new_artifacts.txt` on the Desktop.

## Options
### Specifying output
By default, the `csv` file will have the same name as the `txt` file. In the above examples, the `csv` file outputted will be `artifacts1.csv` and `~/Desktop/new_artifacts.csv`. 

To specify a different output file name and/or file path, use the `-o` flag:
`txt2csv amnh1.txt -o ~/Desktop/artifact_case1.csv`

In that example, our input is `amnh1.txt`, located in the current directory, and the output is `artifact_case1.csv` located on the Desktop.

### Separating inline numbers

