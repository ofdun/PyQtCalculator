import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Calculator')
        self.setGeometry(300, 300, 300, 300)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.result_label = QLabel('0')
        self.result_label.setAlignment(Qt.AlignRight)
        grid.addWidget(self.result_label, 0, 0, 1, 4)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        row = 1
        for button_row in buttons:
            col = 0
            for button in button_row:
                button = QPushButton(button)
                button.clicked.connect(self.buttonClicked)
                grid.addWidget(button, row, col, 1, 1)
                col += 1
            row += 1

        self.show()

    def buttonClicked(self):
        button = self.sender()
        if button.text() == '=':
            result = str(eval(self.result_label.text()))
            self.result_label.setText(result)
        elif button.text() == 'C':
            self.result_label.setText('0')
        else:
            if self.result_label.text() == '0':
                self.result_label.setText(button.text())
            else:
                self.result_label.setText(
                    self.result_label.text() + button.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())
