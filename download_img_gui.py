# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\download_img_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DownloadIMG(object):
    def setupUi(self, DownloadIMG):
        DownloadIMG.setObjectName("DownloadIMG")
        DownloadIMG.resize(611, 411)
        with open("style.css", "r") as style:
            DownloadIMG.setStyleSheet(style.read())
        self.background = QtWidgets.QFrame(DownloadIMG)
        self.background.setGeometry(QtCore.QRect(0, 0, 611, 411))
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.background)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 531, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vly_one = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vly_one.setContentsMargins(0, 0, 0, 0)
        self.vly_one.setObjectName("vly_one")
        self.lnl_url = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lnl_url.setObjectName("lnl_url")
        self.vly_one.addWidget(self.lnl_url)
        self.lbl_url = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lbl_url.setFont(font)
        self.lbl_url.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_url.setObjectName("lbl_url")
        self.vly_one.addWidget(self.lbl_url)
        self.ptx_out = QtWidgets.QPlainTextEdit(self.background)
        self.ptx_out.setGeometry(QtCore.QRect(10, 150, 591, 151))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ptx_out.setFont(font)
        self.ptx_out.setReadOnly(True)
        self.ptx_out.setPlainText("")
        self.ptx_out.setObjectName("ptx_out")
        self.btn_download = QtWidgets.QPushButton(self.background)
        self.btn_download.setGeometry(QtCore.QRect(90, 360, 191, 31))
        self.btn_download.setObjectName("btn_download")
        self.btn_dir = QtWidgets.QPushButton(self.background)
        self.btn_dir.setEnabled(True)
        self.btn_dir.setGeometry(QtCore.QRect(330, 360, 191, 31))
        self.btn_dir.setObjectName("btn_dir")
        self.btn_exit = QtWidgets.QPushButton(self.background)
        self.btn_exit.setGeometry(QtCore.QRect(290, 360, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.progressBar = QtWidgets.QProgressBar(self.background)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 591, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.lbl_ej_two = QtWidgets.QLabel(self.background)
        self.lbl_ej_two.setGeometry(QtCore.QRect(40, 110, 531, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_ej_two.setFont(font)
        self.lbl_ej_two.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_ej_two.setObjectName("lbl_ej_two")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.background)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 401, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hly_one = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hly_one.setContentsMargins(0, 0, 0, 0)
        self.hly_one.setObjectName("hly_one")
        self.lnl_urlPro = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lnl_urlPro.setObjectName("lnl_urlPro")
        self.hly_one.addWidget(self.lnl_urlPro)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.background)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(450, 80, 121, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.hly_two = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hly_two.setContentsMargins(0, 0, 0, 0)
        self.hly_two.setObjectName("hly_two")
        self.sbx_min = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.sbx_min.setAlignment(QtCore.Qt.AlignCenter)
        self.sbx_min.setMaximum(999)
        self.sbx_min.setObjectName("sbx_min")
        self.hly_two.addWidget(self.sbx_min)
        self.lbl_one = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lbl_one.setObjectName("lbl_one")
        self.hly_two.addWidget(self.lbl_one)
        self.sbx_max = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.sbx_max.setAlignment(QtCore.Qt.AlignCenter)
        self.sbx_max.setMaximum(999)
        self.sbx_max.setObjectName("sbx_max")
        self.hly_two.addWidget(self.sbx_max)

        self.retranslateUi(DownloadIMG)
        QtCore.QMetaObject.connectSlotsByName(DownloadIMG)

    def retranslateUi(self, DownloadIMG):
        _translate = QtCore.QCoreApplication.translate
        DownloadIMG.setWindowTitle(_translate("DownloadIMG", "Dialog"))
        self.lnl_url.setPlaceholderText(_translate("DownloadIMG", "Enlace del capitulo"))
        self.lbl_url.setText(_translate("DownloadIMG", "Ej: https://lectortmo.com/viewer/5af61094f3d49/cascade"))
        self.btn_download.setText(_translate("DownloadIMG", "Iniciar Descarga"))
        self.btn_dir.setText(_translate("DownloadIMG", "Abrir Carpeta"))
        self.btn_exit.setText(_translate("DownloadIMG", "X"))
        self.lbl_ej_two.setText(_translate("DownloadIMG", "Ej: https://lectortmo.com/library/manhua/12266/dou-po-cang-qiong"))
        self.lnl_urlPro.setPlaceholderText(_translate("DownloadIMG", "Enlace del manga"))
        self.lbl_one.setText(_translate("DownloadIMG", "Hasta"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DownloadIMG = QtWidgets.QDialog()
    ui = Ui_DownloadIMG()
    ui.setupUi(DownloadIMG)
    DownloadIMG.show()
    sys.exit(app.exec_())
