# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_scenario_page.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_create_scenario_page(object):
    def setupUi(self, create_scenario_page):
        if not create_scenario_page.objectName():
            create_scenario_page.setObjectName(u"create_scenario_page")
        create_scenario_page.resize(800, 600)
        self.verticalLayout = QVBoxLayout(create_scenario_page)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.back_button = QPushButton(create_scenario_page)
        self.back_button.setObjectName(u"back_button")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.back_button)

        self.create_scenario_tab = QTabWidget(create_scenario_page)
        self.create_scenario_tab.setObjectName(u"create_scenario_tab")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.formLayout = QFormLayout(self.tab_1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(50)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.title_edit = QLineEdit(self.tab_1)
        self.title_edit.setObjectName(u"title_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.title_edit)

        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.scenario_edit = QTextEdit(self.tab_1)
        self.scenario_edit.setObjectName(u"scenario_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scenario_edit.sizePolicy().hasHeightForWidth())
        self.scenario_edit.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.scenario_edit)

        self.create_scenario_tab.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.objectives_group = QGroupBox(self.tab_2)
        self.objectives_group.setObjectName(u"objectives_group")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.objectives_group.sizePolicy().hasHeightForWidth())
        self.objectives_group.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.objectives_group)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.objectives_edit = QTextEdit(self.objectives_group)
        self.objectives_edit.setObjectName(u"objectives_edit")
        self.objectives_edit.setTabChangesFocus(True)

        self.verticalLayout_3.addWidget(self.objectives_edit)


        self.horizontalLayout_2.addWidget(self.objectives_group)

        self.add_objective_button = QToolButton(self.tab_2)
        self.add_objective_button.setObjectName(u"add_objective_button")

        self.horizontalLayout_2.addWidget(self.add_objective_button)

        self.remove_objetive_button = QToolButton(self.tab_2)
        self.remove_objetive_button.setObjectName(u"remove_objetive_button")

        self.horizontalLayout_2.addWidget(self.remove_objetive_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.injects_group = QGroupBox(self.tab_2)
        self.injects_group.setObjectName(u"injects_group")
        self.verticalLayout_4 = QVBoxLayout(self.injects_group)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.injects_edit = QTextEdit(self.injects_group)
        self.injects_edit.setObjectName(u"injects_edit")
        self.injects_edit.setTabChangesFocus(True)

        self.verticalLayout_4.addWidget(self.injects_edit)


        self.horizontalLayout_3.addWidget(self.injects_group)

        self.add_inject_button = QToolButton(self.tab_2)
        self.add_inject_button.setObjectName(u"add_inject_button")

        self.horizontalLayout_3.addWidget(self.add_inject_button)

        self.remove_inject_button = QToolButton(self.tab_2)
        self.remove_inject_button.setObjectName(u"remove_inject_button")

        self.horizontalLayout_3.addWidget(self.remove_inject_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.create_scenario_tab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.questions_group = QGroupBox(self.tab_3)
        self.questions_group.setObjectName(u"questions_group")
        self.verticalLayout_6 = QVBoxLayout(self.questions_group)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.question_edit = QTextEdit(self.questions_group)
        self.question_edit.setObjectName(u"question_edit")
        sizePolicy1.setHeightForWidth(self.question_edit.sizePolicy().hasHeightForWidth())
        self.question_edit.setSizePolicy(sizePolicy1)
        self.question_edit.setTabChangesFocus(True)

        self.horizontalLayout_6.addWidget(self.question_edit)

        self.question_combo_box = QComboBox(self.questions_group)
        self.question_combo_box.setObjectName(u"question_combo_box")

        self.horizontalLayout_6.addWidget(self.question_combo_box)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_5.addWidget(self.questions_group)

        self.add_question_button = QToolButton(self.tab_3)
        self.add_question_button.setObjectName(u"add_question_button")

        self.horizontalLayout_5.addWidget(self.add_question_button)

        self.remove_question_button = QToolButton(self.tab_3)
        self.remove_question_button.setObjectName(u"remove_question_button")

        self.horizontalLayout_5.addWidget(self.remove_question_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.answers_group = QGroupBox(self.tab_3)
        self.answers_group.setObjectName(u"answers_group")
        self.verticalLayout_7 = QVBoxLayout(self.answers_group)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.answer_edit = QTextEdit(self.answers_group)
        self.answer_edit.setObjectName(u"answer_edit")
        sizePolicy1.setHeightForWidth(self.answer_edit.sizePolicy().hasHeightForWidth())
        self.answer_edit.setSizePolicy(sizePolicy1)
        self.answer_edit.setMinimumSize(QSize(0, 0))
        self.answer_edit.setTabChangesFocus(True)

        self.verticalLayout_7.addWidget(self.answer_edit)


        self.horizontalLayout_4.addWidget(self.answers_group)

        self.add_answer_button = QToolButton(self.tab_3)
        self.add_answer_button.setObjectName(u"add_answer_button")

        self.horizontalLayout_4.addWidget(self.add_answer_button)

        self.remove_answer_button = QToolButton(self.tab_3)
        self.remove_answer_button.setObjectName(u"remove_answer_button")

        self.horizontalLayout_4.addWidget(self.remove_answer_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.create_scenario_tab.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.create_scenario_tab)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 20, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.clear_button = QPushButton(create_scenario_page)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout.addWidget(self.clear_button)

        self.next_button = QPushButton(create_scenario_page)
        self.next_button.setObjectName(u"next_button")
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.next_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(create_scenario_page)

        self.create_scenario_tab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(create_scenario_page)
    # setupUi

    def retranslateUi(self, create_scenario_page):
        create_scenario_page.setWindowTitle(QCoreApplication.translate("create_scenario_page", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("create_scenario_page", u"Back", None))
        self.label.setText(QCoreApplication.translate("create_scenario_page", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("create_scenario_page", u"Scenario", None))
        self.create_scenario_tab.setTabText(self.create_scenario_tab.indexOf(self.tab_1), QCoreApplication.translate("create_scenario_page", u"Tab 1", None))
        self.objectives_group.setTitle(QCoreApplication.translate("create_scenario_page", u"Objectives", None))
        self.add_objective_button.setText(QCoreApplication.translate("create_scenario_page", u"+", None))
        self.remove_objetive_button.setText(QCoreApplication.translate("create_scenario_page", u"-", None))
        self.injects_group.setTitle(QCoreApplication.translate("create_scenario_page", u"Injects", None))
        self.add_inject_button.setText(QCoreApplication.translate("create_scenario_page", u"+", None))
        self.remove_inject_button.setText(QCoreApplication.translate("create_scenario_page", u"-", None))
        self.create_scenario_tab.setTabText(self.create_scenario_tab.indexOf(self.tab_2), QCoreApplication.translate("create_scenario_page", u"Tab 2", None))
        self.questions_group.setTitle(QCoreApplication.translate("create_scenario_page", u"Questions", None))
        self.add_question_button.setText(QCoreApplication.translate("create_scenario_page", u"+", None))
        self.remove_question_button.setText(QCoreApplication.translate("create_scenario_page", u"-", None))
        self.answers_group.setTitle(QCoreApplication.translate("create_scenario_page", u"Answers", None))
        self.add_answer_button.setText(QCoreApplication.translate("create_scenario_page", u"+", None))
        self.remove_answer_button.setText(QCoreApplication.translate("create_scenario_page", u"-", None))
        self.create_scenario_tab.setTabText(self.create_scenario_tab.indexOf(self.tab_3), QCoreApplication.translate("create_scenario_page", u"Tab 3", None))
        self.clear_button.setText(QCoreApplication.translate("create_scenario_page", u"Clear", None))
        self.next_button.setText(QCoreApplication.translate("create_scenario_page", u"Next", None))
    # retranslateUi

