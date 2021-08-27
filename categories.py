import db


class Categories:
    def __init__(self):
        self._categories = self._load_categories()

    def _load_categories(self):
        categories = db.client.fetchall('*', table='categories')
        return self.arrange_categories_for_conclusion(categories)

    def arrange_categories_for_conclusion(self, cats):
        categories_for_printing = []
        for category in cats:
            categories_for_printing.append(" ".join([str(category[1])+"\: (", str(category[3])+" )"]))
        return categories_for_printing

    @property
    def categories(self):
        return self._categories
