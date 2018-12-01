What is made
------------
* Lane County property sales (print & online) `bz.bc.propertysales.MMDD`
* Eugene building permits (online) `bz.bc.eugenepermits.MMDD`
* Springfield building permits (online) `bz.bc.springfieldpermits.MMDD`
* Lane County building permits (online) `bz.bc.lanepermits.MMDD`

Quick start
-----------

1. Upload .xls to Google Sheets to view, open with Google Sheets and move out Google Sheets copy up out of "originals" directory up to [Month] directory.
1. Create `Category` column from subhead rows ("Commercial Improved", "Commerical Vacant", etc.)
1. Organize (sort by Category, ascending; Dollar value, descending; Permit date ascending).
1. Download as .csv and copy to `_script` directory so as to clean locally with `clean_data_property_sales.py` script in same `_script` directory. (Change hard-coded source file name in script `clean_data_property_sales.py`.
1. Upload `cleaned_property_sales.csv` to Google sheets to use as source for Tarbell app run locally.
1. Publish Google Sheet to web, Share with `rgnews registerguard` Google account, add id to Tarbell `tarbell_config.py`.
1. Change type of Price column to Format > Number > Plain text in Google Sheet that Tarbell is using. (<== Not sure that this step is necessary ... )
1. Make sure you're requesting the correct Tarbell route/URL (see `tarbell_config.py` for the possibilities) and that column and template variable names match. 
1. View source of the local Tarbell result from browser and cut-and-paste into NCS HTML editor. Add "Lane County property sales from [month] [starting date number] through [ending date number], [year]." line at top of body copy and "Lane County [Month] [Year] property sales" headline

Notes
--------------

* Jupyter & Pandas workflow tk ... 
