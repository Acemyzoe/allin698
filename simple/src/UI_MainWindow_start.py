from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys, UI_MainWindow, UI_ConnectionSet, UI_Convert, binascii, serial, time, \
    Comm, datetime, threading, re, traceback, serial.tools.list_ports, UI_APDU
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QTextCursor


class ReadAddress(QThread):
    def __init__(self):
        super(ReadAddress, self).__init__()

    def run(self):
        self.strInput = "68 17 00 43 45 AA AA AA AA AA AA 10 DA 5F 05 01 03 40 01 02 00 00 90 0F 16"
        Ports().Prsend(self.strInput)
        self.SA = Comm.SA_add
        if self.SA == '':
            MainWindow.showText('R', ['读地址超时'])
        else:
            print('SA地址', self.SA)
            add = ''
            for i in self.SA:
                add = add + i
            MainWindow.showText('R', ['终端地址为:', add])
            self.add = add
            Comm.SetSA(self.SA)

class Ethernet_configuration(QThread):
    def __init__(self):
        super(Ethernet_configuration, self).__init__()

    def run(self):
        self.strInput_1 = ['06 01 04 45 10 03 00 01 01 02 02 09 04 C0 A8 01 FD 12 22 B8 00',
                           '06 01 13 45 10 04 00 02 06 16 01 09 04 C0 A8 01 09 09 04 FF FF FF 00 09 04 7F 00 00 01 0A 01 30 0A 01 30 00']
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            for i in self.strInput_1:
                reValue = Comm.BuildMessage(i.replace(' ', ''), Comm.SA_add, 'dan')
                print('reValue', reValue)
                if reValue == '0':
                    break
                else:
                    Ports().Prsend(reValue)

class Data_Initialization(QThread):
    def __init__(self):
        super(Data_Initialization, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        # print('Comm.SA_add:', Comm.SA_add, 'type:', type(Comm.SA_add))
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '数据初始化')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)

class Parameter_Initialization(QThread):
    def __init__(self):
        super(Parameter_Initialization, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '参数初始化')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # self.parsing = UI_MessageParsing_start.ParsingMain()
        # self.ui.actionC.triggered.connect(self.parsing.show)

        self.ui.actionA.triggered.connect(self.about)
        self.ui.actionSdf.triggered.connect(self.PrEthernet_configuration)

        self.convert = Convert()
        self.ui.actionDf.triggered.connect(self.convert.show)
        
        self.ui.actionShuju.triggered.connect(self.PrDateIni)
        self.ui.actionCanshu.triggered.connect(self.Prpara)
        
        self.apdu = APUD_send()
        self.ui.actionAPDUzu.triggered.connect(self.apdu.show)
        self.ui.textEdit_2.textChanged.connect(self.move_Cursor)

    def move_Cursor(self):
        self.ui.textEdit_2.moveCursor(QTextCursor.End)

    def statusBarshow(self, message):
        self.ui.statusBar.showMessage(message, 3)

    def PrReadAdd(self):
        self.PRD = ReadAddress()
        self.PRD.start()

    def PrEthernet_configuration(self):
        self.PEC = Ethernet_configuration()
        self.PEC.start()

    def PrDateIni(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.pDI = Data_Initialization()
        self.pDI.start()

    def Prpara(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.para = Parameter_Initialization()
        self.para.start()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '你确认要退出吗?', QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def about(self):
        QMessageBox.about(self, '关于', 'V1.0')

    def clear(self):
        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()

    def add_L(self):
        self.ui.textEdit_2.append(datetime.datetime.now().strftime('%m-%d   %T'))
        self.ui.textEdit_2.append('-----------------------')

    def add_R(self):
        self.ui.textEdit.append(datetime.datetime.now().strftime('%m-%d   %T'))
        self.ui.textEdit.append('-----------------------')

    def showText(self, turn, textlist):
        if turn == 'L':
            for x in textlist:
                self.ui.textEdit_2.append(x)
            self.add_L()
        elif turn == 'R':
            for x in textlist:
                self.ui.textEdit.append(x)
            self.add_R()
        else:
            print('ERROR ON turn')

class Ports():
    def __init__(self):
        self.communication_serial_por = ConnectionSet.ui.comboBox.currentText()
        self.check = ConnectionSet.ui.comboBox_3.currentText()
        self.Baud_rate = int(ConnectionSet.ui.comboBox_2.currentText())
        self.stop_bit = int(ConnectionSet.ui.comboBox_4.currentText())
        self.config_S = self.Communication_serial_port()

    def Prsend(self, strInput):
        self.strInput = strInput
        if self.strInput and self.strInput != '0':
            print('strInput:', self.strInput)
            if self.strInput[2] != ' ':
                self.strInput = Comm.makestr(strInput)
            t = MyThread(self.Send, args=(self.strInput,))
            t.start()
            t.join()
            # print('返回值:', t.get_result())
            if t.get_result() == 'ERROR':
                MainWindow.showText('L', ['无法发送'])
            else:
                Comm.Analysis().start698(t.get_result())
                MainWindow.showText('L', ['发送报文:', strInput, '收到报文:', Comm.makestr(t.get_result())])
        else:
            print('ERROR with strInput', strInput)

    def Send(self, strInput):
        print(self.config_S)
        if self.config_S[2] == '偶':
            self.parity_ = 'E'
        try:
            self.t = serial.Serial(self.config_S[0], self.config_S[1], timeout=0.5, parity=self.parity_,
                                   stopbits=self.config_S[3])
            self.t.write(bytes.fromhex(strInput))
            remessage = Ports.Receive(self)
            self.t.close()
        except:
            remessage = 'ERROR'
            traceback.print_exc(file=open('bug.txt', 'a+'))
        return remessage

    def Receive(self):
        time_start = time.time()
        try:
            while 1:
                time.sleep(1.5)
                num = self.t.inWaiting()
                if num > 25:
                    data = str(binascii.b2a_hex(self.t.read(num)))[2:-1]
                    print('num:', num)
                    print('Received: ', data)
                    break
                time_out = time.time()
                if time_out - time_start > 8:
                    data = 'ERROR'
                    break
            return data
        except:
            pass

    def Communication_serial_port(self):
        return self.communication_serial_por, self.Baud_rate, self.check, self.stop_bit

    def Meter_reading_serial_port(self):
        self.communication_serial_port = ConnectionSet.ui.comboBox_5.currentText()
        self.check = ConnectionSet.ui.comboBox_6.currentText()
        self.Baud_rate = int(ConnectionSet.ui.comboBox_7.currentText())
        self.stop_bit = int(ConnectionSet.ui.comboBox_8.currentText())

    def Prsend_zu(self, strInput):
        self.strInput_zu = strInput
        t = MyThread(self.Send_zu, args=(self.strInput_zu,))
        t.start()
        t.join()

    def Send_zu(self, strInput):
        print(self.config_S)
        if self.config_S[2] == '偶':
            self.parity_ = 'E'
        self.t = serial.Serial(self.config_S[0], self.config_S[1], timeout=0.5, parity=self.parity_,
                               stopbits=self.config_S[3])
        self.t.write(bytes.fromhex(strInput))
        self.t.close()
        MainWindow.showText('L', ['发送报文:', strInput])

class ConnectionSet(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_ConnectionSet.Ui_Dialog()
        self.ui.setupUi(self)
        addItem = self.GetSerialNumber()
        addItem.sort()
        for self.addItem in addItem:
            self.ui.comboBox.addItem(self.addItem)
            self.ui.comboBox_5.addItem(self.addItem)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowStaysOnTopHint)


    def GetSerialNumber(self):
        SerialNumber = []
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            print("The Serial port can't find!")
        else:
            for i in list(port_list):
                print(i[0])
                SerialNumber.append(i[0])
            return SerialNumber

class Convert(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_Convert.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.pushButton_2.clicked.connect(self.strtohex)
        self.ui.pushButton.clicked.connect(self.hextostr)

    def hextostr(self):
        try:
            self.text = self.ui.textEdit.toPlainText()
            self.output = str(binascii.unhexlify(self.text))
            self.ui.textEdit_2.setText(self.output[2:-1])
        except:
            self.ui.textEdit_2.setText('无法解析')

    def strtohex(self):
        self.text = self.ui.textEdit.toPlainText()
        self.output = str(binascii.hexlify(bytes(self.text, encoding='UTF-8')))
        self.ui.textEdit_2.setText(self.output[2:-1])

class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

def GetAPDU(kind, stat):
    f = open('source\\' + kind, 'r', encoding='UTF-8')
    while 1:
        text2 = f.readline()[:-1]
        if text2 == stat:
            while 1:
                text = f.readline()[:-1]
                if text == '':
                    print('Finished...')
                    MainWindow.statusBarshow('下发完成')
                    break
                point = re.findall('#', text)
                try:
                    if point[0] == '#':
                        text = text.split('#')
                        print(text[0])
                        MainWindow.ui.textEdit_2.append(text[0])
                        Ports().Prsend(Comm.BuildMessage(text[1].replace(' ', ''), Comm.SA_add, 'dan'))
                except:
                    print('GetAPDU ERROR')
                    MainWindow.showText('L', ['无法发送(APDU)'])
                    MainWindow.ui.statusBar.showMessage('Failed...', 2)
                    traceback.print_exc(file=open('bug.txt', 'a+'))
                    break
            f.close()
            break
        else:
            continue

class APUD_send(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_APDU.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.pushButton.clicked.connect(self.GetText)

    def GetText(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            self.text = self.ui.textEdit.toPlainText()
            if self.text:
                if self.ui.radioButton_2.isChecked():
                    Ports().Prsend(Comm.BuildMessage(self.text.replace(' ', ''), Comm.SA_add, 'dan'))
                if self.ui.radioButton.isChecked():
                    Ports().Prsend(self.text.replace(' ', ''))


if __name__ == '__main__':
    # try:
        app = QApplication(sys.argv)
        MainWindow = MainWindow()
        ConnectionSet = ConnectionSet()
        action = MainWindow.ui.actionSd
        action.triggered.connect(ConnectionSet.show)
        MainWindow.show()
        sys.exit(app.exec_())
    # except:
    #     traceback.print_exc(file=open('bug.txt', 'a+'))
