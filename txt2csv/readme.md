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

|       |                               |                                     |
|------:|-------------------------------|-------------------------------------|
| 17916 | 5 Azurite                     | Bisbee, Arizona, USA                |
| 18285 | 12 Shattuckite with bisbeeite | Shattuck Mine, Bisbee, Arizona, USA |

or:

|       |    |                            |                                     |
|------:|---:|----------------------------|-------------------------------------|
| 17916 | 5  | Azurite                    | Bisbee, Arizona, USA                |
| 18285 | 12 | Shattuckite with bisbeeite | Shattuck Mine, Bisbee, Arizona, USA |

## Installation
Best to place executable file (`txt2csv`) in `~/bin`. Remember to add `~/bin` to `$PATH`.

## Creating txt files
To create `txt` file from a `doc` or `docx` file, it's best to copy and paste the contents to a new file created in an app like TextEdit. Remember to remove formatting.

Don't "Save As" in Word because it doesn't create a clean enough `txt` file for this program.

## Text formatting
`txt2csv` takes in any UTF-8-encoded `txt` file. This means that any character that can be represented with Unicode *should* be supported, including diacritics. 

Subscripts and superscripts will work if they're not "fake" (ie. if they're Unicode characters, not rich-text- or application-formatted sub/superscripts). In Word, sub/superscripts accessed through the toolbar buttons tend to not be real Unicode characters, so any formatting will be lost when converted to a `txt` file. If possible, those should be converted to Unicode characters prior to saving as a `txt` file, or they can be surrounded by `<sub></sub>` or `<super></super>` tags.

[More information on Unicode sub/superscripts](https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts).

## Basic Usage
####`txt2csv path/to/file.txt`

For instance, `txt2csv artifacts1.txt` will convert a text file called `artifacts1.txt` inside of the current directory. Alternatively, `txt2csv ~/Desktop/new_artifacts.txt` will convert a text file called `new_artifacts.txt` on the Desktop.

## Options
For a list of all possible options, use:
####`txt2csv -h` OR `txt2csv --help`

### Specifying output
By default, the `csv` file will have the same name as the `txt` file. In the above examples, the `csv` file outputted will be `artifacts1.csv` and `~/Desktop/new_artifacts.csv`. To specify a different output file name and/or file path, use the `-o` flag:

####`txt2csv amnh1.txt -o ~/Desktop/artifact_case1.csv` OR `txt2csv amnh1.txt --output ~/Desktop/artifact_case1.csv`

In that example, our input is `amnh1.txt`, located in the current directory, and the output is `artifact_case1.csv` located on the Desktop.

### Separating inline numbers
If the input data has inline numbering, the numbers will need to be separated into their own column for sorting. To do that, use the `-n` flag, followed by the location of the inline numbers (the line number).

####`txt2csv artifacts.txt -n 2` OR `txt2csv artifacts.txt --numbered 2`

The line above specifies inline numbering at line number **2** and will convert:
```
17916
5 Azurite
Bisbee, Arizona, USA
 
18285
12 Shattuckite with bisbeeite
Shattuck Mine, Bisbee, Arizona, USA
```
to:

|       |    |                            |                                     |
|------:|---:|----------------------------|-------------------------------------|
| 17916 | 5  | Azurite                    | Bisbee, Arizona, USA                |
| 18285 | 12 | Shattuckite with bisbeeite | Shattuck Mine, Bisbee, Arizona, USA |

### Excluding lines
While processing data, `txt2csv` can ignore a list of line numbers and exclude them from the final `csv` file. Every line number listed has to exist in every chunk, otherwise an error will be thrown.

####`txt2csv artifacts.txt -x 1 4` OR `txt2csv artifacts.txt --exclude 1 4`

The line above specifies that lines **1** and **4** from every chunk should be ignored, converting:
```
17916
Azurite
Bisbee, Arizona, USA
Courtesy of some donor
 
18285
Shattuckite with bisbeeite
Shattuck Mine, Bisbee, Arizona, USA
Courtesty of another donor
```
to:

|    |                              |
|---:|------------------------------|
| 5  | Azurite                      |
| 12 | Shattuckite with bisbeeite   |

### Combining lines
The `-c` or `--combine` flag will combine the specified lines together in a single cell. Given the following input:
```
22
Azurite
Bisbee, Arizona, USA
 
16
Aragonite
Bisbee, Arizona, USA
```
####`txt2csv artifacts.txt -c 2 3` OR `txt2csv artifacts.txt --combine 2 3`
The command above will keep lines **2** and **3** in one cell, with each item separated by a line break, so the result will be:

|    |                      | 
|---:|----------------------|
| 22 | Azurite              |
|    | Bisbee, Arizona, USA |
| 16 | Aragonite            |
|    | Bisbee, Arizona, USA |

### All together
####`txt2csv artifacts.txt -o ~/Desktop/output.csv -n 1 -x 2 -c 1 3`
The command above will `artifacts.txt`, outputting `output.csv` on the Desktop. 

The following options are specified:

*  There is inline numbering on line **1**.
*  Line **2** will be excluded.
*  Lines **1** and **3** will be combined. Because line 1 has inline numbering, only the elements after the number will be combined with line 3.

Given `artifacts.txt` with the following content:
```
22 Azurite
8863
Bisbee, Arizöna, USA
 
16 H₂O⁸
14043
Bisbee, Arizona, USA
 
5 Azurite
17916
Bisbee, Arizona, USA

19 Aragonite
25795
Bisbee, Arizona, USA
Gift of William Earl Dodge
```

Running the command above will return an `output.csv` file on the Desktop, with the following content (when opened in Google Sheets):

|    |                            |
|---:|----------------------------|
| 22 | Azurite                    |
|    | Bisbee, Arizöna, USA       |
| 16 | H₂O⁸                       |
|    | Bisbee, Arizona, USA       |
| 5  | Azurite                    |
|    | Bisbee, Arizona, USA       |
| 19 | Aragonite                  |
|    | Bisbee, Arizona, USA       |
|    | Gift of William Earl Dodge |

