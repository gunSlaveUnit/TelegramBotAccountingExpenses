import db


class Expenses:
    def __init__(self):
        pass

    @staticmethod
    def pop_expense(row_id):
        db.client.delete('expenses', row_id)
