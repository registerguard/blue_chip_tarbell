What is made
------------
* Lane County property sales (print & online) `bz.bc.propertysales.YYDD`
* Eugene building permits (online) `bz.bc.eugenepermits.YYDD`
* Springfield building permits (online) `bz.bc.springfieldpermits.YYDD`
* Lane County building permits (online) `bz.bc.lanepermits.YYDD`

Quick start
-----------

1. Upload .xls to Google Sheets to view, organize (sort by Category, ascending; Dollar value, descending; Permit date ascending).
1. Export .csv to clean locally with file in `_script` directory.
1. Upload `cleaned.csv` to Google sheets to use as source for Tarbell app run locally.  
1. View source of the local Tarbell result from browser and cut-and-paste into NCS HTML editor.

Cleaning notes
--------------
1. Add category from subhead row, title case.

* Jupyter & Pandas
