from collections import UserDict
from datetime import datetime
import uuid


class Transaction:
    _date_fmt = "%d/%m/%Y"

    def __init__(self, amt, tag, desc=None, dot=None):
        self._tag = tag
        self._amount = amt
        self._description = desc
        self._date = dot or datetime.today().strftime(self._date_fmt)
        # if all goes well without exceptions then generate
        # a unique id for the transaction
        self._id = uuid.uuid4()

    @property
    def id(self):
        return self._uuid.hex

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, val):
        self._tag = val

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, val):
        self._amount = float(format(val, ".3f"))

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, val):
        self._date = datetime.strptime(val, "%d/%m/%Y").date()


class Transactions(dict):
    def __delitem__(self, key):
        print("hello")
        del super()[key]
