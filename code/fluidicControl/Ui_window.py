# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/fluidicControl/ui/window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 899)
        MainWindow.setMaximumSize(QtCore.QSize(1800, 900))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setKerning(True)
        self.centralWidget.setFont(font)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.centralWidget.setObjectName("centralWidget")
        self.Pump_A = QtWidgets.QGroupBox(self.centralWidget)
        self.Pump_A.setGeometry(QtCore.QRect(20, 30, 850, 850))
        self.Pump_A.setMaximumSize(QtCore.QSize(850, 850))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Pump_A.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Pump_A.setFont(font)
        self.Pump_A.setMouseTracking(False)
        self.Pump_A.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Pump_A.setAcceptDrops(False)
        self.Pump_A.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Pump_A.setAutoFillBackground(False)
        self.Pump_A.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"")
        self.Pump_A.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Pump_A.setFlat(True)
        self.Pump_A.setCheckable(False)
        self.Pump_A.setChecked(False)
        self.Pump_A.setObjectName("Pump_A")
        self.staticFlow_pumpA = QtWidgets.QGroupBox(self.Pump_A)
        self.staticFlow_pumpA.setGeometry(QtCore.QRect(30, 155, 780, 215))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.staticFlow_pumpA.setFont(font)
        self.staticFlow_pumpA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.staticFlow_pumpA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.staticFlow_pumpA.setCheckable(True)
        self.staticFlow_pumpA.setChecked(False)
        self.staticFlow_pumpA.setObjectName("staticFlow_pumpA")
        self.labelStatic_flowRate_pumpA = QtWidgets.QLabel(self.staticFlow_pumpA)
        self.labelStatic_flowRate_pumpA.setGeometry(QtCore.QRect(90, 72, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelStatic_flowRate_pumpA.setFont(font)
        self.labelStatic_flowRate_pumpA.setObjectName("labelStatic_flowRate_pumpA")
        self.labelStatic_runTime_pumpA = QtWidgets.QLabel(self.staticFlow_pumpA)
        self.labelStatic_runTime_pumpA.setGeometry(QtCore.QRect(500, 72, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelStatic_runTime_pumpA.setFont(font)
        self.labelStatic_runTime_pumpA.setObjectName("labelStatic_runTime_pumpA")
        self.flow_rate_pumpA = QtWidgets.QDoubleSpinBox(self.staticFlow_pumpA)
        self.flow_rate_pumpA.setGeometry(QtCore.QRect(90, 115, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.flow_rate_pumpA.setFont(font)
        self.flow_rate_pumpA.setMaximum(12000.0)
        self.flow_rate_pumpA.setSingleStep(0.01)
        self.flow_rate_pumpA.setObjectName("flow_rate_pumpA")
        self.run_time_pumpA = QtWidgets.QDoubleSpinBox(self.staticFlow_pumpA)
        self.run_time_pumpA.setGeometry(QtCore.QRect(480, 115, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.run_time_pumpA.setFont(font)
        self.run_time_pumpA.setMaximum(12000.0)
        self.run_time_pumpA.setSingleStep(0.01)
        self.run_time_pumpA.setObjectName("run_time_pumpA")
        self.progressBar_staticFlow_pumpA = QtWidgets.QProgressBar(self.staticFlow_pumpA)
        self.progressBar_staticFlow_pumpA.setGeometry(QtCore.QRect(320, 5, 450, 55))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.progressBar_staticFlow_pumpA.setFont(font)
        self.progressBar_staticFlow_pumpA.setProperty("value", 0)
        self.progressBar_staticFlow_pumpA.setObjectName("progressBar_staticFlow_pumpA")
        self.dynamicFlow_pumpA = QtWidgets.QGroupBox(self.Pump_A)
        self.dynamicFlow_pumpA.setGeometry(QtCore.QRect(30, 390, 780, 310))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dynamicFlow_pumpA.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dynamicFlow_pumpA.setFont(font)
        self.dynamicFlow_pumpA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dynamicFlow_pumpA.setCheckable(True)
        self.dynamicFlow_pumpA.setChecked(False)
        self.dynamicFlow_pumpA.setObjectName("dynamicFlow_pumpA")
        self.labelDynamic_from_pumpA = QtWidgets.QLabel(self.dynamicFlow_pumpA)
        self.labelDynamic_from_pumpA.setGeometry(QtCore.QRect(50, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_from_pumpA.setFont(font)
        self.labelDynamic_from_pumpA.setStyleSheet("color: rgb(0, 0, 0);")
        self.labelDynamic_from_pumpA.setObjectName("labelDynamic_from_pumpA")
        self.labelDynamic_to_pumpA = QtWidgets.QLabel(self.dynamicFlow_pumpA)
        self.labelDynamic_to_pumpA.setGeometry(QtCore.QRect(470, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_to_pumpA.setFont(font)
        self.labelDynamic_to_pumpA.setStyleSheet("color: rgb(0, 0, 0);")
        self.labelDynamic_to_pumpA.setObjectName("labelDynamic_to_pumpA")
        self.labelDynamic_startFRate_pumpA = QtWidgets.QLabel(self.dynamicFlow_pumpA)
        self.labelDynamic_startFRate_pumpA.setGeometry(QtCore.QRect(90, 72, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_startFRate_pumpA.setFont(font)
        self.labelDynamic_startFRate_pumpA.setObjectName("labelDynamic_startFRate_pumpA")
        self.labelDynamic_endFRate_pumpA = QtWidgets.QLabel(self.dynamicFlow_pumpA)
        self.labelDynamic_endFRate_pumpA.setGeometry(QtCore.QRect(475, 72, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_endFRate_pumpA.setFont(font)
        self.labelDynamic_endFRate_pumpA.setObjectName("labelDynamic_endFRate_pumpA")
        self.labelDynamic_sweep_pumpA = QtWidgets.QLabel(self.dynamicFlow_pumpA)
        self.labelDynamic_sweep_pumpA.setGeometry(QtCore.QRect(20, 230, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_sweep_pumpA.setFont(font)
        self.labelDynamic_sweep_pumpA.setObjectName("labelDynamic_sweep_pumpA")
        self.flowRate_start_pumpA = QtWidgets.QDoubleSpinBox(self.dynamicFlow_pumpA)
        self.flowRate_start_pumpA.setGeometry(QtCore.QRect(140, 110, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.flowRate_start_pumpA.setFont(font)
        self.flowRate_start_pumpA.setMaximum(12000.0)
        self.flowRate_start_pumpA.setSingleStep(0.01)
        self.flowRate_start_pumpA.setObjectName("flowRate_start_pumpA")
        self.flowRate_end_pumpA = QtWidgets.QDoubleSpinBox(self.dynamicFlow_pumpA)
        self.flowRate_end_pumpA.setGeometry(QtCore.QRect(530, 110, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.flowRate_end_pumpA.setFont(font)
        self.flowRate_end_pumpA.setMaximum(12000.0)
        self.flowRate_end_pumpA.setSingleStep(0.01)
        self.flowRate_end_pumpA.setObjectName("flowRate_end_pumpA")
        self.dynamic_sweepRate_pumpA = QtWidgets.QDoubleSpinBox(self.dynamicFlow_pumpA)
        self.dynamic_sweepRate_pumpA.setGeometry(QtCore.QRect(345, 210, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.dynamic_sweepRate_pumpA.setFont(font)
        self.dynamic_sweepRate_pumpA.setMinimum(-12000.0)
        self.dynamic_sweepRate_pumpA.setMaximum(12000.0)
        self.dynamic_sweepRate_pumpA.setSingleStep(0.01)
        self.dynamic_sweepRate_pumpA.setObjectName("dynamic_sweepRate_pumpA")
        self.progressBar_dynamicFlow_pumpA = QtWidgets.QProgressBar(self.dynamicFlow_pumpA)
        self.progressBar_dynamicFlow_pumpA.setGeometry(QtCore.QRect(320, 5, 450, 55))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_dynamicFlow_pumpA.setFont(font)
        self.progressBar_dynamicFlow_pumpA.setProperty("value", 0)
        self.progressBar_dynamicFlow_pumpA.setObjectName("progressBar_dynamicFlow_pumpA")
        self.customFlow_pumpA = QtWidgets.QGroupBox(self.Pump_A)
        self.customFlow_pumpA.setGeometry(QtCore.QRect(30, 720, 780, 115))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.customFlow_pumpA.setFont(font)
        self.customFlow_pumpA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.customFlow_pumpA.setCheckable(True)
        self.customFlow_pumpA.setChecked(False)
        self.customFlow_pumpA.setObjectName("customFlow_pumpA")
        self.upload_pumpA = QtWidgets.QPushButton(self.customFlow_pumpA)
        self.upload_pumpA.setGeometry(QtCore.QRect(90, 68, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.upload_pumpA.setFont(font)
        self.upload_pumpA.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.upload_pumpA.setObjectName("upload_pumpA")
        self.progressBar_customFlow_pumpA = QtWidgets.QProgressBar(self.customFlow_pumpA)
        self.progressBar_customFlow_pumpA.setGeometry(QtCore.QRect(320, 5, 450, 55))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_customFlow_pumpA.setFont(font)
        self.progressBar_customFlow_pumpA.setProperty("value", 0)
        self.progressBar_customFlow_pumpA.setObjectName("progressBar_customFlow_pumpA")
        self.ON_btn_pumpA = QtWidgets.QPushButton(self.Pump_A)
        self.ON_btn_pumpA.setGeometry(QtCore.QRect(50, 30, 230, 110))
        self.ON_btn_pumpA.setMaximumSize(QtCore.QSize(230, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ON_btn_pumpA.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ON_btn_pumpA.setFont(font)
        self.ON_btn_pumpA.setMouseTracking(True)
        self.ON_btn_pumpA.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ON_btn_pumpA.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.ON_btn_pumpA.setCheckable(False)
        self.ON_btn_pumpA.setChecked(False)
        self.ON_btn_pumpA.setAutoDefault(False)
        self.ON_btn_pumpA.setDefault(False)
        self.ON_btn_pumpA.setFlat(False)
        self.ON_btn_pumpA.setObjectName("ON_btn_pumpA")
        self.OFF_btn_pumpA = QtWidgets.QPushButton(self.Pump_A)
        self.OFF_btn_pumpA.setGeometry(QtCore.QRect(580, 30, 230, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.OFF_btn_pumpA.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.OFF_btn_pumpA.setFont(font)
        self.OFF_btn_pumpA.setMouseTracking(True)
        self.OFF_btn_pumpA.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.OFF_btn_pumpA.setStyleSheet("background-color: rgb(200, 0, 0);\n"
"\n"
"\n"
"")
        self.OFF_btn_pumpA.setCheckable(False)
        self.OFF_btn_pumpA.setChecked(False)
        self.OFF_btn_pumpA.setObjectName("OFF_btn_pumpA")
        self.Pump_B = QtWidgets.QGroupBox(self.centralWidget)
        self.Pump_B.setGeometry(QtCore.QRect(930, 30, 850, 850))
        self.Pump_B.setMaximumSize(QtCore.QSize(850, 850))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Pump_B.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Pump_B.setFont(font)
        self.Pump_B.setAutoFillBackground(False)
        self.Pump_B.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.Pump_B.setAlignment(QtCore.Qt.AlignCenter)
        self.Pump_B.setFlat(True)
        self.Pump_B.setCheckable(False)
        self.Pump_B.setObjectName("Pump_B")
        self.staticFlow_pumpB = QtWidgets.QGroupBox(self.Pump_B)
        self.staticFlow_pumpB.setGeometry(QtCore.QRect(30, 155, 780, 215))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.staticFlow_pumpB.setFont(font)
        self.staticFlow_pumpB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.staticFlow_pumpB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.staticFlow_pumpB.setCheckable(True)
        self.staticFlow_pumpB.setChecked(False)
        self.staticFlow_pumpB.setObjectName("staticFlow_pumpB")
        self.labelStatic_flowRate_pumpB = QtWidgets.QLabel(self.staticFlow_pumpB)
        self.labelStatic_flowRate_pumpB.setGeometry(QtCore.QRect(90, 72, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelStatic_flowRate_pumpB.setFont(font)
        self.labelStatic_flowRate_pumpB.setObjectName("labelStatic_flowRate_pumpB")
        self.labelStatic_runTime_pumpB = QtWidgets.QLabel(self.staticFlow_pumpB)
        self.labelStatic_runTime_pumpB.setGeometry(QtCore.QRect(500, 72, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelStatic_runTime_pumpB.setFont(font)
        self.labelStatic_runTime_pumpB.setObjectName("labelStatic_runTime_pumpB")
        self.flow_rate_pumpB = QtWidgets.QDoubleSpinBox(self.staticFlow_pumpB)
        self.flow_rate_pumpB.setGeometry(QtCore.QRect(90, 115, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.flow_rate_pumpB.setFont(font)
        self.flow_rate_pumpB.setMaximum(12000.0)
        self.flow_rate_pumpB.setSingleStep(0.01)
        self.flow_rate_pumpB.setObjectName("flow_rate_pumpB")
        self.run_time_pumpB = QtWidgets.QDoubleSpinBox(self.staticFlow_pumpB)
        self.run_time_pumpB.setGeometry(QtCore.QRect(480, 115, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.run_time_pumpB.setFont(font)
        self.run_time_pumpB.setMaximum(12000.0)
        self.run_time_pumpB.setSingleStep(0.01)
        self.run_time_pumpB.setObjectName("run_time_pumpB")
        self.progressBar_staticFlow_pumpB = QtWidgets.QProgressBar(self.staticFlow_pumpB)
        self.progressBar_staticFlow_pumpB.setGeometry(QtCore.QRect(320, 5, 450, 55))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_staticFlow_pumpB.setFont(font)
        self.progressBar_staticFlow_pumpB.setProperty("value", 0)
        self.progressBar_staticFlow_pumpB.setObjectName("progressBar_staticFlow_pumpB")
        self.customFlow_pumpB = QtWidgets.QGroupBox(self.Pump_B)
        self.customFlow_pumpB.setGeometry(QtCore.QRect(30, 720, 780, 115))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.customFlow_pumpB.setFont(font)
        self.customFlow_pumpB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.customFlow_pumpB.setCheckable(True)
        self.customFlow_pumpB.setChecked(False)
        self.customFlow_pumpB.setObjectName("customFlow_pumpB")
        self.upload_pumpB = QtWidgets.QPushButton(self.customFlow_pumpB)
        self.upload_pumpB.setGeometry(QtCore.QRect(90, 68, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.upload_pumpB.setFont(font)
        self.upload_pumpB.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.upload_pumpB.setObjectName("upload_pumpB")
        self.progressBar_customFlow_pumpB = QtWidgets.QProgressBar(self.customFlow_pumpB)
        self.progressBar_customFlow_pumpB.setGeometry(QtCore.QRect(320, 5, 450, 55))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_customFlow_pumpB.setFont(font)
        self.progressBar_customFlow_pumpB.setProperty("value", 0)
        self.progressBar_customFlow_pumpB.setObjectName("progressBar_customFlow_pumpB")
        self.ON_btn_pumpB = QtWidgets.QPushButton(self.Pump_B)
        self.ON_btn_pumpB.setGeometry(QtCore.QRect(50, 30, 230, 110))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ON_btn_pumpB.setFont(font)
        self.ON_btn_pumpB.setMouseTracking(True)
        self.ON_btn_pumpB.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ON_btn_pumpB.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.ON_btn_pumpB.setCheckable(False)
        self.ON_btn_pumpB.setChecked(False)
        self.ON_btn_pumpB.setAutoRepeat(False)
        self.ON_btn_pumpB.setObjectName("ON_btn_pumpB")
        self.OFF_btn_pumpB_2 = QtWidgets.QPushButton(self.Pump_B)
        self.OFF_btn_pumpB_2.setGeometry(QtCore.QRect(580, 30, 230, 110))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.OFF_btn_pumpB_2.setFont(font)
        self.OFF_btn_pumpB_2.setMouseTracking(True)
        self.OFF_btn_pumpB_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.OFF_btn_pumpB_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.OFF_btn_pumpB_2.setStyleSheet("background-color: rgb(200, 0, 0);")
        self.OFF_btn_pumpB_2.setCheckable(False)
        self.OFF_btn_pumpB_2.setChecked(False)
        self.OFF_btn_pumpB_2.setObjectName("OFF_btn_pumpB_2")
        self.dynamicFlow_pumpB = QtWidgets.QGroupBox(self.Pump_B)
        self.dynamicFlow_pumpB.setGeometry(QtCore.QRect(30, 390, 780, 310))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dynamicFlow_pumpB.setFont(font)
        self.dynamicFlow_pumpB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dynamicFlow_pumpB.setCheckable(True)
        self.dynamicFlow_pumpB.setChecked(False)
        self.dynamicFlow_pumpB.setObjectName("dynamicFlow_pumpB")
        self.labelDynamic_from_pumpB = QtWidgets.QLabel(self.dynamicFlow_pumpB)
        self.labelDynamic_from_pumpB.setGeometry(QtCore.QRect(50, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_from_pumpB.setFont(font)
        self.labelDynamic_from_pumpB.setStyleSheet("color: rgb(0, 0, 0);")
        self.labelDynamic_from_pumpB.setObjectName("labelDynamic_from_pumpB")
        self.labelDynamic_to_pumpB = QtWidgets.QLabel(self.dynamicFlow_pumpB)
        self.labelDynamic_to_pumpB.setGeometry(QtCore.QRect(470, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_to_pumpB.setFont(font)
        self.labelDynamic_to_pumpB.setStyleSheet("color: rgb(0, 0, 0);")
        self.labelDynamic_to_pumpB.setObjectName("labelDynamic_to_pumpB")
        self.labelDynamic_startFRate_pumpB = QtWidgets.QLabel(self.dynamicFlow_pumpB)
        self.labelDynamic_startFRate_pumpB.setGeometry(QtCore.QRect(90, 72, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_startFRate_pumpB.setFont(font)
        self.labelDynamic_startFRate_pumpB.setObjectName("labelDynamic_startFRate_pumpB")
        self.labelDynamic_endFRate_pumpB = QtWidgets.QLabel(self.dynamicFlow_pumpB)
        self.labelDynamic_endFRate_pumpB.setGeometry(QtCore.QRect(475, 72, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_endFRate_pumpB.setFont(font)
        self.labelDynamic_endFRate_pumpB.setObjectName("labelDynamic_endFRate_pumpB")
        self.labelDynamic_sweep_pumpB = QtWidgets.QLabel(self.dynamicFlow_pumpB)
        self.labelDynamic_sweep_pumpB.setGeometry(QtCore.QRect(20, 230, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelDynamic_sweep_pumpB.setFont(font)
        self.labelDynamic_sweep_pumpB.setObjectName("labelDynamic_sweep_pumpB")
        self.flowRate_start_pumpB = QtWidgets.QDoubleSpinBox(self.dynamicFlow_pumpB)
        self.flowRate_start_pumpB.setGeometry(QtCore.QRect(140, 110, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.flowRate_start_pumpB.setFont(font)
        self.flowRate_start_pumpB.setMaximum(12000.0)
        self.flowRate_start_pumpB.setSingleStep(0.01)
        self.flowRate_start_pumpB.setObjectName("flowRate_start_pumpB")
        self.flowRate_end_pumpB = QtWidgets.QDoubleSpinBox(self.dynamicFlow_pumpB)
        self.flowRate_end_pumpB.setGeometry(QtCore.QRect(530, 110, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.flowRate_end_pumpB.setFont(font)
        self.flowRate_end_pumpB.setMaximum(12000.0)
        self.flowRate_end_pumpB.setSingleStep(0.01)
        self.flowRate_end_pumpB.setObjectName("flowRate_end_pumpB")
        self.dynamic_sweepRate_pumpB = QtWidgets.QDoubleSpinBox(self.dynamicFlow_pumpB)
        self.dynamic_sweepRate_pumpB.setGeometry(QtCore.QRect(345, 210, 230, 90))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.dynamic_sweepRate_pumpB.setFont(font)
        self.dynamic_sweepRate_pumpB.setMinimum(-12000.0)
        self.dynamic_sweepRate_pumpB.setMaximum(12000.0)
        self.dynamic_sweepRate_pumpB.setSingleStep(0.01)
        self.dynamic_sweepRate_pumpB.setObjectName("dynamic_sweepRate_pumpB")
        self.progressBar_dynamicFlow_pumpB = QtWidgets.QProgressBar(self.dynamicFlow_pumpB)
        self.progressBar_dynamicFlow_pumpB.setGeometry(QtCore.QRect(320, 5, 450, 55))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_dynamicFlow_pumpB.setFont(font)
        self.progressBar_dynamicFlow_pumpB.setProperty("value", 0)
        self.progressBar_dynamicFlow_pumpB.setObjectName("progressBar_dynamicFlow_pumpB")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(890, 0, 20, 900))
        self.line.setMaximumSize(QtCore.QSize(50, 900))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(10)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Pump_A.setTitle(_translate("MainWindow", "Pump A"))
        self.staticFlow_pumpA.setTitle(_translate("MainWindow", "Static Flow"))
        self.labelStatic_flowRate_pumpA.setText(_translate("MainWindow", "Flow Rate (uL / Min)"))
        self.labelStatic_runTime_pumpA.setText(_translate("MainWindow", "Run Time (Sec)"))
        self.dynamicFlow_pumpA.setTitle(_translate("MainWindow", "Dynamic Flow"))
        self.labelDynamic_from_pumpA.setText(_translate("MainWindow", "FROM:"))
        self.labelDynamic_to_pumpA.setText(_translate("MainWindow", " TO:"))
        self.labelDynamic_startFRate_pumpA.setText(_translate("MainWindow", "Start Flow Rate (uL/ Min)"))
        self.labelDynamic_endFRate_pumpA.setText(_translate("MainWindow", "End Flow Rate (uL/ Min)"))
        self.labelDynamic_sweep_pumpA.setText(_translate("MainWindow", "Sweep Rate (uL/ Min)"))
        self.customFlow_pumpA.setTitle(_translate("MainWindow", "Custom Flow"))
        self.upload_pumpA.setText(_translate("MainWindow", "Upload CSV File"))
        self.ON_btn_pumpA.setText(_translate("MainWindow", "ON"))
        self.OFF_btn_pumpA.setText(_translate("MainWindow", "OFF"))
        self.Pump_B.setTitle(_translate("MainWindow", "Pump B"))
        self.staticFlow_pumpB.setTitle(_translate("MainWindow", "Static Flow"))
        self.labelStatic_flowRate_pumpB.setText(_translate("MainWindow", "Flow Rate (uL / Min)"))
        self.labelStatic_runTime_pumpB.setText(_translate("MainWindow", "Run Time (Sec)"))
        self.customFlow_pumpB.setTitle(_translate("MainWindow", "Custom Flow"))
        self.upload_pumpB.setText(_translate("MainWindow", "Upload CSV File"))
        self.ON_btn_pumpB.setText(_translate("MainWindow", "ON"))
        self.OFF_btn_pumpB_2.setText(_translate("MainWindow", "OFF"))
        self.dynamicFlow_pumpB.setTitle(_translate("MainWindow", "Dynamic Flow"))
        self.labelDynamic_from_pumpB.setText(_translate("MainWindow", "FROM:"))
        self.labelDynamic_to_pumpB.setText(_translate("MainWindow", " TO:"))
        self.labelDynamic_startFRate_pumpB.setText(_translate("MainWindow", "Start Flow Rate (uL/ Min)"))
        self.labelDynamic_endFRate_pumpB.setText(_translate("MainWindow", "End Flow Rate (uL/ Min)"))
        self.labelDynamic_sweep_pumpB.setText(_translate("MainWindow", "Sweep Rate (uL/ Min)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
