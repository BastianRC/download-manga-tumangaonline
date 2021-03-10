import sys, os, requests, webbrowser, time
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.Qt import Qt, QPoint, QIcon
from download_img_gui import Ui_DownloadIMG
from objects.download_tmo import Download_TMO, Download_Multi_TMO
from playsound import playsound

class Win_DownloadImg(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DownloadIMG()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.btn_download.clicked.connect(self.StartDownload)
        self.ui.btn_dir.clicked.connect(self.OpenDir)
        self.ui.btn_exit.clicked.connect(self.close)

        self.show()
    
    #Inicia la descarga por capitulo.
    def StartDownload(self):
        try:
            if self.ui.lnl_url.text() != "" and self.ui.lnl_urlPro.text() == "":
                count = 0

                tmo = Download_TMO(self.ui.lnl_url.text())

                self.ui.progressBar.setMaximum(len(tmo.urlImgsCh))

                text = "{}\n{}".format(tmo.infoProject[0].rstrip(), tmo.infoProject[1].lstrip().replace('\n', ' ').rstrip())
                
                for data in tmo.urlImgsCh:
                    count += 1
                    if not os.path.isdir(tmo.dirMain):
                        os.mkdir(tmo.dirMain)

                    if os.name != "posix":
                        if not os.path.isdir("{}\\{}\\{}".format(os.getcwd(), tmo.dirMain, tmo.dirChapter)):
                            os.mkdir("{}\\{}\\{}".format(os.getcwd(), tmo.dirMain, tmo.dirChapter))

                        img_name = "{}\\{}\\{}.jpg".format(tmo.dirMain, tmo.dirChapter, count)
                    else:
                        if not os.path.isdir("{}/{}/{}".format(os.getcwd(), tmo.dirMain, tmo.dirChapter)):
                            os.mkdir("{}/{}/{}".format(os.getcwd(), tmo.dirMain, tmo.dirChapter))

                        img_name = "{}/{}/{}.jpg".format(tmo.dirMain, tmo.dirChapter, count)

                    if not os.path.isfile(img_name):
                        self.ui.ptx_out.setPlainText("{}\nDescargando: {}\n".format(text, data))
                    else:
                        self.ui.ptx_out.setPlainText("{}\nSobreescribiendo: {}\n".format(text, data))
                        
                    print(img_name)

                    response = requests.get(data)

                    file_img = open(img_name, "wb")

                    QApplication.processEvents()
                    self.ui.progressBar.setValue(count)

                    file_img.write(response.content)
                    file_img.close()
                
                self.ui.ptx_out.setPlainText("{}\n¡Finalizado!".format(self.ui.ptx_out.toPlainText()))
                self.OnSoundFinish()
                self.ui.progressBar.setValue(0)

            elif self.ui.lnl_urlPro.text() != "" and self.ui.lnl_url.text() == "":
                self.StartMultiDownload()
            else:
                self.ui.ptx_out.setPlainText("Elige solo una opcion de descarga.")
        except AttributeError:
            self.ui.ptx_out.setPlainText("Hay un problema con el enlace.")
    
    #Inicia la descarga multiple.
    def StartMultiDownload(self):
        count = 0
        tmo = Download_Multi_TMO(self.ui.lnl_urlPro.text())

        try:
            for i in range(int(self.ui.sbx_min.text()), int(self.ui.sbx_max.text())+1):
                chapter = Download_TMO(tmo.GetUrlChapter()[i])

                self.ui.progressBar.setMaximum(len(chapter.urlImgsCh))

                text = "{}\n{}".format(chapter.infoProject[0].rstrip(), chapter.infoProject[1].lstrip().replace('\n', ' ').rstrip())

                for data in chapter.urlImgsCh:
                    count += 1
                    if not os.path.isdir(chapter.dirMain):
                        os.mkdir(chapter.dirMain)

                    if os.name != "posix":
                        if not os.path.isdir("{}\\{}\\{}".format(os.getcwd(), chapter.dirMain, chapter.dirChapter)):
                            os.mkdir("{}\\{}\\{}".format(os.getcwd(), chapter.dirMain, chapter.dirChapter))

                        img_name = "{}\\{}\\{}.jpg".format(chapter.dirMain, chapter.dirChapter, count)
                    else:
                        if not os.path.isdir("{}/{}/{}".format(os.getcwd(), chapter.dirMain, chapter.dirChapter)):
                            os.mkdir("{}/{}/{}".format(os.getcwd(), chapter.dirMain, chapter.dirChapter))

                        img_name = "{}/{}/{}.jpg".format(chapter.dirMain, chapter.dirChapter, count)

                    if not os.path.isfile(img_name):
                        self.ui.ptx_out.setPlainText("{}\nDescargando: {}\n".format(text, data))
                    else:
                        self.ui.ptx_out.setPlainText("{}\nSobreescribiendo: {}\n".format(text, data))
                    
                    print(img_name)

                    response = requests.get(data)

                    file_img = open(img_name, "wb")

                    QApplication.processEvents()
                    self.ui.progressBar.setValue(count)

                    file_img.write(response.content)
                    file_img.close()
                
                count = 0
                self.ui.progressBar.setValue(0)

            self.ui.ptx_out.setPlainText("{}\n¡Finalizado!".format(self.ui.ptx_out.toPlainText()))
            self.OnSoundFinish()

        except AttributeError:
            self.ui.ptx_out.setPlainText("Hay un problema con el enlace.")
        except ValueError:
            self.ui.ptx_out.setPlainText("No has colocado un rango de capitulos correcto.")
        except KeyError:
            self.ui.ptx_out.setPlainText("No existen los capitulos.\n¡Revisa el enlace o el rango!")
    
    #Activa el sonido al acabar la descarga.
    def OnSoundFinish(self):
        try:
            playsound("sounds\\finish-him.mp3")
        except:
            playsound("sounds/finish-him.mp3")
    
    #Abre la carpeta del programa.
    def OpenDir(self):
        path = os.getcwd()
        webbrowser.open(os.path.realpath(path))

    def mousePressEvent(self, event):
        try:
            self.oldPos = event.globalPos()
        except: 
            pass

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()	
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win_DownloadImg()
    win.show()

    sys.exit(app.exec_())
