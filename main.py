from PyQt5.QtWidgets import QApplication
from screens.connect import ConnectUi

app = QApplication([])
widget = ConnectUi()
widget.show()
app.exec_()