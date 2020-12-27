# BookReaderTool

## Overview

This project is to develop Book Reader Tool deployed on AWS. The functionality of this site is to upload the classic book pdf files, 
view the selected book and search the necessary word in English.
Since the pdfs consist of the scanned images, the OCR technology is used to implement the search functionality, where 
Google Vision API and Tesseract library are used for OCR.
As a backend, the Django framework is used, and the database is Sqlite.

## Structure

- core, payments, reading, ui, users

    Django Backend source code
    
- static

    Javascript, CSS source code for stylist of the project

- templates

    The Front end files with HTML5

- storage

    Django code for Database
    
- utils

    The several tools for file management & text analysis for search functionality
    
- requirements

    All the dependencies for this project

- manage.py

    The main execution file
    
## Installation

- Environment

    Python 3.6, Ubuntu 18.04, Wiindows 10
    
- Dependency Installation

    Please navigate to this project directory and run the following command in the terminal.
    
    ```
        pip3 install -r requirements.txt
    ```
    
## Execution

- Please run the following command in the terminal.

    ```
        python3 manage.py migrate        
    ```  
