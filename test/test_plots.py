from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter
from PySide6.QtCore import QTimer, Qt
import pyqtgraph as pg


class MonitoringWindow(QMainWindow):
    """Окно мониторинга с графиками CPU и RAM"""

    def __init__(self, serv, parent=None):
        super().__init__(parent)
        self.serv = serv
        self.setWindowTitle("More")
        self.setGeometry(100, 100, 1200, 600)

        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Создаем горизонтальный layout
        main_layout = QHBoxLayout(central_widget)

        # Создаем Splitter для гибкого изменения размеров
        splitter = QSplitter(Qt.Horizontal)

        # Первый график - CPU
        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget1.setTitle("CPU Usage", color="b", size="16pt")
        self.graphWidget1.setLabel('left', 'Percent', units='%')
        self.graphWidget1.setLabel('bottom', 'Time')
        self.graphWidget1.showGrid(x=True, y=True)
        self.graphWidget1.setYRange(0, 100, padding=0)
        self.graphWidget1.addLegend()

        # Второй график - RAM
        self.graphWidget2 = pg.PlotWidget()
        self.graphWidget2.setTitle("RAM Usage", color="g", size="16pt")
        self.graphWidget2.setLabel('left', 'Percent', units='%')
        self.graphWidget2.setLabel('bottom', 'Time')
        self.graphWidget2.showGrid(x=True, y=True)
        self.graphWidget2.setYRange(0, 100, padding=0)
        self.graphWidget2.addLegend()  # Добавляем легенду

        # Добавляем графики в splitter
        splitter.addWidget(self.graphWidget1)
        splitter.addWidget(self.graphWidget2)

        # Устанавливаем начальные размеры
        splitter.setSizes([600, 600])

        # Добавляем splitter в layout
        main_layout.addWidget(splitter)

        # Данные для отображения
        self.time_points = list(range(100))
        self.cpu_percents = [0] * 100
        self.ram_percents = [0] * 100

        # Инициализация кривых с подписями
        self.curve_cpu = self.graphWidget1.plot(
            self.time_points, self.cpu_percents,
            pen=pg.mkPen(color='r', width=2),
            name="Current: 0.0%"
        )

        self.curve_ram = self.graphWidget2.plot(
            self.time_points, self.ram_percents,
            pen=pg.mkPen(color='b', width=2),
            name="Current: 0.0%"
        )

        # Таймер для обновления графиков
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plots)

        # Флаг для отслеживания состояния таймера
        self.timer_running = False

    def start_monitoring(self):
        """Запуск мониторинга"""
        if not self.timer_running:  # Проверяем, не запущен ли уже таймер
            self.timer.start(1000)  # Запускаем таймер с интервалом 1 секунда
            self.timer_running = True  # Отмечаем, что таймер теперь работает

    def stop_monitoring(self):
        """Остановка мониторинга"""
        if self.timer_running:  # Проверяем, работает ли таймер
            self.timer.stop()  # Останавливаем таймер
            self.timer_running = False  # Отмечаем, что таймер больше не работает

    def closeEvent(self, event):
        """Обработка закрытия окна"""
        self.stop_monitoring()  # Останавливаем мониторинг перед закрытием
        event.accept()  # Подтверждаем закрытие окна

    def update_plots(self):
        data = self.serv.get_data()  # Получаем свежие данные с сервера
        new_cpu = data[2]  # Забираем процент CPU
        new_ram = data[1]  # Забираем процент RAM

        # Обновляем данные
        self.cpu_percents.pop(0)  # Удаляем самое старое значение CPU
        self.cpu_percents.append(new_cpu)  # Добавляем новое значение CPU
        self.ram_percents.pop(0)  # Удаляем самое старое значение RAM
        self.ram_percents.append(new_ram)  # Добавляем новое значение RAM

        # Обновляем графики
        self.curve_cpu.setData(self.time_points, self.cpu_percents)  # Рисуем обновлённый график CPU
        self.curve_ram.setData(self.time_points, self.ram_percents)  # Рисуем обновлённый график RAM

        # Обновляем легенду с текущими значениями
        if hasattr(self.graphWidget1, 'legend') and self.graphWidget1.legend is not None:
            if len(self.graphWidget1.legend.items) > 0:  # Проверяем, есть ли элементы в легенде
                self.graphWidget1.legend.items[0][1].setText(
                    f"Current: {new_cpu:.1f}%")  # Обновляем текст с текущим CPU

        if hasattr(self.graphWidget2, 'legend') and self.graphWidget2.legend is not None:
            if len(self.graphWidget2.legend.items) > 0:  # Проверяем, есть ли элементы в легенде
                self.graphWidget2.legend.items[0][1].setText(
                    f"Current: {new_ram:.1f}%")  # Обновляем текст с текущим RAM