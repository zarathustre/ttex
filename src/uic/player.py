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
        self.temp_label = QLabel(Player)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setGeometry(QRect(250, 220, 341, 20))
        self.player_time_bar = QProgressBar(Player)
        self.player_time_bar.setObjectName(u"player_time_bar")
        self.player_time_bar.setGeometry(QRect(100, 380, 591, 23))
        self.player_time_bar.setValue(24)

        self.retranslateUi(Player)

        QMetaObject.connectSlotsByName(Player)
    # setupUi

    def retranslateUi(self, Player):
        Player.setWindowTitle(QCoreApplication.translate("Player", u"Form", None))
        self.temp_label.setText(QCoreApplication.translate("Player", u"TextLabel", None))
    # retranslateUi

