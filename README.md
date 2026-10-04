# Автотесты сервиса "Яндекс.Самокат"
UI-автотесты на pytest + Selenium (Firefox) с использованием Page Object Model и Allure-отчёта для учебного сервиса "Яндекс.Самокат".

---

## Установка
1. python -m venv venv
2. venv\Scripts\Activate.ps1 (PowerShell) / venv\Scripts\activate.bat (cmd)
3. pip install -r requirements.txt

---

## Запуск тестов
pytest tests/ -v

---

## Генерация Allure-отчёта
Требуется Allure CLI версии **2.41.0 или выше** (в версиях до 2.41.0 есть баг — вкладки "Behaviors" и "Packages" не отображаются, issue allure-framework/allure2#2194, исправлено в #3353).

1. pytest tests/ --alluredir=allure-results
2. allure generate allure-results -o allure-report --clean
3. allure open allure-report

