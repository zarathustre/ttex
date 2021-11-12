from PySide6.QtWidgets import QFrame, QLabel, QSizePolicy, QToolButton, QSlider
from PySide6.QtCore import Qt

def add_horizontal_line(parent, layout):
    line = QFrame(parent)
    line.setFrameShape(QFrame.HLine)
    line.setFrameShadow(QFrame.Sunken)
    layout.addWidget(line)

def add_label(parent, layout, text, size_policy=False, object_name=None, return_condition=False):
    label = QLabel(parent)
    if size_policy: 
        add_size_policy(label)
    if object_name: 
        label.setObjectName(object_name)
    label.setText(text)
    label.setWordWrap(True)
    layout.addWidget(label)
    if return_condition:
        return label

def add_size_policy(widget):
    sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
    widget.setSizePolicy(sizePolicy)

def add_tool_button(parent, layout, text, object_name=None, connection=None):
    button = QToolButton(parent)
    if object_name:
        button.setObjectName(object_name)
    if connection:
        button.clicked.connect(connection)
    button.setText(text)
    layout.addWidget(button)

def add_horizontal_slider(parent, layout, object_name=None, return_condition=False):
    slider = QSlider(parent)
    slider.setOrientation(Qt.Horizontal)
    slider.setFixedWidth(100)
    slider.setMinimum(1)
    slider.setMaximum(10)
    slider.setSingleStep(1)
    if object_name:
        slider.setObjectName(object_name)
    layout.addWidget(slider)
    if return_condition:
        return slider