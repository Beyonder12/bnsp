pip install Flask Flask-SQLAlchemy
lsof -i :5000
kill -9 <PID>


sqlite3 mydatabase.db
.tables
PRAGMA table_info(Item);
SELECT * FROM Item;
.exit
