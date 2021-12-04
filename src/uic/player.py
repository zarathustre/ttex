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
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.player_terminate_button = QPushButton(Player)
        self.player_terminate_button.setObjectName(u"player_terminate_button")

        self.horizontalLayout.addWidget(self.player_terminate_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.team_nick_label = QLabel(Player)
        self.team_nick_label.setObjectName(u"team_nick_label")

        self.horizontalLayout.addWidget(self.team_nick_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.player_time_counter = QLCDNumber(Player)
        self.player_time_counter.setObjectName(u"player_time_counter")

        self.horizontalLayout.addWidget(self.player_time_counter)


        self.verticalLayout.addLayout(self.horizontalLayout)

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
#if QT_CONFIG(statustip)
        self.player_terminate_button.setStatusTip(QCoreApplication.translate("Player", u"Terminate the session (all entries will be lost)", None))
#endif // QT_CONFIG(statustip)
        self.player_terminate_button.setText(QCoreApplication.translate("Player", u"Terminate", None))
        self.team_nick_label.setText(QCoreApplication.translate("Player", u"Team ", None))
#if QT_CONFIG(statustip)
        self.player_time_counter.setStatusTip(QCoreApplication.translate("Player", u"Remaining time", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.player_scenario_text.setStatusTip(QCoreApplication.translate("Player", u"Main scenario", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.player_injects_group.setStatusTip(QCoreApplication.translate("Player", u"Injects", None))
#endif // QT_CONFIG(statustip)
        self.player_injects_group.setTitle(QCoreApplication.translate("Player", u"Injects", None))
        self.player_tab.setTabText(self.player_tab.indexOf(self.tab_1), QCoreApplication.translate("Player", u"Scenario", None))
        self.player_questions_group.setTitle(QCoreApplication.translate("Player", u"Questions", None))
        self.player_tab.setTabText(self.player_tab.indexOf(self.tab_2), QCoreApplication.translate("Player", u"Questions", None))
    # retranslateUi

