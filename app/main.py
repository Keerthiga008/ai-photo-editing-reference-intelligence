from __future__ import annotations

import sys
from pathlib import Path

from PySide6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Photo Editing AI Studio")
        self.resize(1200, 800)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QVBoxLayout(central_widget)

        title = QtWidgets.QLabel("Reference-Driven AI Editing")
        title.setStyleSheet("font-size: 22px; font-weight: 600;")
        layout.addWidget(title)

        info = QtWidgets.QLabel(
            "Project foundation for image analysis, reference intelligence, and Photoshop handoff."
        )
        layout.addWidget(info)

        btn = QtWidgets.QPushButton("Open Project")
        btn.clicked.connect(self.on_open_project)
        layout.addWidget(btn)

        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer)

    def on_open_project(self) -> None:
        QtWidgets.QMessageBox.information(
            self,
            "Project Status",
            "Application shell is ready. Extend this with import, reference, and processing workflows.",
        )


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
