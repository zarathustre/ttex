# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_scenario_page.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_StartScenario(object):
    def setupUi(self, StartScenario):
        if not StartScenario.objectName():
            StartScenario.setObjectName(u"StartScenario")
        StartScenario.resize(800, 600)
        self.verticalLayout = QVBoxLayout(StartScenario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_button = QPushButton(StartScenario)
        self.back_button.setObjectName(u"back_button")

        self.horizontalLayout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.start_stack = QStackedWidget(StartScenario)
        self.start_stack.setObjectName(u"start_stack")
        self.role_page = QWidget()
        self.role_page.setObjectName(u"role_page")
        self.gridLayout = QGridLayout(self.role_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(50)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.player_button = QPushButton(self.role_page)
        self.player_button.setObjectName(u"player_button")

        self.gridLayout.addWidget(self.player_button, 4, 1, 1, 1)

        self.evaluator_button = QPushButton(self.role_page)
        self.evaluator_button.setObjectName(u"evaluator_button")

        self.gridLayout.addWidget(self.evaluator_button, 3, 1, 1, 1)

        self.label = QLabel(self.role_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.start_stack.addWidget(self.role_page)

        self.verticalLayout.addWidget(self.start_stack)


        self.retranslateUi(StartScenario)

        QMetaObject.connectSlotsByName(StartScenario)
    # setupUi

    def retranslateUi(self, StartScenario):
        StartScenario.setWindowTitle(QCoreApplication.translate("StartScenario", u"Form", None))
#if QT_CONFIG(statustip)
        self.back_button.setStatusTip(QCoreApplication.translate("StartScenario", u"Go back", None))
#endif // QT_CONFIG(statustip)
        self.back_button.setText(QCoreApplication.translate("StartScenario", u"Back", None))
#if QT_CONFIG(statustip)
        self.player_button.setStatusTip(QCoreApplication.translate("StartScenario", u"Launch a player session (there must be at least 1 evaluator before you can join)", None))
#endif // QT_CONFIG(statustip)
        self.player_button.setText(QCoreApplication.translate("StartScenario", u"Player", None))
#if QT_CONFIG(statustip)
        self.evaluator_button.setStatusTip(QCoreApplication.translate("StartScenario", u"Launch an evaluator session to host a scenario (players can then join this room to participate)", None))
#endif // QT_CONFIG(statustip)
        self.evaluator_button.setText(QCoreApplication.translate("StartScenario", u"Evaluator", None))
        self.label.setText(QCoreApplication.translate("StartScenario", u"Pick your role", None))
    # retranslateUi

