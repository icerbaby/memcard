#файл с интерфейсом с=меню

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


txt_question = QLineEdit()
txt_answer = QLineEdit()
txt_wrong1 = QLineEdit()
txt_wrong2 = QLineEdit()
txt_wrong3 = QLineEdit()

form_layout = QFormLayout()

form_layout.addRow("встал, вопрос", txt_question)
form_layout.addRow("otvet", txt_answer)
form_layout.addRow("nepravilno 1", txt_wrong1)
form_layout.addRow("nepravilno 2", txt_wrong2)
form_layout.addRow("nepravilno 3", txt_wrong3)