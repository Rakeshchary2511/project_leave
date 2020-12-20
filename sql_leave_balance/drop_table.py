import cx_Oracle


def dropTable():
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
            sql_drop = "drop table sql_leave"
            cur.execute(sql_drop)
        except Exception as err:
            print("Error while inserting into the database!!", err)
        else:
            print("Dropped succesfully!!")
            conn.commit()
    finally:
        cur.close()
        conn.close()


dropTable()
