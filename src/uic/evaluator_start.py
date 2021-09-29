# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'evaluator_start.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_EvaluatorStart(object):
    def setupUi(self, EvaluatorStart):
        if not EvaluatorStart.objectName():
            EvaluatorStart.setObjectName(u"EvaluatorStart")
        EvaluatorStart.resize(800, 600)
        self.verticalLayout = QVBoxLayout(EvaluatorStart)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.lobby_count = QLCDNumber(EvaluatorStart)
        self.lobby_count.setObjectName(u"lobby_count")
        self.lobby_count.setFrameShape(QFrame.Box)

        self.horizontalLayout.addWidget(self.lobby_count)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.evaluator_start_tab = QTabWidget(EvaluatorStart)
        self.evaluator_start_tab.setObjectName(u"evaluator_start_tab")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.title_label = QLabel(self.tab_1)
        self.title_label.setObjectName(u"title_label")

        self.horizontalLayout_2.addWidget(self.title_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.scenario_text = QTextBrowser(self.tab_1)
        self.scenario_text.setObjectName(u"scenario_text")

        self.verticalLayout_2.addWidget(self.scenario_text)

        self.objectives_group = QGroupBox(self.tab_1)
        self.objectives_group.setObjectName(u"objectives_group")
        self.verticalLayout_3 = QVBoxLayout(self.objectives_group)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout_2.addWidget(self.objectives_group)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.time_edit = QTimeEdit(self.tab_1)
        self.time_edit.setObjectName(u"time_edit")

        self.horizontalLayout_3.addWidget(self.time_edit)

        self.start_timer_button = QPushButton(self.tab_1)
        self.start_timer_button.setObjectName(u"start_timer_button")

        self.horizontalLayout_3.addWidget(self.start_timer_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.terminate_button = QPushButton(self.tab_1)
        self.terminate_button.setObjectName(u"terminate_button")

        self.horizontalLayout_3.addWidget(self.terminate_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.evaluator_start_tab.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.evaluator_start_tab.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.evaluator_start_tab)

        self.time_bar = QProgressBar(EvaluatorStart)
        self.time_bar.setObjectName(u"time_bar")
        self.time_bar.setValue(100)
        self.time_bar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.time_bar)


        self.retranslateUi(EvaluatorStart)

        self.evaluator_start_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EvaluatorStart)
    # setupUi

    def retranslateUi(self, EvaluatorStart):
        EvaluatorStart.setWindowTitle(QCoreApplication.translate("EvaluatorStart", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("EvaluatorStart", u"Scenario", None))
        self.objectives_group.setTitle(QCoreApplication.translate("EvaluatorStart", u"Objectives", None))
        self.start_timer_button.setText(QCoreApplication.translate("EvaluatorStart", u"Start Timer", None))
        self.terminate_button.setText(QCoreApplication.translate("EvaluatorStart", u"Terminate", None))
        self.evaluator_start_tab.setTabText(self.evaluator_start_tab.indexOf(self.tab_1), QCoreApplication.translate("EvaluatorStart", u"Tab 1", None))
        self.evaluator_start_tab.setTabText(self.evaluator_start_tab.indexOf(self.tab_2), QCoreApplication.translate("EvaluatorStart", u"Tab 2", None))
    # retranslateUi

