from datetime import datetime

current_data = datetime.today().strftime('%Y-%m-%d')

SQLITE_DATABASE_NAME = "guestbook.db"
SQLITE_DATABASE_BACKUP_NAME = 'backup_' + current_data + '.db'
