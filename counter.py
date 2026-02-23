!pip install PySide6


from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QLineEdit
)
from PySide6.QtCore import QTimer
import sys
class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("تایمر معکوس")
        self.setFixedSize(300, 200)

        self.time_left = 0

        # ---------- ویجت‌ها ----------
        self.label = QLabel("زمان باقی‌مانده: 0", self)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.input_time = QLineEdit(self)
        self.input_time.setPlaceholderText("زمان را به ثانیه وارد کنید")

        self.start_btn = QPushButton("شروع")
        self.start_btn.clicked.connect(self.start_timer)

        # ---------- تایمر ----------
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        # ---------- لایه ----------
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_time)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)

    def start_timer(self):
        try:
            self.time_left = int(self.input_time.text())
            if self.time_left <= 0:
                return
            self.label.setText(f"زمان باقی‌مانده: {self.time_left}")
            self.timer.start(1000)  # هر ۱ ثانیه
        except ValueError:
            self.label.setText("عدد معتبر وارد کنید")

    def update_time(self):
        self.time_left -= 1
        self.label.setText(f"زمان باقی‌مانده: {self.time_left}")

        if self.time_left <= 0:
            self.timer.stop()
            self.label.setText("⏰ زمان تمام شد!")


if __name__ == "__main__":
    from PySide6.QtCore import Qt

    app = QApplication(sys.argv)
    window = CountdownApp()
    window.show()
    sys.exit(app.exec())
