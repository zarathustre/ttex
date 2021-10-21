# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Player(object):
    def setupUi(self, Player):
        if not Player.objectName():
            Player.setObjectName(u"Player")
        Player.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Player)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.player_tab = QTabWidget(Player)
        self.player_tab.setObjectName(u"player_tab")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.player_scenario_text = QTextBrowser(self.tab_1)
        self.player_scenario_text.setObjectName(u"player_scenario_text")

        self.verticalLayout_2.addWidget(self.player_scenario_text)

        self.player_injects_group = QGroupBox(self.tab_1)
        self.player_injects_group.setObjectName(u"player_injects_group")
        self.verticalLayout_4 = QVBoxLayout(self.player_injects_group)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_2.addWidget(self.player_injects_group)

        self.player_tab.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.player_questions_group = QGroupBox(self.tab_2)
        self.player_questions_group.setObjectName(u"player_questions_group")
        self.verticalLayout_5 = QVBoxLayout(self.player_questions_group)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_3.addWidget(self.player_questions_group)

        self.player_tab.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.player_tab)


        self.retranslateUi(Player)

        self.player_tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Player)
    # setupUi

    def retranslateUi(self, Player):
        Player.setWindowTitle(QCoreApplication.translate("Player", u"Form", None))
        self.player_injects_group.setTitle(QCoreApplication.translate("Player", u"Injects", None))
        self.player_tab.setTabText(self.player_tab.indexOf(self.tab_1), QCoreApplication.translate("Player", u"Tab 1", None))
        self.player_questions_group.setTitle(QCoreApplication.translate("Player", u"Questions", None))
        self.player_tab.setTabText(self.player_tab.indexOf(self.tab_2), QCoreApplication.translate("Player", u"Tab 2", None))
    # retranslateUi

