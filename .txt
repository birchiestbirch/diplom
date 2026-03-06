def plots():
    from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QSplitter
    from PySide6.QtCore import QTimer
    from PySide6.QtCore import Qt
    import pyqtgraph as pg
    import sys
    from oop_test import server
    from pydactyl import PterodactylClient

    # Инициализация сервера
    srv = server(PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH'))


    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Мониторинг сервера")
            self.setGeometry(100, 100, 1200, 600)

            # Создаем центральный виджет
            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            # Создаем горизонтальный layout
            main_layout = QHBoxLayout(central_widget)

            # Создаем Splitter для гибкого изменения размеров
            splitter = QSplitter(Qt.Horizontal)

            # Первый график - CPU (статические заголовки)
            self.graphWidget1 = pg.PlotWidget()
            self.graphWidget1.setTitle("CPU Usage", color="b", size="16pt")
            self.graphWidget1.setLabel('left', 'Percent', units='%')
            self.graphWidget1.setLabel('bottom', 'Time')
            self.graphWidget1.showGrid(x=True, y=True)
            self.graphWidget1.setYRange(0, 100, padding=0)

            # Второй график - RAM (статические заголовки)
            self.graphWidget2 = pg.PlotWidget()
            self.graphWidget2.setTitle("RAM Usage", color="g", size="16pt")
            self.graphWidget2.setLabel('left', 'Percent', units='%')
            self.graphWidget2.setLabel('bottom', 'Time')
            self.graphWidget2.showGrid(x=True, y=True)
            self.graphWidget2.setYRange(0, 100, padding=0)

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

            # Инициализация кривых
            self.curve_cpu = self.graphWidget1.plot(self.time_points, self.cpu_percents,
                                                    pen=pg.mkPen(color='r', width=2))
            self.curve_ram = self.graphWidget2.plot(self.time_points, self.ram_percents,
                                                    pen=pg.mkPen(color='b', width=2))

            # Таймер для обновления графиков
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_plots)
            self.timer.start(1000)

            # Первоначальное обновление
            self.update_plots()

        def update_plots(self):
            try:
                data = srv.get_data()
                new_cpu = data[2]
                new_ram = data[1]

                # Обновляем данные
                self.cpu_percents.pop(0)
                self.cpu_percents.append(new_cpu)
                self.ram_percents.pop(0)
                self.ram_percents.append(new_ram)

                # Обновляем графики
                self.curve_cpu.setData(self.time_points, self.cpu_percents)
                self.curve_ram.setData(self.time_points, self.ram_percents)

                # Заголовки остаются статичными - ничего не меняем
                # Можно добавить отображение текущих значений в другом месте при необходимости

            except Exception as e:
                print(f"Ошибка при получении данных: {e}")


    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()