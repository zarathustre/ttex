from PySide6.QtWidgets import QWidget, QHeaderView, QFileDialog
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
        self.set_buttons_enabled(False)
        self.table_view_handler()

    def assign_widgets(self):
        self.scenarios_tree.selectionModel().selectionChanged.connect(self.on_selection_change)
        self.delete_button.clicked.connect(self.delete_selected_scenario)
        self.export_button.clicked.connect(self.export_to_json)
        self.import_button.clicked.connect(self.import_from_json)

    def on_selection_change(self):
        selected_item = self.scenarios_tree.selectionModel().selectedRows()
        if selected_item:
            self.set_buttons_enabled(True)

    def set_buttons_enabled(self, condition):
        self.delete_button.setEnabled(condition)
        self.export_button.setEnabled(condition)
        self.start_button.setEnabled(condition)

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

    def get_all_scenarios(self):
        db = Database('scenes.db')
        q = "SELECT id, title, date FROM scenarios"
        return db.query_db(q)

    def delete_selected_scenario(self):
        selected_item = self.scenarios_tree.selectionModel().selectedRows()
        if selected_item: 
            db = Database('scenes.db')
            id = self.items_model.itemFromIndex(selected_item[0]).data()
            q1 = "DELETE FROM qaw WHERE scenario = ?"
            q2 = "DELETE FROM scenarios WHERE id = ?"
            db.query_db(q1, [id])
            db.query_db(q2, [id])
            self.items_model.removeRow(selected_item[0].row()) 

    def get_selected_id(self):
        selected_item = self.scenarios_tree.selectionModel().selectedRows()
        if selected_item: 
            return self.items_model.itemFromIndex(selected_item[0]).data()

        return None

    def get_from_db(self):
        id = self.get_selected_id()
        if id:
            db = Database('scenes.db')
            scenarios_q = "SELECT * FROM scenarios WHERE id = ?"
            qaw_q = "SELECT question, answer, weight FROM qaw WHERE scenario = ?"

            scenarios_r = db.query_db(scenarios_q, [id])[0]
            objectives = [o for o in scenarios_r[3:8] if o is not None]
            injects = [i for i in scenarios_r[8:13] if i is not None]

            qaw_r = db.query_db(qaw_q, [id])

            return {
                'id': scenarios_r[0],
                'date': scenarios_r[-1],
                'title': scenarios_r[1].capitalize(),
                'scenario': scenarios_r[2],
                'objectives': objectives,
                'injects': injects,
                'qaw': qaw_r 
            }

        return None

    def export_to_json(self):
        result = self.get_from_db()

        if result:
            for i, qaw in enumerate(result['qaw']):
                result['Question ' + str(i+1)] = '(Weight: ' + str(qaw[2]) + ') - ' + qaw[0]
                result['Answer ' + str(i+1)] = qaw[1]

            del result['qaw']

            folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
            file_path = folder_path + f"/{result['title']}.json"

            result = {k.capitalize(): v for k,v in result.items()}

            with open(file_path, 'w') as f:
                json.dump(result, f, indent=4)

    def import_from_json(self):
        file_path = QFileDialog.getOpenFileName(self, 'Select File', filter='*.json')
        
        with open(file_path[0], 'r') as f:
            data = json.load(f)

        print(data)