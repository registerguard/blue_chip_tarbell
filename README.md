What is made
------------
* Lane County property sales (print & online) `bz.bc.propertysales.YYDD`
* Eugene building permits (online) `bz.bc.eugenepermits.YYDD`
* Springfield building permits (online) `bz.bc.springfieldpermits.YYDD`
* Lane County building permits (online) `bz.bc.lanepermits.YYDD`

Quick start
-----------

1. Upload .xls to Google Sheets to view, open with Google Sheets and move out Google Sheets copy up out of "originals" directory up to [Month] directory.
1. Create `Category` column from subhead rows ("Commercial Improved", "Commerical Vacant", etc.)
1. Organize (sort by Category, ascending; Dollar value, descending; Permit date ascending).
1. Rename sheet "data".
1. Download as .csv to clean locally with file in `_script` directory.
1. Upload `cleaned.csv` to Google sheets to use as source for Tarbell app run locally.
1. Change type of Price column to Format > Number > Plain text in Google Sheet that Tarbell is using.
1. View source of the local Tarbell result from browser and cut-and-paste into NCS HTML editor.

Notes
--------------

* Jupyter & Pandas workflow tk ... 
