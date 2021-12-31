"""trans window's ui setup"""
import os
from master import config
from master.UI import linebox
if config.IS_USE_PYSIDE:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore


class TransWindowUi():
    """ApduDiyDialogUi"""
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """set layout"""
        self.setWindowTitle('698日志解析工具_{ver}'.format(ver=config.TRANS_WINDOW_TITLE_ADD))
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SOFTWARE_PATH, config.TRANS_ICO_PATH)))
        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('&文件')
        self.open_action = QtGui.QAction('&打开...', self)
        self.open_action.setShortcut('Ctrl+o')
        self.reload_action = QtGui.QAction('&重新载入', self)
        self.reload_action.setShortcut('Ctrl+r')
        self.clear_action = QtGui.QAction('&清空', self)
        self.clear_action.setShortcut('Ctrl+l')
        self.find_action = QtGui.QAction('查找', self)
        self.find_action.setShortcut('Ctrl+f')
        self.next_msg_action = QtGui.QAction('跳至下一条报文', self)
        self.next_msg_action.setShortcut('Ctrl+d')
        self.priv_msg_action = QtGui.QAction('跳至上一条报文', self)
        self.priv_msg_action.setShortcut('Ctrl+Shift+d')
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.reload_action)
        self.file_menu.addAction(self.clear_action)
        self.file_menu.addAction(self.find_action)
        self.file_menu.addAction(self.next_msg_action)
        self.file_menu.addAction(self.priv_msg_action)
        self.file_menu.addSeparator()
        self.help_menu = self.menubar.addMenu('&帮助')
        self.about_action = QtGui.QAction('&关于', self)
        self.about_action.setShortcut('F1')
        self.help_menu.addAction(self.about_action)

        self.dummy_l = QtGui.QLabel()
        self.dummy_l.setText('   ')

        self.input_w = QtGui.QWidget()
        self.input_box = linebox.CodeEditor()
        # self.input_box = QtGui.QTextEdit()
        self.find_box = QtGui.QLineEdit()
        self.find_box.setPlaceholderText('搜索...')
        self.find_last_b = QtGui.QPushButton()
        self.find_last_b.setMaximumWidth(30)
        self.find_last_b.setText('<')
        self.find_next_b = QtGui.QPushButton()
        self.find_next_b.setMaximumWidth(30)
        self.find_next_b.setText('>')
        self.find_l = QtGui.QLabel()
        self.msg_priv_b = QtGui.QPushButton()
        self.msg_priv_b.setMaximumWidth(50)
        self.msg_priv_b.setText('上一条')
        self.msg_next_b = QtGui.QPushButton()
        self.msg_next_b.setMaximumWidth(50)
        self.msg_next_b.setText('下一条')
        self.input_zoom_in_b = QtGui.QPushButton()
        self.input_zoom_in_b.setMaximumWidth(30)
        self.input_zoom_in_b.setText('+')
        self.input_zoom_out_b = QtGui.QPushButton()
        self.input_zoom_out_b.setMaximumWidth(30)
        self.input_zoom_out_b.setText('-')
        self.input_foot_hbox = QtGui.QHBoxLayout()
        self.input_foot_hbox.addWidget(self.find_box)
        self.input_foot_hbox.addWidget(self.find_last_b)
        self.input_foot_hbox.addWidget(self.find_next_b)
        self.input_foot_hbox.addWidget(self.find_l)
        self.input_foot_hbox.addStretch(1)
        self.input_foot_hbox.addWidget(self.msg_priv_b)
        self.input_foot_hbox.addWidget(self.msg_next_b)
        self.input_foot_hbox.addStretch(1)
        self.input_foot_hbox.addWidget(self.input_zoom_in_b)
        self.input_foot_hbox.addWidget(self.input_zoom_out_b)
        self.input_vbox = QtGui.QVBoxLayout(self.input_w)
        self.input_vbox.setContentsMargins(0, 0, 0, 0)
        self.input_vbox.setSpacing(1)
        self.input_vbox.addWidget(self.input_box)
        self.input_vbox.addLayout(self.input_foot_hbox)

        self.output_w = QtGui.QWidget()
        self.msg_box = QtGui.QPlainTextEdit()
        self.msg_box.setMinimumHeight(30)
        self.output_box = QtGui.QTextEdit()
        self.output_copy_b = QtGui.QPushButton()
        self.output_copy_b.setMaximumWidth(80)
        self.output_copy_b.setText('复制到剪贴板')
        self.output_zoom_in_b = QtGui.QPushButton()
        self.output_zoom_in_b.setMaximumWidth(30)
        self.output_zoom_in_b.setText('+')
        self.output_zoom_out_b = QtGui.QPushButton()
        self.output_zoom_out_b.setMaximumWidth(30)
        self.output_zoom_out_b.setText('-')
        self.output_foot_hbox = QtGui.QHBoxLayout()
        self.output_foot_hbox.addStretch(1)
        self.output_foot_hbox.addWidget(self.output_copy_b)
        self.output_foot_hbox.addStretch(1)
        self.output_foot_hbox.addWidget(self.output_zoom_in_b)
        self.output_foot_hbox.addWidget(self.output_zoom_out_b)
        self.output_vbox = QtGui.QVBoxLayout(self.output_w)
        self.output_vbox.setContentsMargins(0, 0, 0, 0)
        self.output_vbox.setSpacing(1)
        self.output_vspliter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.output_vspliter.addWidget(self.msg_box)
        self.output_vspliter.addWidget(self.output_box)
        self.output_vspliter.setStretchFactor(0, 1)
        self.output_vspliter.setStretchFactor(1, 12)
        self.output_vbox.addWidget(self.output_vspliter)
        self.output_vbox.addLayout(self.output_foot_hbox)

        self.main_hsplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.main_hsplitter.addWidget(self.input_w)
        self.main_hsplitter.addWidget(self.output_w)
        self.main_hsplitter.setStretchFactor(0, 2)
        self.main_hsplitter.setStretchFactor(1, 3)

        self.proc_bar = QtGui.QProgressBar()
        # self.proc_bar.setEnabled(True)
        self.proc_bar.setMinimumSize(QtCore.QSize(200, 0))
        self.proc_bar.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed))
        self.proc_bar.setTextVisible(False)
        
        self.proc_l = QtGui.QLabel()
        self.proc_l.setText('就绪')
        self.auto_wrap_cb = QtGui.QCheckBox()
        self.auto_wrap_cb.setText('自动换行')
        self.show_level_cb = QtGui.QCheckBox()
        self.show_level_cb.setText('报文结构')
        self.show_dtype_cb = QtGui.QCheckBox()
        self.show_dtype_cb.setText('数据类型')
        self.always_top_cb = QtGui.QCheckBox()
        self.always_top_cb.setText('置顶')

        self.foot_hbox = QtGui.QHBoxLayout()
        self.foot_hbox.addWidget(self.proc_bar)
        self.foot_hbox.addWidget(self.proc_l)
        self.foot_hbox.addStretch(1)
        self.foot_hbox.addWidget(self.auto_wrap_cb)
        self.foot_hbox.addWidget(self.show_level_cb)
        self.foot_hbox.addWidget(self.show_dtype_cb)
        self.foot_hbox.addWidget(self.always_top_cb)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.setContentsMargins(0, 0, 0, 0)
        self.main_vbox.setSpacing(1)
        self.main_vbox.addWidget(self.main_hsplitter)
        self.main_vbox.addLayout(self.foot_hbox)
        self.main_widget = QtGui.QWidget()
        self.main_widget.setLayout(self.main_vbox)
        self.setCentralWidget(self.main_widget)
        self.resize(1000, 666)
