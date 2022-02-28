# GUI imports
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout

# アプリケーションの作成
app = QApplication(sys.argv)

# ウィンドウの作成
# ウィンドウのタイトルの設定
# ウィンドウの幅の設定(固定)
# ウィンドウの表示する位置を任意に変更する
# スタイルシートで背景色の変更
window = QWidget()
window.setWindowTitle("App of administrating report by using Barcode")
window.setFixedSize(1000, 700)
window.move(200, 200)
window.setStyleSheet("background: #fff;")

# レイアウトを構成するための箱みたいなもの
grid = QGridLayout()

window.setLayout(grid)

# ウィンドウを開く
window.show()

# アプリケーションの開始
sys.exit(app.exec())