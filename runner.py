import ctypes
import threading
import time

# Загружаем скомпилированную библиотеку с нашим ассемблерным кодом
lib = ctypes.CDLL("./librace.so")

# Настраиваем доступ к глобальной переменной из ассемблерного кода
shared_counter = ctypes.c_int64.in_dll(lib, "shared_counter")

# Сбрасываем счетчик в 0 перед стартом
shared_counter.value = 0

print("Запуск двух потоков с ассемблерным кодом (без LOCK)...")
start_time = time.time()

# Создаем два настоящих системных потока ОС
t1 = threading.Thread(target=lib.thread_function)
t2 = threading.Thread(target=lib.thread_function)

t1.start()
t2.start()

t1.join()
t2.join()

expected = 20000000 # Каждый из двух потоков делает по 10 000 000 итераций
actual = shared_counter.value

print(f"Время выполнения: {time.time() - start_time:.4f} сек.")
print(f"Ожидаемый математический результат: {expected}")
print(f"Фактический результат в памяти ОЗУ: {actual}")
print(f"Потеряно инкрементов из-за Context Switch: {expected - actual}")
