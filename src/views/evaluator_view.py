from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from src.uic.evaluator import Ui_Evaluator
from ..lite import Database
import json


class Evaluator(QWidget, Ui_Evaluator):
    def __init__(self):
        super(Evaluator, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()
        

    def init_widgets(self):
        self.delete_button.setEnabled(False)
        self.export_button.setEnabled(False)
        self.table_view_handler()


    def assign_widgets(self):
        self.scenarios_tree.selectionModel().selectionChanged.connect(lambda: self.on_selection_change())
        self.delete_button.clicked.connect(lambda: self.delete_selected_scenario())
        self.export_button.clicked.connect(lambda: self.export_to_file())


    def on_selection_change(self):
        selected_item = self.scenarios_tree.selectionModel().selectedRows()
        if selected_item:
            self.delete_button.setEnabled(True)
            self.export_button.setEnabled(True)


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


    def export_to_file(self):
        db = Database('scenes.db')
        scenarios_q = "SELECT * FROM scenarios WHERE id = ?"
        qaw_q = "SELECT question, answer, weight FROM qaw WHERE scenario = ?"
        
        selected_item = self.scenarios_tree.selectionModel().selectedRows()
        if selected_item: 
            id = self.items_model.itemFromIndex(selected_item[0]).data()

            scenarios_r = db.query_db(scenarios_q, [id])[0]
            objectives = [o for o in scenarios_r[3:8] if o is not None]
            injects = [i for i in scenarios_r[8:13] if i is not None]

            qaw_r = db.query_db(qaw_q, [id])
            
            dict = {
                'Id': scenarios_r[0],
                'Date created': scenarios_r[-1],
                'Title': scenarios_r[1].capitalize(),
                'Scenario': scenarios_r[2],
                'Objectives': objectives,
                'Injects': injects,
            }

            i = 0
            for qaw in qaw_r:
                dict['Question ' + str(i+1)] = '(Weight: ' + str(qaw[2]) + ') - ' + qaw[0]
                dict['Answer ' + str(i+1)] = qaw[1]
                i += 1

            # for k,v in dict.items():
            #     print(k + ': ' + str(v))

            # TODO file chooser + set file name to scenario title
            # TODO export to txt, import from file

            with open('export.json', 'w') as f:
                json.dump(dict, f, indent=4)    