# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial_banco.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_inicial_banco(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 506)
        Dialog.setStyleSheet("background-color: cyan\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 110, 211, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 70, 141, 41))
        self.label_2.setStyleSheet("label.Visible := not label.Visible ;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 170, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(270, 170, 121, 20))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(216, 210, 51, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 210, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.pushButton.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}\n"
"QPushButton:hover:!pressed {border: 2px solid green;}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 280, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}\n"
"QPushButton:hover:!pressed {border: 2px solid green;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(250, 310, 161, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 330, 75, 23))
        self.pushButton_3.setStyleSheet("QPushButton {background-color: #A3C1DA; color: red;}\n"
"QPushButton:hover:!pressed {border: 2px solid red;}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(250, 140, 151, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 10, 81, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../bank.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#0000ff;\">Bem Vindo :D</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#0000ff;\">IgBank</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">Usu??rio:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#0000ff;\">Senha:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Fazer Login"))
        self.pushButton_2.setText(_translate("Dialog", "Cadastrar-se"))
        self.pushButton_3.setText(_translate("Dialog", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = tela_inicial_banco()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
