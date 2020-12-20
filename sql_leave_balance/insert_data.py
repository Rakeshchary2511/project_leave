import cx_Oracle


def insertData(table, dataTuple):
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
            sql_insert = """insert into {} values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20)""".format(
                table)
            cur.executemany(sql_insert, dataTuple)
        except Exception as err:
            print("Error while inserting into the database!!", err)
        else:
            print("Inserted succesfully!!")
            conn.commit()
    finally:
        cur.close()
        conn.close()


dataToInsert = [
    (1, 'Adda Pelos', 1, 1, 3, 1, 3, 4, 1, 5, 2, 1, 2, 5, 2, 3, 1, 2, 1, "HR"),
    (2, 'Percival Veazey', 5, 2, 5, 5, 1, 2, 2,
     2, 3, 5, 3, 5, 3, 2, 5, 5, 4, "Tech. LEAD"),
    (3, 'Jacquelin Whitecross', 3, 1, 5, 5, 1, 5, 1,
     5, 5, 4, 3, 2, 1, 4, 3, 5, 4, "Jr. Scientist"),
    (4, 'Margarette Collidge', 4, 2, 4, 3, 5, 1, 3,
     2, 5, 1, 2, 3, 3, 3, 5, 3, 4, "Sr. Scientist"),
    (5, 'Alleen Greeves', 3, 1, 3, 3, 4, 1, 4, 2,
     3, 3, 5, 3, 3, 5, 5, 4, 4, "Sr. Scientist"),
    (6, 'Raymund Blaise', 1, 1, 5, 4, 2, 5, 2, 4, 3, 2, 2, 5, 5, 5, 2, 3, 5, "HR"),
    (7, 'Muhammad Bagott', 3, 2, 4, 4, 1, 5, 2,
     1, 1, 5, 4, 3, 3, 4, 4, 3, 3, "Manager"),
    (8, 'Chrissie MacKey', 4, 1, 4, 3, 5, 2,
     3, 5, 2, 1, 1, 2, 4, 5, 3, 3, 5, "HR"),
    (9, 'Willow Churn', 3, 2, 2, 3, 3, 3, 5, 2,
     3, 3, 1, 1, 3, 4, 5, 1, 3, "Jr. Scientist"),
    (10, 'Yardley Brewin', 2, 1, 3, 1, 2, 5, 5,
     4, 5, 3, 4, 3, 2, 3, 4, 5, 3, "Tech. LEAD")
]
insertData("sql_leave", dataToInsert)
