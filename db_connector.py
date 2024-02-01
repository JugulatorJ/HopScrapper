import mysql.connector as connector
import os
from dotenv import load_dotenv

load_dotenv()


class ConnectToDB:

    def __init__(self):

        self.connection = connector.connect(user='root', password=os.getenv("DB_PASS"),
                                            host='127.0.0.1', database='certificates',
                                            auth_plugin='mysql_native_password')
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print('Próba połączenia z bazą danych MySQLWorkbench powiodła się.\n')
        else:
            print('Próba połączenia z bazą danych MySQLWorkbench nie powiodła się.')


class ModifyDB(ConnectToDB):

    def __init__(self):
        super().__init__()

    def insert_data(self, table_name, certificate_dict):

        insert_query = "INSERT INTO {} " \
                       "(entry_id, lot_id, contract_number, hop_name," \
                       " crop_year, alpha_acid, beta_acid, total_oil, cohumulone) " \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)".format(table_name)

        self.cursor.execute(insert_query, tuple(certificate_dict.values()))
        self.connection.commit()
        print(self.cursor.rowcount, "record inserted.")
