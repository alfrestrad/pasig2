# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 681, 201))
        self.groupBox.setObjectName("groupBox")
        self.cmb1 = QtWidgets.QComboBox(self.groupBox)
        self.cmb1.setGeometry(QtCore.QRect(30, 50, 231, 22))
        self.cmb1.setObjectName("cmb1")
        self.lb1 = QtWidgets.QLabel(self.groupBox)
        self.lb1.setGeometry(QtCore.QRect(30, 110, 231, 16))
        self.lb1.setObjectName("lb1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 231, 16))
        self.label_2.setObjectName("label_2")
        self.lb2 = QtWidgets.QLabel(self.groupBox)
        self.lb2.setGeometry(QtCore.QRect(30, 140, 211, 16))
        self.lb2.setObjectName("lb2")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(200, 680, 75, 23))
        self.btn2.setObjectName("btn2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 260, 671, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 470, 671, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(120, 680, 75, 23))
        self.btn1.setObjectName("btn1")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(30, 680, 75, 23))
        self.btn3.setObjectName("btn3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vectorial"))
        self.groupBox.setTitle(_translate("MainWindow", "Entrada de información"))
        self.lb1.setText(_translate("MainWindow", "Sistema de referencia"))
        self.label_2.setText(_translate("MainWindow", "Seleccione shapefile"))
        self.lb2.setText(_translate("MainWindow", "Número de atributos"))
        self.btn2.setText(_translate("MainWindow", "Cancelar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Geoprocesos"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Salida"))
        self.btn1.setText(_translate("MainWindow", "Ayuda"))
        self.btn3.setText(_translate("MainWindow", "Ejecutar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
