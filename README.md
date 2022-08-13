# Difference generator

### Hexlet tests and linter status:



[![Actions Status](https://github.com/seeu359/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/seeu359/python-project-lvl2/actions)
<a href="https://codeclimate.com/github/seeu359/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/592c10dfa0e8e72e5fea/maintainability" /></a>
<a href="https://codeclimate.com/github/seeu359/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/592c10dfa0e8e72e5fea/test_coverage" /></a>
[![Code check](https://github.com/seeu359/python-project-lvl2/actions/workflows/lint_and_pytest_checks.yml/badge.svg)](https://github.com/seeu359/python-project-lvl2/actions/workflows/lint_and_pytest_checks.yml)

---
### Installation: 

Clone repository and install:  
``$ git clone https://github.com/seeu359/python-project-lvl2.git``

### Instruction:
Difference generator - Command Line Interface. The utility compares 2 files and 
returns the difference between them as formatted text.  
The utility is able to work with the formats: ```json```, ```yaml```


**To compare files in the terminal, type:**  
>```$ gendiff <path1>  <path2>```

### Arguments

1. -**h, --help** - ```$ gendif -h``` - shows a prompt;
2. **-f, --format** - ```$ gendif -f``` - Allows you to select the format of the 
difference output. **Available formats:**
  
   1. `-f stylish`- default form. Example output:
  
   >{  
     common: {  
 +  follow: false  
     setting1: Value 1  
 -  setting2: 200  
 -  setting3: true  
 +  setting3: {   
       key: value  
     }  
}
    2. `-f plain`. Example output:  
  
    > Property 'common.follow' was added with value: false  
Property 'common.setting2' was removed  
Property 'common.setting3' was updated. From true to [complex value  
Property 'common.setting4' was added with value: 'blah blah'
    3. `-f json`. Returns the difference in json format.
  
        >{"-follow": false, "=host": "hexlet.io", "-proxy": "123.234.53.22", "-timeout": 50, "+timeout": 20, "+verbose": true}
---
        









<a href="https://asciinema.org/a/511274" target="_blank"><img src="https://asciinema.org/a/511274.svg" /></a>
<a href="https://asciinema.org/a/511276" target="_blank"><img src="https://asciinema.org/a/511276.svg" /></a>
<a href="https://asciinema.org/a/512623" target="_blank"><img src="https://asciinema.org/a/512623.svg" /></a>
<a href="https://asciinema.org/a/514463" target="_blank"><img src="https://asciinema.org/a/514463.svg" /></a>
<a href="https://asciinema.org/a/514465" target="_blank"><img src="https://asciinema.org/a/514465.svg" /></a>