
import mariadb


def just_connect():
    import dbcreds
    import mariadb
    try:
        conn = mariadb.connect(
        user=dbcreds.user, 
        password=dbcreds.password,
        host=dbcreds.host, 
        port=dbcreds.port, 
        database=dbcreds.database)

        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("OPERATIONAL ERROR: ", error)
    except Exception as error:
        print("unexpected error: ", error)
        



def cursor_result(cursor, the_procedure, list_of_args=[]):
    try:
        cursor.execute(the_procedure, list_of_args)
        result = cursor.fetchall()
        return result
    except mariadb.ProgrammingError as error:
        print('Programming Error: ', error)
    except mariadb.IntegrityError as error:
        print('integrityError:', error)
    except mariadb.DataError as error:
        print("data Error: ", error)
    except Exception as error:
        print("unexpected error: ", error)


    

def cursor_no_result(cursor, the_procedure, list_of_args=[]):
    cursor.execute(the_procedure, list_of_args)
    



def the_closer(cursor):
    conn=cursor.connection            
    cursor.close()
    conn.close()

def error_result(result):
    match result:
        case mariadb.ProgrammingError:
            print("programming error: ")
            return str('programming error')



def run_statement(statement, list_of_args=[]):
    cursor = just_connect()
    if(cursor == None):
        return "connection error"
    results = cursor_result(cursor, statement, list_of_args)
    the_closer(cursor)
    return results