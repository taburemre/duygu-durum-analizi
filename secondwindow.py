from PyQt5.QtGui import QImage
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
from PyQt5.QtCore import QTimer
from face_cam import cam_detect
from face_img import Detect



class SecondWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.secondwindow()
        self.timer = QTimer()
        # noinspection PyUnresolvedReferences
        self.timer.timeout.connect(self.opencamera)
        self.cap = cv2.VideoCapture(0)
        self.source = None





    def secondwindow( self ):
        self.picture=''
        self.setStyleSheet("background: #efecf7;")
        self.setWindowTitle("Yunus Emre TABUR Graduation Project")
        self.setWindowIcon(QtGui.QIcon('images/logo.jpg'))
        self.setMinimumSize(1200, 850)
        self.setMaximumSize(1200,850)

        #geçiş oluşturma
        self.table=QtWidgets.QTabWidget(self)
        self.table.setStyleSheet("border: 0px solid black;border-radius: 0px; background:#fbfafd;")
        self.table.move(0, 0)
        self.table.resize(1200, 840)
        self.table.setTabShape(QtWidgets.QTabWidget.TabShape(QtWidgets.QTabWidget.Triangular))

        #MainPage Buton
        self.mainpagebuton = QtWidgets.QPushButton(self)
        self.mainpagebuton.move(440, 30)
        self.mainpagebuton.resize(281, 51)
        self.mainpagebuton.setText("Back to Main Page")
        self.mainpagebuton.setStyleSheet(
            "border: 10px solid #0e0917;border-radius: 20px;background: #0e0917;color:#ffffff;")
        self.mainpagebuton.setFont(QtGui.QFont("MS Shell Dlg 2", 15, QtGui.QFont.Bold))
        self.mainpagebuton.clicked.connect(self.mainpage_clicked)

        # Resim geçişi oluşturuldu.
        self.picturepass = QtWidgets.QWidget()
        self.picturepass.setStyleSheet("border: 0px solid black;border-radius: 10px;background: #efecf7;")

        # Orjinal Resim başlığı
        self.originalpicturetext = QtWidgets.QLabel(self.picturepass)
        self.originalpicturetext.setText("ORİJİNAL PİCTURE")
        self.originalpicturetext.setStyleSheet(
            "background-color:#461eb7;color:#ffffff;border-radius:20px;border-style: solid;")
        self.originalpicturetext.move(290, 170)
        self.originalpicturetext.resize(171, 51)
        self.originalpicturetext.setFont(QtGui.QFont("MS Shell Dlg 2", 13, QtGui.QFont.Bold))
        self.originalpicturetext.setAlignment(QtCore.Qt.AlignCenter)

        # Resmin gözükeceği yer
        self.originalpictureimg = QtWidgets.QLabel(self.picturepass)
        self.originalpictureimg.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.originalpictureimg.move(170, 230)
        self.originalpictureimg.setScaledContents(True)
        self.originalpictureimg.resize(400, 400)

        # Resim seçme butonu
        self.foundoriginalpicture_buton = QtWidgets.QPushButton(self.picturepass)
        self.foundoriginalpicture_buton.setText("CHOOSE PİCTURE")
        self.foundoriginalpicture_buton.setStyleSheet(
            "background-color:#4d9a5c;color:#ffffff;border-radius:20px;border-style: solid;")
        self.foundoriginalpicture_buton.move(290, 630)
        self.foundoriginalpicture_buton.resize(171, 51)
        self.foundoriginalpicture_buton.setFont(QtGui.QFont("MS Shell Dlg 2", 15, QtGui.QFont.Bold))
        self.foundoriginalpicture_buton.clicked.connect(self.choose_picture)

        # Resimde Bulunan Yüzler Başlığı
        self.foundfacepicture = QtWidgets.QLabel(self.picturepass)
        self.foundfacepicture.setText("FOUND THE FACE in PİCTURE ")
        self.foundfacepicture.setStyleSheet(
            "background-color:#461eb7;color:#ffffff;border-radius:20px;border-style: solid;")
        self.foundfacepicture.move(660, 170)
        self.foundfacepicture.resize(261, 51)
        self.foundfacepicture.setFont(QtGui.QFont("MS Shell Dlg 2", 13, QtGui.QFont.Bold))
        self.foundfacepicture.setAlignment(QtCore.Qt.AlignCenter)

        # Resminde Bulunan yuzler gözükeceği yer
        self.foundfacepictureplace = QtWidgets.QLabel(self.picturepass)
        self.foundfacepictureplace.setStyleSheet(
            "border: 5px solid black;border-radius: 10px;background: white;")
        self.foundfacepictureplace.move(590, 230)
        self.foundfacepictureplace.setScaledContents(True)
        self.foundfacepictureplace.resize(400, 400)

        # Resimdeki yuzleri bul butonu
        self.picturefoundface_buton = QtWidgets.QPushButton(self.picturepass)
        self.picturefoundface_buton.setText("FIND FACES IN PICTURE")
        self.picturefoundface_buton.setStyleSheet(
            "background-color:#4d9a5c;color:#ffffff;border-radius:20px;border-style: solid;")
        self.picturefoundface_buton.move(650, 630)
        self.picturefoundface_buton.resize(291, 51)
        self.picturefoundface_buton.setFont(QtGui.QFont("MS Shell Dlg 2", 15, QtGui.QFont.Bold))
        self.picturefoundface_buton.clicked.connect(self.found_face)

        # Kamera geçişi oluşturuldu.
        self.campass = QtWidgets.QWidget()
        self.campass.setStyleSheet("border: 0px solid black;border-radius: 10px;background: #efecf7; ")

        # Kamerada bulanan yüzler başlığı
        self.orijinal_image_text = QtWidgets.QLabel(self.campass)
        self.orijinal_image_text.setText("FACES ON THE CAMERA")
        self.orijinal_image_text.setStyleSheet(
            "background-color:#ee1010;color:#ffffff;border-radius:20px;border-style: solid;")
        self.orijinal_image_text.move(430, 70)
        self.orijinal_image_text.resize(300, 65)
        self.orijinal_image_text.setFont(QtGui.QFont("MS Shell Dlg 2", 12, QtGui.QFont.Bold))
        self.orijinal_image_text.setAlignment(QtCore.Qt.AlignCenter)

        # Kameranın Gözükeceği yer
        self.cam_see_place = QtWidgets.QLabel(self.campass)
        self.cam_see_place.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.cam_see_place.move(230, 150)
        self.cam_see_place.setScaledContents(True)
        self.cam_see_place.resize(700, 400)

        # Kamera Açma butonu
        self.opencam_buton = QtWidgets.QPushButton(self.campass)
        self.opencam_buton.setText("RUN THE CAMERA")
        self.opencam_buton.setStyleSheet(
            "background-color:#360b71;color:#ffffff;border-radius:20px;border-style: solid;")
        self.opencam_buton.move(460, 620)
        self.opencam_buton.resize(241, 51)
        self.opencam_buton.setFont(QtGui.QFont("MS Shell Dlg 2", 15, QtGui.QFont.Bold))
        self.opencam_buton.clicked.connect(self.time_control)



        self.table.addTab(self.campass, "İdentify camera face")
        self.table.addTab(self.picturepass, "İdentify picture face")


    def choose_picture ( self ) :
        self.pictureUrl = QtWidgets.QFileDialog.getOpenFileName(self, "Please select an image ", ''," Image Files ("
                                                                                                    "* .png * .jpg"
                                                                                                    "* .jpeg)")
        self.picture = self.pictureUrl[0]
        self.originalpictureimg.setPixmap(QtGui.QPixmap(self.picture))

    def found_face(self):


        img = cv2.imread(str(self.picture))
        picture = Detect(img)
        cv2.imwrite(' outputt/output.jpg ', picture)
        self.foundfacepictureplace.setPixmap(QtGui.QPixmap(' outputt/output.jpg '))

    def opencamera ( self ) :
        ret, image = self.cap.read()
        image = cam_detect(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        Img = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.cam_see_place.setPixmap(QtGui.QPixmap.fromImage(Img))


    def time_control ( self ) :
        print(self.timer.isActive())
        if not self.timer.isActive() :
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
        else :
            self.timer.stop()
            self.cap.release()


    def mainpage_clicked ( self ) :
        from mainwindow import MainWindows
        self.hide()
        self.mainwin = MainWindows()
        self.mainwin.show()

