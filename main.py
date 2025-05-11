import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.strings = []
        self.initUI()

    def initUI(self):
        
        layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("message")
        layout.addWidget(self.input_field)

        self.button = QPushButton('Put', self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        self.output_label = QLabel('', self)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

        self.setWindowTitle('Window by PyQt6')
        self.setGeometry(100, 100, 300, 200)

    def on_button_click(self):
        input_text = self.input_field.text()
        self.strings.append(input_text)
        text = ''
        for i in self.strings:
            text += f'{i}\n'

        self.output_label.setText(text)

app = QApplication(sys.argv)
ex = MyApp()
ex.show()
sys.exit(app.exec())