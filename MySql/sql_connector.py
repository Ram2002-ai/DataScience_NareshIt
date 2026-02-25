import pyodbc
print(pyodbc.drivers())




conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-H21E7ET;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)

print("Connection Established Successfully ✅")




cursor = conn.cursor()

cursor.execute("SELECT name FROM sys.databases")

cursor.execute("USE INSTITUTE")




# # Step 2: Create Student Table
# create_table_query = """
# IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='student' AND xtype='U')
# CREATE TABLE dbo.student (
#     student_id INT PRIMARY KEY,
#     name VARCHAR(50),
#     age INT,
#     course VARCHAR(50),
#     marks INT,
#     city VARCHAR(50)
# )
# """

# cursor.execute(create_table_query)
# conn.commit()
# print("Student Table Created Successfully ✅")

# # Step 3: Insert Records
# insert_query = """
# INSERT INTO dbo.student (student_id, name, age, course, marks, city)
# VALUES (?, ?, ?, ?, ?, ?)
# """

# students = [
#     (1, 'Ram', 20, 'BCA', 85, 'Bhopal'),
#     (2, 'Shyam', 21, 'BSc', 78, 'Indore'),
#     (3, 'Mohan', 22, 'BCom', 88, 'Gwalior'),
#     (4, 'Rita', 20, 'BCA', 92, 'Delhi'),
#     (5, 'Sita', 23, 'MBA', 75, 'Mumbai')
# ]

# for student in students:
#     cursor.execute(insert_query, student)

# conn.commit()
# print("Records Inserted Successfully ✅")

# Step 4: Fetch Data
cursor.execute("SELECT * FROM dbo.student")
cursor.execute("SELECT * FROM dbo.student WHERE age > 22")
cursor.execute("select*from dbo.student where marks between 80 and 90 ")
print("\nStudent Records:\n")
for row in cursor:
    print(row)


cursor.close()
conn.close()