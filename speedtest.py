#!/usr/bin/env python3


import functools
import sys
import time

import requests


def timed(func):
    """Декоратор: замеряет время выполнения функции и логирует результат.

    Возвращает (elapsed, result) — время в секундах и то, что вернула функция.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        mb = result / (1024 * 1024)
        print(f"  {mb:.2f} MB за {elapsed:.3f} s")

        return elapsed, result
    return wrapper


@timed
def download(url: str) -> int:
    """Скачивает URL целиком, возвращает количество байт."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    r = requests.get(url, headers=headers, timeout=60)
    r.raise_for_status()
    return len(r.content)


def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <URL>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    n = 10

    print(f"URL: {url}")
    print(f"Запросов: {n}\n")

    total_bytes = 0
    total_time = 0.0

    for i in range(1, n + 1):
        print(f"Запрос {i}/{n}:")
        elapsed, n_bytes = download(url)
        total_bytes += n_bytes
        total_time += elapsed
        
        time.sleep(1) # для обхода rate limiting 

    total_mb = total_bytes / (1024 * 1024)
    avg_time = total_time / n
    speed = total_mb / total_time          
    speed_mbits = speed * 8                

    print("\n--- Итоги ---")
    print(f"Всего скачано:          {total_mb:.2f} MB")
    print(f"Общее время:            {total_time:.2f} s")
    print(f"Среднее время запроса:  {avg_time:.3f} s")
    print(f"Средняя скорость:       {speed:.2f} МБ/с ({speed_mbits:.2f} Мбит/с)")


if __name__ == "__main__":
    main()