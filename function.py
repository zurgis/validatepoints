import numpy as np
from numpy.linalg import norm
from math import degrees

def validation(size1: tuple, size2: tuple, 
    points: list, 
    valid_angle: int, 
    valid_dist: int) -> str:
    """Функция валидирует ориентацию и пропорции между точками"""

    # Отношение ширины и высоты картинок
    x = size1[0] / size1[1]
    y = size2[0] / size2[1]

    for i in range(len(points)):
        v1 = np.array([points[i][0][0] * x, points[i][0][1] * x])
        v2 = np.array([points[i][1][0] * y, points[i][1][1] * y])

        dist = norm(v2 - v1) # Расстояние между векторами

        prod_v = np.dot(v1, v2) # Скалярное произведение векторов
        # Модули векторов
        mod_v1 = norm(v1)
        mod_v2 = norm(v2)
        angle_v = prod_v / (mod_v1 * mod_v2) # Найдем угол между векторами
        angle = degrees(angle_v) # Переводим радианы в градусы
        
        if angle > valid_angle or dist > valid_dist:
            return 'Валидация не пройдена'
    return 'Данные валидны'