# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Fri Apr  8 22:40:51 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(836, 584)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(836, 584))
        MainWindow.setMaximumSize(QtCore.QSize(836, 584))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_run_belva = QtGui.QPushButton(self.centralwidget)
        self.pushButton_run_belva.setGeometry(QtCore.QRect(130, 170, 101, 31))
        self.pushButton_run_belva.setObjectName(_fromUtf8("pushButton_run_belva"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(300, 180, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 411, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lineEdit_input_src_dir = QtGui.QLineEdit(self.frame)
        self.lineEdit_input_src_dir.setEnabled(False)
        self.lineEdit_input_src_dir.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.lineEdit_input_src_dir.setObjectName(_fromUtf8("lineEdit_input_src_dir"))
        self.pushButton_input_src_dir = QtGui.QPushButton(self.frame)
        self.pushButton_input_src_dir.setGeometry(QtCore.QRect(310, 10, 93, 29))
        self.pushButton_input_src_dir.setObjectName(_fromUtf8("pushButton_input_src_dir"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 210, 411, 191))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textBrowser_status_msgs = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser_status_msgs.setGeometry(QtCore.QRect(10, 10, 391, 101))
        self.textBrowser_status_msgs.setObjectName(_fromUtf8("textBrowser_status_msgs"))
        self.textBrowser_status_msgs_brief = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser_status_msgs_brief.setGeometry(QtCore.QRect(10, 130, 391, 51))
        self.textBrowser_status_msgs_brief.setObjectName(_fromUtf8("textBrowser_status_msgs_brief"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 121, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 180, 64, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 110, 411, 51))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.lineEdit_output_src_dir = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_output_src_dir.setEnabled(False)
        self.lineEdit_output_src_dir.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.lineEdit_output_src_dir.setObjectName(_fromUtf8("lineEdit_output_src_dir"))
        self.pushButton_output_src_dir = QtGui.QPushButton(self.frame_3)
        self.pushButton_output_src_dir.setGeometry(QtCore.QRect(310, 10, 93, 29))
        self.pushButton_output_src_dir.setObjectName(_fromUtf8("pushButton_output_src_dir"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 420, 411, 131))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.textBrowser_help_text = QtGui.QTextBrowser(self.frame_4)
        self.textBrowser_help_text.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.textBrowser_help_text.setObjectName(_fromUtf8("textBrowser_help_text"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 31, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(430, 40, 391, 101))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.listWidget_substitutions = QtGui.QListWidget(self.frame_5)
        self.listWidget_substitutions.setGeometry(QtCore.QRect(10, 10, 371, 81))
        self.listWidget_substitutions.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_substitutions.setObjectName(_fromUtf8("listWidget_substitutions"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 20, 91, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 140, 171, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.frame_7 = QtGui.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(430, 160, 391, 391))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.listWidget_policies_mutate = QtGui.QListWidget(self.frame_7)
        self.listWidget_policies_mutate.setEnabled(True)
        self.listWidget_policies_mutate.setGeometry(QtCore.QRect(10, 10, 371, 181))
        self.listWidget_policies_mutate.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_policies_mutate.setObjectName(_fromUtf8("listWidget_policies_mutate"))
        self.listWidget_policies_select = QtGui.QListWidget(self.frame_7)
        self.listWidget_policies_select.setEnabled(True)
        self.listWidget_policies_select.setGeometry(QtCore.QRect(10, 200, 371, 181))
        self.listWidget_policies_select.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_policies_select.setObjectName(_fromUtf8("listWidget_policies_select"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OWASP - Basic Expression & Lexicon Variation Algorithms (BELVA) - ver 0.1", None))
        self.pushButton_run_belva.setText(_translate("MainWindow", "Run BELVA", None))
        self.pushButton_input_src_dir.setText(_translate("MainWindow", "Directory", None))
        self.label.setText(_translate("MainWindow", "Import Sources Directory", None))
        self.label_2.setText(_translate("MainWindow", "Status Messages", None))
        self.label_3.setText(_translate("MainWindow", "Progress:", None))
        self.pushButton_output_src_dir.setText(_translate("MainWindow", "Choose File", None))
        self.label_4.setText(_translate("MainWindow", "Output", None))
        self.label_5.setText(_translate("MainWindow", "Help", None))
        self.listWidget_substitutions.setSortingEnabled(True)
        self.label_6.setText(_translate("MainWindow", "Substitutions", None))
        self.label_7.setText(_translate("MainWindow", "Policies (Mutate / Select)", None))
        self.listWidget_policies_mutate.setSortingEnabled(True)
        self.listWidget_policies_select.setSortingEnabled(True)

