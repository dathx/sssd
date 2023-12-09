import pyodbc

class ConnectDB:
    def __init__(self, drive = 'SQL Server' , server = 'VN-PF27VFXB', database = 'duan1_final', username = 'sa', password = 'P@ssword123456'):
        self.drive = drive
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = self.connect()

    def connect(self):
        connection_string = f"DRIVER={self.drive};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        return pyodbc.connect(connection_string)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result