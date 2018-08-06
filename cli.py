#!/usr/bin/env python3


from datetime import datetime
import argparse

from expensemanager import Config


def process_tags():
    print("show list of all tags...")

def process_trxn():
    print("add the new transaction....")


def main():
    parser = argparse.ArgumentParser(description="Manage your daily expenses")
    subparsers = parser.add_subparsers(title="Valid sub commands", dest="subcmd", help="Purpose")

    trxn_subparser = subparsers.add_parser("trxn",
                                            description="Add new credit/debit transaction",
                                            help="Add new credit/debit transaction")

    trxn_subparser.add_argument("amount", type=float, help=("Amount transacted. "
                        "A '+'  prefix indicates a credit whereas a '-' "
                        "prefix indicates a debit."))
    trxn_subparser.add_argument("tag",
                        help="Tag your transaction with "
                        " one or more tags like 'groceries', 'fuel' etc. "
                        "separated by white space. If a category doesn't "
                        "already exists, it will be created")
    trxn_subparser.add_argument("-d", "--date", default=datetime.now().date(),
                        type=lambda val: datetime.
                            strptime(val, "%d/%m/%Y").date(),
                        metavar="TRANSACTION_DATE", help=("Date of transaction"
                        ", default is today's date"))
    trxn_subparser.add_argument("-m", "--message", help="Optional short message"
                        " about the transaction")

    tags_subparser = subparsers.add_parser("tags", description="Show all tags", help="Show all tags")

    args = parser.parse_args()
    print(args)

    if args.subcmd == "tags":
        process_tags()
    elif args.subcmd == "trxn":
        process_trxn()


if __name__ == "__main__":
    main()
