import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QAction
import fiona

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIGLibre - Interface de bureau")
        self.setGeometry(100, 100, 700, 500)

        self.load_button = QPushButton("Charger Shapefile", self)
        self.load_button.setGeometry(250, 20, 200, 40)
        self.load_button.clicked.connect(self.load_shapefile)

        self.table = QTableWidget(self)
        self.table.setGeometry(50, 80, 600, 380)
        self.table.setColumnCount(0)
        self.table.setRowCount(0)

    def load_shapefile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Sélectionner un fichier Shapefile", "", "Shapefiles (*.shp)")
        if file_path:
            with fiona.open(file_path, 'r') as src:
                fields = list(src.schema['properties'].keys())
                self.table.setColumnCount(len(fields))
                self.table.setHorizontalHeaderLabels(fields)
                features = list(src)
                self.table.setRowCount(len(features))
                for row_idx, feature in enumerate(features):
                    for col_idx, field in enumerate(fields):
                        value = str(feature['properties'][field])
                        self.table.setItem(row_idx, col_idx, QTableWidgetItem(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
