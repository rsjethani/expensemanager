#!/usr/bin/env python3


import argparse
import json
from datetime import datetime

def hello():
    print("sffdsfsdf")


def main():
    parser = argparse.ArgumentParser(description="Manage your daily expenses")
    parser.add_argument("amount", type=float, help="Amount transacted. A '+' prefix indicates a credit whereas a '-' prefix indicates a debit. PREFIX IS REQUIRED!")
    parser.add_argument("tags", nargs="+", help="One or more transaction categories like 'groceries', 'petrol' etc. separated by white space. If a category doesn't already exists, it will be created")
    parser.add_argument("-d", "--date", default=datetime.now().date(), type=lambda val: datetime.strptime(val, "%d/%m/%Y").date(), metavar="TRANSACTION_DATE", help="Date of transaction, default is today's date")
    parser.add_argument("-m", "--message", help="Optional short message about the transaction")

    args = parser.parse_args()
    print(args)



if __name__ == "__main__":
    main()