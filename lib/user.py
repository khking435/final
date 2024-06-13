from config.config import conn, cursor

class User :
    def __init__(self,  username, password,user_id=None,):
        self.user_id = user_id
        self.username = username
        self.password = password
    def __str__(self):
        return f'User(id={self.user_id}, username={self.username}, password={self.password})'
    @property
    def username(self):
        """Return the username of the user."""
        return self._username
    @property
    def username(self):
        """Return the username of the user."""
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError('Username cannot be empty')
        self._username = value

    @classmethod
    def create_table (cls):
        '''create table if not exist'''
        sql='''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        '''
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table (cls): 
        ''''drop table'''
        sql = 'DROP TABLE IF EXISTS users'
        cursor.execute(sql)
        conn.commit()
    def save(self):
        """Save user to database."""
        query = '''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        '''
        cursor.execute(query, (self.username, self.password))
        conn.commit()
        self.user_id = cursor.lastrowid
        


    def update (self):  
        '''update user'''
        sql = '''UPDATE users SET username = ?, password = ? WHERE id = ?'''
        cursor.execute(sql, (self.username, self.password, self.id))
        conn.commit()

    def delete (self):
        sql = '''DELETE FROM users WHERE id = ?'''
        cursor.execute(sql, (self.id,))
        conn.commit()

    @classmethod
    def get_by_id (cls, id):
        sql = '''SELECT * FROM users WHERE id = ?'''
        cursor.execute(sql, (id,))
        user = cursor.fetchone()
        if user:
            return cls(*user)
        return None
    

    @classmethod
    def get_all_username (cls, username):
        ''''get all username'''
        sql = '''SELECT * FROM users  ?'''
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
       
