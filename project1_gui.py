# Form implementation generated from reading ui file 'project1_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_remote(object):
    def setupUi(self, remote):
        remote.setObjectName("remote")
        remote.setEnabled(True)
        remote.resize(440, 707)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(remote.sizePolicy().hasHeightForWidth())
        remote.setSizePolicy(sizePolicy)
        remote.setAutoFillBackground(True)
        remote.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.slider_volume = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_volume.setGeometry(QtCore.QRect(59, 330, 321, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_volume.sizePolicy().hasHeightForWidth())
        self.slider_volume.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        self.slider_volume.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.slider_volume.setFont(font)
        self.slider_volume.setAutoFillBackground(False)
        self.slider_volume.setMaximum(9)
        self.slider_volume.setProperty("value", 0)
        self.slider_volume.setSliderPosition(0)
        self.slider_volume.setTracking(True)
        self.slider_volume.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_volume.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.slider_volume.setTickInterval(1)
        self.slider_volume.setObjectName("slider_channel")
        self.button_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_power.setGeometry(QtCore.QRect(70, 610, 111, 61))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.button_power.setFont(font)
        self.button_power.setObjectName("button_power")
        self.button_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_mute.setGeometry(QtCore.QRect(260, 610, 111, 61))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.button_mute.setFont(font)
        self.button_mute.setObjectName("button_mute")
        self.button_volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_up.setGeometry(QtCore.QRect(30, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_volume_up.setFont(font)
        self.button_volume_up.setAutoFillBackground(False)
        self.button_volume_up.setObjectName("button_volume_up")
        self.button_volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_down.setGeometry(QtCore.QRect(30, 500, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_volume_down.setFont(font)
        self.button_volume_down.setObjectName("button_volume_down")
        self.button_channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_up.setGeometry(QtCore.QRect(340, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_channel_up.setFont(font)
        self.button_channel_up.setObjectName("button_channel_up")
        self.button_channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_down.setGeometry(QtCore.QRect(340, 510, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_channel_down.setFont(font)
        self.button_channel_down.setObjectName("button_channel_down")
        self.button_channel_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_0.setGeometry(QtCore.QRect(120, 400, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_0.setFont(font)
        self.button_channel_0.setObjectName("button_channel_0")
        self.button_channel_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_1.setGeometry(QtCore.QRect(190, 400, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_1.setFont(font)
        self.button_channel_1.setObjectName("button_channel_1")
        self.button_channel_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_2.setGeometry(QtCore.QRect(260, 400, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_2.setFont(font)
        self.button_channel_2.setObjectName("button_channel_2")
        self.button_channel_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_5.setGeometry(QtCore.QRect(260, 470, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_5.setFont(font)
        self.button_channel_5.setObjectName("button_channel_5")
        self.button_channel_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_4.setGeometry(QtCore.QRect(190, 470, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_4.setFont(font)
        self.button_channel_4.setObjectName("button_channel_4")
        self.button_channel_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_3.setGeometry(QtCore.QRect(120, 470, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_3.setFont(font)
        self.button_channel_3.setObjectName("button_channel_3")
        self.button_channel_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_8.setGeometry(QtCore.QRect(260, 540, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_8.setFont(font)
        self.button_channel_8.setObjectName("button_channel_8")
        self.button_channel_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_7.setGeometry(QtCore.QRect(190, 540, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_7.setFont(font)
        self.button_channel_7.setObjectName("button_channel_7")
        self.button_channel_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_6.setGeometry(QtCore.QRect(120, 540, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_6.setFont(font)
        self.button_channel_6.setObjectName("button_channel_6")
        self.button_channel_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_9.setGeometry(QtCore.QRect(190, 610, 61, 61))
        font = QtGui.QFont()
        font.setFamily("New Gulim")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_channel_9.setFont(font)
        self.button_channel_9.setObjectName("button_channel_9")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 381, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.image_0 = QtWidgets.QLabel(parent=self.frame)
        self.image_0.setGeometry(QtCore.QRect(10, 10, 361, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_0.sizePolicy().hasHeightForWidth())
        self.image_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.image_0.setFont(font)
        self.image_0.setAutoFillBackground(True)
        self.image_0.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.image_0.setText("")
        self.image_0.setPixmap(QtGui.QPixmap("images\KETV logo.jpg")) #change image
        self.image_0.setScaledContents(True)
        self.image_0.setWordWrap(False)
        self.image_0.setObjectName("image_0")
        self.slider_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.slider_label.setGeometry(QtCore.QRect(60, 356, 321, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.slider_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.slider_label.setFont(font)
        self.slider_label.setAutoFillBackground(False)
        self.slider_label.setObjectName("slider_label")
        remote.setCentralWidget(self.centralwidget)

        self.retranslateUi(remote)
        QtCore.QMetaObject.connectSlotsByName(remote)

    def retranslateUi(self, remote):
        _translate = QtCore.QCoreApplication.translate
        remote.setWindowTitle(_translate("remote", "TV Remote"))
        self.button_power.setText(_translate("remote", "Power"))
        self.button_mute.setText(_translate("remote", "Mute"))
        self.button_volume_up.setText(_translate("remote", "Volume\n"
"Up"))
        self.button_volume_down.setText(_translate("remote", "Volume\n"
"Down"))
        self.button_channel_up.setText(_translate("remote", "Channel\n"
"Up"))
        self.button_channel_down.setText(_translate("remote", "Channel\n"
"Down"))
        self.button_channel_0.setText(_translate("remote", "0"))
        self.button_channel_1.setText(_translate("remote", "1"))
        self.button_channel_2.setText(_translate("remote", "2"))
        self.button_channel_5.setText(_translate("remote", "5"))
        self.button_channel_4.setText(_translate("remote", "4"))
        self.button_channel_3.setText(_translate("remote", "3"))
        self.button_channel_8.setText(_translate("remote", "8"))
        self.button_channel_7.setText(_translate("remote", "7"))
        self.button_channel_6.setText(_translate("remote", "6"))
        self.button_channel_9.setText(_translate("remote", "9"))
        self.slider_label.setText(_translate("remote", " 0         1         2         3         4         5         6         7         8         9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remote = QtWidgets.QMainWindow()
    ui = Ui_remote()
    ui.setupUi(remote)
    remote.show()
    sys.exit(app.exec())
