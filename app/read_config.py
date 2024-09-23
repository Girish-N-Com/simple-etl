import yaml
import psycopg2
import csv
import os
import json

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def connect_to_database(connection_string):
    config = connection_string['app']['config']['database']['connection_string']
    # Extract the necessary information from the config
    host = config['host']
    port = config['port']
    username = config['username']
    password = config['password']
    database_name = config['database_name']

    # Connect to the database using the extracted information
    return psycopg2.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database_name
    )

def read_from_file(file_path):
    # Add your code here to read data from the CSV file
    # For example, you can use the csv module to read the file

    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data

def main():
    # Replace '../config/config.yaml' with the actual path to your config file
    print(os.getcwd())
    
    for input_type in ("source", "target"):
        config_file_path = os.path.join(os.getcwd(),
                                        str.format('config\\{0}.yaml', input_type))
        config = read_config(config_file_path)
        
        connection_type = input(str.format("Enter the connection type for {0} (database or file): ",
                                           input_type))
        if connection_type == "database":
            schema_file_path = os.path.join(os.getcwd(), 'schema\\table_schema.json')
            conn = connect_to_database(connection_string)
            if input_type == "source":
                # Add your database connection code here
                # For example, you can create a cursor and execute SQL queries
                cursor = conn.cursor()
                print("Database connection established successfully.")
                # read form database function
                cursor.execute("SELECT * FROM public.customers")
                data = cursor.fetchall()
                print(data)
                # read form database function
                # create write to database function
            elif input_type == "target":
                # create write to database function
                cursor = conn.cursor()
                print("Database connection established successfully.")
                # create write to database function
                # cursor.execute("""CREATE TABLE public.customers_new (id INT PRIMARY KEY,
                #                first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(100)""") 

            # Don't forget to close the connection when you're done
            conn.close()
        elif connection_type == "file":
            schema_file_path = os.path.join(os.getcwd(), 'schema\\file_schema.json')
            connection_string = config['app']['config']['file']['connection_string']['file_path']
            if input_type == "source":
                # read form file function
                data = read_from_file(connection_string)
            elif input_type == "target":
                # set the fieldnames using the file_schema.json file
                # reading file schema
                with open(schema_file_path) as file:
                    schema = json.load(file)
                print(schema)
                for num, item in enumerate(data):
                    for new, old in zip(schema['source']['columns'], data[num].keys()):
                        data[num][new] = data[num].pop(old)
                print(data)
                
                # create write to file function
                with open(schema['target']['file_name']+'.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, delimiter=schema['source']['delimiter'],
                                            fieldnames=schema['source']['columns'])
                    writer.writeheader()
                    for row in data:
                        writer.writerow(row)
                # Do something with the data
        else:
            print("Invalid source type entered.")


if __name__ == "__main__":
    main()