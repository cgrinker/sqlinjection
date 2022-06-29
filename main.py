"""

"""

from ast import arg
import sqlite3
import argparse
import sys


parser = argparse.ArgumentParser(prog='SQL Inject')

subparsers = parser.add_subparsers(dest='command', help='sub-command help')

parser_seed = subparsers.add_parser('seed', help='Seed the Database')
parser_get = subparsers.add_parser('get', help='Get Salaries')
parser_set = subparsers.add_parser('set', help='Set a Salary')


parser_get.add_argument("-n", "--name", help="EmployeeName")

conn = sqlite3.connect('salleries.db')


def seed():
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS salaries")
    # Create table
    cur.execute("""create table salaries(name text, salary int);""")

    cur.execute("INSERT INTO salaries VALUES ('TeaVan', 32000)")
    cur.execute("INSERT INTO salaries VALUES ('Arman', 1)")
    cur.execute("INSERT INTO salaries VALUES ('Clark', 128000)")
    conn.commit()

    print("Database Seeded")

def get(name):
    cur = conn.cursor()

    if not name:
       return
    else:
        for row in cur.execute(f"SELECT * FROM salaries where name='{name}'"):
            print(row)


if __name__ == '__main__':
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "set":
        print("Unauthorized!")
        sys.exit(-1)

    if args.command == "seed":
        seed()

    if args.command == "get":
        get(args.name)