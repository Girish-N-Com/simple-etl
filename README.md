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
Also added the sample data into the current folder with the the ouput file it creates