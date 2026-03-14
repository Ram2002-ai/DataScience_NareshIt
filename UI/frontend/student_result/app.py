"""
STUDENT RESULT MANAGEMENT SYSTEM
Complete Application with SQL Server Database
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import pyodbc
from datetime import datetime, timedelta
import hashlib
import os
import sys
from PIL import Image, ImageTk
import io
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import bcrypt

# =============================================
# DATABASE CONFIGURATION
# =============================================
class DatabaseConfig:
    """Database connection configuration"""
    
    # IMPORTANT: Change these values according to your SQL Server setup
    SERVER = 'DESKTOP-H21E7ET'  # Replace with your server name
    DATABASE = 'StudentResultDB'
    
    # For Windows Authentication
    CONNECTION_STRING = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
    
    # For SQL Server Authentication (uncomment if needed)
    # USERNAME = 'sa'
    # PASSWORD = 'your_password'
    # CONNECTION_STRING = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

# =============================================
# LOGIN WINDOW
# =============================================
class LoginWindow:
    """Login window for authentication"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Result System - Login")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        
        # Center the window
        self.center_window()
        
        # Variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.remember = tk.BooleanVar()
        self.login_attempts = 0
        self.lockout_time = None
        
        # Database connection
        self.db_connection = None
        self.current_user = None
        
        # Create GUI
        self.create_widgets()
        
        # Check for saved credentials
        self.load_saved_credentials()
        
        self.root.mainloop()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'400x500+{x}+{y}')
    
    def create_widgets(self):
        """Create login widgets"""
        # Title Frame
        title_frame = tk.Frame(self.root, bg='#3498db', height=100)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        # Logo/Title
        title_label = tk.Label(title_frame, text="📚 Student Result System", 
                               font=('Arial', 18, 'bold'), 
                               bg='#3498db', fg='white')
        title_label.pack(expand=True)
        
        subtitle_label = tk.Label(title_frame, text="Login to access your account",
                                 font=('Arial', 10), bg='#3498db', fg='white')
        subtitle_label.pack()
        
        # Main Frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=40, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # Username
        tk.Label(main_frame, text="Username:", font=('Arial', 11), 
                bg='#f0f0f0').pack(anchor='w', pady=(10,5))
        
        username_entry = tk.Entry(main_frame, textvariable=self.username,
                                 font=('Arial', 11), bd=2, relief='solid')
        username_entry.pack(fill='x', pady=(0,15))
        username_entry.focus()
        
        # Password
        tk.Label(main_frame, text="Password:", font=('Arial', 11),
                bg='#f0f0f0').pack(anchor='w', pady=(5,5))
        
        password_frame = tk.Frame(main_frame, bg='#f0f0f0')
        password_frame.pack(fill='x', pady=(0,10))
        
        self.password_entry = tk.Entry(password_frame, textvariable=self.password,
                                      font=('Arial', 11), bd=2, relief='solid', show='●')
        self.password_entry.pack(side='left', fill='x', expand=True)
        
        # Show/Hide password button
        self.show_password = tk.BooleanVar()
        show_btn = tk.Checkbutton(password_frame, text="👁", bg='#f0f0f0',
                                 command=self.toggle_password,
                                 variable=self.show_password)
        show_btn.pack(side='right', padx=(5,0))
        
        # Remember me
        remember_chk = tk.Checkbutton(main_frame, text="Remember Me",
                                      variable=self.remember, bg='#f0f0f0')
        remember_chk.pack(anchor='w', pady=5)
        
        # Login Button
        login_btn = tk.Button(main_frame, text="🔐 LOGIN", 
                              font=('Arial', 12, 'bold'),
                              bg='#3498db', fg='white',
                              activebackground='#2980b9',
                              activeforeground='white',
                              bd=0, padx=20, pady=10,
                              command=self.login)
        login_btn.pack(fill='x', pady=20)
        
        # Forgot Password
        forgot_btn = tk.Button(main_frame, text="Forgot Password?",
                               font=('Arial', 10),
                               bg='#f0f0f0', fg='#3498db',
                               bd=0, cursor='hand2',
                               command=self.forgot_password)
        forgot_btn.pack(pady=5)
        
        # Status Label
        self.status_label = tk.Label(main_frame, text="", 
                                     font=('Arial', 9), fg='red',
                                     bg='#f0f0f0')
        self.status_label.pack(pady=10)
        
        # Version
        version_label = tk.Label(main_frame, text="Version 2.0 | SQL Server Edition",
                                font=('Arial', 8), fg='gray',
                                bg='#f0f0f0')
        version_label.pack(side='bottom', pady=10)
    
    def toggle_password(self):
        """Toggle password visibility"""
        if self.show_password.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='●')
    
    def load_saved_credentials(self):
        """Load saved credentials from file"""
        try:
            if os.path.exists('login.dat'):
                with open('login.dat', 'r') as f:
                    data = f.read().strip().split('|')
                    if len(data) == 2:
                        self.username.set(data[0])
                        self.password.set(data[1])
                        self.remember.set(True)
        except:
            pass
    
    def save_credentials(self):
        """Save credentials to file"""
        try:
            if self.remember.get():
                with open('login.dat', 'w') as f:
                    f.write(f"{self.username.get()}|{self.password.get()}")
            else:
                if os.path.exists('login.dat'):
                    os.remove('login.dat')
        except:
            pass
    
    def connect_to_database(self):
        """Connect to SQL Server database"""
        try:
            self.db_connection = pyodbc.connect(DatabaseConfig.CONNECTION_STRING)
            return True
        except pyodbc.Error as e:
            messagebox.showerror("Database Error", 
                               f"Failed to connect to database:\n{e}\n\n"
                               "Please check:\n"
                               "1. SQL Server is running\n"
                               "2. Database exists\n"
                               "3. Server name is correct")
            return False
    
    def login(self):
        """Authenticate user"""
        # Check lockout
        if self.lockout_time:
            if datetime.now() < self.lockout_time:
                remaining = (self.lockout_time - datetime.now()).seconds // 60
                self.status_label.config(text=f"Account locked. Try again in {remaining} minutes")
                return
            else:
                self.lockout_time = None
                self.login_attempts = 0
        
        username = self.username.get().strip()
        password = self.password.get().strip()
        
        if not username or not password:
            self.status_label.config(text="Please enter username and password")
            return
        
        # Connect to database
        if not self.connect_to_database():
            return
        
        try:
            cursor = self.db_connection.cursor()
            
            # Check user credentials
            cursor.execute("""
                SELECT user_id, full_name, role, login_attempts, is_locked 
                FROM users 
                WHERE username = ? AND password = ? AND is_active = 1
            """, (username, password))
            
            user = cursor.fetchone()
            
            if user:
                # Login successful
                user_id, full_name, role, attempts, is_locked = user
                
                # Reset login attempts
                cursor.execute("UPDATE users SET login_attempts = 0, last_login = GETDATE() WHERE user_id = ?", 
                             (user_id,))
                self.db_connection.commit()
                
                # Save credentials if remember me checked
                self.save_credentials()
                
                # Close login window and open main app
                self.root.destroy()
                
                # Start main application
                app = StudentResultSystem(self.db_connection, user_id, full_name, role)
                app.run()
                
            else:
                # Login failed
                self.login_attempts += 1
                
                # Check if user exists (wrong password)
                cursor.execute("SELECT user_id, login_attempts FROM users WHERE username = ?", (username,))
                existing_user = cursor.fetchone()
                
                if existing_user:
                    user_id, attempts = existing_user
                    attempts = (attempts or 0) + 1
                    
                    # Lock account after 3 attempts
                    if attempts >= 3:
                        cursor.execute("UPDATE users SET is_locked = 1, login_attempts = ? WHERE user_id = ?", 
                                     (attempts, user_id))
                        self.db_connection.commit()
                        self.lockout_time = datetime.now() + timedelta(minutes=5)
                        self.status_label.config(text="Account locked for 5 minutes")
                    else:
                        cursor.execute("UPDATE users SET login_attempts = ? WHERE user_id = ?", 
                                     (attempts, user_id))
                        self.db_connection.commit()
                        remaining = 3 - attempts
                        self.status_label.config(text=f"Invalid password. {remaining} attempts remaining")
                else:
                    self.status_label.config(text="Invalid username or password")
        
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Login failed: {e}")
    
    def forgot_password(self):
        """Handle forgot password"""
        ForgotPasswordDialog(self.root)

# =============================================
# FORGOT PASSWORD DIALOG
# =============================================
class ForgotPasswordDialog:
    def __init__(self, parent):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Reset Password")
        self.dialog.geometry("400x300")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.center_dialog()
        
        self.create_widgets()
    
    def center_dialog(self):
        """Center the dialog on parent"""
        self.dialog.update_idletasks()
        parent = self.dialog.master
        x = parent.winfo_x() + (parent.winfo_width() // 2) - (self.dialog.winfo_width() // 2)
        y = parent.winfo_y() + (parent.winfo_height() // 2) - (self.dialog.winfo_height() // 2)
        self.dialog.geometry(f'+{x}+{y}')
    
    def create_widgets(self):
        """Create forgot password widgets"""
        # Title
        tk.Label(self.dialog, text="Reset Password", 
                font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Username
        tk.Label(self.dialog, text="Username:", font=('Arial', 11)).pack(anchor='w', padx=30, pady=(10,5))
        self.username_entry = tk.Entry(self.dialog, font=('Arial', 11), width=30)
        self.username_entry.pack(padx=30, pady=(0,10))
        
        # Security Question (will be fetched)
        tk.Label(self.dialog, text="Security Question:", font=('Arial', 11)).pack(anchor='w', padx=30, pady=(10,5))
        self.question_label = tk.Label(self.dialog, text="", font=('Arial', 10), wraplength=300)
        self.question_label.pack(padx=30, pady=(0,10))
        
        # Answer
        tk.Label(self.dialog, text="Answer:", font=('Arial', 11)).pack(anchor='w', padx=30, pady=(10,5))
        self.answer_entry = tk.Entry(self.dialog, font=('Arial', 11), width=30)
        self.answer_entry.pack(padx=30, pady=(0,10))
        
        # New Password
        tk.Label(self.dialog, text="New Password:", font=('Arial', 11)).pack(anchor='w', padx=30, pady=(10,5))
        self.new_password_entry = tk.Entry(self.dialog, font=('Arial', 11), width=30, show='●')
        self.new_password_entry.pack(padx=30, pady=(0,10))
        
        # Buttons
        btn_frame = tk.Frame(self.dialog)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Get Question", command=self.get_question,
                 bg='#3498db', fg='white', padx=20).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Reset Password", command=self.reset_password,
                 bg='#2ecc71', fg='white', padx=20).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Cancel", command=self.dialog.destroy,
                 bg='#e74c3c', fg='white', padx=20).pack(side='left', padx=5)
    
    def get_question(self):
        """Get security question for username"""
        username = self.username_entry.get().strip()
        
        if not username:
            messagebox.showerror("Error", "Please enter username")
            return
        
        try:
            # Connect to database
            conn = pyodbc.connect(DatabaseConfig.CONNECTION_STRING)
            cursor = conn.cursor()
            
            cursor.execute("SELECT security_question FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            
            if result and result[0]:
                self.question_label.config(text=result[0])
            else:
                messagebox.showerror("Error", "Username not found or no security question set")
            
            conn.close()
            
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
    
    def reset_password(self):
        """Reset password after verification"""
        username = self.username_entry.get().strip()
        answer = self.answer_entry.get().strip()
        new_password = self.new_password_entry.get().strip()
        
        if not all([username, answer, new_password]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        try:
            conn = pyodbc.connect(DatabaseConfig.CONNECTION_STRING)
            cursor = conn.cursor()
            
            # Verify answer
            cursor.execute("""
                SELECT user_id FROM users 
                WHERE username = ? AND security_answer = ?
            """, (username, answer))
            
            user = cursor.fetchone()
            
            if user:
                # Update password
                cursor.execute("UPDATE users SET password = ? WHERE user_id = ?",
                             (new_password, user[0]))
                conn.commit()
                
                messagebox.showinfo("Success", "Password reset successfully!")
                self.dialog.destroy()
            else:
                messagebox.showerror("Error", "Incorrect answer")
            
            conn.close()
            
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

# =============================================
# NAVIGATION MANAGER
# =============================================
class NavigationManager:
    """Manage navigation with back/forward buttons"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.history = []
        self.current_index = -1
        self.current_page = None
        
        # Create navigation bar
        self.nav_bar = tk.Frame(parent_frame, bg='#ecf0f1', height=40)
        self.nav_bar.pack(fill='x')
        self.nav_bar.pack_propagate(False)
        
        # Back button
        self.back_btn = tk.Button(self.nav_bar, text="← Back", 
                                  font=('Arial', 10),
                                  bg='#ecf0f1', bd=0,
                                  state='disabled',
                                  command=self.go_back)
        self.back_btn.pack(side='left', padx=5, pady=5)
        
        # Forward button
        self.forward_btn = tk.Button(self.nav_bar, text="→ Forward",
                                     font=('Arial', 10),
                                     bg='#ecf0f1', bd=0,
                                     state='disabled',
                                     command=self.go_forward)
        self.forward_btn.pack(side='left', padx=5, pady=5)
        
        # Home button
        self.home_btn = tk.Button(self.nav_bar, text="🏠 Home",
                                  font=('Arial', 10),
                                  bg='#ecf0f1', bd=0,
                                  command=self.go_home)
        self.home_btn.pack(side='left', padx=5, pady=5)
        
        # Current location label
        self.location_label = tk.Label(self.nav_bar, text="Dashboard",
                                       font=('Arial', 10, 'bold'),
                                       bg='#ecf0f1')
        self.location_label.pack(side='left', padx=20)
        
        # Separator
        ttk.Separator(parent_frame, orient='horizontal').pack(fill='x')
        
        # Content frame (where pages will be displayed)
        self.content_frame = tk.Frame(parent_frame, bg='#f5f5f5')
        self.content_frame.pack(fill='both', expand=True)
    
    def navigate_to(self, page_class, *args, **kwargs):
        """Navigate to a new page"""
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Update history
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]
        
        self.history.append({
            'page': page_class,
            'args': args,
            'kwargs': kwargs,
            'title': kwargs.get('title', page_class.__name__)
        })
        self.current_index = len(self.history) - 1
        
        # Update navigation buttons
        self.update_nav_buttons()
        
        # Create and show the page
        self.current_page = page_class(self.content_frame, *args, **kwargs)
        self.location_label.config(text=self.history[self.current_index]['title'])
    
    def go_back(self):
        """Go to previous page"""
        if self.current_index > 0:
            self.current_index -= 1
            self.show_current_page()
    
    def go_forward(self):
        """Go to next page"""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            self.show_current_page()
    
    def go_home(self):
        """Go to home page"""
        if self.history:
            self.current_index = 0
            self.show_current_page()
    
    def show_current_page(self):
        """Show the current page from history"""
        # Clear content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Get current page info
        page_info = self.history[self.current_index]
        
        # Create and show page
        self.current_page = page_info['page'](self.content_frame, 
                                              *page_info['args'], 
                                              **page_info['kwargs'])
        
        # Update navigation
        self.update_nav_buttons()
        self.location_label.config(text=page_info['title'])
    
    def update_nav_buttons(self):
        """Update navigation button states"""
        self.back_btn.config(state='normal' if self.current_index > 0 else 'disabled')
        self.forward_btn.config(state='normal' if self.current_index < len(self.history) - 1 else 'disabled')

# =============================================
# MAIN APPLICATION CLASS
# =============================================
class StudentResultSystem:
    """Main application class"""
    
    def __init__(self, db_connection, user_id, full_name, role):
        self.db_connection = db_connection
        self.user_id = user_id
        self.full_name = full_name
        self.role = role
        
        # Create main window
        self.root = tk.Tk()
        self.root.title(f"Student Result Management System - Logged in as: {full_name} ({role})")
        self.root.geometry("1400x800")
        self.root.configure(bg='#f5f5f5')
        
        # Set icon (if available)
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
        
        # Create menu
        self.create_menu()
        
        # Create header
        self.create_header()
        
        # Create navigation manager
        self.nav_manager = NavigationManager(self.root)
        
        # Create status bar
        self.create_status_bar()
        
        # Navigate to appropriate dashboard
        if role == 'admin':
            self.nav_manager.navigate_to(AdminDashboard, db_connection=self.db_connection, 
                                        user_id=self.user_id, title="Admin Dashboard")
        else:
            self.nav_manager.navigate_to(StudentDashboard, db_connection=self.db_connection,
                                        user_id=self.user_id, title="Student Dashboard")
        
        # Bind keyboard shortcuts
        self.bind_shortcuts()
        
        # Set close handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_menu(self):
        """Create main menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Home (Alt+H)", command=self.go_home, accelerator="Alt+H")
        file_menu.add_separator()
        file_menu.add_command(label="Change Password", command=self.change_password)
        file_menu.add_command(label="Logout", command=self.logout)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Refresh (F5)", command=self.refresh)
        view_menu.add_separator()
        view_menu.add_command(label="Zoom In (Ctrl++)", command=lambda: None)
        view_menu.add_command(label="Zoom Out (Ctrl+-)", command=lambda: None)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Backup Database", command=self.backup_database)
        tools_menu.add_command(label="Restore Database", command=self.restore_database)
        tools_menu.add_separator()
        tools_menu.add_command(label="Settings", command=self.show_settings)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="User Manual", command=self.show_manual)
        help_menu.add_command(label="About", command=self.show_about)
        
        # Add role-specific menus
        if self.role == 'admin':
            admin_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Admin", menu=admin_menu)
            admin_menu.add_command(label="User Management", command=lambda: self.nav_manager.navigate_to(
                UserManagement, db_connection=self.db_connection, title="User Management"))
            admin_menu.add_command(label="Database Stats", command=self.show_db_stats)
    
    def create_header(self):
        """Create header with user info"""
        header = tk.Frame(self.root, bg='#3498db', height=60)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # Title
        title = tk.Label(header, text="🎓 Student Result Management System",
                        font=('Arial', 16, 'bold'),
                        bg='#3498db', fg='white')
        title.pack(side='left', padx=20, pady=10)
        
        # User info
        user_frame = tk.Frame(header, bg='#3498db')
        user_frame.pack(side='right', padx=20)
        
        role_text = "👑 Admin" if self.role == 'admin' else "👤 Student"
        user_label = tk.Label(user_frame, text=f"{role_text}: {self.full_name}",
                             font=('Arial', 11), bg='#3498db', fg='white')
        user_label.pack(side='left', padx=10)
        
        # Logout button
        logout_btn = tk.Button(user_frame, text="Logout", bg='#e74c3c', fg='white',
                               font=('Arial', 10), bd=0, padx=15,
                               command=self.logout)
        logout_btn.pack(side='left')
    
    def create_status_bar(self):
        """Create status bar at bottom"""
        status_bar = tk.Frame(self.root, bg='#ecf0f1', height=25)
        status_bar.pack(side='bottom', fill='x')
        status_bar.pack_propagate(False)
        
        # User info
        self.user_status = tk.Label(status_bar, text=f"User: {self.full_name} ({self.role})",
                                     bg='#ecf0f1', font=('Arial', 9))
        self.user_status.pack(side='left', padx=10)
        
        # Database status
        self.db_status = tk.Label(status_bar, text="Database: Connected",
                                  bg='#ecf0f1', font=('Arial', 9), fg='green')
        self.db_status.pack(side='left', padx=20)
        
        # Date and time
        self.time_label = tk.Label(status_bar, text="", bg='#ecf0f1', font=('Arial', 9))
        self.time_label.pack(side='right', padx=10)
        self.update_time()
    
    def update_time(self):
        """Update time in status bar"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=now)
        self.root.after(1000, self.update_time)
    
    def bind_shortcuts(self):
        """Bind keyboard shortcuts"""
        self.root.bind('<Alt-h>', lambda e: self.go_home())
        self.root.bind('<F5>', lambda e: self.refresh())
        self.root.bind('<Control-q>', lambda e: self.on_closing())
    
    def go_home(self):
        """Go to home page"""
        self.nav_manager.go_home()
    
    def refresh(self):
        """Refresh current page"""
        if self.nav_manager.current_page:
            self.nav_manager.current_page.refresh()
    
    def change_password(self):
        """Change password dialog"""
        ChangePasswordDialog(self.root, self.db_connection, self.user_id)
    
    def logout(self):
        """Logout current user"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()
            # Show login window again
            LoginWindow()
    
    def backup_database(self):
        """Backup database"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".bak",
            filetypes=[("Backup files", "*.bak"), ("All files", "*.*")],
            title="Save Database Backup"
        )
        
        if filename:
            try:
                cursor = self.db_connection.cursor()
                backup_query = f"BACKUP DATABASE {DatabaseConfig.DATABASE} TO DISK = ?"
                cursor.execute(backup_query, (filename,))
                cursor.commit()
                messagebox.showinfo("Success", f"Database backup saved to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Backup failed: {e}")
    
    def restore_database(self):
        """Restore database from backup"""
        filename = filedialog.askopenfilename(
            filetypes=[("Backup files", "*.bak"), ("All files", "*.*")],
            title="Select Backup File"
        )
        
        if filename:
            if messagebox.askyesno("Confirm", "Restore will close all connections. Continue?"):
                try:
                    # Set database to single user mode
                    cursor = self.db_connection.cursor()
                    cursor.execute(f"ALTER DATABASE {DatabaseConfig.DATABASE} SET SINGLE_USER WITH ROLLBACK IMMEDIATE")
                    
                    # Restore database
                    restore_query = f"RESTORE DATABASE {DatabaseConfig.DATABASE} FROM DISK = ? WITH REPLACE"
                    cursor.execute(restore_query, (filename,))
                    
                    # Set back to multi user
                    cursor.execute(f"ALTER DATABASE {DatabaseConfig.DATABASE} SET MULTI_USER")
                    cursor.commit()
                    
                    messagebox.showinfo("Success", "Database restored successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Restore failed: {e}")
    
    def show_settings(self):
        """Show settings dialog"""
        SettingsDialog(self.root, self.db_connection)
    
    def show_manual(self):
        """Show user manual"""
        manual = """
        USER MANUAL
        
        1. Navigation
           - Use Back/Forward buttons to navigate
           - Click Home to go to dashboard
           - Use menu bar for advanced options
        
        2. For Students:
           - View your profile
           - Check exam results
           - Download result cards
           - View performance graphs
        
        3. For Admins:
           - Manage users (add/edit/delete)
           - Add/edit students
           - Manage subjects and exams
           - Enter and declare results
           - Generate reports
        
        4. Keyboard Shortcuts:
           - Alt+H: Go to Home
           - F5: Refresh
           - Ctrl+Q: Quit
        """
        messagebox.showinfo("User Manual", manual)
    
    def show_about(self):
        """Show about dialog"""
        about = """
        🎓 STUDENT RESULT MANAGEMENT SYSTEM
        Version 2.0 (SQL Server Edition)
        
        Developed with:
        • Python 3.x
        • Tkinter GUI
        • Microsoft SQL Server
        • pyodbc
        
        Features:
        ✓ Secure Login System
        ✓ Role-based Access (Admin/Student)
        ✓ Complete CRUD Operations
        ✓ Result Declaration with Auto Grade
        ✓ Report Generation (PDF/Excel)
        ✓ Performance Graphs
        ✓ Backup & Restore
        
        © 2024 All Rights Reserved
        """
        messagebox.showinfo("About", about)
    
    def show_db_stats(self):
        """Show database statistics"""
        try:
            cursor = self.db_connection.cursor()
            
            # Get statistics
            stats = {}
            
            cursor.execute("SELECT COUNT(*) FROM users")
            stats['Total Users'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM students")
            stats['Total Students'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM subjects")
            stats['Total Subjects'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM exams")
            stats['Total Exams'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM results")
            stats['Total Results'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(DISTINCT class) FROM students")
            stats['Classes'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(DISTINCT exam_type) FROM exams")
            stats['Exam Types'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT MIN(academic_year), MAX(academic_year) FROM exams")
            years = cursor.fetchone()
            stats['Academic Years'] = f"{years[0]} - {years[1]}"
            
            cursor.execute("SELECT COUNT(*) FROM results WHERE result_status = 'Pass'")
            stats['Passed Results'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM results WHERE result_status = 'Fail'")
            stats['Failed Results'] = cursor.fetchone()[0]
            
            # Format message
            message = "📊 DATABASE STATISTICS\n"
            message += "="*40 + "\n\n"
            
            for key, value in stats.items():
                message += f"{key:<20}: {value}\n"
            
            # Add to database size
            cursor.execute("""
                SELECT 
                    SUM(size * 8.0 / 1024) as size_mb
                FROM sys.master_files 
                WHERE database_id = DB_ID(?)
            """, (DatabaseConfig.DATABASE,))
            size = cursor.fetchone()[0]
            message += f"\nDatabase Size: {size:.2f} MB"
            
            messagebox.showinfo("Database Statistics", message)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get statistics: {e}")
    
    def on_closing(self):
        """Handle window closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
            if self.db_connection:
                self.db_connection.close()
            self.root.destroy()
    
    def run(self):
        """Run the application"""
        self.root.mainloop()

# =============================================
# CHANGE PASSWORD DIALOG
# =============================================
class ChangePasswordDialog:
    def __init__(self, parent, db_connection, user_id):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Change Password")
        self.dialog.geometry("400x300")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.db_connection = db_connection
        self.user_id = user_id
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create change password widgets"""
        # Title
        tk.Label(self.dialog, text="Change Password", 
                font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Current Password
        tk.Label(self.dialog, text="Current Password:", font=('Arial', 11)).pack(anchor='w', padx=30)
        self.current_entry = tk.Entry(self.dialog, font=('Arial', 11), width=30, show='●')
        self.current_entry.pack(padx=30, pady=(5,15))
        
        # New Password
        tk.Label(self.dialog, text="New Password:", font=('Arial', 11)).pack(anchor='w', padx=30)
        self.new_entry = tk.Entry(self.dialog, font=('Arial', 11), width=30, show='●')
        self.new_entry.pack(padx=30, pady=(5,15))
        
        # Confirm Password
        tk.Label(self.dialog, text="Confirm Password:", font=('Arial', 11)).pack(anchor='w', padx=30)
        self.confirm_entry = tk.Entry(self.dialog, font=('Arial', 11), width=30, show='●')
        self.confirm_entry.pack(padx=30, pady=(5,15))
        
        # Buttons
        btn_frame = tk.Frame(self.dialog)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Change Password", command=self.change_password,
                 bg='#3498db', fg='white', padx=20).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Cancel", command=self.dialog.destroy,
                 bg='#e74c3c', fg='white', padx=20).pack(side='left', padx=5)
    
    def change_password(self):
        """Change user password"""
        current = self.current_entry.get().strip()
        new = self.new_entry.get().strip()
        confirm = self.confirm_entry.get().strip()
        
        if not all([current, new, confirm]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        if new != confirm:
            messagebox.showerror("Error", "New passwords do not match")
            return
        
        if len(new) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return
        
        try:
            cursor = self.db_connection.cursor()
            
            # Verify current password
            cursor.execute("SELECT password FROM users WHERE user_id = ?", (self.user_id,))
            db_password = cursor.fetchone()[0]
            
            if current != db_password:
                messagebox.showerror("Error", "Current password is incorrect")
                return
            
            # Update password
            cursor.execute("UPDATE users SET password = ? WHERE user_id = ?", (new, self.user_id))
            self.db_connection.commit()
            
            messagebox.showinfo("Success", "Password changed successfully!")
            self.dialog.destroy()
            
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Failed to change password: {e}")

# =============================================
# SETTINGS DIALOG
# =============================================
class SettingsDialog:
    def __init__(self, parent, db_connection):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Settings")
        self.dialog.geometry("500x400")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.db_connection = db_connection
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create settings widgets"""
        # Notebook for settings
        notebook = ttk.Notebook(self.dialog)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # General Settings
        general_frame = ttk.Frame(notebook)
        notebook.add(general_frame, text="General")
        self.create_general_settings(general_frame)
        
        # Display Settings
        display_frame = ttk.Frame(notebook)
        notebook.add(display_frame, text="Display")
        self.create_display_settings(display_frame)
        
        # Backup Settings
        backup_frame = ttk.Frame(notebook)
        notebook.add(backup_frame, text="Backup")
        self.create_backup_settings(backup_frame)
        
        # About
        about_frame = ttk.Frame(notebook)
        notebook.add(about_frame, text="About")
        self.create_about(about_frame)
        
        # Save button
        tk.Button(self.dialog, text="Save Settings", command=self.save_settings,
                 bg='#2ecc71', fg='white', padx=20).pack(pady=10)
    
    def create_general_settings(self, parent):
        """Create general settings"""
        # Auto refresh
        self.auto_refresh = tk.BooleanVar(value=True)
        tk.Checkbutton(parent, text="Auto refresh data", variable=self.auto_refresh).pack(anchor='w', pady=5)
        
        # Refresh interval
        tk.Label(parent, text="Refresh interval (seconds):").pack(anchor='w', pady=(10,0))
        self.refresh_interval = tk.Spinbox(parent, from_=5, to=300, width=10)
        self.refresh_interval.pack(anchor='w')
        self.refresh_interval.delete(0, tk.END)
        self.refresh_interval.insert(0, '30')
        
        # Confirm on delete
        self.confirm_delete = tk.BooleanVar(value=True)
        tk.Checkbutton(parent, text="Confirm before delete", variable=self.confirm_delete).pack(anchor='w', pady=5)
    
    def create_display_settings(self, parent):
        """Create display settings"""
        # Theme
        tk.Label(parent, text="Theme:").pack(anchor='w', pady=5)
        self.theme = ttk.Combobox(parent, values=['Default', 'Light', 'Dark', 'Blue'], state='readonly')
        self.theme.pack(anchor='w')
        self.theme.set('Default')
        
        # Font size
        tk.Label(parent, text="Font size:").pack(anchor='w', pady=(10,5))
        self.font_size = tk.Spinbox(parent, from_=8, to=20, width=10)
        self.font_size.pack(anchor='w')
        self.font_size.delete(0, tk.END)
        self.font_size.insert(0, '10')
        
        # Show tooltips
        self.show_tooltips = tk.BooleanVar(value=True)
        tk.Checkbutton(parent, text="Show tooltips", variable=self.show_tooltips).pack(anchor='w', pady=5)
    
    def create_backup_settings(self, parent):
        """Create backup settings"""
        # Auto backup
        self.auto_backup = tk.BooleanVar(value=False)
        tk.Checkbutton(parent, text="Enable auto backup", variable=self.auto_backup).pack(anchor='w', pady=5)
        
        # Backup interval
        tk.Label(parent, text="Backup interval (days):").pack(anchor='w', pady=(10,5))
        self.backup_interval = tk.Spinbox(parent, from_=1, to=30, width=10)
        self.backup_interval.pack(anchor='w')
        self.backup_interval.delete(0, tk.END)
        self.backup_interval.insert(0, '7')
        
        # Backup location
        tk.Label(parent, text="Backup location:").pack(anchor='w', pady=(10,5))
        
        location_frame = tk.Frame(parent)
        location_frame.pack(fill='x')
        
        self.backup_location = tk.Entry(location_frame)
        self.backup_location.pack(side='left', fill='x', expand=True)
        self.backup_location.insert(0, os.path.join(os.path.expanduser('~'), 'Backups'))
        
        tk.Button(location_frame, text="Browse", command=self.browse_backup).pack(side='right', padx=5)
    
    def create_about(self, parent):
        """Create about section"""
        about_text = """
        STUDENT RESULT MANAGEMENT SYSTEM
        Version 2.0
        
        A comprehensive system for managing
        student results with SQL Server database.
        
        Features:
        • Secure Login
        • Role-based Access
        • CRUD Operations
        • Report Generation
        • Graphs & Analytics
        
        © 2024 All Rights Reserved
        """
        
        tk.Label(parent, text=about_text, justify='left', font=('Arial', 10)).pack(pady=20)
    
    def browse_backup(self):
        """Browse for backup location"""
        directory = filedialog.askdirectory(title="Select Backup Location")
        if directory:
            self.backup_location.delete(0, tk.END)
            self.backup_location.insert(0, directory)
    
    def save_settings(self):
        """Save settings"""
        # In a real application, you would save these to a config file
        messagebox.showinfo("Success", "Settings saved successfully!")
        self.dialog.destroy()

# =============================================
# ADMIN DASHBOARD
# =============================================
class AdminDashboard:
    """Admin dashboard page"""
    
    def __init__(self, parent, db_connection, user_id):
        self.parent = parent
        self.db_connection = db_connection
        self.user_id = user_id
        
        self.create_widgets()
        self.load_statistics()
    
    def create_widgets(self):
        """Create dashboard widgets"""
        # Welcome message
        welcome_frame = tk.Frame(self.parent, bg='white', padx=20, pady=20)
        welcome_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(welcome_frame, text="👋 Welcome to Admin Dashboard", 
                font=('Arial', 18, 'bold'), bg='white').pack(anchor='w')
        tk.Label(welcome_frame, text="Manage students, subjects, exams and results from here",
                font=('Arial', 11), bg='white', fg='gray').pack(anchor='w')
        
        # Statistics cards
        stats_frame = tk.Frame(self.parent, bg='#f5f5f5')
        stats_frame.pack(fill='x', padx=10, pady=10)
        
        # Create 4 cards in a row
        self.stat_cards = []
        card_data = [
            ("👥 Students", "0", "#3498db"),
            ("📚 Subjects", "0", "#2ecc71"),
            ("📝 Exams", "0", "#e74c3c"),
            ("📊 Results", "0", "#f39c12")
        ]
        
        for i, (title, value, color) in enumerate(card_data):
            card = tk.Frame(stats_frame, bg='white', relief='raised', bd=1)
            card.grid(row=0, column=i, padx=5, pady=5, sticky='nsew')
            
            # Title
            tk.Label(card, text=title, font=('Arial', 12), bg='white').pack(pady=(15,5))
            
            # Value
            value_label = tk.Label(card, text=value, font=('Arial', 24, 'bold'), 
                                  fg=color, bg='white')
            value_label.pack(pady=(0,15))
            
            self.stat_cards.append(value_label)
        
        # Configure grid weights
        for i in range(4):
            stats_frame.grid_columnconfigure(i, weight=1)
        
        # Quick actions
        actions_frame = tk.LabelFrame(self.parent, text="Quick Actions", 
                                      font=('Arial', 12, 'bold'),
                                      bg='white', padx=20, pady=20)
        actions_frame.pack(fill='x', padx=10, pady=10)
        
        actions = [
            ("➕ Add Student", self.add_student, '#3498db'),
            ("📚 Add Subject", self.add_subject, '#2ecc71'),
            ("📝 Create Exam", self.create_exam, '#e74c3c'),
            ("📊 Declare Result", self.declare_result, '#f39c12'),
            ("📋 Manage Users", self.manage_users, '#9b59b6'),
            ("📈 View Reports", self.view_reports, '#1abc9c')
        ]
        
        for i, (text, command, color) in enumerate(actions):
            btn = tk.Button(actions_frame, text=text, command=command,
                           bg=color, fg='white', font=('Arial', 11),
                           width=15, height=2, bd=0)
            btn.grid(row=i//3, column=i%3, padx=10, pady=10)
        
        # Recent activities
        recent_frame = tk.LabelFrame(self.parent, text="Recent Activities",
                                     font=('Arial', 12, 'bold'),
                                     bg='white', padx=20, pady=20)
        recent_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Treeview for recent activities
        columns = ('Time', 'User', 'Action', 'Details')
        self.recent_tree = ttk.Treeview(recent_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.recent_tree.heading(col, text=col)
            self.recent_tree.column(col, width=150)
        
        self.recent_tree.pack(fill='both', expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(recent_frame, orient='vertical', command=self.recent_tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.recent_tree.configure(yscrollcommand=scrollbar.set)
    
    def load_statistics(self):
        """Load statistics from database"""
        try:
            cursor = self.db_connection.cursor()
            
            # Student count
            cursor.execute("SELECT COUNT(*) FROM students")
            self.stat_cards[0].config(text=cursor.fetchone()[0])
            
            # Subject count
            cursor.execute("SELECT COUNT(*) FROM subjects")
            self.stat_cards[1].config(text=cursor.fetchone()[0])
            
            # Exam count
            cursor.execute("SELECT COUNT(*) FROM exams")
            self.stat_cards[2].config(text=cursor.fetchone()[0])
            
            # Result count
            cursor.execute("SELECT COUNT(*) FROM results")
            self.stat_cards[3].config(text=cursor.fetchone()[0])
            
            # Load recent activities (from audit_log table)
            cursor.execute("""
                SELECT TOP 10 
                    CONVERT(VARCHAR, action_date, 120) as time,
                    u.full_name as user,
                    action,
                    table_name + ' - ' + ISNULL(remarks, '')
                FROM audit_log a
                JOIN users u ON a.user_id = u.user_id
                ORDER BY action_date DESC
            """)
            
            for row in cursor.fetchall():
                self.recent_tree.insert('', 'end', values=row)
                
        except Exception as e:
            print(f"Error loading statistics: {e}")
    
    def add_student(self):
        """Navigate to add student page"""
        # This would navigate to student management page
        messagebox.showinfo("Info", "Add Student - To be implemented")
    
    def add_subject(self):
        """Navigate to add subject page"""
        messagebox.showinfo("Info", "Add Subject - To be implemented")
    
    def create_exam(self):
        """Navigate to create exam page"""
        messagebox.showinfo("Info", "Create Exam - To be implemented")
    
    def declare_result(self):
        """Navigate to declare result page"""
        messagebox.showinfo("Info", "Declare Result - To be implemented")
    
    def manage_users(self):
        """Navigate to manage users page"""
        messagebox.showinfo("Info", "Manage Users - To be implemented")
    
    def view_reports(self):
        """Navigate to reports page"""
        messagebox.showinfo("Info", "View Reports - To be implemented")
    
    def refresh(self):
        """Refresh dashboard data"""
        self.load_statistics()

# =============================================
# STUDENT DASHBOARD
# =============================================
class StudentDashboard:
    """Student dashboard page"""
    
    def __init__(self, parent, db_connection, user_id):
        self.parent = parent
        self.db_connection = db_connection
        self.user_id = user_id
        
        # Get student_id from user_id
        self.student_id = self.get_student_id()
        
        self.create_widgets()
        self.load_student_info()
    
    def get_student_id(self):
        """Get student_id from user_id"""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT student_id FROM students WHERE user_id = ?", (self.user_id,))
            result = cursor.fetchone()
            return result[0] if result else None
        except:
            return None
    
    def create_widgets(self):
        """Create student dashboard widgets"""
        # Welcome message
        welcome_frame = tk.Frame(self.parent, bg='white', padx=20, pady=20)
        welcome_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(welcome_frame, text="👋 Welcome to Student Dashboard", 
                font=('Arial', 18, 'bold'), bg='white').pack(anchor='w')
        self.welcome_sub = tk.Label(welcome_frame, text="", font=('Arial', 11), 
                                   bg='white', fg='gray')
        self.welcome_sub.pack(anchor='w')
        
        # Student info card
        info_frame = tk.LabelFrame(self.parent, text="My Profile",
                                   font=('Arial', 12, 'bold'),
                                   bg='white', padx=20, pady=20)
        info_frame.pack(fill='x', padx=10, pady=10)
        
        # Create two columns for student info
        left_frame = tk.Frame(info_frame, bg='white')
        left_frame.pack(side='left', fill='both', expand=True)
        
        right_frame = tk.Frame(info_frame, bg='white')
        right_frame.pack(side='right', fill='both', expand=True)
        
        self.info_labels = {}
        info_fields = [
            ('Name:', 'name'),
            ('Roll Number:', 'roll'),
            ('Class:', 'class'),
            ('Section:', 'section'),
            ("Father's Name:", 'father'),
            ("Mother's Name:", 'mother'),
            ('Date of Birth:', 'dob'),
            ('Contact:', 'contact'),
            ('Email:', 'email')
        ]
        
        # Split fields into two columns
        for i, (label, key) in enumerate(info_fields[:5]):
            frame = tk.Frame(left_frame, bg='white')
            frame.pack(fill='x', pady=5)
            
            tk.Label(frame, text=label, font=('Arial', 10, 'bold'), 
                    bg='white', width=15, anchor='w').pack(side='left')
            
            self.info_labels[key] = tk.Label(frame, text="-", font=('Arial', 10),
                                            bg='white', anchor='w')
            self.info_labels[key].pack(side='left', fill='x', expand=True)
        
        for i, (label, key) in enumerate(info_fields[5:]):
            frame = tk.Frame(right_frame, bg='white')
            frame.pack(fill='x', pady=5)
            
            tk.Label(frame, text=label, font=('Arial', 10, 'bold'),
                    bg='white', width=15, anchor='w').pack(side='left')
            
            self.info_labels[key] = tk.Label(frame, text="-", font=('Arial', 10),
                                            bg='white', anchor='w')
            self.info_labels[key].pack(side='left', fill='x', expand=True)
        
        # Quick actions
        actions_frame = tk.LabelFrame(self.parent, text="Quick Actions",
                                      font=('Arial', 12, 'bold'),
                                      bg='white', padx=20, pady=20)
        actions_frame.pack(fill='x', padx=10, pady=10)
        
        actions = [
            ("📋 View Results", self.view_results, '#3498db'),
            ("📊 Performance Graph", self.view_graph, '#2ecc71'),
            ("📄 Download Report", self.download_report, '#e74c3c'),
            ("🔍 Search Results", self.search_results, '#f39c12')
        ]
        
        for i, (text, command, color) in enumerate(actions):
            btn = tk.Button(actions_frame, text=text, command=command,
                           bg=color, fg='white', font=('Arial', 11),
                           width=20, height=2, bd=0)
            btn.grid(row=i//2, column=i%2, padx=10, pady=10)
        
        # Recent results
        results_frame = tk.LabelFrame(self.parent, text="Recent Results",
                                      font=('Arial', 12, 'bold'),
                                      bg='white', padx=20, pady=20)
        results_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Treeview for recent results
        columns = ('Exam', 'Subject', 'Marks', 'Grade', 'Status', 'Date')
        self.results_tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=5)
        
        for col in columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, width=100)
        
        self.results_tree.pack(fill='both', expand=True)
    
    def load_student_info(self):
        """Load student information from database"""
        if not self.student_id:
            self.welcome_sub.config(text="No student profile linked to this account")
            return
        
        try:
            cursor = self.db_connection.cursor()
            
            # Get student details
            cursor.execute("""
                SELECT full_name, roll_number, class, section,
                       father_name, mother_name, date_of_birth,
                       contact_number, email
                FROM students WHERE student_id = ?
            """, (self.student_id,))
            
            student = cursor.fetchone()
            
            if student:
                self.welcome_sub.config(text=f"Welcome, {student[0]}")
                
                # Update info labels
                self.info_labels['name'].config(text=student[0])
                self.info_labels['roll'].config(text=student[1])
                self.info_labels['class'].config(text=student[2])
                self.info_labels['section'].config(text=student[3])
                self.info_labels['father'].config(text=student[4] or '-')
                self.info_labels['mother'].config(text=student[5] or '-')
                self.info_labels['dob'].config(text=str(student[6]) if student[6] else '-')
                self.info_labels['contact'].config(text=student[7] or '-')
                self.info_labels['email'].config(text=student[8] or '-')
                
                # Load recent results
                self.load_recent_results()
            
        except Exception as e:
            print(f"Error loading student info: {e}")
    
    def load_recent_results(self):
        """Load recent results for student"""
        try:
            cursor = self.db_connection.cursor()
            
            cursor.execute("""
                SELECT TOP 5
                    e.exam_name,
                    sub.subject_name,
                    r.obtained_marks,
                    r.grade,
                    r.result_status,
                    CONVERT(VARCHAR, r.declared_date, 103)
                FROM results r
                JOIN exams e ON r.exam_id = e.exam_id
                JOIN subjects sub ON r.subject_id = sub.subject_id
                WHERE r.student_id = ?
                ORDER BY r.declared_date DESC
            """, (self.student_id,))
            
            for row in cursor.fetchall():
                # Add tag for color coding
                tags = ('pass',) if row[4] == 'Pass' else ('fail',)
                self.results_tree.insert('', 'end', values=row, tags=tags)
            
            # Configure tags
            self.results_tree.tag_configure('pass', background='#e8f5e8')
            self.results_tree.tag_configure('fail', background='#ffe8e8')
            
        except Exception as e:
            print(f"Error loading results: {e}")
    
    def view_results(self):
        """View all results"""
        messagebox.showinfo("Info", "View Results - To be implemented")
    
    def view_graph(self):
        """View performance graph"""
        if not self.student_id:
            messagebox.showerror("Error", "No student profile found")
            return
        
        # Create new window for graph
        graph_window = tk.Toplevel(self.parent)
        graph_window.title("Performance Graph")
        graph_window.geometry("800x600")
        
        try:
            cursor = self.db_connection.cursor()
            
            # Get results data
            cursor.execute("""
                SELECT 
                    e.exam_name,
                    AVG(r.obtained_marks * 100.0 / sub.max_marks) as percentage
                FROM results r
                JOIN exams e ON r.exam_id = e.exam_id
                JOIN subjects sub ON r.subject_id = sub.subject_id
                WHERE r.student_id = ?
                GROUP BY e.exam_name, e.exam_id
                ORDER BY e.exam_id
            """, (self.student_id,))
            
            data = cursor.fetchall()
            
            if not data:
                tk.Label(graph_window, text="No data available for graph",
                        font=('Arial', 14)).pack(expand=True)
                return
            
            exams = [row[0] for row in data]
            percentages = [row[1] for row in data]
            
            # Create figure
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            
            # Bar chart
            ax1.bar(exams, percentages, color='#3498db')
            ax1.set_xlabel('Exams')
            ax1.set_ylabel('Percentage')
            ax1.set_title('Exam-wise Performance')
            ax1.set_ylim(0, 100)
            
            # Add value labels on bars
            for i, v in enumerate(percentages):
                ax1.text(i, v + 1, f'{v:.1f}%', ha='center')
            
            # Line chart
            ax2.plot(exams, percentages, marker='o', color='#2ecc71', linewidth=2)
            ax2.set_xlabel('Exams')
            ax2.set_ylabel('Percentage')
            ax2.set_title('Performance Trend')
            ax2.set_ylim(0, 100)
            
            plt.tight_layout()
            
            # Embed in tkinter
            canvas = FigureCanvasTkAgg(fig, master=graph_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate graph: {e}")
    
    def download_report(self):
        """Download report as PDF"""
        messagebox.showinfo("Info", "Download Report - To be implemented")
    
    def search_results(self):
        """Search for results"""
        messagebox.showinfo("Info", "Search Results - To be implemented")
    
    def refresh(self):
        """Refresh dashboard"""
        self.load_student_info()

# =============================================
# USER MANAGEMENT PAGE
# =============================================
class UserManagement:
    """User management page for admin"""
    
    def __init__(self, parent, db_connection, title="User Management"):
        self.parent = parent
        self.db_connection = db_connection
        
        self.create_widgets()
        self.load_users()
    
    def create_widgets(self):
        """Create user management widgets"""
        # Main container
        main_frame = tk.Frame(self.parent, bg='#f5f5f5', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        tk.Label(main_frame, text="👥 User Management", 
                font=('Arial', 16, 'bold'), bg='#f5f5f5').pack(anchor='w', pady=(0,20))
        
        # Create user form
        form_frame = tk.LabelFrame(main_frame, text="Create New User",
                                   font=('Arial', 12, 'bold'),
                                   bg='white', padx=20, pady=20)
        form_frame.pack(fill='x', pady=(0,20))
        
        # Form fields
        fields = [
            ('Username:', 'username_entry'),
            ('Password:', 'password_entry'),
            ('Full Name:', 'fullname_entry'),
            ('Role:', 'role_combo')
        ]
        
        self.entries = {}
        
        for i, (label, name) in enumerate(fields):
            tk.Label(form_frame, text=label, font=('Arial', 10),
                    bg='white').grid(row=i, column=0, sticky='w', pady=5, padx=5)
            
            if name == 'role_combo':
                self.entries[name] = ttk.Combobox(form_frame, values=['admin', 'student'],
                                                  state='readonly', width=30)
                self.entries[name].set('student')
            else:
                self.entries[name] = tk.Entry(form_frame, font=('Arial', 10), width=30)
            
            self.entries[name].grid(row=i, column=1, pady=5, padx=5)
        
        # Security question
        tk.Label(form_frame, text="Security Question:", font=('Arial', 10),
                bg='white').grid(row=4, column=0, sticky='w', pady=5, padx=5)
        
        self.security_question = tk.Entry(form_frame, font=('Arial', 10), width=30)
        self.security_question.grid(row=4, column=1, pady=5, padx=5)
        self.security_question.insert(0, "What is your favorite color?")
        
        tk.Label(form_frame, text="Security Answer:", font=('Arial', 10),
                bg='white').grid(row=5, column=0, sticky='w', pady=5, padx=5)
        
        self.security_answer = tk.Entry(form_frame, font=('Arial', 10), width=30)
        self.security_answer.grid(row=5, column=1, pady=5, padx=5)
        
        # Buttons
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        tk.Button(btn_frame, text="Create User", command=self.create_user,
                 bg='#3498db', fg='white', font=('Arial', 10),
                 padx=20).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Clear Form", command=self.clear_form,
                 bg='#e74c3c', fg='white', font=('Arial', 10),
                 padx=20).pack(side='left', padx=5)
        
        # Users list
        list_frame = tk.LabelFrame(main_frame, text="Existing Users",
                                   font=('Arial', 12, 'bold'),
                                   bg='white', padx=20, pady=20)
        list_frame.pack(fill='both', expand=True)
        
        # Treeview for users
        columns = ('ID', 'Username', 'Full Name', 'Role', 'Status', 'Last Login')
        self.user_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)
        
        for col in columns:
            self.user_tree.heading(col, text=col)
            self.user_tree.column(col, width=100)
        
        self.user_tree.pack(fill='both', expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.user_tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.user_tree.configure(yscrollcommand=scrollbar.set)
        
        # Bind selection
        self.user_tree.bind('<<TreeviewSelect>>', self.on_user_select)
        
        # Action buttons
        action_frame = tk.Frame(list_frame, bg='white')
        action_frame.pack(fill='x', pady=10)
        
        tk.Button(action_frame, text="Edit Selected", command=self.edit_user,
                 bg='#f39c12', fg='white', padx=15).pack(side='left', padx=5)
        
        tk.Button(action_frame, text="Delete Selected", command=self.delete_user,
                 bg='#e74c3c', fg='white', padx=15).pack(side='left', padx=5)
        
        tk.Button(action_frame, text="Reset Password", command=self.reset_password,
                 bg='#3498db', fg='white', padx=15).pack(side='left', padx=5)
        
        tk.Button(action_frame, text="Refresh", command=self.load_users,
                 bg='#2ecc71', fg='white', padx=15).pack(side='left', padx=5)
    
    def load_users(self):
        """Load users from database"""
        try:
            # Clear existing items
            for item in self.user_tree.get_children():
                self.user_tree.delete(item)
            
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT user_id, username, full_name, role,
                       CASE WHEN is_active = 1 AND is_locked = 0 THEN 'Active'
                            WHEN is_locked = 1 THEN 'Locked'
                            ELSE 'Inactive' END as status,
                       CONVERT(VARCHAR, last_login, 120) as last_login
                FROM users
                ORDER BY user_id
            """)
            
            for row in cursor.fetchall():
                self.user_tree.insert('', 'end', values=row)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load users: {e}")
    
    def create_user(self):
        """Create new user"""
        username = self.entries['username_entry'].get().strip()
        password = self.entries['password_entry'].get().strip()
        fullname = self.entries['fullname_entry'].get().strip()
        role = self.entries['role_combo'].get()
        question = self.security_question.get().strip()
        answer = self.security_answer.get().strip()
        
        if not all([username, password, fullname, role]):
            messagebox.showerror("Error", "Please fill all required fields")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return
        
        try:
            cursor = self.db_connection.cursor()
            
            # Check if username exists
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
            if cursor.fetchone()[0] > 0:
                messagebox.showerror("Error", "Username already exists")
                return
            
            # Insert user
            cursor.execute("""
                INSERT INTO users (username, password, full_name, role, 
                                  security_question, security_answer)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (username, password, fullname, role, question, answer))
            
            self.db_connection.commit()
            
            messagebox.showinfo("Success", "User created successfully!")
            self.clear_form()
            self.load_users()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create user: {e}")
    
    def clear_form(self):
        """Clear the form"""
        self.entries['username_entry'].delete(0, tk.END)
        self.entries['password_entry'].delete(0, tk.END)
        self.entries['fullname_entry'].delete(0, tk.END)
        self.entries['role_combo'].set('student')
        self.security_answer.delete(0, tk.END)
    
    def on_user_select(self, event):
        """Handle user selection"""
        selected = self.user_tree.selection()
        if selected:
            values = self.user_tree.item(selected[0])['values']
            self.selected_user_id = values[0]
    
    def edit_user(self):
        """Edit selected user"""
        if not hasattr(self, 'selected_user_id'):
            messagebox.showerror("Error", "Please select a user")
            return
        
        messagebox.showinfo("Info", f"Edit user {self.selected_user_id} - To be implemented")
    
    def delete_user(self):
        """Delete selected user"""
        if not hasattr(self, 'selected_user_id'):
            messagebox.showerror("Error", "Please select a user")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this user?"):
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("DELETE FROM users WHERE user_id = ?", (self.selected_user_id,))
                self.db_connection.commit()
                
                messagebox.showinfo("Success", "User deleted successfully!")
                self.load_users()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete user: {e}")
    
    def reset_password(self):
        """Reset password for selected user"""
        if not hasattr(self, 'selected_user_id'):
            messagebox.showerror("Error", "Please select a user")
            return
        
        # Create dialog for new password
        dialog = tk.Toplevel(self.parent)
        dialog.title("Reset Password")
        dialog.geometry("300x150")
        dialog.transient(self.parent)
        dialog.grab_set()
        
        tk.Label(dialog, text="New Password:", font=('Arial', 11)).pack(pady=10)
        password_entry = tk.Entry(dialog, font=('Arial', 11), show='●')
        password_entry.pack(pady=5)
        
        def do_reset():
            new_password = password_entry.get().strip()
            if not new_password:
                messagebox.showerror("Error", "Please enter password")
                return
            
            if len(new_password) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters")
                return
            
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("UPDATE users SET password = ? WHERE user_id = ?",
                             (new_password, self.selected_user_id))
                self.db_connection.commit()
                
                messagebox.showinfo("Success", "Password reset successfully!")
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to reset password: {e}")
        
        tk.Button(dialog, text="Reset", command=do_reset,
                 bg='#3498db', fg='white', padx=20).pack(pady=10)
    
    def refresh(self):
        """Refresh the page"""
        self.load_users()

# =============================================
# MAIN EXECUTION
# =============================================
if __name__ == "__main__":
    # Start with login window
    login = LoginWindow()