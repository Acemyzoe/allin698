# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Customize.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(694, 523)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 671, 141))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(76, 21, 104, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(21, 23, 54, 16))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 23, 48, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 21, 301, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(21, 53, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(260, 53, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(21, 83, 81, 16))
        self.label_5.setObjectName("label_5")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setGeometry(QtCore.QRect(100, 51, 141, 22))
        self.dateTimeEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dateTimeEdit.setProperty("showGroupSeparator", False)
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setCurrentSectionIndex(0)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(100, 81, 141, 22))
        self.dateTimeEdit_2.setProperty("showGroupSeparator", False)
        self.dateTimeEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setCurrentSectionIndex(0)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(320, 53, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(260, 83, 71, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(330, 81, 41, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(380, 81, 61, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 671, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 321, 264))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 2, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 3, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_2.addWidget(self.checkBox_7, 4, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_2.addWidget(self.checkBox_6, 5, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 6, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_13 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_3.addWidget(self.checkBox_13, 0, 0, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_3.addWidget(self.checkBox_14, 3, 0, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_3.addWidget(self.checkBox_15, 2, 0, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_3.addWidget(self.checkBox_16, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_17 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout_4.addWidget(self.checkBox_17, 2, 0, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout_4.addWidget(self.checkBox_18, 1, 0, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout_4.addWidget(self.checkBox_19, 3, 0, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout_4.addWidget(self.checkBox_20, 4, 0, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout_4.addWidget(self.checkBox_21, 5, 0, 1, 1)
        self.checkBox_22 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout_4.addWidget(self.checkBox_22, 6, 0, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout_4.addWidget(self.checkBox_23, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 5, 0, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout_3.addWidget(self.checkBox_24, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_25 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout_5.addWidget(self.checkBox_25, 0, 0, 1, 1)
        self.checkBox_26 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_26.setObjectName("checkBox_26")
        self.gridLayout_5.addWidget(self.checkBox_26, 3, 0, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_27.setObjectName("checkBox_27")
        self.gridLayout_5.addWidget(self.checkBox_27, 2, 0, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_28.setObjectName("checkBox_28")
        self.gridLayout_5.addWidget(self.checkBox_28, 4, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 40)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkBox_35 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_35.setObjectName("checkBox_35")
        self.gridLayout_6.addWidget(self.checkBox_35, 0, 0, 1, 1)
        self.checkBox_31 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_31.setObjectName("checkBox_31")
        self.gridLayout_6.addWidget(self.checkBox_31, 3, 0, 1, 1)
        self.checkBox_32 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_32.setObjectName("checkBox_32")
        self.gridLayout_6.addWidget(self.checkBox_32, 4, 0, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_29.setObjectName("checkBox_29")
        self.gridLayout_6.addWidget(self.checkBox_29, 2, 0, 1, 1)
        self.checkBox_30 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_30.setObjectName("checkBox_30")
        self.gridLayout_6.addWidget(self.checkBox_30, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 5, 0, 1, 1)
        self.checkBox_36 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_36.setObjectName("checkBox_36")
        self.gridLayout_5.addWidget(self.checkBox_36, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(350, 40, 301, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(350, 20, 301, 16))
        self.label_8.setObjectName("label_8")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 480, 239, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "记录数据读取选项"))
        self.comboBox.setItemText(0, _translate("Dialog", "实时数据"))
        self.comboBox.setItemText(1, _translate("Dialog", "分钟冻结-5002"))
        self.comboBox.setItemText(2, _translate("Dialog", "日冻结-5004"))
        self.label.setText(_translate("Dialog", "数据标识:"))
        self.label_2.setText(_translate("Dialog", "RSC方法:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "04-指定采集启动时间及电能表集合"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "05-指定采集存储时间及电能表集合"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "06-指定采集启动时间内连续间隔值及电能表集合"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "07-指定采集存储时间内连续间隔值及电能表集合"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "10-指定选取最新的n条记录"))
        self.label_3.setText(_translate("Dialog", "采集开始时间:"))
        self.label_4.setText(_translate("Dialog", "电能表MS:"))
        self.label_5.setText(_translate("Dialog", "采集结束时间:"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy/M/d HH:mm:ss"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("Dialog", "yyyy/M/d HH:mm:ss"))
        self.label_6.setText(_translate("Dialog", "全部用户地址"))
        self.label_7.setText(_translate("Dialog", "时间及单位:"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "sec"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "min"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "hour"))
        self.groupBox_2.setTitle(_translate("Dialog", "对象属性描述符"))
        self.checkBox.setText(_translate("Dialog", "00000200"))
        self.checkBox_3.setText(_translate("Dialog", "00300200"))
        self.checkBox_2.setText(_translate("Dialog", "00200200"))
        self.checkBox_4.setText(_translate("Dialog", "00400200"))
        self.checkBox_9.setText(_translate("Dialog", "00700200"))
        self.checkBox_10.setText(_translate("Dialog", "00600200"))
        self.checkBox_5.setText(_translate("Dialog", "00800200"))
        self.checkBox_7.setText(_translate("Dialog", "10100200"))
        self.checkBox_6.setText(_translate("Dialog", "10200200"))
        self.checkBox_8.setText(_translate("Dialog", "10300200"))
        self.checkBox_11.setText(_translate("Dialog", "00500200"))
        self.checkBox_12.setText(_translate("Dialog", "00100200"))
        self.checkBox_13.setText(_translate("Dialog", "10400200"))
        self.checkBox_14.setText(_translate("Dialog", "10700200"))
        self.checkBox_15.setText(_translate("Dialog", "10600200"))
        self.checkBox_16.setText(_translate("Dialog", "10800200"))
        self.checkBox_17.setText(_translate("Dialog", "20010200"))
        self.checkBox_18.setText(_translate("Dialog", "20000200"))
        self.checkBox_19.setText(_translate("Dialog", "20010400"))
        self.checkBox_20.setText(_translate("Dialog", "20020200"))
        self.checkBox_21.setText(_translate("Dialog", "20030200"))
        self.checkBox_22.setText(_translate("Dialog", "20040200"))
        self.checkBox_23.setText(_translate("Dialog", "10900200"))
        self.checkBox_24.setText(_translate("Dialog", "10500200"))
        self.checkBox_25.setText(_translate("Dialog", "20050200"))
        self.checkBox_26.setText(_translate("Dialog", "20080200"))
        self.checkBox_27.setText(_translate("Dialog", "20070200"))
        self.checkBox_28.setText(_translate("Dialog", "20090200"))
        self.checkBox_35.setText(_translate("Dialog", "200A0200"))
        self.checkBox_31.setText(_translate("Dialog", "40000200"))
        self.checkBox_32.setText(_translate("Dialog", "40010200"))
        self.checkBox_29.setText(_translate("Dialog", "20210200"))
        self.checkBox_30.setText(_translate("Dialog", "20140200"))
        self.checkBox_36.setText(_translate("Dialog", "20060200"))
        self.label_8.setText(_translate("Dialog", "自定义对象属性描述符(多个关联以\',\'隔开):"))
        self.pushButton_3.setText(_translate("Dialog", "发送并关闭"))
        self.pushButton.setText(_translate("Dialog", "发送"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))

