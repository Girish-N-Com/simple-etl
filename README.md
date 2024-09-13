# simple-etl
Create a simple ETL tool using python libraries

Created the basic folder structure


Using github updated the main.py to get cli arguments for type 'file' and 'database'.
For each type there can only be specific values that the user can send, for 'file' type he can only send a path of the file as connection_string and for the 'database' type he can only send the database connection_string as host, port, username, password, database_name. Both are tested manully and work correctly as of now.


Created read_config and updated the config.yaml file, the read_config.py is used to read the config.yaml file and make connection to the database or read file contents based on user input.


Separated the config files for source and target yaml files.
Updated the read_config.py file to read for both source and target connection_strings.
Connection to database and file read are successful.


Created schemas for file and table in json format.
These schemas will be used to read and write to file or database table.
The code is updated to read from an existing file and write to a file with the schema definition.
Also added the sample data into the current folder with the the output file it creates


Added if else statements for differentiating source and target.
Updated the file_schema dn table_schema respectively.




When the source is set to the database and the target is set to a file,
When the source is set to the database and the target is set to a database,
When the source is set to the file and the target is set to a file,
When the source is set to the file and the target is set to a database,

if source is database

    if, the table in the input schema does not exists, inform the user that
    table does not exists, cannot proceed
    else, read the table content

    if, the table in the target does not exists, check with the user if it
    can be created using the input schema or not
        if yes, create a new table with the input schema.
        else, inform the user that without target we cannot write to table.

    if, the target file does not exists, create new file.

elif source is file

    if, input file does not exists in the given path, inform the user
    File not found!
    else, read the file content
    
    if, the table in the target does not exists, check with the user if it
    can be created using the input schema or not
        if yes, create a new table with the input schema and write data to it.
        else, inform the user that without target we cannot write to table.
    else, write data to it.

    if, the target file does not exists, create new file.



Instead of using psycopg2 which can only support postgres database, make use
of sqlalchemy to generate models for the tables which and create them or 
read from these model tables from the connected database.

Add a type in the database.yaml file to represent the type of database 
for sqlalchemy.



Integrate the above application to be used with API, make use of FastAPI.
The user should be able run the FastAPI app and invoke an api endpoint to
start the process of reading from source and writing to the target. The
endpoint should also be able to take inputs from the user. 



Performing column level transformation outside of the database is more
costly, complex and time consuming as it will involves more resource/apps.
This application is helpful for extracting data from source table, if 
required map the column names to the target column names, and load the 
extracted data into the target table.
Download the code and start the fast api server locally with the command:
-
Set schema for database of file with
- http://simple-etl-fastapi/setSourceSchema -type database/file -schemaType json/yaml -filePath upload_the_file_from_this_path
- http://simple-etl-fastapi/setTargetSchema -type database/file -schemaType json/yaml -filePath upload_the_file_from_this_path
- http://simple-etl-fastapi/setTargetSchema -type database/file -schemaType json/yaml -filePath upload_the_file_from_this_path
- 