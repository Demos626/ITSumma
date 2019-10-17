# Задание (junior web-developer)

Реализовать программный комплекс для мониторинга состояния загруженности
операционной системы (ОС) на Python>=3.6.
Этот комплекс должен состоять их трех отдельных сервисов.

## Описание сервисов

Первый сервис (*Data Producer*) должен непосредственно быть запущен на целевом
сервере, собирать информацию о ресурсах ОС через заданный промежуток времени
(значение которого в секундах задается переменной окружения `INTERVAL` в файле
`.env`, см. `.env.example` для примера) и отправлять их в сервис,
который будет отвечать за обработку этих данных (*Data Receiver*).

Сервис *Data Receiver* должен принимать данные по HTTP на URL,
заданный в файле .env через переменную окружения `RECEIVER_URL`,
и сохранять эти данные в промежуточное хранилище (например, Redis), которое должно быть доступно
для чтения сервису *Web Server*.

*Web Server* должен принимать запросы на получение актуальных значений определенного списка метрик
от сторонних клиентов по адресу, заданному
через переменную окружения `WEB_SERVER_URL`, и возвращать в ответе эти значения.

## Формат данных

* *Data Receiver* принимает данные от *Data Producer* по протоколу HTTP в формате JSON в виде
    ```json
    {"cpu": 1.0, "gpu": 1.0}
    ```
    где ключи - названия метрик, а значения - их величины.
    Для работы тестов *Data Producer*'у достаточно передавать в *Data Receiver* текущее
    значение загрузки процессора c ключом `cpu`.

* *Web Server* принимает GET запросы по протоколу HTTP и отдает
всем клиентам данные в том же формате, что описан выше (`{"cpu": 1.0, "gpu": 1.0}`).
При этом в URL запроса необходимо передавать GET-параметр `topics`, который должен
содержать список метрик через запятую, например, `http://localhost:8080/?topics=cpu,gpu`.
В ответе должно возвращаться только последнее полученное значение для каждой из запрошенных клиентом метрик.

## Порядок выполнения задания
Нужно сделать приватный форк репозитория https://github.com/devopsprodigy/itsumma-task. Сделать три сервиса, проверить тестами. Не забудьте закомитить requirements.txt для установки зависимостей.

## Проверка
Для проверки соответствия вашей реализации заданным условиям необходимо запускать тесты,
находящиеся в данном репозитории (предварительно создав `.env` файл на основе `.env.example`
и установив зависимости из `requirements-test.txt`):

```shell script
pip install -r requirements-test.txt
python -m unittest
```

## Оформление решения
Предоставить ссылку на ваш репозиторий нам на почту leliseeva@itsumma.ru или телеграм @LaraLaraHR с указанием имени соискателя, добавить в контрибьюторы пользователя exsmund. 
