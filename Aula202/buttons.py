from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty
from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            [' ', '0', '.', '=']
        ]

        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self.__gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    self.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button
                )
                button.clicked.connect(buttonSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, checked, button):
        buttonText = button.text()
        self.display.insert(buttonText)
