from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QLabel, QFormLayout, QGroupBox, QVBoxLayout
from k_medians import ClusteriserKMedians


class Ui_Widget(object):
    def setupUi(self, Widget):
        self.clf = ClusteriserKMedians()

        Widget.setObjectName("Widget")
        Widget.resize(800, 600)

        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(30, 40, 741, 541))
        self.widget.setObjectName("widget")

        self.xLineEdit = QtWidgets.QLineEdit(Widget)
        self.xLineEdit.setGeometry(QtCore.QRect(30, 40, 71, 41))
        self.xLineEdit.setObjectName("xLineEdit")

        self.yLineEdit = QtWidgets.QLineEdit(Widget)
        self.yLineEdit.setGeometry(QtCore.QRect(120, 40, 61, 41))
        self.yLineEdit.setObjectName("yLineEdit")

        self.AddPointButton = QtWidgets.QPushButton(Widget)
        self.AddPointButton.setGeometry(QtCore.QRect(200, 40, 101, 41))
        self.AddPointButton.setObjectName("AddPointButton")
        self.AddPointButton.clicked.connect(self.on_add_point_button_clicked)

        self.GetClustersButton = QtWidgets.QPushButton(Widget)
        self.GetClustersButton.setGeometry(QtCore.QRect(120, 120, 80, 61))
        self.GetClustersButton.setObjectName("GetClustersButton")
        self.GetClustersButton.clicked.connect(self.on_euclidian_button_clicked)

        self.ChebyshevButton = QtWidgets.QPushButton(Widget)
        self.ChebyshevButton.setGeometry(QtCore.QRect(220, 120, 80, 61))
        self.ChebyshevButton.setObjectName("ChebyshevButton")
        self.ChebyshevButton.clicked.connect(self.on_chebyshev_button_clicked)

        self.scrollArea = QtWidgets.QScrollArea(Widget)
        self.scrollArea.setGeometry(QtCore.QRect(340, 40, 421, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.ClusterNumberLineEdit = QtWidgets.QLineEdit(Widget)
        self.ClusterNumberLineEdit.setGeometry(QtCore.QRect(30, 130, 71, 41))
        self.ClusterNumberLineEdit.setObjectName("ClusterNumberLneEdit")

        self.OutputScrollArea = QtWidgets.QScrollArea(Widget)
        self.OutputScrollArea.setGeometry(QtCore.QRect(30, 200, 271, 361))
        self.OutputScrollArea.setWidgetResizable(True)
        self.OutputScrollArea.setObjectName("OutputScrollArea")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 269, 359))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.OutputScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.AddPointButton.setText(_translate("Widget", "Add point"))
        self.GetClustersButton.setText(_translate("Widget", "Euclidian"))
        self.ChebyshevButton.setText(_translate("Widget", "Chebyshev"))

    def on_add_point_button_clicked(self):
        x = self.xLineEdit.text()
        y = self.yLineEdit.text()
        self.clf.add_point(int(x), int(y))
        self.xLineEdit.clear()
        self.yLineEdit.clear()

    def show_clusters(self, img_count, output):
        formLayout = QFormLayout()
        groupBox = QGroupBox()

        for i in range(img_count + 1):
            label2 = QLabel()
            label2.setPixmap(QtGui.QPixmap('report' + str(i) + '.png'))
            formLayout.addRow(label2)

        groupBox.setLayout(formLayout)

        self.scrollArea.setWidget(groupBox)
        self.scrollArea.setWidgetResizable(True)

        layout = QVBoxLayout()
        layout.addWidget(self.scrollArea)

        container = QtWidgets.QWidget()
        self.OutputScrollArea.setWidget(container)

        lay = QtWidgets.QVBoxLayout(container)
        lay.setContentsMargins(10, 10, 0, 0)

        label = QtWidgets.QLabel(output)
        lay.addWidget(label)
        lay.addStretch()

    def on_euclidian_button_clicked(self):
        cluster_number = self.ClusterNumberLineEdit.text()
        img_count, output = self.clf.get_clusters(int(cluster_number), 'euclidean')
        self.clf.clear_clusters()

        self.show_clusters(img_count, output)

    def on_chebyshev_button_clicked(self):
        cluster_number = self.ClusterNumberLineEdit.text()
        img_count, output = self.clf.get_clusters(int(cluster_number), 'chebyshev')
        self.clf.clear_clusters()

        self.show_clusters(img_count, output)
