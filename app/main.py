import argparse
import os
import psycopg2
# Create the argument parser
parser = argparse.ArgumentParser(description='Process type and connection string.')

# Add the required arguments
parser.add_argument('--type', help='Type argument', choices=['database', 'file'], default='file')
parser.add_argument('--connection_string', help='Connection string argument', required=True)

# Parse the command-line arguments
args = parser.parse_args()

# Store the arguments before exiting the program
arguments = {
    "type": args.type,
    "connection_string": args.connection_string
}

# Use the type and connection string in your code
# ...

# Print the arguments
for arg in vars(args):
    print(arg, getattr(args, arg))

# Print the stored arguments
print(arguments)

# Check the type and modify the connection string accordingly
if args.type == 'file':
    # Assume connection_string is a path
    file_path = args.connection_string
    # Validate the file path
    if not os.path.isfile(file_path):
        print("Invalid file path specified.")
        exit(1)
    # Use the file_path in your code
    # ...
elif args.type == 'database':
    # Assume connection_string contains host, port_number, username, password, and database_name separated by commas
    host, port, username, password, database_name = args.connection_string.split(',')
    
    # Validate the database connection
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database_name
        )
        print("Database connection successful.")
        conn.close()
    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)
        exit(1)
    
    # Use the host, port_number, username, password, and database_name in your code
    # ...
else:
    print("Invalid type specified.")
