Python Parser
=============
parse files to json from different file types example (csv, xml)

Installation
============
    pip install -r requirements.txt
    
Run
====
    parser.py <file_type> <file_path>
  

Run Example:

```
    >>> parser.py csv csv/customers.csv
    >>> parser.py csv csv/customers.csv csv/vehicles.csv
    >>> parser.py xml xml/customer1.xml
    >>> parser.py xml xml/customer1.xml xml/customers.xml
``` 

    
To handle issues:

```
    >>> parser.py txt txt/customer/txt
    txt file type is not supported
    >>> parser.py csv csv.csv
    read csv file error
    csv data conversion error
    write to json file error
    >>> parser.py
    program takes <file_type> <file_path>
    example > parser.py csv csv/customers.csv
```



    
    
    