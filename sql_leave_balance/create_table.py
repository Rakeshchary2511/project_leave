import cx_Oracle


def createTable():
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
            sql_create = """create table sql_leave(
            userid INT primary key,
            userName VARCHAR(50) NOT NULL,
            earned_leave INT,
            half_pay_leave INT,
            commuted_leave INT,
            special_casual_leave INT,
            eol_with_mc_leave INT,
            disability_half_leave INT,
            leave_not_due_balance INT,
            child_care_leave INT,
            unauthorized_absence_leave INT,
            disability_full_leave INT,
            study_leave INT,
            comp_off_leave INT,
            maternity_leave INT,
            miscarriage_leave INT,
            paternity_leave INT,
            adoption_leave INT,
            eol_without_mc_leave INT,
            position VARCHAR(50) NOT NULL
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


createTable()
