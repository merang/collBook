# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settingsUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingsWindow(object):
    def setupUi(self, settingsWindow):
        settingsWindow.setObjectName("settingsWindow")
        settingsWindow.resize(595, 641)
        settingsWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(settingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upperHorizontalLayout = QtWidgets.QHBoxLayout()
        self.upperHorizontalLayout.setObjectName("upperHorizontalLayout")
        self.selectionWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectionWidget.sizePolicy().hasHeightForWidth())
        self.selectionWidget.setSizePolicy(sizePolicy)
        self.selectionWidget.setLineWidth(1)
        self.selectionWidget.setObjectName("selectionWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setItalic(False)
        item.setFont(font)
        self.selectionWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.selectionWidget.addItem(item)
        self.upperHorizontalLayout.addWidget(self.selectionWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.labelPrefPage = QtWidgets.QWidget()
        self.labelPrefPage.setObjectName("labelPrefPage")
        self.gridLayout = QtWidgets.QGridLayout(self.labelPrefPage)
        self.gridLayout.setObjectName("gridLayout")
        self.labelDimentionsGroup = QtWidgets.QGroupBox(self.labelPrefPage)
        self.labelDimentionsGroup.setObjectName("labelDimentionsGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.labelDimentionsGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.yLabel = QtWidgets.QLabel(self.labelDimentionsGroup)
        self.yLabel.setObjectName("yLabel")
        self.gridLayout_5.addWidget(self.yLabel, 0, 2, 1, 1)
        self.xLabel = QtWidgets.QLabel(self.labelDimentionsGroup)
        self.xLabel.setObjectName("xLabel")
        self.gridLayout_5.addWidget(self.xLabel, 0, 0, 1, 1)
        self.value_X = QtWidgets.QSpinBox(self.labelDimentionsGroup)
        self.value_X.setMinimum(1)
        self.value_X.setMaximum(9999)
        self.value_X.setObjectName("value_X")
        self.gridLayout_5.addWidget(self.value_X, 1, 0, 1, 1)
        self.value_Y = QtWidgets.QSpinBox(self.labelDimentionsGroup)
        self.value_Y.setMinimum(1)
        self.value_Y.setMaximum(9999)
        self.value_Y.setObjectName("value_Y")
        self.gridLayout_5.addWidget(self.value_Y, 1, 2, 1, 1)
        self.relFontLabell = QtWidgets.QLabel(self.labelDimentionsGroup)
        self.relFontLabell.setObjectName("relFontLabell")
        self.gridLayout_5.addWidget(self.relFontLabell, 0, 3, 1, 1)
        self.value_RelFont = QtWidgets.QSpinBox(self.labelDimentionsGroup)
        self.value_RelFont.setProperty("value", 12)
        self.value_RelFont.setObjectName("value_RelFont")
        self.gridLayout_5.addWidget(self.value_RelFont, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.labelDimentionsGroup, 0, 0, 1, 1)
        self.labelIncludeGroup = QtWidgets.QGroupBox(self.labelPrefPage)
        self.labelIncludeGroup.setObjectName("labelIncludeGroup")
        self.formLayout_3 = QtWidgets.QFormLayout(self.labelIncludeGroup)
        self.formLayout_3.setObjectName("formLayout_3")
        self.value_inc_Associated = QtWidgets.QCheckBox(self.labelIncludeGroup)
        self.value_inc_Associated.setChecked(True)
        self.value_inc_Associated.setObjectName("value_inc_Associated")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.value_inc_Associated)
        self.value_inc_VerifiedBy = QtWidgets.QCheckBox(self.labelIncludeGroup)
        self.value_inc_VerifiedBy.setObjectName("value_inc_VerifiedBy")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.value_inc_VerifiedBy)
        self.value_VerifiedBy = QtWidgets.QLineEdit(self.labelIncludeGroup)
        self.value_VerifiedBy.setObjectName("value_VerifiedBy")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.value_VerifiedBy)
        self.value_inc_CollectionName = QtWidgets.QCheckBox(self.labelIncludeGroup)
        self.value_inc_CollectionName.setObjectName("value_inc_CollectionName")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.value_inc_CollectionName)
        self.value_CollectionName = QtWidgets.QPlainTextEdit(self.labelIncludeGroup)
        self.value_CollectionName.setEnabled(False)
        self.value_CollectionName.setObjectName("value_CollectionName")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.value_CollectionName)
        self.value_inc_Logo = QtWidgets.QGroupBox(self.labelIncludeGroup)
        self.value_inc_Logo.setCheckable(True)
        self.value_inc_Logo.setChecked(False)
        self.value_inc_Logo.setObjectName("value_inc_Logo")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.value_inc_Logo)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.value_LogoAlignment = QtWidgets.QComboBox(self.value_inc_Logo)
        self.value_LogoAlignment.setObjectName("value_LogoAlignment")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.horizontalLayout.addWidget(self.value_LogoAlignment)
        self.label_5 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.value_LogoMargin = QtWidgets.QSpinBox(self.value_inc_Logo)
        self.value_LogoMargin.setMaximum(9999)
        self.value_LogoMargin.setProperty("value", 3)
        self.value_LogoMargin.setObjectName("value_LogoMargin")
        self.horizontalLayout.addWidget(self.value_LogoMargin)
        self.horizontalLayout.setStretch(1, 10)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.value_LogoPath = QtWidgets.QLineEdit(self.value_inc_Logo)
        self.value_LogoPath.setEnabled(False)
        self.value_LogoPath.setObjectName("value_LogoPath")
        self.gridLayout_4.addWidget(self.value_LogoPath, 0, 1, 1, 1)
        self.toolButton_GetLogoPath = QtWidgets.QToolButton(self.value_inc_Logo)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rc_/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_GetLogoPath.setIcon(icon)
        self.toolButton_GetLogoPath.setIconSize(QtCore.QSize(18, 18))
        self.toolButton_GetLogoPath.setObjectName("toolButton_GetLogoPath")
        self.gridLayout_4.addWidget(self.toolButton_GetLogoPath, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.value_LogoScaling = QtWidgets.QSlider(self.value_inc_Logo)
        self.value_LogoScaling.setMaximum(100)
        self.value_LogoScaling.setProperty("value", 100)
        self.value_LogoScaling.setOrientation(QtCore.Qt.Horizontal)
        self.value_LogoScaling.setObjectName("value_LogoScaling")
        self.horizontalLayout_2.addWidget(self.value_LogoScaling)
        self.label_scalingValue = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_scalingValue.setText("")
        self.label_scalingValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_scalingValue.setObjectName("label_scalingValue")
        self.horizontalLayout_2.addWidget(self.label_scalingValue)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 2)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.value_LogoOpacity = QtWidgets.QSlider(self.value_inc_Logo)
        self.value_LogoOpacity.setMaximum(100)
        self.value_LogoOpacity.setProperty("value", 30)
        self.value_LogoOpacity.setOrientation(QtCore.Qt.Horizontal)
        self.value_LogoOpacity.setObjectName("value_LogoOpacity")
        self.horizontalLayout_3.addWidget(self.value_LogoOpacity)
        self.label_opacityValue = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_opacityValue.setText("")
        self.label_opacityValue.setObjectName("label_opacityValue")
        self.horizontalLayout_3.addWidget(self.label_opacityValue)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 2)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.value_inc_Logo)
        self.value_inc_Barcode = QtWidgets.QCheckBox(self.labelIncludeGroup)
        self.value_inc_Barcode.setEnabled(False)
        self.value_inc_Barcode.setObjectName("value_inc_Barcode")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.value_inc_Barcode)
        self.gridLayout.addWidget(self.labelIncludeGroup, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.labelPrefPage)
        self.TaxPrefPage = QtWidgets.QWidget()
        self.TaxPrefPage.setObjectName("TaxPrefPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TaxPrefPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupbox_Kingdom = QtWidgets.QGroupBox(self.TaxPrefPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_Kingdom.sizePolicy().hasHeightForWidth())
        self.groupbox_Kingdom.setSizePolicy(sizePolicy)
        self.groupbox_Kingdom.setObjectName("groupbox_Kingdom")
        self.formLayout_6 = QtWidgets.QFormLayout(self.groupbox_Kingdom)
        self.formLayout_6.setObjectName("formLayout_6")
        self.value_Kingdom = QtWidgets.QComboBox(self.groupbox_Kingdom)
        self.value_Kingdom.setObjectName("value_Kingdom")
        self.value_Kingdom.addItem("")
        self.value_Kingdom.addItem("")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_Kingdom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_6.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.gridLayout_3.addWidget(self.groupbox_Kingdom, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.TaxPrefPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_TaxAlignSource = QtWidgets.QLabel(self.groupBox)
        self.label_TaxAlignSource.setObjectName("label_TaxAlignSource")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_TaxAlignSource)
        self.value_TaxAlignSource = QtWidgets.QComboBox(self.groupBox)
        self.value_TaxAlignSource.setObjectName("value_TaxAlignSource")
        self.value_TaxAlignSource.addItem("")
        self.value_TaxAlignSource.addItem("")
        self.value_TaxAlignSource.addItem("")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_TaxAlignSource)
        self.label_NameChangePolicy = QtWidgets.QLabel(self.groupBox)
        self.label_NameChangePolicy.setObjectName("label_NameChangePolicy")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_NameChangePolicy)
        self.value_NameChangePolicy = QtWidgets.QComboBox(self.groupBox)
        self.value_NameChangePolicy.setObjectName("value_NameChangePolicy")
        self.value_NameChangePolicy.addItem("")
        self.value_NameChangePolicy.addItem("")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.value_NameChangePolicy)
        self.label_AuthChangePolicy = QtWidgets.QLabel(self.groupBox)
        self.label_AuthChangePolicy.setObjectName("label_AuthChangePolicy")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_AuthChangePolicy)
        self.value_AuthChangePolicy = QtWidgets.QComboBox(self.groupBox)
        self.value_AuthChangePolicy.setObjectName("value_AuthChangePolicy")
        self.value_AuthChangePolicy.addItem("")
        self.value_AuthChangePolicy.addItem("")
        self.value_AuthChangePolicy.addItem("")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.value_AuthChangePolicy)
        self.groupbox_TNRS = QtWidgets.QGroupBox(self.groupBox)
        self.groupbox_TNRS.setEnabled(False)
        self.groupbox_TNRS.setObjectName("groupbox_TNRS")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupbox_TNRS)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupbox_TNRS)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.value_TNRS_Threshold = QtWidgets.QSpinBox(self.groupbox_TNRS)
        self.value_TNRS_Threshold.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.value_TNRS_Threshold.setMinimum(1)
        self.value_TNRS_Threshold.setMaximum(100)
        self.value_TNRS_Threshold.setProperty("value", 1)
        self.value_TNRS_Threshold.setObjectName("value_TNRS_Threshold")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_TNRS_Threshold)
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.groupbox_TNRS)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.TaxPrefPage)
        self.upperHorizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.upperHorizontalLayout)
        self.lowerHorizontalLayout = QtWidgets.QHBoxLayout()
        self.lowerHorizontalLayout.setObjectName("lowerHorizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lowerHorizontalLayout.addItem(spacerItem1)
        self.button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_Cancel.setObjectName("button_Cancel")
        self.lowerHorizontalLayout.addWidget(self.button_Cancel)
        self.button_SaveExit = QtWidgets.QPushButton(self.centralwidget)
        self.button_SaveExit.setAutoDefault(False)
        self.button_SaveExit.setObjectName("button_SaveExit")
        self.lowerHorizontalLayout.addWidget(self.button_SaveExit)
        self.verticalLayout.addLayout(self.lowerHorizontalLayout)
        self.verticalLayout.setStretch(1, 3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        settingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        settingsWindow.setMenuBar(self.menubar)

        self.retranslateUi(settingsWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.value_LogoAlignment.setCurrentIndex(4)
        self.value_Kingdom.setCurrentIndex(1)
        self.value_inc_VerifiedBy.toggled['bool'].connect(self.value_VerifiedBy.setEnabled)
        self.value_inc_VerifiedBy.stateChanged['int'].connect(self.value_VerifiedBy.setFocus)
        self.value_inc_CollectionName.toggled['bool'].connect(self.value_CollectionName.setEnabled)
        self.value_inc_CollectionName.stateChanged['int'].connect(self.value_CollectionName.setFocus)
        self.value_TaxAlignSource.currentTextChanged['QString'].connect(settingsWindow.toggleTNRSSettings)
        self.selectionWidget.currentRowChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.value_Kingdom.currentTextChanged['QString'].connect(settingsWindow.kingdomChanged)
        self.value_LogoScaling.sliderMoved['int'].connect(settingsWindow.scalingChanged)
        self.value_LogoOpacity.valueChanged['int'].connect(settingsWindow.opacityChanged)
        QtCore.QMetaObject.connectSlotsByName(settingsWindow)

    def retranslateUi(self, settingsWindow):
        _translate = QtCore.QCoreApplication.translate
        settingsWindow.setWindowTitle(_translate("settingsWindow", "Preferences"))
        __sortingEnabled = self.selectionWidget.isSortingEnabled()
        self.selectionWidget.setSortingEnabled(False)
        item = self.selectionWidget.item(0)
        item.setText(_translate("settingsWindow", "Labels"))
        item = self.selectionWidget.item(1)
        item.setText(_translate("settingsWindow", "Taxonomy"))
        self.selectionWidget.setSortingEnabled(__sortingEnabled)
        self.labelDimentionsGroup.setTitle(_translate("settingsWindow", "Dimensions"))
        self.yLabel.setText(_translate("settingsWindow", "height (mm)"))
        self.xLabel.setText(_translate("settingsWindow", "width (mm)"))
        self.relFontLabell.setText(_translate("settingsWindow", "Base font side"))
        self.labelIncludeGroup.setTitle(_translate("settingsWindow", "Include"))
        self.value_inc_Associated.setText(_translate("settingsWindow", "Include associated taxa"))
        self.value_inc_VerifiedBy.setText(_translate("settingsWindow", "Include verified by"))
        self.value_inc_CollectionName.setText(_translate("settingsWindow", "Include collection name"))
        self.value_inc_Logo.setTitle(_translate("settingsWindow", "Include collection logo"))
        self.label_2.setText(_translate("settingsWindow", "Logo Alignment"))
        self.value_LogoAlignment.setItemText(0, _translate("settingsWindow", "Upper Left"))
        self.value_LogoAlignment.setItemText(1, _translate("settingsWindow", "Upper Center"))
        self.value_LogoAlignment.setItemText(2, _translate("settingsWindow", "Upper Right"))
        self.value_LogoAlignment.setItemText(3, _translate("settingsWindow", "Center Left"))
        self.value_LogoAlignment.setItemText(4, _translate("settingsWindow", "Centered"))
        self.value_LogoAlignment.setItemText(5, _translate("settingsWindow", "Center Right"))
        self.value_LogoAlignment.setItemText(6, _translate("settingsWindow", "Lower Left"))
        self.value_LogoAlignment.setItemText(7, _translate("settingsWindow", "Lower Center"))
        self.value_LogoAlignment.setItemText(8, _translate("settingsWindow", "Lower Right"))
        self.label_5.setText(_translate("settingsWindow", "Margin"))
        self.toolButton_GetLogoPath.setText(_translate("settingsWindow", "..."))
        self.label_3.setText(_translate("settingsWindow", "Logo Scaling   "))
        self.label_4.setText(_translate("settingsWindow", "Logo Opacity  "))
        self.value_inc_Barcode.setText(_translate("settingsWindow", "Include catalogNumber barcode"))
        self.groupbox_Kingdom.setTitle(_translate("settingsWindow", "Kingdom"))
        self.value_Kingdom.setItemText(0, _translate("settingsWindow", "Fungi"))
        self.value_Kingdom.setItemText(1, _translate("settingsWindow", "Plantae"))
        self.groupBox.setTitle(_translate("settingsWindow", "Taxanomic alignment"))
        self.label_TaxAlignSource.setText(_translate("settingsWindow", "Source"))
        self.value_TaxAlignSource.setItemText(0, _translate("settingsWindow", "ITIS (local)"))
        self.value_TaxAlignSource.setItemText(1, _translate("settingsWindow", "Catalog of Life (web API)"))
        self.value_TaxAlignSource.setItemText(2, _translate("settingsWindow", "Taxonomic Name Resolution Service (web API)"))
        self.label_NameChangePolicy.setText(_translate("settingsWindow", "Name change policy"))
        self.value_NameChangePolicy.setItemText(0, _translate("settingsWindow", "Accept all suggestions"))
        self.value_NameChangePolicy.setItemText(1, _translate("settingsWindow", "Always ask"))
        self.label_AuthChangePolicy.setText(_translate("settingsWindow", "Authority change policy"))
        self.value_AuthChangePolicy.setItemText(0, _translate("settingsWindow", "Accept all suggestions"))
        self.value_AuthChangePolicy.setItemText(1, _translate("settingsWindow", "Always ask"))
        self.value_AuthChangePolicy.setItemText(2, _translate("settingsWindow", "Fill blanks"))
        self.groupbox_TNRS.setTitle(_translate("settingsWindow", "TNRS Settings"))
        self.label.setText(_translate("settingsWindow", "scoreThreshold"))
        self.button_Cancel.setText(_translate("settingsWindow", "Cancel"))
        self.button_SaveExit.setText(_translate("settingsWindow", "Save and exit"))

import Resources_rc
