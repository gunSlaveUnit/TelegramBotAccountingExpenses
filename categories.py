from db import DBClient
from envparser import EnvParser

config = EnvParser.parse()
client = DBClient(database=config['DB_NAME'],
                  user=config['DB_USER'], password=config['DB_PASS'],
                  host=config['DB_HOST'], port=config['DB_PORT'])


class Categories:
    def __init__(self):
        self._categories = self._load_categories()

    def _load_categories(self):
        categories = client.fetchall('*', table='categories')
        return self.arrange_categories_for_conclusion(categories)

    def arrange_categories_for_conclusion(self, cats):
        categories_for_printing = []
        for category in cats:
            categories_for_printing.append(" ".join([str(category[1])+"\: (", str(category[3])+" )"]))
        return categories_for_printing

    @property
    def categories(self):
        return self._categories
