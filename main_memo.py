#файл запуска

from main_layout import *
from main_data import *
from memo_windows import *
from kak_xotite import *

from random import choice, shuffle

ans_buttons = [ans1_button, ans2_button, ans3_button, ans4_button]
shuffle(ans_buttons)

q1 = Form("ВОПРОС 1", "1", "2", "3", "4")
q2 = Form("ВОПРОС 2", "2", "1", "3", "4")
q3 = Form("ВОПРОС 3", "3", "2", "1", "4")
q4 = Form("ВОПРОС 4", "4", "2", "3", "1")
q5 = Form("ВОПРОС 5", "2", "1", "3", "4")

questions = [q1, q2, q3, q4, q5]

def random_answer():
    global frm_card
    cur_q = choice(questions)
    frm_card = FormView(cur_q, question_label, ans_buttons[0], ans_buttons[1], ans_buttons[2], ans_buttons[3])
    frm_card.show()

def add_question_func():
    new_q = Form(
        txt_question.text(),
        txt_answer.text(),
        txt_wrong1.text(),
        txt_wrong2.text(),
        txt_wrong3.text(),
    )

    questions.append(new_q)
    txt_question.clear()
    txt_answer.clear()
    txt_wrong1.clear()
    txt_wrong2.clear()
    txt_wrong3.clear()

def clear_inputs_func():
    txt_question.clear()
    txt_answer.clear()
    txt_wrong1.clear()
    txt_wrong2.clear()
    txt_wrong3.clear()




showQuestion()
random_answer()

def check_result():
    if ans_button.text() == "otvetit":
        correct = frm_card.answer_W.isChecked()
        incorrect = frm_card.wrong_answer1_W.isChecked() or frm_card.wrong_answer2_W.isChecked() or frm_card.wrong_answer3_W.isChecked()

        if correct:
            print("pravilno!")
            showAnswer()
        
        if incorrect:
            print("nepravilno!")
            showAnswer()
    
    else:
        showQuestion()
        random_answer()

def show_menu():
    wdgt_main.hide()
    wdgt_menu.show()
    
def show_main():
    wdgt_menu.hide()
    wdgt_main.show()

menu_button.clicked.connect(show_menu)
main_button.clicked.connect(show_main)

        
main_window = QWidget()
main_window.resize(800, 600)

ans_button.clicked.connect(check_result)
add_question.clicked.connect(add_question_func)
clear_button.clicked.connect(clear_inputs_func)

main_window.setLayout(layout_main)
show_main()
main_window.show()
app.exec()