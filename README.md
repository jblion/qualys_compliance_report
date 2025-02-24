
# Qualys CSV Compliance Report Splitter

Qualys can generate compliance reports in several formats.

When choosing the CSV file, it generates a unsual formatted file.

It contains several sections which have to be splitted to ensure we always have the same column's count.

There are 4 parts in this file: 
* a header : contains some information about the way the report has been generated
* a summary part : contains the list of hosts which their global compliance level
* an asset tags part : list all tags of all concerned servers
* a results parts : each control which its status and the expected value


## Authors

- [@jblion](https://www.github.com/jblion)


## Installation

Copy the script, Tune variables for files to be generated and voila
    
## Tech Stack

1 version in **Bash**

1 version in **Python**

Use the one you prefer.
