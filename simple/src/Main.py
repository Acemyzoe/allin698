from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys, UI_MainWindow, UI_ConnectionSet, threading, datetime, serial, serial.tools.list_ports, binascii, \
    time, Comm, queue, UI_APDU, Offline, re
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox
from PyQt5.QtCore import Qt, pyqtSignal,QObject
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    stat_bar = pyqtSignal(str)
    show_text = pyqtSignal(list)
    warm_ = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionA.triggered.connect(self.about)
        self.ui.textEdit_2.textChanged.connect(self.move_Cursor)
        self.control_link()
        self.config = config()
        self.ui.actionSd.triggered.connect(self.config.show)
        self.ui.lineEdit.textChanged.connect(self.showmenu_bar)
        self.apdu = APUD_send()
        self.ui.actionAPDUzu.triggered.connect(self.apdu.show)
        self.setWindowIcon(QIcon('engineering.ico'))
        self.ui.action.triggered.connect(self.close)
        self.warm_.connect(self.warm)

        self.stat_bar.connect(self.statusBarshow)
        self.show_text.connect(self.showText)

        self.port_ = port(self.config.return_port())

        self.off = Offline.check(q,self.port_)
        self.ui.actionSdf.triggered.connect(self.off.show)
        self.ui.actionstop.setDisabled(1)

    def control(self):
        name = self.sender().text()
        print('name', name)
        f = open('Data\\Default', 'r', encoding='UTF-8')
        while 1:
            dic = {}
            text2 = f.readline()[:-1]
            if text2 == name:
                while 1:
                    text = f.readline()[:-1]
                    if text == '':
                        print('Finished...')
                        break
                    else:
                        text = text.split('#')
                        dic[text[0]] = text[1]
                f.close()
                print('dic', dic)
                self.port_.write_list(list(dic.items()))
                break
            else:
                continue

    def move_Cursor(self):
        self.ui.textEdit_2.moveCursor(QTextCursor.End)

    def statusBarshow(self, message):
        self.ui.statusBar.showMessage(message, 0)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '??????', '??????????????????????', QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()

    def about(self):
        QMessageBox.about(self, '??????', 'SGD')

    def warm(self):
        QMessageBox.warning(self, '??????', '??????????????????', QMessageBox.Ok)

    def clear(self):
        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()

    def add_L(self):
        self.ui.textEdit_2.append(datetime.datetime.now().strftime('%m-%d   %T'))
        self.ui.textEdit_2.append('-----------------------')

    def add_R(self):
        self.ui.textEdit.append(datetime.datetime.now().strftime('%m-%d   %T'))
        self.ui.textEdit.append('-----------------------')

    def showText(self, list_):
        turn = list_[0]
        textlist = list_[1]
        if turn == 'L':
            for x in textlist:
                self.ui.textEdit_2.append(x)
            self.add_L()
        elif turn == 'R':
            for x in textlist:
                if x == 0:
                    continue
                self.ui.textEdit.append(str(x))
            self.add_R()
        else:
            print('ERROR ON turn')

    def control_link(self):
        list_ = [self.ui.actionShuju, self.ui.actionCanshu]
        for x in list_:
            x.triggered.connect(self.control)

    def getadd(self):
        message = '68 17 00 43 45 AA AA AA AA AA AA 10 DA 5F 05 01 03 40 01 02 00 00 90 0F 16'
        self.port_.write_list([['?????????...', message.replace(' ', '')]])

    def showmenu_bar(self):
        self.ui.menu_4.setDisabled(0)
        self.ui.menu_2.setDisabled(0)
        self.ui.menu_5.setDisabled(0)
        self.ui.actionSdf.setDisabled(0)


class config(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_ConnectionSet.Ui_Dialog()
        self.ui.setupUi(self)
        self.serial = serial.Serial()
        self.addItem = self.GetSerialNumber()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('engineering.ico'))
        #TODO
        while 1:
            if self.addItem == None:
                Warn = QMessageBox.warning(self, '??????', '??????????????????', QMessageBox.Reset | QMessageBox.Cancel)
                if Warn == QMessageBox.Cancel:
                    self.close()
                    
                if Warn == QMessageBox.Reset:
                    self.addItem = self.GetSerialNumber()
                continue
            else:
                break
        self.ui.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save)
        self.addItem.sort()
        for addItem in self.addItem:
            self.ui.comboBox.addItem(addItem)

    def save(self):
        self.serial = serial.Serial()
        self.port_ = port(self.serial)
        self.serial.port = self.ui.comboBox.currentText()
        self.serial.baudrate = int(self.ui.comboBox_2.currentText())
        self.serial.parity = self.ui.comboBox_3.currentText()
        self.serial.stopbits = int(self.ui.comboBox_4.currentText())
        self.serial.timeout = 1
        if self.port_.is_alive():
            print('pass')
        else:
            self.port_.setDaemon(True)
            self.port_.start()
        MainWindow.getadd()

    def GetSerialNumber(self):
        SerialNumber = []
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            print("The Serial port can't find!")
        else:
            for i in list(port_list):
                SerialNumber.append(i[0])
            return SerialNumber
            # return [0,1]

    def return_port(self):
        return self.serial


class port(threading.Thread,QObject):
    mesasge = pyqtSignal()

    def __init__(self, port):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        self.serial = port
        self.analysis = Comm.Analysis()
        self.list = []

        self.mesasge.connect(self.stop)

        self.__runflag = threading.Event()
        self.__runflag.clear()

    def stop(self):
        self.__runflag.set()
        print('stop')
        print(self.__runflag.is_set(),'stop?is set?')

    def run(self):
        global q
        last = ''
        try:
            self.serial.open()
        except:
            MainWindow.warm_.emit()
            return 0
        data = ''
        while 1:
            if q.empty():
                time.sleep(1)
                num = self.serial.inWaiting()
                if num > 0:
                    data = data + str(binascii.b2a_hex(self.serial.read(num)))[2:-1]
                    print('Received1: ', data)

                    if data[0] == '6' and data[1] == '8':
                        if Comm.check(Comm.makelist(data)) == 0:
                            print('??????????????????', data)

                        else:
                            print('???????????????!????????????:', data)
                            continue

                    re_value = self.analysis.start698(data)
                    if re_value == '??????':
                        data = ''
                        continue

                    elif re_value == 0:
                        pass


            else:
                self.list_new = q.get()
                print('list', self.list_new)
                if self.list_new != []:
                    for message in self.list_new[0]:
                        print(self.__runflag.is_set(), 'stop???????')
                        if self.__runflag.isSet():               ###############################
                            self.__runflag.clear()
                            break
                        print('message', message)
                        if re.search('??????', message[0]):
                            MainWindow.show_text.emit(['L', [message[0], message[1]]])
                            print('??????')
                            time.sleep(int(message[1]))
                            continue

                        elif re.search('??????', message[0]):
                            MainWindow.show_text.emit(['L', [message[0], message[1]]])
                            compare_text = message[1].lower()
                            print('last', last, 'compare_text', compare_text.replace(' ', ''))
                            com = re.search(compare_text.replace(' ', ''), last)
                            if com:
                                MainWindow.show_text.emit(['R', ['????????????']])
                            else:
                                MainWindow.show_text.emit(['R', ['????????????']])
                            continue

                        if message[1][0] == '6':
                            self.serial.write(binascii.a2b_hex(message[1]))
                            MainWindow.show_text.emit(['L', [message[0], Comm.makestr(message[1])]])
                        else:
                            new_message = Comm.BuildMessage(message[1], Comm.makelist(sa)[::-1])
                            self.serial.write(binascii.a2b_hex(new_message))
                            MainWindow.show_text.emit(['L', [message[0], Comm.makestr(new_message)]])
                            try:
                                print('message[0]',message[0])
                                if re.search('?????????',message[0]):
                                    print('??????10s')
                                    MainWindow.show_text.emit(['L', ['??????10s']])
                            except:
                                pass
                        s = 1
                        data = ''
                        while 1:
                            time.sleep(1)
                            num = self.serial.inWaiting()
                            if num > 0:
                                data = data + str(binascii.b2a_hex(self.serial.read(num)))[2:-1]
                                print('Received2: ', Comm.makestr(data))

                                if data[0] == '6' and data[1] == '8':
                                    if Comm.check(Comm.makelist(data)) == 0:
                                        print('??????????????????', data)

                                    else:
                                        print('???????????????!????????????:', data)
                                        continue

                                last = data.lower()
                                re_value = self.analysis.start698(data)

                                if re_value == '??????':
                                    MainWindow.show_text.emit(['R', ['??????:', Comm.makestr(data), '????????????']])
                                    try:
                                        if re.search('?????????', message[0]):
                                            time.sleep(10)
                                    except:
                                        pass
                                    break
                                # elif re_value == 0:
                                #     pass
                                else:
                                    MainWindow.show_text.emit(['R', ['Received:', Comm.makestr(data), re_value]])
                                    break
                                data = ''

                            s += 1
                            if s > 5:
                                MainWindow.show_text.emit(['R', ['????????????']])
                                break
                            else:
                                continue

                sa = Comm.re_sa()
                print('re_message:sa', sa)
                if type(sa) is list:
                    sa = Comm.list2str(sa[::-1])
                MainWindow.ui.lineEdit.setText(Comm.list2str(sa))
                MainWindow.stat_bar.emit('??????????????????')

    def write_list(self, message_list):
        self.list.append(message_list)
        print('self.list: ', self.list)
        global q
        q.put(self.list)
        self.list = []


class APUD_send(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_APDU.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.pushButton.clicked.connect(self.GetText)
        self.setWindowIcon(QIcon('engineering.ico'))

    def GetText(self):
        global q
        self.text = self.ui.textEdit.toPlainText()
        if self.text:
            q.put([[['??????APDU', self.text.replace(' ', '')]]])


def receive(q, dic):
    # print('receivr', [list(dic.items())])
    q.put([list(dic.items())])


if __name__ == '__main__':
    q = queue.Queue(1)
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
