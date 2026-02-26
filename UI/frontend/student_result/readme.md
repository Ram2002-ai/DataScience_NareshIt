================================================
STUDENT RESULT MANAGEMENT SYSTEM
SQL Server Edition - Version 2.0
================================================

A comprehensive Student Result Management System built with Python Tkinter 
and Microsoft SQL Server database.

----------------------------------------------------------------------
TABLE OF CONTENTS
----------------------------------------------------------------------
1. SYSTEM REQUIREMENTS
2. INSTALLATION GUIDE
3. DATABASE SETUP
4. CONFIGURATION
5. RUNNING THE APPLICATION
6. DEFAULT LOGIN CREDENTIALS
7. FEATURES OVERVIEW
8. TROUBLESHOOTING
9. SUPPORT

----------------------------------------------------------------------
1. SYSTEM REQUIREMENTS
----------------------------------------------------------------------

Hardware Requirements:
- Processor: 1 GHz or faster
- RAM: 2 GB minimum (4 GB recommended)
- Hard Disk: 500 MB free space
- Screen Resolution: 1366 x 768 or higher

Software Requirements:
- Windows 7/8/10/11 (64-bit recommended)
- Python 3.8 or higher
- Microsoft SQL Server 2012 or higher (Express edition works fine)
- SQL Server Management Studio (SSMS) - optional but recommended
- ODBC Driver 17 for SQL Server

----------------------------------------------------------------------
2. INSTALLATION GUIDE
----------------------------------------------------------------------

Step 1: Install Python
----------------------
1. Download Python from https://www.python.org/downloads/
2. Run installer - CHECK "Add Python to PATH"
3. Verify installation: Open Command Prompt and type:
   python --version

Step 2: Install SQL Server
--------------------------
Option A: SQL Server Express (Free)
- Download from: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
- Choose "Express" edition
- Install with default settings
- Remember your server name (usually: DESKTOP-XXXXXX or localhost\SQLEXPRESS)

Option B: SQL Server Developer (Free for development)
- Same as above, choose "Developer" edition

Step 3: Install ODBC Driver
--------------------------
Download and install "ODBC Driver 17 for SQL Server" from:
https://go.microsoft.com/fwlink/?linkid=2249006

Step 4: Install Python Packages
------------------------------
Open Command Prompt and navigate to your project folder:
cd C:\path\to\StudentResultSystem

Install all required packages:
pip install -r requirements.txt

Or install individually:
pip install pyodbc
pip install Pillow
pip install openpyxl
pip install reportlab
pip install matplotlib
pip install bcrypt
pip install python-dateutil
pip install pandas

----------------------------------------------------------------------
3. DATABASE SETUP
----------------------------------------------------------------------

Method 1: Using SQL Server Management Studio (SSMS)
---------------------------------------------------
1. Install SSMS from: https://aka.ms/ssmsfullsetup
2. Open SSMS and connect to your SQL Server
3. Open the 'database.sql' file (File -> Open -> File)
4. Execute the script (Press F5 or click Execute)
5. Verify database 'StudentResultDB' is created

Method 2: Using Command Line (sqlcmd)
------------------------------------
Open Command Prompt and run:
sqlcmd -S YOUR_SERVER_NAME -i database.sql

Example:
sqlcmd -S localhost\SQLEXPRESS -i database.sql

----------------------------------------------------------------------
4. CONFIGURATION
----------------------------------------------------------------------

Before running the application, update the database connection settings:

1. Open 'main.py' in a text editor
2. Find the DatabaseConfig class (around line 40)
3. Update the SERVER name to match your SQL Server:

   class DatabaseConfig:
       SERVER = 'YOUR_SERVER_NAME'  # Change this!
       
   Examples:
   - For default instance: SERVER = 'localhost'
   - For named instance: SERVER = 'localhost\\SQLEXPRESS'
   - For remote server: SERVER = '192.168.1.100'
   - For Windows Authentication: Keep as is
   - For SQL Authentication: Uncomment and update username/password

----------------------------------------------------------------------
5. RUNNING THE APPLICATION
----------------------------------------------------------------------

Method 1: Double-click
----------------------
Simply double-click on 'main.py' file

Method 2: Command Line
---------------------
Open Command Prompt in the project folder:
python main.py

Method 3: Create Shortcut
-------------------------
Create a batch file 'run.bat' with content:
@echo off
cd /d C:\path\to\StudentResultSystem
python main.py
pause

----------------------------------------------------------------------
6. DEFAULT LOGIN CREDENTIALS
----------------------------------------------------------------------

After database setup, use these credentials:

ADMIN ACCOUNT:
-------------
Username: admin
Password: admin@123
Role: Administrator (full access)

STUDENT ACCOUNTS:
----------------
No default student accounts. Create students through admin panel:
1. Login as admin
2. Go to User Management
3. Create new user with role 'student'
4. Then add student details in Student Management

----------------------------------------------------------------------
7. FEATURES OVERVIEW
----------------------------------------------------------------------

LOGIN SYSTEM:
------------
✓ Secure authentication
✓ Password recovery with security questions
✓ Remember me functionality
✓ Account lockout after 3 failed attempts
✓ Session management

ADMIN FEATURES:
--------------
✓ Dashboard with statistics
✓ User management (CRUD)
✓ Student management (CRUD)
✓ Subject management (CRUD)
✓ Exam management (CRUD)
✓ Result declaration
✓ Bulk result entry
✓ Report generation
✓ Database backup/restore
✓ Audit logs

STUDENT FEATURES:
----------------
✓ Personal dashboard
✓ View profile
✓ Check results
✓ Performance graphs
✓ Download report cards
✓ Search results
✓ Change password

NAVIGATION:
----------
✓ Back/Forward buttons on all pages
✓ Home button for quick access
✓ Menu bar with all options
✓ Status bar with information
✓ Keyboard shortcuts

REPORTING:
---------
✓ Individual report cards (PDF)
✓ Class result summaries
✓ Subject-wise analysis
✓ Top performers list
✓ Performance graphs
✓ Export to Excel/CSV

----------------------------------------------------------------------
8. TROUBLESHOOTING
----------------------------------------------------------------------

PROBLEM: "No module named pyodbc"
SOLUTION: pip install pyodbc

PROBLEM: "Cannot connect to database"
SOLUTION: 
- Check SQL Server is running (Services.msc -> SQL Server)
- Verify server name in DatabaseConfig
- Enable TCP/IP in SQL Server Configuration Manager
- Check Windows Firewall
- Try using 'localhost' or '127.0.0.1'

PROBLEM: "ODBC Driver 17 not found"
SOLUTION: Download and install from Microsoft website

PROBLEM: "Login failed for user"
SOLUTION:
- For Windows Auth: Use trusted connection
- For SQL Auth: Enable mixed mode in SQL Server

PROBLEM: "Database already exists"
SOLUTION: Drop existing database or modify script to use different name

PROBLEM: "Permission denied"
SOLUTION: Run as administrator or check file permissions

PROBLEM: "Port already in use"
SOLUTION: Change SQL Server port or stop conflicting service

----------------------------------------------------------------------
9. FILE STRUCTURE
----------------------------------------------------------------------

StudentResultSystem/
│
├── main.py                 # Main application (15,000+ lines)
├── database.sql            # Database creation script
├── requirements.txt        # Python dependencies
├── README.txt              # This file
├── login.dat               # Saved credentials (auto-generated)
├── reports/                # Generated reports folder (auto-created)
├── backups/                # Database backups folder (auto-created)
└── exports/                # Exported data folder (auto-created)

----------------------------------------------------------------------
10. SUPPORT
----------------------------------------------------------------------

For issues and queries:
- Check Troubleshooting section above
- Verify all installation steps
- Ensure Python and SQL Server versions are compatible
- Check database connection parameters

Common Error Codes:
------------------
- 8141: CHECK constraint error - Fix constraint syntax
- 1767: Foreign key error - Create tables in correct order
- 208: Invalid object - Object doesn't exist
- 8197: Object doesn't exist - Check creation order

Quick Fixes:
-----------
1. Can't connect: Restart SQL Server service
2. Login failed: Reset password
3. Import errors: Reinstall packages
4. Display issues: Update graphics drivers

----------------------------------------------------------------------
CREDITS
----------------------------------------------------------------------
Developed for educational institutions to efficiently manage 
and declare student results.

Technologies Used:
- Python 3.x
- Tkinter GUI
- Microsoft SQL Server
- pyodbc
- ReportLab for PDF
- Matplotlib for graphs

© 2024 Student Result Management System
Version 2.0 (SQL Server Edition)
----------------------------------------------------------------------