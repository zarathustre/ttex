from PySide6.QtWidgets import QWidget, QTreeWidgetItem
from src.uic.evaluator import Ui_Evaluator
from ..lite import Database


class Evaluator(QWidget, Ui_Evaluator):
    def __init__(self):
        super(Evaluator, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()


    def init_widgets(self):
        scenarios = self.get_all_scenarios()
        self.scenarios_tree.setHeaderLabels(['Id', 'Scenario'])

        # TODO add functions to query the db and return cleaned data

        for scenario in scenarios:
            row = QTreeWidgetItem(self.scenarios_tree)
            row.setText(0, str(scenario[0]))
            row.setText(1, str(scenario[1]).capitalize())


    def assign_widgets(self):
        pass


    def get_all_scenarios(self):
        db = Database('scenes.db')
        q = "SELECT id, title FROM scenarios"
        scenarios = db.query_db(q, [])
        return scenarios