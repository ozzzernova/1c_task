import numpy as np

x, y, x_1, y_1, A, B, C, K = map(int, input().split())

time = 0

labirint = np.full((2 * K + 1, 2 * K + 1), 0)   # 0 - стена

labirint[K][K] = 1

visited = np.full((2 * K + 1, 2 * K + 1), 0)

#   0
# 1 x 3
#   2

def find_rotation(x, y, x_1, y_1):
    if x == x_1 and y == y_1 + 1: return 0
    elif x == x_1 + 1 and y == y_1: return 1
    elif x == x_1 and y == y_1 - 1: return 2
    else: return 3

current_position = [x, y]
current_rotation = find_rotation(x, y, x_1, y_1)


def double_matrix(matrix, cur_pos):
    old_size = len(matrix)
    new_size = old_size * 2
    new_matrix = np.zeros((new_size, new_size), dtype=matrix.dtype)
    new_matrix[old_size // 2:old_size // 2 + old_size, old_size // 2:old_size // 2 + old_size] = matrix

    cur_pos = [cur_pos[0] + old_size / 2, cur_pos[1] + old_size / 2]

    return new_matrix



def get_original_map(pos, original_map):
    if (pos[0] - K < 0 or pos[0] + K >= len(original_map) or pos[1] - K < 0 or pos[1] + K >= len(original_map)): original_map = double_matrix(original_map)
    return original_map[pos[0] - K: pos[0] + K + 1][pos[1] - K: pos[1] + K + 1]


# это проверки пересечения лучом из середины текущей клетки в середину рассматриваемой клетки стен
def left_up_trig(x, y, or_map):
  tg = (K - x) / (K - y)   # x - по строкам, у - по столбцам
  x_c = x
  y_c = y
  while (x_c != K or y_c != K):
    if (or_map[x_c][y_c] == 0):
      return 0;
    if (x + (y_c - y + 0.5) * tg + 0.5 == x_c + 1):
      y_c = y_c + 1
      x_c = x_c + 1
    elif (int(x + (y_c - y + 0.5) * tg + 0.5) == x_c):
      y_c = y_c + 1
    else:
      x_c = x_c + 1

  return 1


def right_up_trig(x, y, or_map):
  tg = abs((K - x) / (y - K))   # x - по строкам, у - по столбцам
  x_c = x
  y_c = y
  while (x_c != K or y_c != K):
    if (or_map[x_c][y_c] == 0):
      return 0;
    if (x + (y - y_c + 0.5) * tg + 0.5 == x_c + 1):
      y_c = y_c - 1
      x_c = x_c + 1
    elif (int(x + (y - y_c + 0.5) * tg + 0.5) == x_c):
      y_c = y_c - 1
    else:
      x_c = x_c + 1

  return 1


def left_down_trig(x, y, or_map):
  tg = abs((K - x) / (y - K))   # x - по строкам, у - по столбцам
  x_c = x
  y_c = y
  while (x_c != K or y_c != K):
    if (or_map[x_c][y_c] == 0):
      return 0;
    if (2 * K + 1 - (y_c - y + 0.5) * tg - 0.5 == x_c):
      y_c = y_c + 1
      x_c = x_c - 1
    elif (int(2 * K + 1 - (y_c - y + 0.5) * tg - 0.5) == x_c):
      y_c = y_c + 1
    else:
      x_c = x_c - 1

  return 1


def right_down_trig(x, y, or_map):
  tg = abs((K - x) / (y - K))   # x - по строкам, у - по столбцам
  x_c = x
  y_c = y
  while (x_c != K or y_c != K):
    if (or_map[x_c][y_c] == 0):
      return 0;
    if (2 * K + 1 - (y - y_c + 0.5) * tg - 0.5 == x_c - 1):
      y_c = y_c - 1
      x_c = x_c - 1
    elif (int(2 * K + 1 - (y - y_c + 0.5) * tg - 0.5) == x_c):
      y_c = y_c - 1
    else:
      x_c = x_c - 1

  return 1


# основная функция, которая переписывает карту местности при освещении огнем
def make_fire(or_map):
  map = get_original_map(current_position, or_map)
  for i in range(2 * K + 1):
    for j in range(2 * K + 1):
      if (i < K and j < K): labirint[current_position[0] - K + i][current_position[1] - K + j] = left_up_trig(i, j, map)
      elif (i < K and j > K): labirint[current_position[0] - K + i][current_position[1] - K + j] = right_up_trig(i, j, map)
      elif (i > K and j < K): labirint[current_position[0] - K + i][current_position[1] - K + j] = left_down_trig(i, j, map)
      elif (i > K and j > K): labirint[current_position[0] - K + i][current_position[1] - K + j] = right_down_trig(i, j, map)
      elif (i == K and j < K):
        flag = 1
        for k in range(0, K):
          if (map[K][k] == 0):
            flag = 0
            break
        labirint[current_position[0] - K + i][current_position[1] - K + j] = flag
      elif (i == K and j > K):
        flag = 1
        for k in range(K + 1, 2 * K + 1):
          if (map[K][k] == 0):
            flag = 0
            break
        labirint[current_position[0] - K + i][current_position[1] - K + j] = flag
      elif (i < K and j == K):
        flag = 1
        for k in range(0, K):
          if (map[k][K] == 0):
            flag = 0
            break
        labirint[current_position[0] - K + i][current_position[1] - K + j] = flag
      elif (i > K and j == K):
        flag = 1
        for k in range(K + 1, 2 * K + 1):
          if (map[k][K] == 0):
            flag = 0
            break
        labirint[current_position[0] - K + i][current_position[1] - K + j] = flag


def find_neighbors(cur_pos):
  x, y = cur_pos
  neighbors = set()

  for neighbor_point in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
    if (labirint[neighbor_point[0]][neighbor_point[1]] == 1):
      neighbors.add(neighbor_point)

  return neighbors

def try_to_go():
  # пытаемся пройти в стену по текущему направлению
  return 0

def solution():
  nonlocal current_rotation
  if (B + 3 * A > C):
    make_fire(current_position)
  else:
    while (not try_to_go()):
      current_rotation = (current_rotation + 1) % 4


