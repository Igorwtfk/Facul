# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_transf.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_transf(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 500)
        Dialog.setStyleSheet("background-color: cyan")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 80, 161, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 160, 141, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 130, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 220, 75, 23))
        self.pushButton.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}\n"
"QPushButton:hover:!pressed {border: 3px solid green;}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 130, 131, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 160, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}\n"
"QPushButton:hover:!pressed {border: 3px solid yellow;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(277, 250, 141, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 190, 51, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 190, 121, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#0000ff;\">TRANSFERÊNCIA</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">VALOR TRANSFERÊNCIA:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Transferir"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">CONTA A TRANSFERIR:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Voltar"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">SENHA:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = tela_transf()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
