import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QFileDialog, QLabel


class CustomFileDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Escolha um arquivo")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Nenhum arquivo selecionado", self)
        self.layout.addWidget(self.label)

        self.open_button = QPushButton("Abrir Arquivo", self)
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)

        self.custom_button = QPushButton("Botão Personalizado", self)
        self.custom_button.clicked.connect(self.custom_action)
        self.layout.addWidget(self.custom_button)

        self.cancel_button = QPushButton("Cancelar", self)
        self.cancel_button.clicked.connect(self.reject)
        self.layout.addWidget(self.cancel_button)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self)
        if file_name:
            self.label.setText(file_name)

    def custom_action(self):
        # Adicione a ação que você deseja para o botão personalizado
        self.label.setText("Ação do botão personalizado executada.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = CustomFileDialog()
    dialog.exec()