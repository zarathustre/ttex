from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from src.uic.evaluator import Ui_Evaluator
from ..lite import Database


class Evaluator(QWidget, Ui_Evaluator):
    def __init__(self):
        super(Evaluator, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()


    def init_widgets(self):
        self.table_view_handler()


    def assign_widgets(self):
        self.delete_button.clicked.connect(lambda: self.delete_selected_scenario())


    def table_view_handler(self):
        scenarios = self.get_all_scenarios()
        
        self.items_model = QStandardItemModel()
        self.items_model.setHorizontalHeaderLabels(['Id', 'Scenario'])

        for scenario in scenarios:
            col1 = QStandardItem(str(scenario[0]))
            col1.setData(str(scenario[0]))
            col1.setEditable(False)
            col2 = QStandardItem(scenario[1])
            #col2.setData(scenario[1])
            col2.setEditable(False)
            self.items_model.appendRow([col1, col2])

        self.scenarios_tree.setModel(self.items_model)


    def get_all_scenarios(self):
        db = Database('scenes.db')
        q = "SELECT id, title FROM scenarios"
        scenarios = db.query_db(q)
        return scenarios

    
    def delete_selected_scenario(self):
        db = Database('scenes.db')
        q1 = "DELETE FROM qaw WHERE scenario = ?"
        q2 = "DELETE FROM scenarios WHERE id = ?"
        
        selected_item = self.scenarios_tree.selectionModel().selectedRows() 
        id = self.items_model.itemFromIndex(selected_item[0]).data()
        
        db.query_db(q1, [id])
        db.query_db(q2, [id])

        self.items_model.removeRow(selected_item[0].row()) 
