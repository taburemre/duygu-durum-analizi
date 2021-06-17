import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
from mainwindow import MainWindows

def main():
    # Uygulamayı oluştur
    app = QApplication(sys.argv)

    # main screen
    main_pix = QPixmap('images/main.png')
    main = QSplashScreen(main_pix, Qt.WindowStaysOnTopHint)
    main.setMask(main_pix.mask())
    main.show()
    app.processEvents()

    # 5 saniye bekle
    time.sleep(5)

    # Ana pencereyi göster
    mainWindow = MainWindows()
    mainWindow.show()

    # Ana pencere gösterilince splash screen'i kapan
    main.finish(mainWindow)

    # Uygulamayı çalıştır
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
