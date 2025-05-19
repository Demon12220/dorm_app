@echo off
echo Мастер создания установщика "Система управления общежитием"
echo ======================================================
echo.

REM Проверяем, установлен ли Python
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ОШИБКА] Python не найден! Пожалуйста, установите Python 3.6 или выше.
    echo Загрузить можно с https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Проверяем, установлен ли pip
python -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ОШИБКА] Pip не найден! Пожалуйста, убедитесь, что установка Python включает pip.
    pause
    exit /b 1
)

echo [1/5] Установка необходимых Python пакетов...
python -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo [ОШИБКА] Не удалось установить зависимости.
    pause
    exit /b 1
)

echo.
echo [2/5] Создание иконки приложения...
python create_icon.py
if %ERRORLEVEL% NEQ 0 (
    echo [ПРЕДУПРЕЖДЕНИЕ] Не удалось создать иконку. Будет использована иконка по умолчанию.
)

echo.
echo [3/5] Очистка папки сборки если она существует...
if exist "dist" (
    rmdir /s /q "dist"
)
if exist "build" (
    rmdir /s /q "build"
)

echo.
echo [4/5] Сборка приложения с помощью PyInstaller...
python -m PyInstaller app_desktop.spec
if %ERRORLEVEL% NEQ 0 (
    echo [ОШИБКА] Не удалось собрать приложение с помощью PyInstaller.
    pause
    exit /b 1
)

echo.
echo [5/5] Создание установщика...

REM Проверка наличия Inno Setup
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" dormitory_setup.iss
    if %ERRORLEVEL% NEQ 0 (
        echo [ОШИБКА] Не удалось создать установщик.
        pause
        exit /b 1
    )
) else (
    echo [ОШИБКА] Inno Setup не найден. Пожалуйста, установите Inno Setup 6.
    echo Загрузить можно с https://jrsoftware.org/isdl.php
    pause
    exit /b 1
)

echo.
echo ======================================================
echo Установщик успешно создан!
echo Вы найдете его в папке output\dormitory_setup.exe
echo.
echo Для установки запустите этот файл на целевом компьютере.
echo.
pause
