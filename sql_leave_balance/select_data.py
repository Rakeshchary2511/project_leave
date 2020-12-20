import cx_Oracle


def selectAllData(table):
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
            sql_select_all = """ select * from {} """.format(table)
            cur.execute(sql_select_all)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except Exception as err:
            print("Error while inserting into the database!!", err)
        else:
            print("Fetching all Succesful!!")
    finally:
        cur.close()
        conn.close()


def selectUserLeave(userid, leaveType):
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
            sql_select_data = """ select {} from sql_leave where userid = {} """.format(
                leaveType, userid)
            cur.execute(sql_select_data)
            return (cur.fetchone()[0])
        except Exception as err:
            print("Error while inserting into the database!!", err)
        else:
            print("Fetch Succesful!!")
    finally:
        cur.close()
        conn.close()


# table = "sql_leave"
# selectUserLeave(3, 'half_pay_leave')
