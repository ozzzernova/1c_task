# 1c_task
Отборочное задание на кафедру 1С, Озернова Вероника

# Запуск:

python3 solution.py

# Задание 5: Алгоритм

Нам нужно приблизить оптимальное время полного прохода лабиринта минотавром. Для этого рассмотрим несколько случаев:

- В + 3 * А > C - то есть время, которое будет затрачено на то, чтобы проверить все стены и перейти в ячейку больше, чем если бы мы разожгли костер и осмотрели клетки вокруг. Из этого предположения зажигаем костер(об этом позже) и исследуем новые территории. При этом нужно учитывать 

- Иначе - нам выгоднее "лбом" проверить соседние клетки на существование в них стен. Как только находим клетку, которую еще не посещали, переходим в нее и продолжаем наши поиски уже из нее.

Как мы исследуем окрестности при помощи костра - рассматриваем для каждой точки квадрата 2К + 1 вокруг нас луч, соединяющий середину нашей текущей точки и рассматриваемой. Далее рассмотрим один из нескольких случаев - когда они находятся на одной(горизонтальной или вертикальной) прямой с текущей точкой или в одном из оставшихся квадратов. Для квадратов рассматриваем тангенс угла, под которым выпущен луч и путь по клеткам, которые задевает луч - если какая-то клетка является стеной, то мы не можем увидеть рассматриваемую клетку. Для прямой - просто перебираем точки по горизонтали/вертикали с нами. Если все точки были проходами, то фиксируем значение 1 на карте для этой точки
