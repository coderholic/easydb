import os
import sqlite3

class EasyDB:
    def __init__(self, filename, schema = None, **kwargs):
        if os.path.exists(filename) or schema:
            self.connection = sqlite3.connect(filename)
        elif not schema:
            raise Exception, "The specified database file does not exist, and you haven't provided a schema"
        else:
            for table_name, fields in schema.items():
                query = "CREATE TABLE %s (%s)" % (table_name, ", ".join(fields))
                self.query(query)

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def query(self, *args, **kwargs):
        cursor = self.connection.cursor()
        result = cursor.execute(*args, **kwargs)
        return result
