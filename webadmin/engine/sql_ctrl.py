from django.db import connection, transaction

def sql_update( table, id, condition, value ):
    cursor = connection.cursor()
    sql = "UPDATE %s SET %s = %s WHERE id = %s"%( table, condition, value, id )
    cursor.execute(sql)
    transaction.commit_unless_managed()


def sql_one( sql ):
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit_unless_managed()
