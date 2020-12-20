import cx_Oracle

from datetime import date


def calculateDuration(start, end):
    st = start.split('-')
    ed = end.split('-')
    startDate = date(year=int(st[2]), month=int(st[1]), day=int(st[0]))
    endDate = date(year=int(ed[2][:4]), month=int(ed[1]), day=int(ed[0]))
    return (endDate - startDate)


def insertApplicationData(userid, leave, start, end, reason):
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

            sql_select = """ select userName from {} where userid = {} """.format(
                'sql_leave', userid)
            cur.execute(sql_select)
            row = cur.fetchone()
            username = row[0]
            duration = calculateDuration(start, end)
            duration = (str(duration).split(',')[0])

            sql = "insert into sql_application values (:1, :2, :3, :4, :5, :6, :7)"
            cur.execute(sql, [userid, username, leave,
                              reason, start, end, duration])
        except Exception as err:
            print("Error while inserting into the database!!", err)
        else:
            print("Inserted succesfully!!")
            conn.commit()
    finally:
        cur.close()
        conn.close()


userid = 2
leave = "sick_leave"
start = "25-10-2020"
end = "26-10-2020"
reason = "I am feeling sick since 2 days"
#insertApplicationData(userid, leave, start, end, reason)