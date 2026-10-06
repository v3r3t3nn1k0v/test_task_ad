# Internet Speed Tester

Простой скрипт на Python для замера скорости интернета. Последовательно выполняет 10 HTTP GET-запросов к указанному URL, замеряет время и объём скачанных данных, печатает среднюю скорость в МБ/с.

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/v3r3t3nn1k0v/test_task_ad.git
cd test_task_ad
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

### 3. Активировать

```bash
source venv/bin/activate          # Linux / macOS
venv/Scripts/activate             # Windows
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python speedtest.py <URL>
```

Список рекомендуемых URL — в файле [`list.md`](list.md).

## Структура проекта

```
test_task_ad/
├── speedtest.py       # основной скрипт
├── requirements.txt   # зависимости
├── list.md            # рекомендуемые URL для теста
├── .gitignore
└── README.md
```
