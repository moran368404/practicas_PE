import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Formulario(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Ingrese su nombre:")
        self.input_text = QLineEdit()
        self.button = QPushButton("Aceptar")

        layout.addWidget(self.label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Conectar el botón con una función (Signal & Slot)
        self.button.clicked.connect(self.mostrar_mensaje)

    def mostrar_mensaje(self):
        nombre = self.input_text.text()
        self.label.setText(f"Hola, {nombre}!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Formulario()
    ventana.show()
    sys.exit(app.exec_())
