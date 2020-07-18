from learnbot_dsl.learnbotCode.Highlighter import *
from enum import Enum, auto
from PySide2 import QtWidgets

MESSAGE_STYLE = '''
font-weight: bold;
'''

POSITION_STYLE = '''
font-style: italic;
'''

SNIPPET_STYLE = '''
font-family: Courier, monospace;
color: white;
'''

class Severity(Enum):
    ERROR = auto()
    INFO = auto()

class Notification(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.vLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.vLayout)

        self.summaryLayout = QtWidgets.QHBoxLayout()
        self.vLayout.addLayout(self.summaryLayout)

        self.icon = QtWidgets.QLabel()
        self.icon.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        self.summaryLayout.addWidget(self.icon)

        self.message = QtWidgets.QLabel()
        self.message.setWordWrap(True)
        self.message.setStyleSheet(MESSAGE_STYLE)
        self.summaryLayout.addWidget(self.message)

        self.position = QtWidgets.QLabel()
        self.position.setStyleSheet(POSITION_STYLE)
        self.vLayout.addWidget(self.position)

        self.snippet = QtWidgets.QTextEdit()
        self.snippet.setReadOnly(True)
        self.snippet.setStyleSheet(SNIPPET_STYLE)
        p = self.snippet.palette()
        p.setColor(self.snippet.viewport().backgroundRole(), QtGui.QColor(51, 51, 51, 255))
        self.snippet.setPalette(p)
        self.vLayout.addWidget(self.snippet)

        self.highlighter = Highlighter(self.snippet)

    def setSeverity(self, severity):
        if severity == Severity.ERROR:
            icon = QtGui.QIcon.fromTheme('dialog-error')
        elif severity == Severity.INFO:
            icon = QtGui.QIcon.fromTheme('dialog-info')

        self.icon.setPixmap(icon.pixmap(QtCore.QSize(16, 16)))

    def setMessage(self, message):
        self.message.setText(message)

    def setPosition(self, start, end = None):
        if end:
            params = (start[0], start[1], end[0], end[1])
            position = 'at %s:%s—%s:%s' % params
        else:
            params = (start[0], start[1])
            position = 'at %s:%s' % params

        self.position.setText(position)

    def setSnippet(self, snippet):
        self.snippet.setText(snippet)