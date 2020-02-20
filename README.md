# ChEMBL-Mapping
Python script to map ChEMBL small molecules to Gene Symbols

This script is based on the Chembl Websource client (https://github.com/chembl/chembl_webresource_client) and used to get all small molecules with their trivial names for a list of proteins. 

It reads in a table in pandas and creates a list of Gene Symbols from a given column and queries the Chembl database via the websource client. The resulting data is then formatted and written to a tab delimited text file.
