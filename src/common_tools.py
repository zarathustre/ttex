from PySide6.QtWidgets import QFrame, QLabel, QSizePolicy, QToolButton, QWidget, QSpinBox
from PySide6.QtCore import QRect

def add_horizontal_line(parent, layout):
    line = QFrame(parent)
    line.setFrameShape(QFrame.HLine)
    line.setFrameShadow(QFrame.Sunken)
    layout.addWidget(line)

def add_label(parent, layout, text, size_policy=False, object_name=None):
    label = QLabel(parent)
    if size_policy: 
        add_size_policy(label)
    if object_name: 
        label.setObjectName(object_name)
    label.setText(text)
    label.setWordWrap(True)
    layout.addWidget(label)

def add_size_policy(widget):
    sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
    widget.setSizePolicy(sizePolicy)

def add_tool_button(parent, layout, text, object_name=None, connection=None, return_value=False):
    button = QToolButton(parent)
    if object_name:
        button.setObjectName(object_name)
    if connection:
        button.clicked.connect(connection)
    button.setText(text)
    layout.addWidget(button)
    if return_value:
        return button

def add_tool_box_page(parent, title, object_name):
    page = QWidget()
    page.setObjectName(object_name)
    page.setGeometry(QRect(0, 0, 738, 350))
    parent.addItem(page, title)

def add_spin_box(parent, layout, object_name=None):
    spin_box = QSpinBox(parent)
    spin_box.setMinimum(1)
    spin_box.setMaximum(10)
    if object_name:
        spin_box.setObjectName(object_name)
    layout.addWidget(spin_box)
