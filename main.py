import sqlite3
from pathlib import Path


def db_init():
    root_path = Path(__file__).parent

    db_path = root_path / 'sample.db'
    sql = f"CREATE TABLE 'my_task' ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'task' TEXT);"
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(sql)
    except sqlite3.OperationalError:
        pass
    else:
        conn.commit()
    finally:
        conn.close()
        return db_path


def write_task(db_path):
    conn = sqlite3.connect(db_path)
    task = input('\nタスクを入力してください\n')

    sql = f'INSERT INTO my_task (task) VALUES (?);'

    conn.execute(sql, (task,))
    conn.commit()

    conn.close()


def read_tasks(db_path):
    conn = sqlite3.connect(db_path)

    sql = 'SELECT id, task FROM my_task;'

    results = conn.execute(sql).fetchall()
    conn.close()
    return results


def delete_task(db_path):
    num = int(input('完了した番号を入力指定ください\n'))
    conn = sqlite3.connect(db_path)

    sql = f'DELETE FROM my_task WHERE id = ?;'

    conn.execute(sql, (num,))
    conn.commit()
    conn.close()


def delete_db(db_path):
    print("\n本当にDB初期化おk？？ if so push 'q'")
    push_key = input()
    if push_key == 'q':
        sql_drop = f"DROP TABLE my_task; "
        sql_crate_table = f"CREATE TABLE 'my_task' ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, " \
                          f"'task' TEXT);"
        conn = sqlite3.connect(db_path)
        conn.execute(sql_drop)
        conn.execute(sql_crate_table)
        conn.commit()
        conn.close()


def main():
    db_path = db_init()
    while True:
        results = read_tasks(db_path)
        print('--------------------------------------------------')
        for id_int, task in results:
            print(f'{id_int}, {task}')

        print('--------------------------------------------------')
        print('1:完了しましたぜ  2:タスクを追加する  3:DBを初期化  4:終了する')

        num = input()

        if num == '1':
            delete_task(db_path)
        elif num == '2':
            write_task(db_path)
        elif num == '3':
            pass
            delete_db(db_path)
        elif num == '4':
            exit()
        else:
            continue


if __name__ == '__main__':
    main()
