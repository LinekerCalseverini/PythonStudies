from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE


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
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            [' ', '0', '.', '=']
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self.__gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if buttonText not in '0123456789.':
                    self.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
