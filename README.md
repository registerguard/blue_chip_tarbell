What is made
------------
* Lane County property sales (print & online) `bz.bc.propertysales.MMDD`
* Eugene building permits (online) `bz.bc.eugenepermits.MMDD`
* Springfield building permits (online) `bz.bc.springfieldpermits.MMDD`
* Lane County building permits (online) `bz.bc.lanepermits.MMDD`

Quick start
-----------

1. In Google Drive `Blue Chip/YYYY/`, create `Month` and `Month/originals` folders.
1. Upload .xls to Google Sheets to the appropriate `originals` to view, open with Google Sheets and move the Google Sheets-generated copy up out of the "originals" directory to the parent [Month] directory.  
~~1. Create `Category` column from subhead rows ("Commercial Improved", "Commerical Vacant", etc.)~~
1. Delete first five rows of header crud.
1. Using " " as a delimiter, `JOIN` Column A ("Category) and Column B ("Vacant / Improved") into a third column, Column C.  
e.g., `=JOIN(" ", A2, B2)`  
Copy and Paste special => Paste values only Column C data into Column C. Give Column C a column header of "Category". Delete Columns A & B. View => Freeze first row.
1. Organize (sort by Category, ascending; Sales Price/Dollar Value, descending; Sales Date/Permit Date, ascending).
1. Download as .csv and copy to local `_scripts` directory so as to clean locally with `clean_data_property_sales.py` script in same `_script` directory. **Important:** In order to do that you'll first have to update the `LANE_COUNTY_SALES_DATA_CSV` file source file name in `secrets.json`, then run script.  
~~1. Upload `cleaned_property_sales.csv` to Google Sheets. Open with Google Sheets and use converted file as source for Tarbell app run locally.~~
~~1. Publish Google Sheet to web, Share with `rgnews registerguard` Google account, update `SPREADSHEET_KEY` id in `secrets.json`.~~
~~1. Change type of Price column to Format > Number > Plain text in Google Sheet that Tarbell is using. (<== Not sure that this step is necessary, especially if you Freeze the header row ... )~~
1. Fire up the local Tarbell server (`tarbell serve`). Don't forget to activate via `workon` the right virtualenv for Tarbell to work.  
1. Make sure you're requesting the correct Tarbell route/URL (see `tarbell_config.py` for the possibilities) and that column and template variable names match. For Lane County property sales it's `/property_sales`.
1. View source of the local Tarbell result from browser and cut-and-paste into NCS HTML editor. Add "Lane County property sales from [month] [starting date number] through [ending date number], [year]." line at top of body copy and "Lane County [Month] [Year] property sales" headline and a Taxonomy of `Permanent Topic > Local Business > Names & Faces`. In MWC/NCS, set the `Publication` date to the first Tuesday of the month. Publish using the MWC/NCS `Online publication time: Use publication` option.

Notes
--------------

* Jupyter & Pandas workflow tk ... 
