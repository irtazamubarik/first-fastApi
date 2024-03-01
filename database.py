import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'mysql',
    'passwd': '',
    'db': 'test',
    'unix_socket': '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)
