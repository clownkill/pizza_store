import sqlite3 as sq

from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    SQL = '''
    CREATE TABLE IF NOT EXISTS menu (
        img TEXT,
        name TEXT PRIMARY KEY,
        description TEXT,
        price TEXT
    )
    '''
    base.execute(SQL)
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute(
            'INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values())
        )
        base.commit()


async def sql_read_menu(message):
    for pizza in cur.execute("SELECT * FROM menu").fetchall():
        await bot.send_photo(
            message.from_user.id,
            pizza[0],
            f"{pizza[1]}\nОписание: {pizza[2]}\nЦена: {pizza[-1]}",
        )