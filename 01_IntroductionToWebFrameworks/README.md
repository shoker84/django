# Приложение "Объявления"
## История изменений:
### 9.6 Практическая работа `(в процессе)`
Создайте новостной сайт, у которого должны быть следующие возможности:
* регистрация пользователя;
* хранение дополнительных данных о пользователе: телефон, город, флаг верификации, количество опубликованных новостей. Реализуйте это через расширение модели профиля.
* аутентификация пользователя;
* просмотр данных аккаунта;
* пользователи должны быть разделены на три группы: (обычные пользователи, верифицированные пользователи и модераторы);
* возможность создание новостей. Должно быть доступно только верифицированным пользователям (для верификация необходимо решение модератора, необходимо добавить ему для этого дополнительное разрешение);
* публикация новости возможна только после одобрения модератором (необходимо добавить ему для этого дополнительное разрешение);
* реализуйте возможность добавления комментария к новости (должны выводиться под текстом новости, если комментарий оставляет аутентифицированный пользователь, то в шаблоне выводить имя);
* возможность указать тег для новости и затем фильтровать список новостей по нему и по дате создания.

### 8.6 Практическая работа `(выполнено, ожидает оценки)`
Доработайте проект из прошлого модуля, добавив к нему следующую функциональность:
- Добавьте страницы для логина и разлогина
- Сделайте шапку сайта динамической:
  - для аутентифицированного пользователя - сообщение с приветствием и ссылку на страницу разлогина
  - для неаутентифицированного - ссылку на страницу входа
- Установите время жизни сессии в 1 месяц
- Измените таблицу “Комментарий” - добавьте поле user c FK связью с таблицей User
- Измените логику работы комментариев:
  - для залогинненого пользователя доступно только поле “текст комментария”, при этом, при сохранении комментария в поле user должен сохраниться текущий юзер
  - для незалогиненного пользователя доступны 2 поля - имя пользователя, текст комментария. Комментарий можно опубликовать, указав любое имя пользователя
- Отредактируйте вывод комментариев так, чтобы выводился username автора, если комментарий оставил авторизованный пользователь, или текст из поля “имя пользователя” с пометкой “аноним”, если комментарий оставил незалогиненный пользователь.
##### Примечание разработчика:
- изменить `nav-bar` для отображения `Вход` или `<Username> | Выход`
- настроить общую шаблонизацию проекта `(готово)`
  - настроить `settings.py` для получения нормального доступа к общим шаблонам для всех приложений
    - `'DIRS': [BASE_DIR / 'templates']` - не работает
    - `'DIRS': [os.path.join(BASE_DIR, 'templates')]` - соблюдаем пути
  - удалено приложение `__templates__`, который служил в качестве папки для общих шаблонов
  - перенести шаблоны в `templates`
  - перенастроить пути для файлов представления и внутри шаблонов

### 6.7 Практическая работа `(выполнено, ожидает оценки)`
Доработайте проект из прошлого модуля, добавив к нему административную панель:
- создайте админку с помощью ModelAdmin для моделей Новости и Комментарий
- добавьте понятные представления элементов для модели Новость (с полями: название, дата публикации и активность) и модели Комментарий (с полями: имя пользователя и текст комментария (укороченный до 15 символов, далее троеточие))
- в списке новостей выведите все ее поля, кроме текста новости
- в списке комментариев выведите все поля
- реализуйте возможность фильтрации комментариев по имени пользователя
- реализуйте возможность фильтрации новостей по флагу активности
- добавьте возможность просматривать и редактировать комментарии к новости с помощью TabularInline
- добавьте 2 действия для массового перевода новостей: в статус “активно” и статус “неактивно”
- добавьте действие для комментариев, которое будет проставлять текст выбранным комментариям “Удалено администратором”.

### 4.8 Практическая работа `(выполнено, зачтено)`
- Доработайте модель объявления: добавьте поля: описание, цена, дата публикации, дата окончания публикации.
- Создайте модель для хранения контактной информации об авторе объявления. (Обязательные поля: имя, электронная почта, телефон).
- Свяжите модели объявления и автора связью один-ко-многим так, чтобы у одного автора могло быть несколько объявлений.
- Добавьте модель для хранения рубрики объявления (Возможные значения: Авто, Недвижимость, Работа), поля: наименование.
- Свяжите рубрику с объявлением с использованием связи вида один-ко-многим.
- Реализуйте вывод списка объявлений по адресу /advertisements в формате:
> Заголовок | Цена | Наименование рубрики

- При нажатии на заголовок должен произойти переход на детальную страницу объявления, на которой должны быть представлены следующие данные:
  - Заголовок
  - Цена
  - Описание
  - Рубрика
  - Тип объявления
  - Контактная информация
  - Количество просмотров
- По умолчанию цена должна отображаться в рублях, рядом можно разместить цену в долларах по курсу ЦБ.

### 3.7 Практическая работа `(выполнено, зачтено)`
- Создайте middleware, которое будет логировать информацию о посетителе сайта и сохранять следующие данные в текстовый файл: дата и время события, запрошенный URL, HTTP метод.
- Создайте Class Based View по адресу  /advertisements, в котором:
  - метод get - будет возвращать список объявлений (Список определяется в коде представления (4 и более записей) и передается через контекст),
  - метод post, возвращает сообщение о, том что запрос на создание новой записи успешно выполнен.
  - попробуйте реализовать счетчик запросов, так чтобы на каждый новый вызов данного метода увеличивал счетчик и отобразите число вызовов в шаблоне.
- Создайте два TemplateView, один должен отображать контактную информацию по адресу /сontacts (адрес, телефон, эл. почта должны передаваться через контекст), другой должен отображать информацию о компании по адресу /about (название компании и текст с описанием должны передаваться через контекст)
- Создайте главную страницу по адресу /. Нужно использовать представление-класс.
  - метод get должен возвращать html форму, на которой должны быть представлены следующие элементы: выбора категории из списка, выбор региона из списка, текстовое поле для ввода названия объявления и кнопка “Найти”. (Значения для выбора нужно передавать из представления)

### 2.7 Практическая работа `(выполнено, зачтено)`
- Добавьте несколько новых страничек (пять) с объявлениями и отредактируйте страницу списка.
- На главной, т.е странице списка отобразите текст «Прошел все курсы на SkillBox. Продаю готовые домашние задания». И список курсов со ссылками на страницы детального отображения. На странице конкретного курса должно быть фото, ссылка на курс и цена решения.

### 1.8 Практическая работа `(выполнено, зачтено)`
#### Основное задание
- Перейдите в Gitlab, нажав на кнопку "Перейти в Gitlab". Если у вас нет репозитория локально, клонируйте его и Домашнюю работу необходимо выполнять в нем. После выполнения сделайте коммит, отправьте в свой репозиторий и пришлите преподавателю ссылку на коммит для проверки.
- Активируйте виртуальное окружение (Описание приложено в документах модуля)
- Установите Django с помощью команды


    pip install Django==2.2

- Перейдите в директорию 01_IntroductionToWebFrameworks/todo и выполните команду


    python manage.py migrate

- Создайте суперпользователя командой


    python manage.py createsuperuser

- Запустите приложение командой


    python manage.py runserver

- Проверьте корректность работы приложения перейдя по адресу http://127.0.0.1:8000/ (В случае успешного запуска по этому адресу будет располагаться сообщение, что страница не найдена (Page not found)).
- Перейдите по адресу http://127.0.0.1:8000/admin/ и введите логин и пароль, которые указывали при создании суперпользователя, в случае успеха должна отобразиться административная панель.


#### Дополнительное задание
Измените код таким образом, чтобы список дел произвольно выводил 5 элементов, для этого измените код в файле views.py в папке todo/tasks.