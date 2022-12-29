import connect_db


def fetchOperators():
    conn = connect_db.connectOracle()
    c = conn.cursor()
    c.execute(
        'select * from PRONGC.operator where rownum < 2')  # use triple quotes if you want to spread your query across multiple lines
    for row in c:
        print(row)


if __name__ == '__main__':
    fetchOperators()
