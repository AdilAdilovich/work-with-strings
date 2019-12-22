#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        text = self.textEdit_text.toPlainText().strip().replace(',', '').replace('.', '')  # получаем наш текст
        if text == "":
            self.textEdit_words.insertPlainText("Нет текста")
        else:

            def ret(i):
                return i[1]
            in_text = text.replace('\n', ' ').split(' ')
            popular_words = [[in_text[0], 1]]
            for index, item in enumerate(in_text):
                bool = False
                if (index == 0):
                    continue
                for elem in popular_words:
                    if elem[0].lower() == item.lower():
                        elem[1] += 1
                        bool = True
                        break
                if(bool == False):
                    popular_words.append([item, 1])
            popular_words.sort(key=lambda i: i[0], reverse=1)
            self.textEdit_words.clear()
            if len(popular_words) > 5:
                for i in range(5):
                    self.textEdit_words.insertPlainText(str(popular_words[i][0]) + " " + str(popular_words[i][1]) + "\n")
            else:
                for item in popular_words:
                    self.textEdit_words.insertPlainText(str(item[0]) + " " + str(item[1]) + "\n")


    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
