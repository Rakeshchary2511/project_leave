import cx_Oracle


def createApplicationTable():
    try:
        # create connection
        conn = cx_Oracle.connect("system", "123456", "localhost:1521/xe")
        print("connected!!")
    except Exception as err:
        print("Error while connecting to the database!!", err)
    else:
        try:
            # create cursor
            cur = conn.cursor()
            sql_create = """create table sql_application(
            userid INT,
            userName VARCHAR(50),
            leave VARCHAR(50),
            reason VARCHAR(200),
            start_date VARCHAR(10) NOT NULL,
            end_date VARCHAR(12) NOT NULL,
            duration VARCHAR(10)
            )"""
            cur.execute(sql_create)
        except Exception as err:
            print("Error while inserting into the database!!", err)
        else:
            print("Table created succesfully!!")
            conn.commit()
    finally:
        cur.close()
        conn.close()


createApplicationTable()
