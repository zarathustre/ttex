from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from src.uic.evaluator import Ui_Evaluator
from ..lite import Database


class Evaluator(QWidget, Ui_Evaluator):
    def __init__(self):
        super(Evaluator, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()
        

    def init_widgets(self):
        self.delete_button.setEnabled(False)
        self.table_view_handler()


    def assign_widgets(self):
        self.delete_button.clicked.connect(lambda: self.delete_selected_scenario())
        self.scenarios_tree.selectionModel().selectionChanged.connect(lambda: self.on_selection_change())


    def on_selection_change(self):
        selected_item = self.scenarios_tree.selectionModel().selectedRows()
        if selected_item:
            self.delete_button.setEnabled(True)


    def table_view_handler(self):
        scenarios = self.get_all_scenarios()
        
        self.items_model = QStandardItemModel()
        self.items_model.setHorizontalHeaderLabels(['Id', 'Scenario', 'Date'])

        for scenario in scenarios:
            col1 = QStandardItem(str(scenario[0]))
            col2 = QStandardItem(scenario[1])
            col3 = QStandardItem(scenario[2])
            col1.setData(str(scenario[0]))
            col1.setEditable(False)
            col2.setEditable(False)
            col3.setEditable(False)
            col1.setTextAlignment(Qt.AlignHCenter)
            col2.setTextAlignment(Qt.AlignHCenter)
            col3.setTextAlignment(Qt.AlignHCenter)
            self.items_model.appendRow([col1, col2, col3])

        self.scenarios_tree.setModel(self.items_model)
        self.scenarios_tree.setColumnWidth(0, 100)
        self.scenarios_tree.setColumnWidth(2, 150)
        self.scenarios_tree.header().setDefaultAlignment(Qt.AlignHCenter)
        self.scenarios_tree.header().setStretchLastSection(False)
        self.scenarios_tree.header().setSectionResizeMode(1, QHeaderView.Stretch)
        self.scenarios_tree.sortByColumn(2, Qt.DescendingOrder)
        self.scenarios_tree.setCurrentIndex(self.scenarios_tree.rootIndex())
        # self.scenarios_tree.setCurrentIndex(self.items_model.index(0, 0, self.scenarios_tree.rootIndex()))  # select first row


    def get_all_scenarios(self):
        db = Database('scenes.db')
        q = "SELECT id, title, date FROM scenarios"
        scenarios = db.query_db(q)
        return scenarios

    
    def delete_selected_scenario(self):
        db = Database('scenes.db')
        q1 = "DELETE FROM qaw WHERE scenario = ?"
        q2 = "DELETE FROM scenarios WHERE id = ?"
        
        selected_item = self.scenarios_tree.selectionModel().selectedRows()
        if selected_item: 
            id = self.items_model.itemFromIndex(selected_item[0]).data()
            db.query_db(q1, [id])
            db.query_db(q2, [id])
            self.items_model.removeRow(selected_item[0].row()) 