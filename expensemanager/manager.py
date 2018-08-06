
import tags
import transactions as trxn

class Manager:

    def add_trxn(self, trxn):
        tags.all_tags[trxn.tag] += 1
        pass

    def remove_trxn(self, trxn_id):
        tags.all_tags[trxn.tag] += 1
        pass

