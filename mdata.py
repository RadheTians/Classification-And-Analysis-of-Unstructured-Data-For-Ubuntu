

from PyQt5 import QtCore, QtGui, QtWidgets
import mde
import sys

class Ui_Dialog(object):

    def __init__(self):
        self.taker_Data_Set=[]  
        self.d=0

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(959, 597)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 30, 811, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 51))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 100, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.GetterType)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 100, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.GetterCreate)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 100, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.GetterModify)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(790, 100, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.GetterAccess)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(15, 141, 931, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
	Dialog.setWindowTitle("META-DATA EXTRACTOR")
	Dialog.setWindowIcon(QtGui.QIcon('mde.png'))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">ENTER PATH :</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">SORT ACCORDING :</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "FILE TYPE"))
        self.pushButton_2.setText(_translate("Dialog", "AGE OF FILE"))
        self.pushButton_3.setText(_translate("Dialog", "LAST MODIFIED"))
        self.pushButton_4.setText(_translate("Dialog", "LAST ACCESS"))
    
    def GetterType(self):
        r = -1
        q=1
        self.d=self.d+1

        # for one_set in taker:
        input_set = self.textEdit.toPlainText()
        self.taker_Data_Set = mde.abcd(input_set,q,self.d)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['FILE','FILETYPE','AGE OF FILE','LAST MODIFIED','LAST ACCESS'])	
        header = self.tableWidget.horizontalHeader()       
	header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
	header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        for one_set in self.taker_Data_Set:
         
            r += 1
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[1]))
            self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(one_set[2]))
            self.tableWidget.setItem(r, 3, QtWidgets.QTableWidgetItem(one_set[3]))
            self.tableWidget.setItem(r, 4, QtWidgets.QTableWidgetItem(one_set[4]))
        
        self.tableWidget.setVisible(True)

    def GetterCreate(self):
        r = -1
        q=2
        self.d=self.d+1
     
        input_set = self.textEdit.toPlainText()
        self.taker_Data_Set = mde.abcd(input_set,q,self.d)
        # for one_set in taker:
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
	self.tableWidget.setHorizontalHeaderLabels(['FILE','FILETYPE','AGE OF FILE','LAST MODIFIED','LAST ACCESS'])
	header = self.tableWidget.horizontalHeader()       
	header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
	header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        for one_set in self.taker_Data_Set:
            '''for k, v in one_set.items():
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(k))
            self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(v))
            r+=1
            print(k,"===>>\t\t",v)
            print(one_set)'''
            r += 1
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[1]))
            self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(one_set[2]))
            self.tableWidget.setItem(r, 3, QtWidgets.QTableWidgetItem(one_set[3]))
            self.tableWidget.setItem(r, 4, QtWidgets.QTableWidgetItem(one_set[4]))
           
        self.tableWidget.setVisible(True)

    def GetterModify(self):
        r = -1
        q=3
        self.d=self.d+1
        
        input_set = self.textEdit.toPlainText() 
        self.taker_Data_Set = mde.abcd(input_set,q,self.d)
        # for one_set in taker:
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
	self.tableWidget.setHorizontalHeaderLabels(['FILE','FILETYPE','AGE OF FILE','LAST MODIFIED','LAST ACCESS'])
	header = self.tableWidget.horizontalHeader()       
	header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
	header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        for one_set in self.taker_Data_Set:
            '''for k, v in one_set.items():
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(k))
            self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(v))
            r+=1
            print(k,"===>>\t\t",v)
            print(one_set)'''
            r += 1
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[1]))
            self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(one_set[2]))
            self.tableWidget.setItem(r, 3, QtWidgets.QTableWidgetItem(one_set[3]))
            self.tableWidget.setItem(r, 4, QtWidgets.QTableWidgetItem(one_set[4]))
          
        self.tableWidget.setVisible(True)

    def GetterAccess(self):
        r = -1
        q=4
        self.d=self.d+1

        input_set = self.textEdit.toPlainText()
        self.taker_Data_Set = mde.abcd(input_set,q,self.d)
        # for one_set in taker:
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
	self.tableWidget.setHorizontalHeaderLabels(['FILE','FILETYPE','AGE OF FILE','LAST MODIFIED','LAST ACCESS'])
	header = self.tableWidget.horizontalHeader()       
	header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
	header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
	header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        for one_set in self.taker_Data_Set:
            '''for k, v in one_set.items():
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(k))
            self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(v))
            r+=1
            print(k,"===>>\t\t",v)
            print(one_set)'''
            r += 1
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[1]))
            self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(one_set[2]))
            self.tableWidget.setItem(r, 3, QtWidgets.QTableWidgetItem(one_set[3]))
            self.tableWidget.setItem(r, 4, QtWidgets.QTableWidgetItem(one_set[4]))
       
        self.tableWidget.setVisible(True)
   
def Caller():

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
	Caller()

