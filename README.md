##XML Rebuilder##
Correct invalid xml structure

Run in **python 2.7**
Developed in **Debian 8.7.1**

###Setup Env###
Install xml parsing base module lxml
>$ sudo apt-get install python-lxml

Download and prepare generateDS
>$ wget https://pypi.python.org/packages/5c/80/013f5fd98ea80912f7c7b33278113d14479279b230492f0e9103ad921f9e/generateDS-2.28b0.tar.gz#md5=408c0ab4b47cd68ec7bd15dae23a7fe3
>$ tar zxvf generateDS-2.28b0.tar.gz
>$ cd generateDS-2.28b0/
>$ python generateDS.py --silence --external-encoding='utf-8' -o <generated-parser.py> -s <generated-parser-subs.py> <xml-schema.xsd>

Put <generated-parser.py> and <generated-parser-subs.py> under same level as Rebuild.py

Import generated parser in Rebuild.py

Update run() method to ajust schema types

Make Rebuild.py executable
>$ chmod 755 Rebuild.py

###Exceution###
Put all invalid files in Input/ folder

Run script
>$ ./Rebuild.py

Log is printed in terminal

All corrected files are in the Output/ folder

Origin files are moved to backup folder which named by current date

All skipped and failed files are remained in Input/ folder

**ATTENTION**
*The generated <simpleType> validation method are empty, especially for these XXX_ID elements, should be checked again*

###Enjoy###
;)