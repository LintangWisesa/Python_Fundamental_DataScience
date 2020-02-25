
### Export MongoDB to JSON & CSV

Open cmd as admin, go to _mongodb/server/version/bin_. For Mac OS, add _sudo_ in every command!

- Export to JSON

	```bash
    $ mongoexport --db=db_name --collection=col_name --out=file_name.json
    ```

- Export to CSV

    ```bash
	$ mongoexport --db=ptabc --collection=col_name --type=csv --fields=kolom1,kolom2,kolom3 --out=file_name.csv
    ```

#

### Import JSON & CSV to MongoDB

Copy datasets file to _mongodb/server/version/bin_, open cmd as admin, go to _mongodb/server/version/bin_. For Mac OS, add _sudo_ in every command!

- Import JSON
	
    ```bash
    $ mongoimport --db=db_name --collection=col_name --file=file_name.json
    ```

- import CSV
	
    ```bash
    $ mongoimport --db=db_name --collection=col_name --type=csv --headerline --file=file_name.csv
    ```