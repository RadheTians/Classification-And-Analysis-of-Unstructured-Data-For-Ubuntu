
 # META-DATA EXTRACTOR
 
  META-DATA EXTRACTOR is a tool for classification and analysis of unstructured data,which extracts metadata of files in the unstructure ddata 
  using mongoDB.
 
  Thus, it allows Metadata-based classification using mongoDB. 
 
 ## USAGE
   
   Python2, PyQt5, monngoDB Cluster.
   
 ## REQUIREMENT
 
   Environment:
  
   Source code to this tool is coded in Python2, with its GUI running in PyQt5 env.
 
 
   Packages:

   subprocess, os, pymongo.


   Command Line Interface(CLI):
  
   exiftool.
 
 
 ## INSTALLATION 
 
   Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages subprocess, os, pymongo and set env for Python2.
 
   Packages :  

   $ pip install subprocess
   $ pip install os
   $ pip install pymongo

 
   Python2 env :
 
   $ sudo apt update
   $ sudo apt upgrade
   $ sudo apt install python2.7 python-pip


   Setting up PyQt5 env for Python2 :

   $ sudo apt-get install python-pyqt5


   Installing Command line interface(CLI) exiftool :
 
   $ sudo apt install libimage-exiftool-perl
 

 ## USER INSTRUCTIONS
 
   1)Open terminal(Ctrl+Alt+T), and change/move to the directory of the file mdata.py ,i.e, mini.

   $ cd /'PATH'/mini

 
   2)Open the tool to start, by executing mdata.py file.
 
   $ python mdata.py
 
   
   3)Enter the pathname in the tool for metadata extraction and click on the button for its corresponding type of sorted output.

