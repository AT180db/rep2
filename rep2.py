import time

class Timer:
    def enter(self):
        """Метод входа в контекстный менеджер"""
        self.start_time = time.perf_counter()
        return self


def exit(self, exc_type, exc_value, exc_tb):
    """Метод выхода из контекстного менеджера"""
    self.end_time = time.perf_counter()
    duration = self.end_time - self.start_time
    print(f"Цикл/блок кода выполнялся {duration:.4f} секунд.")

with Timer():
    for _ in range(10**7):
        pass  # Заглушка
