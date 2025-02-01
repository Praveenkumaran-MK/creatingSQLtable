def createtable():
	import sqlite3
	# Connect to the database
	con = sqlite3.connect('Employee.db')
	cur = con.cursor()
	
	# Get the number of columns and table name from the user
	nocol = int(input("Enter number of columns: "))
	tablename = input("Enter table name: ")
	
	# Get column names, data types, and sizes from the user
	colname = [input(f"Enter heading for column {i}: ") for i in range(nocol)]
	dt = [input(f"Enter datatype for column {i} (int, char, varchar): ") for i in range(nocol)]
	size = []
	
	# Function to get the size for char or varchar data types
	def forsize(i):
	       if i.lower() in ['char', 'varchar']:
	       	asktime = int(input(f"Enter size for column {colname[n]}: "))
	       	size.append(f"({asktime})")
	       else:
	       	size.append('')
	       	
	# Process data types and sizes
	default = ['int', 'char', 'varchar']
	for n, dtype in enumerate(dt):
	   forsize(dtype)
	   if dtype.lower() not in default:
	       print(f"You entered wrong datatype for column {n+1}, so it is taken to be int by default")
	       dt[n] = 'int'
	       size[n] = ''
	       
	  # Combine column names, data types, and sizes
	combinelist = []
	for i in range(nocol):
	   combine = f"{colname[i]} {dt[i]}{size[i]}"
	   combinelist.append(combine)
	   
	   # Create the SQL statement to create the table
	a = f"CREATE TABLE {tablename} ("
	a += ", ".join(combinelist)
	a += ");"
	
	# Print the final SQL statement
	print(a)
	
	# Execute the SQL statement
	cur.execute(a)
	con.commit()
	con.close()
createtable()