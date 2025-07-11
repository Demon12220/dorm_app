# Руководство пользователя информационной системы "Общежитие"

## Содержание
1. [Введение](#введение)
2. [Установка приложения](#установка-приложения)
3. [Вход в систему](#вход-в-систему)
4. [Главная панель управления](#главная-панель-управления)
5. [Работа с жильцами](#работа-с-жильцами)
6. [Работа с комнатами](#работа-с-комнатами)
7. [Работа с платежами](#работа-с-платежами)
8. [Типичные сценарии использования](#типичные-сценарии-использования)
9. [Часто задаваемые вопросы](#часто-задаваемые-вопросы)

## Введение

Информационная система "Общежитие" предназначена для удобного управления данными о жильцах общежития, учета комнат и отслеживания платежей. Данное руководство поможет вам разобраться в основных функциях системы и начать эффективно с ней работать.

Система представлена в виде настольного приложения Windows, которое легко устанавливается и не требует дополнительной настройки.

## Установка приложения

Для установки приложения:

1. Запустите установочный файл `dormitory_setup.exe`
2. В открывшемся мастере установки нажмите кнопку "Далее"
3. Выберите папку для установки приложения или оставьте предложенную по умолчанию
4. Выберите создание значка на рабочем столе (по желанию)
5. Нажмите "Установить"
6. Дождитесь завершения процесса установки
7. После завершения установки запустите приложение через ярлык на рабочем столе или в меню "Пуск"

## Вход в систему

1. Запустите приложение с помощью ярлыка на рабочем столе или из меню "Пуск"
2. Нажмите кнопку "Войти" в верхнем меню
3. Введите ваши учетные данные:
   - Имя пользователя (логин)
   - Пароль
4. Нажмите кнопку "Войти"

**Важно:** Если вы впервые входите с учетной записью администратора, используйте:
- Логин: `admin`
- Пароль: `admin123`

После первого входа рекомендуется сменить пароль администратора.

## Главная панель управления

После успешного входа вы увидите панель управления – основной рабочий экран системы:

Основные элементы интерфейса:
- **Верхнее меню** – доступ ко всем разделам системы
- **Быстрые ссылки** – карточки для быстрого перехода к основным функциям
- **Статистика заселения** – информация о текущем состоянии общежития
- **Имя пользователя** (в правом верхнем углу) – доступ к настройкам и выход из системы

## Работа с жильцами

### Просмотр списка жильцов

1. Нажмите на пункт меню "Жильцы" в верхней части экрана
2. На открывшейся странице вы увидите полный список всех жильцов
3. Используйте поиск по странице браузера (Ctrl+F) для быстрого поиска по имени

### Добавление нового жильца

1. На странице списка жильцов нажмите кнопку "Добавить жильца"
2. Заполните все обязательные поля (отмечены символом *)
3. Выберите комнату из выпадающего списка
4. Выберите дату заселения (по умолчанию установлена текущая дата)
5. Нажмите кнопку "Сохранить"

**Примечание:** Если нужная комната не отображается в списке, проверьте, что она активна и есть свободные места.

### Редактирование данных жильца

1. В списке жильцов найдите нужную запись
2. Нажмите кнопку "Редактировать" в правой части строки
3. Внесите необходимые изменения
4. Нажмите кнопку "Сохранить"

### Выселение жильца

1. Откройте запись жильца для редактирования
2. Установите дату выселения
3. Нажмите кнопку "Сохранить"

### Удаление записи о жильце

**Внимание:** Удаление записей следует производить только в случае ошибочного ввода. При выселении жильца рекомендуется устанавливать дату выселения, а не удалять запись.

1. В списке жильцов найдите нужную запись
2. Нажмите кнопку "Удалить" в правой части строки
3. Подтвердите действие в появившемся диалоговом окне

## Работа с комнатами

### Просмотр списка комнат

1. Нажмите на пункт меню "Комнаты" в верхней части экрана
2. На открывшейся странице вы увидите полный список всех комнат
3. В списке отображается информация о статусе комнаты, вместимости и текущих жильцах

### Добавление новой комнаты

1. На странице списка комнат нажмите кнопку "Добавить комнату"
2. Заполните поля:
   - Номер комнаты (уникальный идентификатор)
   - Этаж
   - Вместимость (количество спальных мест)
   - Активность (установите галочку для активных комнат)
3. Нажмите кнопку "Сохранить"

**Совет:** Используйте единообразную систему нумерации комнат, например, первая цифра – номер этажа, следующие две – номер комнаты на этаже (101, 102, 201, 202 и т.д.)

### Редактирование информации о комнате

1. В списке комнат найдите нужную комнату
2. Нажмите кнопку "Редактировать"
3. Внесите необходимые изменения
4. Нажмите кнопку "Сохранить"

**Примечание:** Если изменяется вместимость комнаты, система не проверяет количество текущих жильцов. Убедитесь, что не возникнет перенаселения.

### Деактивация комнаты

Если комната временно не используется (например, на ремонте):

1. Откройте запись комнаты для редактирования
2. Снимите галочку "Активна"
3. Нажмите кнопку "Сохранить"

Деактивированная комната не будет предлагаться при заселении новых жильцов.

### Удаление комнаты

1. В списке комнат найдите нужную запись
2. Нажмите кнопку "Удалить"
3. Подтвердите действие

**Важно:** Система не позволяет удалить комнату, в которой проживают жильцы. Сначала необходимо выселить всех жильцов из комнаты.

## Работа с платежами

### Просмотр списка платежей

1. Нажмите на пункт меню "Платежи"
2. На открывшейся странице вы увидите список всех платежей
3. В списке отображается информация о сумме, периоде и статусе оплаты

### Регистрация нового платежа

1. На странице платежей нажмите кнопку "Добавить платеж"
2. Заполните форму:
   - Выберите жильца из выпадающего списка
   - Укажите сумму платежа
   - Установите начало и конец оплаченного периода
   - Выберите статус платежа (оплачено/не оплачено)
3. Нажмите кнопку "Сохранить"

### Редактирование информации о платеже

1. В списке платежей найдите нужную запись
2. Нажмите кнопку "Редактировать"
3. Внесите необходимые изменения
4. Нажмите кнопку "Сохранить"

### Удаление платежа

1. В списке платежей найдите нужную запись
2. Нажмите кнопку "Удалить"
3. Подтвердите действие

## Типичные сценарии использования

### Заселение нового жильца

1. Перейдите в раздел "Комнаты" и убедитесь, что есть свободные места
2. Перейдите в раздел "Жильцы" и нажмите "Добавить жильца"
3. Заполните все данные о жильце
4. Выберите комнату для заселения
5. Сохраните запись
6. Перейдите в раздел "Платежи" и добавьте первый платеж жильца

### Перевод жильца в другую комнату

1. Перейдите в раздел "Жильцы"
2. Найдите жильца и нажмите "Редактировать"
3. Измените комнату на новую
4. Сохраните изменения

### Учет оплаты проживания

1. Перейдите в раздел "Платежи"
2. Нажмите "Добавить платеж"
3. Выберите жильца, внесшего оплату
4. Укажите сумму и период оплаты
5. Установите статус "оплачено"
6. Сохраните запись

### Завершение проживания (выселение)

1. Перейдите в раздел "Жильцы"
2. Найдите жильца и нажмите "Редактировать"
3. Установите дату выселения
4. Сохраните изменения
5. Убедитесь, что все платежи за проживание внесены

## Часто задаваемые вопросы

### Что делать, если нет подходящей комнаты в списке при заселении?

Проверьте:
1. Все ли комнаты активны (имеют статус "Активна")
2. Есть ли свободные места в комнатах
3. Возможно, требуется добавить новую комнату

### Как узнать, кто проживает в конкретной комнате?

1. Перейдите в раздел "Комнаты"
2. Найдите нужную комнату – в таблице будет отображено количество жильцов
3. Перейдите в раздел "Жильцы" и отфильтруйте по номеру комнаты (используя поиск браузера)

### Как проверить платежи конкретного жильца?

1. Перейдите в раздел "Платежи"
2. Используйте поиск браузера (Ctrl+F), чтобы найти фамилию жильца

### Что означают разные цвета в статистике заселения?

- **Красный** - низкая заселенность (менее 30%)
- **Жёлтый** - средняя заселенность (30-70%)
- **Зелёный** - высокая заселенность (более 70%)

### Как выйти из системы?

1. В правом верхнем углу нажмите на имя пользователя
2. В выпадающем меню выберите "Выйти"

### Нужен ли интернет для работы приложения?

Нет, приложение работает полностью автономно и не требует подключения к интернету.

### Где хранятся данные приложения?

Данные хранятся в локальной базе данных SQLite, которая размещается в папке установки приложения.

### Как обновить приложение?

Для обновления необходимо:
1. Удалить текущую версию через Панель управления Windows
2. Установить новую версию, запустив файл обновленного установщика

---

*При возникновении вопросов или проблем при использовании системы обратитесь к системному администратору.*
