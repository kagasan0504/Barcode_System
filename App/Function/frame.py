# GUI imports
from datetime import datetime
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit, QHBoxLayout, QSizePolicy, QListView, QComboBox

grid = QGridLayout()
main_layout = QGridLayout()

info_student = {
    "number": [],
    "name": [],
    "group": [],
    "theme": [],
    "status": [],
    "first_receive": [],
    "final_receive": []
}

def frame1():
    header_label = QLabel()
    header_label.setFixedHeight(75)
    header_label.setStyleSheet("background-color: #666;")
    header_label.move(0, 0)
    Resister_label = QLabel("Resiter")
    Resister_label.setStyleSheet("""
        font-size: 30px;
        color: #fab;
        background-color: '#759374';
        padding: 10px 20px;
        margin: 5px 0;
    """)
    Accept_label = QLabel("receive")
    Accept_label.setStyleSheet("""
        font-size: 30px;
        color: #fab;
        background-color: '#759374';
        padding: 10px 20px;
        margin: 2px 0;
    """)
    sidebar_left = QGridLayout()
    base_vbox = QVBoxLayout()
    main_layout_select()
    sidebar_left.addWidget(Accept_label, )
    base_vbox.addWidget(header_label)
    grid.addWidget(Resister_label, 1, 0, 1, 3)
    grid.addWidget(Accept_label, 2, 0, 1, 3)
    # grid.addLayout(sidebar_left, 1, 0, 18, 1)
    grid.addLayout(base_vbox, 0, 3, 1, 14)
    grid.addLayout(main_layout, 1, 3, 18, 14)

def main_layout_select():
    resister_top()
    # automate_resister()

def resister_top():
    ComboBox_Listview = QListView()
    # ComboBox_Listview.setObjectName("ComboBox")
    ComboBox_Listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    ComboBox = QComboBox()
    ComboBox.setView(ComboBox_Listview)
    ComboBox.setObjectName("ComboBox")
    ComboBox.setEditable(True)
    ComboBox.lineEdit().setObjectName("ComboBox")
    ComboBox.lineEdit().setReadOnly(True)
    ComboBox.PopupOffcet = (0, 10)
    ComboBox.fade = True
    ComboBox.slide = True
    ComboBox.stretch = True
    ComboBox.addItem("2NC")
    ComboBox.addItem("3NC")
    
    # ===================================================================================================
    ComboBox.setStyleSheet("""
        QAbstractItemView{
            color: #fff;
            background-color: #de4a3e;
            outline: none;
            border: solid #de4a3e;
            border-radius: 3px;
        }
        *{
            height: 80px;
            color: #687;
            background-color: transparent;
            opacity: 0;
            border-style: solid;
            border-width: 2px;
            border-color: #de4a3e;
            border-radius: 3px;
        }
        ::drop-down {
            image: url(":/icon/icon.png");
            border: 0px;
            height: 100px;
            width: 100px;
        }
        ::down-arrow {
            image: url(":/icon/icon.png");
            height: 100px;
            width: 100px;
        }
        /*QComboBox::drop-down:hover#ComboBox {
            image: url("icon.png");
        }
        QComboBox::drop-down:on#ComboBox {
            image: url("icon.png");
        }*/
    """)
    ComboBox_Listview.setStyleSheet ("""
        QListView#ComboBox {
            color: #fff;
            background-color: transparent;
            outline: none;
            border-radius: 3px;
            border-style: solid;
            border-width: 1px;
            border-color: #de4a3e;
        }
        QListView::item:hover#ComboBox,
        QListView::item:selected#ComboBox {
            background-color: #c64236;
        }
        QListView::item#ComboBox {
            color: #fff;
            padding-top: 4px;
            padding-bottom: 4px;
            padding-left: 5px;
            height: 60px;
            border-style: 1px solid;
            border-radius: 3px;
        }
        QListView#ComboBox {
            background-color: #de4a3e;
            color: black;
            outline: none;
            border-style: solid;
            border-color: #de4a3e;
            border-radius: 3px;
        }
    """)
    # ===================================================================================================

    main_layout.addWidget(ComboBox, 0, 0)

# ======================================================================
# バーコード読み込み画面
# ======================================================================
def automate_resister():
    for i in reversed(range(main_layout.count())): 
        main_layout.itemAt(i).widget().deleteLater()
    EmptySide_label = QLabel()
    EmptyBottom_label = QLabel()
    SystemName_label = QLabel("レポート提出管理")
    BarcodeNumber_label = QLabel("223NC19EC091FC")
    YearTerm_label = QLabel("2022年度")
    ExperimentName_label = QLabel("3NC実験")
    StudentNumberTitle_label = QLabel("学籍番号")
    StudentNumber_label = QLabel("19EC091")
    StudentNameTitle_label = QLabel("氏名")
    StudentName_label = QLabel("蛭田　陸")
    StudentGroupTitle_label = QLabel("グループ")
    StudentGroup_label = QLabel("S1")
    StudentThemeTitle_label = QLabel("テーマ名")
    StudentTheme_label = QLabel("周波数と周波数特性の基礎")
    ReportStatusTitle_label = QLabel("Status")
    ReportStatus_label = QLabel("エラー : 既に最終受取済")
    FirstReceiveTitle_label = QLabel("1次受取")
    FirstReceive_label = QLabel(str(datetime.now()))
    FinalReceiveTitle_label = QLabel("最終受取")
    FinalReceive_label = QLabel(str(datetime.now()))
    # print(datetime.now())
    main_layout.addWidget(EmptySide_label, 0, 0, 11, 1)
    main_layout.addWidget(EmptyBottom_label, 10, 1, 1, 15)
    main_layout.addWidget(SystemName_label, 1, 3, 1, 5)
    main_layout.addWidget(BarcodeNumber_label, 2, 3, 1, 12)
    main_layout.addWidget(YearTerm_label, 3, 1, 1, 7)
    main_layout.addWidget(ExperimentName_label, 3, 9, 1, 7)
    main_layout.addWidget(StudentNumberTitle_label, 4, 1, 1, 2)
    main_layout.addWidget(StudentNumber_label, 4, 3, 1, 5)
    main_layout.addWidget(StudentNameTitle_label, 5, 1, 1, 2)
    main_layout.addWidget(StudentName_label, 5, 3, 1, 5)
    main_layout.addWidget(StudentGroupTitle_label, 5, 9, 1, 3)
    main_layout.addWidget(StudentGroup_label, 5, 12, 1, 3)
    main_layout.addWidget(StudentThemeTitle_label, 6, 1, 1, 2)
    main_layout.addWidget(StudentTheme_label, 6, 3, 1, 12)
    main_layout.addWidget(ReportStatusTitle_label, 7, 1, 1, 2)
    main_layout.addWidget(ReportStatus_label, 7, 3, 1, 12)
    main_layout.addWidget(FirstReceiveTitle_label, 8, 1, 1, 2)
    main_layout.addWidget(FirstReceive_label, 8, 3, 1, 5)
    main_layout.addWidget(FinalReceiveTitle_label, 9, 1, 1, 2)
    main_layout.addWidget(FinalReceive_label, 9, 3, 1, 5)