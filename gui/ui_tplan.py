# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerHRWYHf.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(943, 487)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayoutWidget = QWidget(self.page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 120, 224, 89))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(False)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.gridLayoutWidget_2 = QWidget(self.page)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 220, 250, 102))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 2)

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(300, 130, 351, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 179))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(360, 110, 191, 20))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(720, 240, 201, 20))
        self.label_10.setFont(font2)
        self.scrollArea_2 = QScrollArea(self.page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(670, 270, 271, 41))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 269, 39))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 340, 111, 24))
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(550, 310, 101, 21))
        font4 = QFont()
        font4.setPointSize(8)
        self.pushButton_3.setFont(font4)
        self.gridLayoutWidget_4 = QWidget(self.page)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(690, 150, 239, 71))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.gridLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_4.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 2)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(499, 400, 441, 81))
        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(760, 340, 79, 24))
        self.pushButton_5 = QPushButton(self.page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(850, 360, 61, 24))
        self.pushButton_6 = QPushButton(self.page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(840, 310, 101, 21))
        self.pushButton_6.setFont(font4)
        self.pushButton_7 = QPushButton(self.page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(820, 380, 121, 21))
        self.pushButton_7.setFont(font4)
        StackedWidget.addWidget(self.page)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Dimen\u00e7\u00e3o em Y:", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Dimen\u00e7\u00e3o em X:", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"DIMEN\u00c7\u00d5ES DA QUADR\u00cdCULA", None))
        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"QUADRICULA\u00c7\u00c3O", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"N\u00famero de Se\u00e7\u00f5es Transversais:", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"N\u00famero de Se\u00e7\u00f5es Longitudinais:", None))
        self.pushButton.setText(QCoreApplication.translate("StackedWidget", u"GERAR QUADR\u00cdCULAS", None))
        self.label_9.setText(QCoreApplication.translate("StackedWidget", u"COTAS DO TERRENO NATURAL", None))
        self.label_10.setText(QCoreApplication.translate("StackedWidget", u"INCLINA\u00c7\u00c3O DE PROJETO (%)", None))
        self.pushButton_2.setText(QCoreApplication.translate("StackedWidget", u"PLATAFORMA", None))
        self.pushButton_3.setText(QCoreApplication.translate("StackedWidget", u"IMPORTAR .XLSX", None))
        self.label_12.setText(QCoreApplication.translate("StackedWidget", u"Adotada:", None))
        self.label_11.setText(QCoreApplication.translate("StackedWidget", u"Calculada:", None))
        self.label_13.setText(QCoreApplication.translate("StackedWidget", u"COTA DE PLATAFOMRA", None))
        self.groupBox.setTitle(QCoreApplication.translate("StackedWidget", u"Descri\u00e7\u00e3o", None))
        self.pushButton_4.setText(QCoreApplication.translate("StackedWidget", u"CALCULAR", None))
        self.pushButton_5.setText(QCoreApplication.translate("StackedWidget", u"Relat\u00f3rio", None))
        self.pushButton_6.setText(QCoreApplication.translate("StackedWidget", u"IMPORTAR .XLSX", None))
        self.pushButton_7.setText(QCoreApplication.translate("StackedWidget", u"RESUMO DE VOLUMES", None))
    # retranslateUi

