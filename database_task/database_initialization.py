import pyodbc

connection = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                            'Direct=True;'
                            'Database=test.db;'
                            'String Types=Unicode')

cursor = connection.cursor()
cursor.execute('CREATE TABLE news (news text, city text, date_of_post text)')
cursor.execute('CREATE TABLE ads (ad_text text, expiration_date text)')
cursor.execute('CREATE TABLE twits (user_name text, post_text text, date_of_post text)')
cursor.execute('CREATE TABLE twits_ads (ad_text text, expiration_date text)')

connection.commit()

cursor.close()
connection.close()
