# Практическая работа 7  
# Django Class Based Views
## Цель практической работы
Применить встроенные generic class-based views для отображения списка сущностей и деталей выбранной сущности, реализации страниц по созданию новых записей и редактированию существующих, написания view для удаления и архивации сущностей в БД.
## Что нужно сделать
Воспользуйтесь кодовой базой с занятия или [из дополнительных материалов](https://gitlab.skillbox.ru/learning_materials/python_django_solutions/-/tree/master/module-materials/m07-cbv).
### Продукты
Создайте представления для продуктов при помощи generic views:
1. `+` View для отображения списка продуктов:
   - `+` каждый элемент в списке должен иметь в себе ссылку для перехода на страницу отображения деталей этого продукта; 
   - `+` элементы в списке должны быть только неархивированными.
2. View для отображения деталей выбранного продукта. На этой странице должны быть ссылки на следующие страницы:
   - `+` возврат к списку продуктов,
   - `+` обновление текущего продукта, 
   - `+` архивация текущего продукта.
3. `+` View для создания продукта (обработка GET для получения формы и POST для обработки формы и сохранения записи). 
4. `+` View для обновления продукта (обработка GET для получения предзаполненной формы данными из БД по выбранной сущности и POST для обработки формы и обновления записи).
5. `+` View для выполнения архивации выбранной сущности (так называемый soft delete). На GET должна быть страница с вопросом пользователю, уверен ли он, что надо архивировать продукт, на POST — архивация заказа.
### Заказы
Создайте следующие представления для заказов при помощи generic views:
1. `+` View для отображения списка заказов:
   - `+` каждый элемент списка должен иметь в себе ссылку для перехода на страницу отображения деталей этого заказа;
   - `+` каждый элемент в списке должен отображать пользователя, привязанного к заказу;
   - `+` каждый элемент в списке должен отображать все продукты, связанные с заказом.
2. View для отображения деталей выбранного заказа:
   - `+` на этой странице должны быть отображены следующие свойства:
     - `+` пользователь, привязанный к заказу;
     - `+` продукты, связанные с заказом;
   - на этой странице должны быть ссылки на следующие страницы:
     - `+` возврат к списку заказов;
     - `+` обновление текущего заказа;
     - `+` удаление текущего заказа.
3. `+` View для создания заказа с возможностью выбора пользователя и продуктов (обработка GET для получения формы, POST для обработки формы и сохранения записи). 
4. `+` View для обновления `заказа` с возможностью выбора пользователя и продуктов (обработка GET для получения предзаполненной формы данными из БД по выбранной сущности, POST для обработки формы и обновления записи).
5. `+` View для полного удаления выбранной сущности (на GET страница с вопросом пользователю, уверен ли он, что надо удалить заказ, и удаление заказа на POST).
    

## Что оценивается

-   Приложение установлено и настроено.
    
-   Использованы class-based views для всех отображений.
    
-   В шаблонах есть все необходимые ссылки к сущностям, спискам и прочим страницам.
    
-   Выполняется отображение, создание, обновление и удаление сущностей.
    

## Как отправить работу на проверку

Сдайте практическую работу через систему контроля версий Git сервиса Skillbox GitLab. В материалах с практической работой напишите «Сделано» и прикрепите ссылку на репозиторий.