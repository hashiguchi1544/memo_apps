import sqlite3
from pathlib import Path

from colorama import Fore


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


def write_task():
    conn = sqlite3.connect('sample.db')
    task = input('タスクを入力してください\n')

    sql = f'INSERT INTO my_task (task) VALUES (?);'

    conn.execute(sql, (task,))
    conn.commit()

    conn.close()


def read_tasks():
    conn = sqlite3.connect('sample.db')

    sql = 'SELECT id, task FROM my_task;'

    results = conn.execute(sql).fetchall()
    conn.close()
    return results


def delete_task():
    num = int(input('完了した番号を入力指定ください'))
    conn = sqlite3.connect('sample.db')

    sql = f'DELETE FROM my_task WHERE id = ?;'

    conn.execute(sql, (num,))
    conn.commit()
    conn.close()


def delete_db():
    print("本当にDB初期化おk？？ if so push 'q'\n")
    push_key = input()
    if push_key == 'q':
        sql_drop = f"DROP TABLE my_task; "
        sql_crate_table = f"CREATE TABLE 'my_task' ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, " \
                          f"'task' TEXT);"
        conn = sqlite3.connect('sample.db')
        conn.execute(sql_drop)
        conn.execute(sql_crate_table)
        conn.commit()
        conn.close()


def main():
    db_init()
    while True:
        results = read_tasks()
        print(Fore.YELLOW + '--------------------------------------------------')
        for id_int, task in results:
            print(Fore.RESET + f'{id_int}, {task}')

        print(Fore.YELLOW + '--------------------------------------------------')
        print(Fore.MAGENTA + '1:完了しましたぜ  2:タスクを追加する  3:DBを初期化  4:終了する')

        num = input()

        if num == '1':
            delete_task()
        elif num == '2':
            write_task()
        elif num == '3':
            pass
            delete_db()
        elif num == '4':
            exit()
        else:
            continue


if __name__ == '__main__':
    main()
