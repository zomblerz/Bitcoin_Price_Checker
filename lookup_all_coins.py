import requests
from PyQt5 import QtWidgets
from main_window import Ui_MainWindow  # importing our generated file
from main_window import *
from PyQt5.QtWidgets import QTableWidgetItem
import sys

def request_page():
    r = requests.get('https://api.coinmarketcap.com/v2/ticker/')
    json_val = r.json()
    return json_val

def get_coin_value(id):
    json_val = request_page()
    print(json_val["data"][id]["name"])
    print(json_val["data"][id]["quotes"]["USD"]["price"])

def get_coin_id():
    li = []
    json_val = request_page()
    for x in json_val["data"]:
        li.append(str(json_val["data"][x]["id"]))
    return li



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked) # connecting the clicked signal with btnClicked slot
        json_val = request_page()
        li = get_coin_id()
        num_id = 0
        
        
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(100)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Coin by #rank', 'Price in USD','Market Cap','Change 1 Hour','Change 24 Hours','Change 7 days'))
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        #ALLOWS SORTING WHICH IS GLITCHY
        #self.ui.tableWidget.setSortingEnabled(True)

        row = 0
        for x in li:
            col = 0
            cellinfo = QTableWidgetItem(json_val["data"][x]["name"])
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row,col,cellinfo)
            row += 1
        row = 0
        for x in li:
            col = 1
            cellinfo = QTableWidgetItem("${0:.4f}".format(json_val["data"][x]["quotes"]["USD"]["price"]))
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row,col,cellinfo)
            row += 1
        row = 0
        for x in li:
            col = 2
            cellinfo = QTableWidgetItem("${:,.2f}".format(json_val["data"][x]["quotes"]["USD"]["market_cap"]))
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row,col,cellinfo)
            row += 1
        row = 0
        for x in li:
            col = 3
            cellinfo = QTableWidgetItem(str(json_val["data"][x]["quotes"]["USD"]["percent_change_1h"]))
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row,col,cellinfo)
            i = float(json_val["data"][x]["quotes"]["USD"]["percent_change_1h"])
            if i > 0 and i < .5:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,100,0))
            elif i >= .5 and i<2:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,150,0))
            elif i >= 2:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,255,0))
            elif i == 0:
                pass
            elif i < 0 and i > -1:
                self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(150,0,0))
            elif i <= -1:
                self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(255,0,0))
            row += 1
        row = 0
        for x in li:
            col = 4
            cellinfo = QTableWidgetItem("{}".format(json_val["data"][x]["quotes"]["USD"]["percent_change_24h"]))
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row,col,cellinfo)
            i = float(json_val["data"][x]["quotes"]["USD"]["percent_change_24h"])
            if i > 0 and i < 1:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,100,0))
            elif i >= 1 and i<5:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,150,0))
            elif i >= 5:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,255,0))
            elif i == 0:
                pass
            elif i < 0 and i > -5:
                self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(150,0,0))
            elif i <= -5:
                self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(255,0,0))
            row += 1
        row = 0
        for x in li:
            col = 5
            cellinfo = QTableWidgetItem(str(json_val["data"][x]["quotes"]["USD"]["percent_change_7d"]))
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row,col,cellinfo)
            i = float(json_val["data"][x]["quotes"]["USD"]["percent_change_7d"])
            if i > 0 and i < 1:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,100,0))
            elif i >= 1 and i<10:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,150,0))
            elif i >= 10:
                self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,255,0))
            elif i == 0:
                pass
            elif i < 0 and i > -10:
                self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(150,0,0))
            elif i <= -10:
                self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(255,0,0))
            row += 1
            
            
    def btnClicked(self):
            json_val = request_page()
            li = get_coin_id() 
            row = 0
            for x in li:
                col = 0
                cellinfo = QTableWidgetItem(json_val["data"][x]["name"])
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row,col,cellinfo)
                row += 1
            row = 0
            for x in li:
                col = 1
                cellinfo = QTableWidgetItem("${0:.4f}".format(json_val["data"][x]["quotes"]["USD"]["price"]))
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row,col,cellinfo)
                row += 1
            row = 0
            for x in li:
                col = 2
                cellinfo = QTableWidgetItem("${:,.2f}".format(json_val["data"][x]["quotes"]["USD"]["market_cap"]))
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row,col,cellinfo)
                row += 1
            row = 0
            for x in li:
                col = 3
                cellinfo = QTableWidgetItem(str(json_val["data"][x]["quotes"]["USD"]["percent_change_1h"]))
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row,col,cellinfo)
                i = float(json_val["data"][x]["quotes"]["USD"]["percent_change_1h"])
                if i > 0 and i < .5:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,100,0))
                elif i >= .5 and i<2:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,150,0))
                elif i >= 2:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,255,0))
                elif i == 0:
                    pass
                elif i < 0 and i > -1:
                    self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(150,0,0))
                elif i <= -1:
                    self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(255,0,0))
                row += 1
            row = 0
            for x in li:
                col = 4
                cellinfo = QTableWidgetItem("{}".format(json_val["data"][x]["quotes"]["USD"]["percent_change_24h"]))
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row,col,cellinfo)
                i = float(json_val["data"][x]["quotes"]["USD"]["percent_change_24h"])
                if i > 0 and i < 1:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,100,0))
                elif i >= 1 and i<5:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,150,0))
                elif i >= 5:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,255,0))
                elif i == 0:
                    pass
                elif i < 0 and i > -5:
                    self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(150,0,0))
                elif i <= -5:
                    self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(255,0,0))
                row += 1
            row = 0
            for x in li:
                col = 5
                cellinfo = QTableWidgetItem(str(json_val["data"][x]["quotes"]["USD"]["percent_change_7d"]))
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row,col,cellinfo)
                i = float(json_val["data"][x]["quotes"]["USD"]["percent_change_7d"])
                if i > 0 and i < 1:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,100,0))
                elif i >= 1 and i<10:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,150,0))
                elif i >= 10:
                    self.ui.tableWidget.item(row, col).setBackground(QtGui.QColor(0,255,0))
                elif i == 0:
                    pass
                elif i < 0 and i > -10:
                    self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(150,0,0))
                elif i <= -10:
                    self.ui.tableWidget.item(row,col).setBackground(QtGui.QColor(255,0,0))
                row += 1
            
    def handleActivated(self, index):
        json_val = request_page()
        self.ui.value_label.setText("${0:.4f}".format(json_val["data"][(str(self.ui.comboBox.itemData(index)))]["quotes"]["USD"]["price"]))
        self.ui.pc_1h.setText("{}%".format (json_val["data"][(str(self.ui.comboBox.itemData(index)))]["quotes"]["USD"]["percent_change_1h"]))
        self.ui.pc_24h.setText("{}%".format (json_val["data"][(str(self.ui.comboBox.itemData(index)))]["quotes"]["USD"]["percent_change_24h"]))
        self.ui.pc_7d.setText("{}%".format (json_val["data"][(str(self.ui.comboBox.itemData(index)))]["quotes"]["USD"]["percent_change_7d"]))
        
        
        
def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.setWindowTitle('Crypto Price Checker')
    application.show()
    sys.exit(app.exec())
        
        
if __name__ == "__main__":
    main()
