import heapq


def minimal_cost_to_combine_cables(cable_lengths):
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cable_lengths)
    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Видаляємо два найменших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Обчислюємо вартість їх з'єднання та додаємо до загальної вартості
        cost = first + second
        total_cost += cost

        # Додаємо новоутворений кабель назад до купи
        heapq.heappush(cable_lengths, cost)

    return total_cost


# Приклад використання
cable_lengths = [5, 4, 2, 8]
print(minimal_cost_to_combine_cables(cable_lengths))
