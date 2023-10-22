#файл где создали подокна меню и основа програми

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from kak_xotite import form_layout
from main_layout import main_layout

wdgt_main = QWidget()
wdgt_menu = QWidget()

wdgt_main.setLayout(main_layout)
wdgt_menu.setLayout(form_layout)

layout_main = QVBoxLayout()
layout_main.addWidget(wdgt_main)
layout_main.addWidget(wdgt_menu)