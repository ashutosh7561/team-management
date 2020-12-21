import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from PyQt5 import QtCore, QtGui, uic


class BuddyLabel(QLabel):
    def __init__(self, buddy, parent=None):
        super(BuddyLabel, self).__init__(parent)
        self.buddy = buddy

    def mouseDoubleClickEvent(self, event):
        self.hide()
        self.buddy.show()
        self.buddy.setFocus()


class CustWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            "C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\view\\users_table_entry_template.ui",
            self,
        )
        self.username.putText("dummy_name")
        self.user_id.putText("dummy_user_id")
        self.user_post.putText("dummy_user_post")
        self.user_special_rights.putText("dummy_special_rights")
        self.user_other_data.putText("dummy_other_data")


class CustLabel(QWidget):
    def __init__(self, parent=None):
        super(CustLabel, self).__init__(parent)

        # Create ui
        self.myEdit = QLineEdit()
        self.myEdit.hide()  # Hide line edit
        self.myEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.myEdit.editingFinished.connect(self.textEdited)
        self.myLabel = BuddyLabel(
            self.myEdit
        )  # Create our custom label, and assign myEdit as its buddy
        # self.myLabel.setText("Nothing has been entered")
        self.myEdit.setText(self.myLabel.text())
        self.myLabel.setSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed
        )  # Change vertical size policy so they both match and you don't get popping when switching

        # Put them under a layout together
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.myLabel)
        hLayout.addWidget(self.myEdit)

        self.setFocus()  # By default this line edit may have focus and the place holder won't show up on load, so focus on the widget

        self.setLayout(hLayout)

        self.callback = self.empty_callback

    def empty_callback(self, *args):
        print("empty callback")
        pass

    def textEdited(self):
        print("edit text")
        self.myLabel.setText(self.myEdit.text())
        # If the input is left empty, revert back to the label showing
        if not self.myEdit.text():
            self.myLabel.setText("Nothing has been entered")

        # hide() triggers editingFinished causing double callback
        # blocking signals stops this
        self.myEdit.blockSignals(True)
        self.myEdit.hide()
        self.myEdit.blockSignals(False)
        self.myLabel.show()
        self.callback(self)

    def mousePressEvent(self, event):
        self.myEdit.hide()
        self.myLabel.setText(self.myEdit.text())
        if not self.myEdit.text() or not self.myLabel.text():
            self.myLabel.setText("Nothing has been entered")
        self.myLabel.show()

    def putText(self, label_text):
        self.myLabel.setText(label_text)
        self.myEdit.setText(label_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustWidget()
    window.show()
    sys.exit(app.exec_())