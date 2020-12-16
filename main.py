import sqlite3
from pathlib import Path

from colorama import Fore


def db_init():
    root_path = Path(__file__).parent

    db_path = root_path / 'sample.db'

    conn = sqlite3.connect(db_path)
    conn.close()


def write_task():
    conn = sqlite3.connect('sample.db')
    task = input('タスクを入力してください')

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


def main():
    db_init()
    while True:
        results = read_tasks()
        print(Fore.YELLOW + '--------------------------------------------------')
        for id_int, task in results:
            print(Fore.RESET + f'{id_int}, {task}')

        print(Fore.YELLOW + '--------------------------------------------------')
        print(Fore.CYAN + '1:完了しましたぜ  2:タスクを追加する  3:終了する')

        num = int(input())

        if num == 1:
            delete_task()
        elif num == 2:
            write_task()
        elif num == 3:
            exit()


if __name__ == '__main__':
    main()
