import sqlite3
from pathlib import Path



def input_task():
    print('入力してください')


def db_init():
    root_path = Path(__file__).parent

    db_path = root_path / 'sample.db'

    conn = sqlite3.connect(db_path)
    conn.close

def main():
    db_init()
    while True:
        print('1 : 入力する')
        print('2 : タクスを確認する')
        print('3 : 終了する')
        num = int(input())

        if num == 1:
            input_task()
        elif num == 2:
            pass
        elif num == 3:
            exit()


if __name__ == '__main__':
    main()
