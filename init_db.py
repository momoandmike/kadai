import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()


def init_db():
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # print(dsn)
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('schema.sql', encoding='utf-8') as f:
        sql = f.read()
    # SQLを実行
    cur.execute(sql)
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる
    conn.close()


def main():
    init_db()


if __name__ == '__main__':
    main()
