import sys
from typing import cast


from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication
from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeLabelResult)

        self.lineInput.installEventFilter(self)

    def changeLabelResult(self):
        text = self.lineInput.text()
        self.labelResult.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            # Tenho certeza que o tipo é KeyPress
            event = cast(QKeyEvent, event)
            text = self.lineInput.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
