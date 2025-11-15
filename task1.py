import numpy as np

# 2. Создать два вектора
x = np.arange(-10, 6, 1)   # от -10 до 5 включительно
y = np.arange(-5, 11, 1)   # от -5 до 10 включительно

print("x:", x)
print("y:", y)

# 3. Построить новый вектор z (нечётные индексы -> x, чётные -> y)
z = []
for i in range(max(len(x), len(y))):
    if i < len(x):
        z.append(x[i])
    if i < len(y):
        z.append(y[i])
z = np.array(z)
print("z (before sort):", z)

z_sorted = np.sort(z)
print("z (sorted):", z_sorted)

# 4. Функция нормы вектора (L1, L2, L_inf)
def vector_norms(v):
    l1 = np.sum(np.abs(v))
    l2 = np.sqrt(np.sum(v**2))
    linf = np.max(np.abs(v))
    return l1, l2, linf

norms_x = vector_norms(x)
norms_y = vector_norms(y)
norms_z = vector_norms(z)

print(f"Norms of x: L1={norms_x[0]}, L2={norms_x[1]}, Linf={norms_x[2]}")
print(f"Norms of y: L1={norms_y[0]}, L2={norms_y[1]}, Linf={norms_y[2]}")
print(f"Norms of z: L1={norms_z[0]}, L2={norms_z[1]}, Linf={norms_z[2]}")

# 6. Функция факториала
def factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("factorial(12) =", factorial(12))

# 7. Вектор из 5 элементов (ручной ввод можно заменить на фиксированный массив для теста)
vec = np.array([float(x) for x in input("Введите 5 элементов вектора через пробел: ").split()])
if len(vec) != 5:
    raise ValueError("Нужно ввести ровно 5 чисел!")

# Добавляем веса
weights = np.array([float(x) for x in input("Введите 5 весов через пробел: ").split()])
if len(weights) != 5 or sum(weights) != 1:
    raise ValueError("Нужно ввести ровно 5 чисел, которые в сумме дают 11!")

print("Введённый вектор:", vec)
print("Минимум:", np.min(vec))
print("Максимум:", np.max(vec))
print("Сумма:", np.sum(vec))

l1_norm = np.sum(np.abs(vec))
weighted_l1_norm = np.sum(weights * np.abs(vec))

print("Обычная L1-норма:", l1_norm)
print("Взвешенная L1-норма:", weighted_l1_norm)
print("Сравнение: ", "равны" if l1_norm == weighted_l1_norm else "разные")