# importando bibliotecas necessarias
from PyQt5 import QtWidgets, uic, QtGui
import sys
from PyQt5.QtWidgets import QMessageBox
from mhyt import yt_download

# Importar arquivo da imagem
import youtube_rc

class YouTube(QtWidgets.QMainWindow):
    def __init__(self):
        super(YouTube, self).__init__()
        # Carrega o arquivo < .ui > para que o PyInstaller encontre o arquivo é necessario por o endereço completo.
        uic.loadUi(r'E:\QT_Creator\layout.ui', self)
        # Define um ícone para a janela do software
        self.setWindowIcon(QtGui.QIcon(r'E:\QT_Creator\download.png'))
        self.setWindowTitle('Video Downloader')
        #Botões
        self.btDownload.clicked.connect(self.download)
        self.btFechar.clicked.connect(self.fechar)

        self.show()

    def download(self):
        if self.rb_mp4.isChecked():
            try:
                url = self.InsertURL.text()
                titulo = self.Insert_Titulo.text()
                if url == '' or titulo == '':
                    # Cria o objeto ou seja a caixa de mensagem
                    self.msg = QMessageBox()
                    # Define o tipo da caixa de mensagem
                    self.msg.setIcon(QMessageBox.Information)
                    # Define o ícone da caixa de mensagem
                    self.msg.setWindowIcon(QtGui.QIcon(r'E:\QT_Creator\download.png'))
                    # Define a mensagem principal
                    self.msg.setText("O campo da URL ou do Título está vazio!")
                    # Define o título da janela
                    self.msg.setWindowTitle("ATENÇÃO")
                    # Exibir a caixa de mensagem
                    self.msg.show()
                else:
                    titulo_mp4 = titulo + '.mp4'
                    yt_download(url, titulo_mp4)
            except:
                pass
        if self.rb_mp3.isChecked():
            try:
                url = self.InsertURL.text()
                titulo = self.Insert_Titulo.text()
                if url == '' or titulo == '':
                    # Cria o objeto ou seja a caixa de mensagem
                    self.msg = QMessageBox()
                    # Define o tipo da caixa de mensagem
                    self.msg.setIcon(QMessageBox.Information)
                    # Define o ícone da caixa de mensagem
                    self.msg.setWindowIcon(QtGui.QIcon(r'E:\QT_Creator\download.png'))
                    # Define a mensagem principal
                    self.msg.setText("O campo da URL ou do Título está vazio!")
                    # Define o título da janela
                    self.msg.setWindowTitle("ATENÇÃO")
                    # Exibir a caixa de mensagem
                    self.msg.show()

                else:
                    titulo_mp3 = titulo + '.mp3'
                    yt_download(url, titulo_mp3, ismusic=True, codec="mp3")
            except:
                pass

    def fechar(self):
        # Cria o objeto ou seja a caixa de mensagem
        self.msg = QMessageBox()
        # Define o tipo da caixa de mensagem
        self.msg.setIcon(QMessageBox.Warning)
        # Define o ícone da caixa de mensagem
        self.msg.setWindowIcon(QtGui.QIcon(r'E:\QT_Creator\download.png'))
        # Define o título da janela
        self.msg.setWindowTitle('ATENÇÃO')
        # Define a mensagem principal
        self.msg.setText('Deseja sair do programa?')
        self.msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        # Define um botão para a caixa de mensagem
        btSim = self.msg.button(QMessageBox.Ok)
        # Define o texto do botão Ok da caixa de mensagem
        btSim.setText('Sim')
        # Define um botão para a caixa de mensagem
        btNao = self.msg.button(QMessageBox.Cancel)
        # Define o texto do botão Cancel da caixa de mensagem
        btNao.setText('Não')
        # Exibir a caixa de mensagem
        self.msg.exec()
        if self.msg.clickedButton() == btSim:
            sys.exit(0)
        else:
            pass

app = QtWidgets.QApplication(sys.argv)
window = YouTube()
app.exec_()
