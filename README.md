# Sprint_7 — Автотесты API Яндекс.Самокат

Автотесты для учебного сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/docs/). Проверяют корректность работы ручек API: коды ответов, тела, обработку ошибок.

## Тестовые данные

- Курьеры и заказы создаются перед тестом и удаляются после
- Генерация случайных логинов, паролей, имён
- Параметризация для проверки разных сценариев

## Allure-отчёт

| Декоратор | Назначение |
|---|---|
| `@allure.feature` | Группировка по ручкам |
| `@allure.story` | Сценарии внутри ручек |
| `@allure.severity` | Критичность тестов (CRITICAL / NORMAL / MINOR) |
| `@allure.step` | Шаги запросов в отчёте |

## Запуск

```bash
pip install -r requirements.txt
pytest tests/ --alluredir=allure_results -v
allure generate allure_results -o allure_report --clean
allure open allure_report

## Результаты

23 теста пройдены

3 теста выявили баги сервера
