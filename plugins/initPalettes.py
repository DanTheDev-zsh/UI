from PyQt5 import QtCore, QtGui


# for initializing color schemes for text and background/etc
def initPalettes(self):
    self.paletteBlue = QtGui.QPalette()
    self.paletteRed = QtGui.QPalette()
    self.paletteGreen = QtGui.QPalette()
    self.paletteBlack = QtGui.QPalette()
    self.backgroundPaletteLightGrayTextBlue = QtGui.QPalette()
    self.mainBackgroundPalette = QtGui.QPalette()

    brushLightGray = QtGui.QBrush(QtGui.QColor(130, 130, 130))
    brushLightGray.setStyle(QtCore.Qt.SolidPattern)
    brushGray = QtGui.QBrush(QtGui.QColor(120, 120, 120))
    brushGray.setStyle(QtCore.Qt.SolidPattern)
    brushBlue = QtGui.QBrush(QtGui.QColor(0, 0, 255))
    brushBlue.setStyle(QtCore.Qt.SolidPattern)
    brushRed = QtGui.QBrush(QtGui.QColor(255, 0, 0))
    brushRed.setStyle(QtCore.Qt.SolidPattern)
    brushGreen = QtGui.QBrush(QtGui.QColor(187, 240, 202))
    brushGreen.setStyle(QtCore.Qt.SolidPattern)
    brushBlack = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brushBlack.setStyle(QtCore.Qt.SolidPattern)
    brushDark = QtGui.QBrush(QtGui.QColor(37, 37, 37))
    brushDark.setStyle(QtCore.Qt.SolidPattern)
    brushWhite = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brushWhite.setStyle(QtCore.Qt.SolidPattern)

    self.paletteBlue.setBrush(
        QtGui.QPalette.Active, QtGui.QPalette.WindowText, brushBlue
    )
    self.paletteBlue.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brushBlue
    )
    self.paletteBlue.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brushGray
    )
    self.paletteRed.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brushRed)
    self.paletteRed.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brushRed
    )
    self.paletteRed.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brushGray
    )
    self.paletteGreen.setBrush(
        QtGui.QPalette.Active, QtGui.QPalette.WindowText, brushGreen
    )
    self.paletteGreen.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brushGreen
    )
    self.paletteGreen.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brushGray
    )
    self.paletteBlack.setBrush(
        QtGui.QPalette.Active, QtGui.QPalette.WindowText, brushBlack
    )
    self.paletteBlack.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brushBlack
    )
    self.paletteBlack.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brushGray
    )
    self.backgroundPaletteLightGrayTextBlue.setBrush(
        QtGui.QPalette.Active, QtGui.QPalette.Window, brushLightGray
    )
    self.backgroundPaletteLightGrayTextBlue.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.Window, brushLightGray
    )
    self.backgroundPaletteLightGrayTextBlue.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.Window, brushLightGray
    )
    self.backgroundPaletteLightGrayTextBlue.setBrush(
        QtGui.QPalette.Active, QtGui.QPalette.WindowText, brushBlue
    )
    self.backgroundPaletteLightGrayTextBlue.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brushBlue
    )
    self.backgroundPaletteLightGrayTextBlue.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brushGray
    )
    self.mainBackgroundPalette.setBrush(
        QtGui.QPalette.Active, QtGui.QPalette.Window, brushDark
    )
    self.mainBackgroundPalette.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.Window, brushDark
    )
    self.mainBackgroundPalette.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.Window, brushDark
    )
    self.mainBackgroundPalette.setBrush(
        QtGui.QPalette.Active, QtGui.QPalette.WindowText, brushWhite
    )
    self.mainBackgroundPalette.setBrush(
        QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brushWhite
    )
    self.mainBackgroundPalette.setBrush(
        QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brushWhite
    )
