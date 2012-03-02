# EasyDB

A really simple **SQLite wrapper** that saves you from having to worry about creating tables or managing connections.

It can be used on existing SQLite database by simply passing in the database filename:

```python
from easydb import EasyDB
db = EasyDB('filename.db')
cursor = db.query("SELECT * FROM mytable")
```

New databases can be creating by specifying your schema as a dictionary, eg:

```python
schema = {
    'table_name': ['column_name column_type', …],
    'table_name': ['column_name column_type', …],
    'table_name': ['column_name column_type', …]
}
db = EasyDB('filename.db', schema)
```

If the database file already exists then the schema won't be updated, but if it doesn't exist then it'll be created with the given schema. Here's a full example:

```python
from easydb import EasyDB
db = EasyDb('my.db', {'users': ['username text', 'description text']})

db.query("INSERT INTO users (username, description) VALUES (?, ?)", ('ben', 'some sort of description'))

for result in db.query("SELECT * FROM users"):
    print result
# => ('ben', 'some sort of description')
```
