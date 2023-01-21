import mysql.connector
import os

import time


usr = os.environ["MYSQL_USER"]
pwd = os.environ["MYSQL_PASS"]
host = os.environ["MYSQL_HOST"]
port = os.environ["MYSQL_PORT"]
dataase = os.environ["MYSQL_DB"]


cnx = mysql.connector.connect(user=usr, password=pwd, host=host, port=port, db=database)

cursor = cnx.cursor()

# Create table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS `records` (`msg_id` VARCHAR(50), `epoch` BIGINT)")

i = 0
while True:
    cursor.execute(f'INSERT INTO `records` (`msg_id`, `epoch`) VALUES ("{i}", {int(time.time())})')
    i += 1
    time.sleep(10)


cnx.close()
