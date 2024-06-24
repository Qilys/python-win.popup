# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(361, 302)
        Form.setStyleSheet("#frame_beijin{\n"
                           "    background-color: rgb(255, 255, 255);\n"
                           "    border-radius:10px;\n"
                           "}\n"
                           "#frame_biaoti{\n"
                           "    background-color: rgba(245, 245, 245, 245);\n"
                           "    border-top-left-radius: 10px;\n"
                           "    border-top-right-radius: 10px;\n"
                           "}\n"
                           "#frame_neirong{\n"
                           "    background-color: rgb(255, 255, 255);\n"
                           "    border-bottom-left-radius: 10px;\n"
                           "    border-bottom-right-radius: 10px;\n"
                           "}\n"
                           "#label_name{ \n"
                           "    font-family:华文细黑;\n"
                           "    font-size:18px;\n"
                           "    color:rgb(28, 25, 108, 85%);\n"
                           "}\n"
                           "#Button_close{\n"
                           "    color:rgb(148, 149, 149, 65%);\n"
                           "    border:1px solid rgb(243, 243, 243, 65%);\n"
                           "    width:35px;\n"
                           "    height:35px;\n"
                           "    font-size:25px;\n"
                           "    border:none;\n"
                           "}\n"
                           "#Button_close:hover{\n"
                           "    background-color: rgb(148, 149, 149,10%);\n"
                           "    border-radius:5px\n"
                           "}\n"
                           "#textEdit{\n"
                           "    background-color: rgb(255, 255, 255);\n"
                           "    border:1px solid rgb(240, 240, 240);\n"
                           "    border-radius: 10px;\n"
                           "    font-family:华文细黑;\n"
                           "    font-size:18px;\n"
                           "    color:rgb(28, 25, 108, 85%);\n"
                           "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_beijin = QtWidgets.QFrame(self.widget)
        self.frame_beijin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_beijin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_beijin.setObjectName("frame_beijin")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_beijin)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_biaoti = QtWidgets.QFrame(self.frame_beijin)
        self.frame_biaoti.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_biaoti.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_biaoti.setObjectName("frame_biaoti")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_biaoti)
        self.horizontalLayout.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.frame_biaoti)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.Button_close = QtWidgets.QPushButton(self.frame_biaoti)
        self.Button_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_close.setObjectName("Button_close")
        self.horizontalLayout.addWidget(self.Button_close)
        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.frame_biaoti)
        self.frame_neirong = QtWidgets.QFrame(self.frame_beijin)
        self.frame_neirong.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_neirong.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_neirong.setObjectName("frame_neirong")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_neirong)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_neirong)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setMarkdown("")
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setCursorWidth(0)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_3.addWidget(self.frame_neirong)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 11)
        self.verticalLayout_2.addWidget(self.frame_beijin)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button_close.setText(_translate("Form", "×"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'华文细黑\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:19px;\"><br /></p></body></html>"))