# Решатель квадратных уравнений

Проект состоит из двух файлов.

quadratic_equation.py: Содержит скрипт, который позволяет рещить квадратное уравнение.

tests.py: Скрипт производит тестирование работы quadratic_equation.py



# Как использовать

Скрипт quadratic_equation.py использует функцию sqrt из модуля math

```Python
from math import sqrt
```

для вычисления квадратного корня


```Python
    root1 = (-b - sqrt(discriminant)) / (2 * a)
```
Для решения квадратного уравнения определена функция 
```Python
get_roots(a, b, c)
```
, которая принимает три коэффициента, на основе которых подсчитываются корни квадратного уравнения.

Ответ функции представлен в виде двух переменных root1 и root2.

Скрипт tests.py тестирует код, который решает квадратное уравнение. Всего четыре теста:
1. Тестирует на наличие вещественных корней. test_solves_real_roots(self)
2. На то, что первый корень больше второго. test_first_root_less_than_second(self)
3. На то, что второй корень имеет значение None, если есть только одно решение. test_second_root_is_none_if_one_solution(self)
4. На то что оба корня возвращают None, если дискриминант отрицательный. test_returns_none_for_complex_solution(self)

Каждая из функций может вернуть три варианта ответа: ОК, FAIL, ERROR. OK - если тест пройден успешно. FAIL - если утверждение, заданное в тесте ошибочно. ERROR - если произошла другая ошибка во время тестирования.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы

Ran 4 tests in 0.002s
.E..
======================================================================
ERROR: test_returns_none_for_complex_solution (__main__.QuadraticEquationTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 22, in test_returns_none_for_complex_solution
    root1, root2 = get_roots(1, 2, 3)
  File "/Users/n0name/Documents/GitHub/7_mistery_fix/quadratic_equation.py", line 6, in get_roots
    root1 = (-b - sqrt(discriminant)) / (2 * a)
ValueError: math domain error

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=1)

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
