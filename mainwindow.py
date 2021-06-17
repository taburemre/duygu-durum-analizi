import sys as system
from PyQt5 import QtWidgets, QtGui, QtCore
from secondwindow import SecondWindow



class MainWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainwindow()

    def mainwindow( self ):
        self.setWindowIcon(QtGui.QIcon('images/logo.jpg'))
        self.setWindowTitle("Yunus Emre TABUR Graduation Project")
        self.setMinimumSize(1200, 1100)
        self.setMaximumSize(1200, 1100)

        #graduation topic
        self.graduation_topic=QtWidgets.QLabel(self)
        self.graduation_topic.setText("Graduation Topic: \n FACIAL EMOTION SITUATION ANALYSIS")
        self.graduation_topic.setFont(QtGui.QFont("MS Shell Dlg 2", 15))
        self.graduation_topic.setAlignment(QtCore.Qt.AlignCenter)
        self.graduation_topic.resize(800, 191)
        self.graduation_topic.move(260, 220)

        # İmages
        self.images = QtWidgets.QLabel(self)
        self.images.setPixmap(QtGui.QPixmap("images/emre.jpg"))
        self.images.setScaledContents(True)
        self.images.resize(150, 130)
        self.images.move(220, 375)

        #Student images
        self.writer=QtWidgets.QLabel(self)
        self.writer.setText("Graduation Writer:\n Yunus Emre TABUR")
        self.writer.setFont(QtGui.QFont("MS Shell Dlg 2", 18))
        self.writer.setAlignment(QtCore.Qt.AlignCenter)
        self.writer.resize(290, 70)
        self.writer.move(150, 525)

        #Transit Buton
        self.transitionbuton=QtWidgets.QPushButton(self)
        self.transitionbuton.setText("Start Face\nIdentify")
        self.transitionbuton.setFont(QtGui.QFont("MS Shell Dlg 2", 15))
        self.transitionbuton.resize(120, 80)
        self.transitionbuton.move(680, 600)

        #quit buton
        self.backbuton = QtWidgets.QPushButton(self)
        self.backbuton.setText("QUİT")
        self.backbuton.setFont(QtGui.QFont("MS Shell Dlg 2", 15))
        self.backbuton.resize(120, 80)
        self.backbuton.move(480, 600)


        #teacher images
        self.timages=QtWidgets.QLabel(self)
        self.timages.setPixmap(QtGui.QPixmap("images/zeynep.jpg"))
        self.timages.setScaledContents(True)
        self.timages.resize(150, 130)
        self.timages.move(890, 375)

        #teacher name surname
        self.tnamesurname=QtWidgets.QLabel(self)
        self.tnamesurname.setText("Graduation Teacher:\nZeynep ÇİPİLOGLU")
        self.tnamesurname.setFont(QtGui.QFont("MS Shell Dlg 2", 18))
        self.tnamesurname.setAlignment(QtCore.Qt.AlignCenter)
        self.tnamesurname.resize(290, 70)
        self.tnamesurname.move(830, 525)

        #cbü logo
        self.logo=QtWidgets.QLabel(self)
        self.logo.setPixmap(QtGui.QPixmap("images/cbü.png"))
        self.logo.setScaledContents(True)
        self.logo.resize(275, 275)
        self.logo.move(510, 0)

        self.transitionbuton.clicked.connect(self.openWindow)
        self.backbuton.clicked.connect(self.back_clicked)

    def openWindow(self):
        self.secon=SecondWindow()
        self.secon.show()
        self.hide()

    def back_clicked ( self ) :
        import index
        self.hide()
        self.mainwin =index()
        self.mainwin.show()


def main():
    app=QtWidgets.QApplication(system.argv)
    main=MainWindows()
    main.show()
    system.exit(app.exec_())

if __name__ == '__main__':
    main()



