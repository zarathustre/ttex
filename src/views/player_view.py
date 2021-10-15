from PySide6.QtWidgets import QWidget
from src.uic.player import Ui_Player


class Player(QWidget, Ui_Player):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)