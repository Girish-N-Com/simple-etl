import yaml
import psycopg2
import csv
import os

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def connect_to_database(config):
    # Extract the necessary information from the config
    host = config['host']
    port = config['port']
    username = config['username']
    password = config['password']
    database_name = config['database_name']

    # Connect to the database using the extracted information
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database_name
    )

    # Add your database connection code here
    # For example, you can create a cursor and execute SQL queries
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Don't forget to close the connection when you're done
    conn.close()

def read_from_file(file_path):
    # Add your code here to read data from the CSV file
    # For example, you can use the csv module to read the file

    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data

def main():
    # Replace '../config/config.yaml' with the actual path to your config file
    print(os.getcwd())
    config_file_path = os.path.join(os.getcwd(), 'config\\config.yaml')
    config = read_config(config_file_path)
    
    source_type = input("Enter the source type (database or file): ")
    
    if source_type == "database":
        connection_string = config['app']['config']['source']['database']['connection_string']
        connect_to_database(connection_string)
    elif source_type == "file":
        connection_string = config['app']['config']['source']['file']['connection_string']['file_path']
        data = read_from_file(connection_string)
        print(data)
        # Do something with the data
    else:
        print("Invalid source type entered.")


if __name__ == "__main__":
    main()