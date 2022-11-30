from PyQt5.QtWidgets import QMessageBox


def CallMessageBox(text : str):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle("ATTACK ALERT")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()