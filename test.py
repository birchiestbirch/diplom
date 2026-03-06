from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Два графика")
        self.setGeometry(100, 100, 1200, 600)

        # Создаем центральный виджет и основной layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Создаем контейнер для графиков
        graphs_container = QWidget()
        graphs_layout = QHBoxLayout(graphs_container)

        # График 1
        self.plot_widget1 = pg.PlotWidget(title="График 1: Синус")
        self.plot_widget1.setLabel('left', 'Амплитуда')
        self.plot_widget1.setLabel('bottom', 'Время')
        self.plot_widget1.showGrid(x=True, y=True)
        graphs_layout.addWidget(self.plot_widget1)

        # График 2
        self.plot_widget2 = pg.PlotWidget(title="График 2: Косинус")
        self.plot_widget2.setLabel('left', 'Амплитуда')
        self.plot_widget2.setLabel('bottom', 'Время')
        self.plot_widget2.showGrid(x=True, y=True)
        graphs_layout.addWidget(self.plot_widget2)

        # Добавляем контейнер с графиками в основной layout
        main_layout.addWidget(graphs_container)

        # Инициализация данных
        self.x = np.linspace(0, 10, 100)
        self.y1 = np.sin(self.x)
        self.y2 = np.cos(self.x)

        # Отображаем начальные данные
        self.curve1 = self.plot_widget1.plot(self.x, self.y1, pen='b', name='sin(x)')
        self.curve2 = self.plot_widget2.plot(self.x, self.y2, pen='r', name='cos(x)')

        # Настройка таймера для обновления графиков
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plots)
        self.timer.start(100)  # Обновление каждые 100 мс

        # Счетчик времени для анимации
        self.time = 0

    def update_plots(self):
        """Обновление графиков"""
        self.time += 0.1

        # Обновляем данные
        self.y1 = np.sin(self.x + self.time)
        self.y2 = np.cos(self.x + self.time)

        # Обновляем графики
        self.curve1.setData(self.x, self.y1)
        self.curve2.setData(self.x, self.y2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())