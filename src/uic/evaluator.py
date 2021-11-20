# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'evaluator.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Evaluator(object):
    def setupUi(self, Evaluator):
        if not Evaluator.objectName():
            Evaluator.setObjectName(u"Evaluator")
        Evaluator.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Evaluator)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 30, 20, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.create_from_start_button = QToolButton(Evaluator)
        self.create_from_start_button.setObjectName(u"create_from_start_button")

        self.horizontalLayout_2.addWidget(self.create_from_start_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scenarios_tree = QTreeView(Evaluator)
        self.scenarios_tree.setObjectName(u"scenarios_tree")
        self.scenarios_tree.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.scenarios_tree)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, -1, 50, -1)
        self.delete_button = QPushButton(Evaluator)
        self.delete_button.setObjectName(u"delete_button")

        self.horizontalLayout.addWidget(self.delete_button)

        self.import_button = QPushButton(Evaluator)
        self.import_button.setObjectName(u"import_button")

        self.horizontalLayout.addWidget(self.import_button)

        self.export_button = QPushButton(Evaluator)
        self.export_button.setObjectName(u"export_button")

        self.horizontalLayout.addWidget(self.export_button)

        self.start_button = QPushButton(Evaluator)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Evaluator)

        QMetaObject.connectSlotsByName(Evaluator)
    # setupUi

    def retranslateUi(self, Evaluator):
        Evaluator.setWindowTitle(QCoreApplication.translate("Evaluator", u"Form", None))
#if QT_CONFIG(statustip)
        self.create_from_start_button.setStatusTip(QCoreApplication.translate("Evaluator", u"Create new scenario", None))
#endif // QT_CONFIG(statustip)
        self.create_from_start_button.setText(QCoreApplication.translate("Evaluator", u"+", None))
#if QT_CONFIG(statustip)
        self.scenarios_tree.setStatusTip(QCoreApplication.translate("Evaluator", u"Scenarios in the database", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.delete_button.setStatusTip(QCoreApplication.translate("Evaluator", u"Delete selected entry", None))
#endif // QT_CONFIG(statustip)
        self.delete_button.setText(QCoreApplication.translate("Evaluator", u"Delete", None))
#if QT_CONFIG(statustip)
        self.import_button.setStatusTip(QCoreApplication.translate("Evaluator", u"Import scenario from file", None))
#endif // QT_CONFIG(statustip)
        self.import_button.setText(QCoreApplication.translate("Evaluator", u"Import", None))
#if QT_CONFIG(statustip)
        self.export_button.setStatusTip(QCoreApplication.translate("Evaluator", u"Export selected scenario to file", None))
#endif // QT_CONFIG(statustip)
        self.export_button.setText(QCoreApplication.translate("Evaluator", u"Export", None))
#if QT_CONFIG(statustip)
        self.start_button.setStatusTip(QCoreApplication.translate("Evaluator", u"Launch selected scenario", None))
#endif // QT_CONFIG(statustip)
        self.start_button.setText(QCoreApplication.translate("Evaluator", u"Start", None))
    # retranslateUi

