import sqlite3


class Database:
    def __init__(self,path_to_db="main.db"):
        self.path_to_db= path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str , parametrs: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parametrs:
            parametrs = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parametrs)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data= cursor.fetchone()
        connection.close()
        return data
    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY(id) 
                );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql,parametres:dict):
            sql+= " AND ".join([
                f"{item} = ?" for item in parametres

                ])
            return sql,tuple(parametres.values())

    def add_user(self,id: int,name:str,email:str=None, language: str='uz'):
        sql="""
            INSERT INTO Users(id,Name,email,language) VALUES(?,?,?,?)
            """
        self.execute(sql,parametrs=(id,name,email,language),commit=True)
    def select_all_users(self):
            sql= "SELECT * FROM Users"
            return self.execute(sql,fetchall=True)
    def select_user(self,**kwargs):
        sql= "SELECT* FROM Users WHERE"
        sql,parametres=self.format_args(sql,kwargs)


        return self.execute(sql,parametrs=parametres,fetchone=True)
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;",fetchone=True)
    def update_user_email(self,email ,id):
            sql=f"""
                UPDATE users SET emai=? WHERE id=?
                """
            return self.execute(sql,parametrs=(email, id),commit=True)
    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE",commit=True)
def logger(statement):
    print(f"""
____________________________
Executing:
{statement}
_____________________________
""")