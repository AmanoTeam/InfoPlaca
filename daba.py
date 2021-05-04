import sqlite3

db = sqlite3.connect("placabot.db")
cursor = db.cursor()

cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, 
                                             historic,
                                             is_premium INTEGER)"""
        
)

cursor.execute(
        """CREATE TABLE IF NOT EXISTS groups (chat_id INTEGER PRIMARY KEY)"""
        
)

db.commit()