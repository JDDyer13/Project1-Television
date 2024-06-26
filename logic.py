from PyQt6.QtWidgets import *
from project1_gui import *

MIN_VOLUME = 0
MAX_VOLUME = 9
MIN_CHANNEL = 0
MAX_CHANNEL = 9


class Logic(QMainWindow, Ui_remote):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_channel_up.clicked.connect(lambda: self.channel_up())
        self.button_channel_down.clicked.connect(lambda: self.channel_down())
        self.button_volume_up.clicked.connect(lambda: self.volume_up())
        self.button_volume_down.clicked.connect(lambda: self.volume_down())
        self.button_channel_0.clicked.connect(lambda: self.channel0())
        self.button_channel_1.clicked.connect(lambda: self.channel1())
        self.button_channel_2.clicked.connect(lambda: self.channel2())
        self.button_channel_3.clicked.connect(lambda: self.channel3())
        self.button_channel_4.clicked.connect(lambda: self.channel4())
        self.button_channel_5.clicked.connect(lambda: self.channel5())
        self.button_channel_6.clicked.connect(lambda: self.channel6())
        self.button_channel_7.clicked.connect(lambda: self.channel7())
        self.button_channel_8.clicked.connect(lambda: self.channel8())
        self.button_channel_9.clicked.connect(lambda: self.channel9())
        self.slider_volume.valueChanged.connect(lambda: self.volume_slide())

        self.__power = True
        self.__muted = False
        self.__volume = MIN_VOLUME
        self.__channel = MIN_CHANNEL

    def power(self):
        '''
         This function will change the power variable, disable/enable the slider
         and show/hide the image
        '''
        if self.__power:
            self.__power = False
            self.image_0.hide()
            self.slider_volume.setDisabled(True)
        else:
            self.__power = True
            self.image_0.show()
            self.slider_volume.setDisabled(False)

    def mute(self):
        '''
        This function will change the mute variable and disable/enable the slider
        '''
        if self.__power:
            if self.__muted:
                self.__muted = False
                self.slider_volume.setDisabled(False)
            else:
                self.__muted = True
                self.slider_volume.setDisabled(True)

    def channel_up(self):
        '''
        This function will raise the channel by one, if the channel is maximum it will
        set to minimum. If needed as long as the power is set to True
        '''
        if self.__power:
            if self.__channel == MAX_CHANNEL:
                self.__channel = MIN_CHANNEL
            else:
                self.__channel += 1
            self.channel_image()

    def channel_down(self):
        '''
        This function will lower the channel by one, if the channel is at minimum it will
        set to maximum. If needed as long as the power is set to True
        '''
        if self.__power:
            if self.__channel == MIN_CHANNEL:
                self.__channel = MAX_CHANNEL
            else:
                self.__channel -= 1
            self.channel_image()

    def volume_up(self):
        '''
        This function will raise the volume by one and unmute the tv if needed
        as long as the power is set to True
        '''
        if self.__power:
            if self.__muted:
                self.mute()
            if self.__volume == MAX_VOLUME:
                return None
            else:
                self.__volume += 1
                self.slider_volume.setValue(self.__volume)

    def volume_down(self):
        '''
        This function will lower the volume by one and unmute the tv if needed
        as long as the power is set to True
        '''
        if self.__power:
            if self.__muted:
                self.mute()
            if self.__volume == MIN_VOLUME:
                return None
            else:
                self.__volume -= 1
                self.slider_volume.setValue(self.__volume)

    def volume_slide(self):
        '''
        This function changes the volume if the slider is moved
        '''
        self.__volume = self.slider_volume.value()

    def channel0(self):
        '''
        This function sets the channel to 0
        '''
        if self.__power:
            self.__channel = 0
            self.channel_image()

    def channel1(self):
        '''
        This function sets the channel to 1
        '''
        if self.__power:
            self.__channel = 1
            self.channel_image()

    def channel2(self):
        '''
        This function sets the channel to 2
        '''
        if self.__power:
            self.__channel = 2
            self.channel_image()

    def channel3(self):
        '''
        This function sets the channel to 3
        '''
        if self.__power:
            self.__channel = 3
            self.channel_image()

    def channel4(self):
        '''
        This function sets the channel to 4
        '''
        if self.__power:
            self.__channel = 4
            self.channel_image()

    def channel5(self):
        '''
        This function sets the channel to 5
        '''
        if self.__power:
            self.__channel = 5
            self.channel_image()

    def channel6(self):
        '''
        This function sets the channel to 6
        '''
        if self.__power:
            self.__channel = 6
            self.channel_image()

    def channel7(self):
        '''
        This function sets the channel to 7
        '''
        if self.__power:
            self.__channel = 7
            self.channel_image()

    def channel8(self):
        '''
        This function sets the channel to 8
        '''
        if self.__power:
            self.__channel = 8
            self.channel_image()

    def channel9(self):
        '''
        This function sets the channel to 9
        '''
        if self.__power:
            self.__channel = 9
            self.channel_image()

    def channel_image(self):
        '''
        This function sets the image depending on the channel number when called
        '''
        if self.__channel == 0:
            self.image_0.setPixmap(QtGui.QPixmap("images\KETV logo.jpg"))
        elif self.__channel == 1:
            self.image_0.setPixmap(QtGui.QPixmap("images\CBS logo.png"))
        elif self.__channel == 2:
            self.image_0.setPixmap(QtGui.QPixmap("images\\NBC logo.png"))
        elif self.__channel == 3:
            self.image_0.setPixmap(QtGui.QPixmap("images\ESPN logo.jpg"))
        elif self.__channel == 4:
            self.image_0.setPixmap(QtGui.QPixmap("images\\Nickelodeon logo.png"))
        elif self.__channel == 5:
            self.image_0.setPixmap(QtGui.QPixmap("images\Disney logo.jpg"))
        elif self.__channel == 6:
            self.image_0.setPixmap(QtGui.QPixmap("images\Cartoon Network logo.png"))
        elif self.__channel == 7:
            self.image_0.setPixmap(QtGui.QPixmap("images\History Channel logo.jpg"))
        elif self.__channel == 8:
            self.image_0.setPixmap(QtGui.QPixmap("images\Discovery Channel logo.png"))
        elif self.__channel == 9:
            self.image_0.setPixmap(QtGui.QPixmap("images\HBO logo.jpeg"))
