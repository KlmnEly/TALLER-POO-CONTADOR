import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ContadorApp(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Taller POO — Contador Interactivo")
    self.setFixedSize(320, 220)

    self.contador = 0

    self.widget_central = QWidget()
    self.setCentralWidget(self.widget_central)
    self.layout_principal = QVBoxLayout(self.widget_central)

    self.etiqueta_titulo = QLabel("Contador Interactivo")
    self.etiqueta_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.etiqueta_titulo.setStyleSheet(
        "font-size: 16px; font-weight: bold; color: #2C3E50;"
    )

    self.etiqueta_valor = QLabel(str(self.contador))
    self.etiqueta_valor.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.etiqueta_valor.setStyleSheet(
        "font-size: 36px; font-weight: bold; color: #2980B9;"
    )

    self.boton_incrementar = QPushButton("Incrementar (+1)")
    self.boton_incrementar.setStyleSheet(
        "padding: 10px; font-size: 14px; background-color: #27AE60; color:"
        " white; border-radius: 5px;"
    )

    self.boton_incrementar.clicked.connect(self.incrementar_contador)

    self.layout_principal.addWidget(self.etiqueta_titulo)
    self.layout_principal.addWidget(self.etiqueta_valor)
    self.layout_principal.addWidget(self.boton_incrementar)

  def incrementar_contador(self):
    self.contador += 1
    self.etiqueta_valor.setText(str(self.contador))


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = ContadorApp()
  ventana.show()
  sys.exit(app.exec())