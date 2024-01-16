import MySQLdb

def list_states(mysql_username, mysql_password, database_name):
   """Lists all states from the specified database in ascending order by states.id.

   Args:
       mysql_username (str): The MySQL username.
       mysql_password (str): The MySQL password.
       database_name (str): The name of the database to connect to.
   """

   db = MySQLdb.connect(
       host="localhost",
       user=mysql_username,
       passwd=mysql_password,
       db=database_name,
       port=3306
   )

   cursor = db.cursor()
   cursor.execute("SELECT * FROM states ORDER BY id ASC")
   results = cursor.fetchall()

   for row in results:
       print(row)

   db.close()

# Example usage:
if __name__ == "__main__":
   mysql_username = input("Enter MySQL username: ")
   mysql_password = input("Enter MySQL password: ")
   database_name = "hbtn_0e_0_usa"  # Replace with the actual database name if needed
   list_states(mysql_username, mysql_password, database_name)
