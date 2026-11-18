---
id: khatkapi
title: "Базова плата для комп'ютера OpenPlotter на Raspberry Pi"
search_title: "Базова плата Raspberry Pi 5 для OpenPlotter: KhatkaPi"
section: electric
order: 5
description: "KhatkaPi: базова плата, яку я спроєктував, щоб захистити Raspberry Pi 5 з OpenPlotter на човні. Файли проєкту відкриті."
cover: "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDISQp8fKd3wdyEauK5By6n9kwOg3wM9lpZgHxupcTVw_d5sU8bJBr5DTX0cuYpmaS5clgsjyNUUNf9lG_fRs8NCcQ7ccVKTR0lJLfagkZ8GR1HEilVxqmn0bYAynU_aDoSwdK6VTRy8q5D1dLjR2Ap9rf94b0tec7e8IfWdvWwuZRjOKDqzG5fOXg1LLx/s1600/59089.png"
---
Ця плата — дім навігаційного комп'ютера «Віри»: Raspberry Pi 5 з OpenPlotter. Я називаю її KhatkaPi. Файли проєкту відкриті, їх можна [завантажити тут](https://drive.google.com/drive/folders/1qK_36HSr0MhrJ2yZK5vT_KGrrQ-0Dkhr), а повний опис є в моїй оригінальній статті в щоденнику: [KhatkaPi Baseboard](https://diary.sailingvira.com/p/khatkapi-baseboard.html).

## KhatkaPi: хатка для Raspberry Pi

KhatkaPi — це базова плата для Raspberry Pi 5 з OpenPlotter, зроблена, щоб справді захистити електроніку на човні. Я її спроєктував, перевірив, і файли проєкту відкриті. («Хатка» — це маленький будиночок, і для Pi вона саме такою і є.)

Головні ідеї:

- Зроблена для Pi 5 як базова плата, а не HAT, тож можна ставити будь-який корпус-радіатор і адаптер NVMe SSD.
- Усе живе в коробці IP67 (290 x 210 x 100 мм), а плата тримає певну дистанцію між зовнішнім світом і Pi.
- Кожен інтерфейс має захист від статики: 15 кВ через повітря і 8 кВ контактно.
- Зроблена так, щоб втратити якомога менше від удару блискавки, помилки користувача чи якогось іншого пристрою, що збожеволів. Здебільшого спільна земля, а не гальванічна розв'язка, але лінії даних до Pi розв'язані на більшості інтерфейсів, а зовнішні інтерфейси мають власні стабілізатори живлення.
- І, звісно, подвійне захисне лакове покриття від вологи й солоного повітря.

Живлення: захист від перенапруги до 40 В і відключення нижче 9 В, щоб не вбити батарею, з перемикачем примусового живлення до 6 В на крайній випадок. Власний стабілізатор 5 В, 6 А для Pi. Роз'єми для кнопок жорсткого ввімкнення, жорсткого вимкнення і завершення роботи. Коли Pi завершує роботу, вимикається все, крім AIS. Комутований вихід 12 В до 4 А для інших пристроїв, поки Pi працює. І місце під HDMI-розгалужувач, щоб два дзеркальні дисплеї працювали без програмних хитрощів.

На платі: інерційний модуль ICM-20948, у дальньому кутку, подалі від магнітних полів. ШІМ-вентилятор, щоб ворушити повітря в коробці й передавати тепло на її стінки. Гніздо для Arduino Nano з метеодатчиками PyPilot і датчиком тиску BMP280 на платі. Три роз'єми 1-Wire для датчиків температури.

Назовні: I2C (захищений, не розв'язаний, тож тримайте його коротким або в коробці). Два повністю розв'язані порти NMEA 0183, один під ехолот. Порт для Maiana AIS/GPS, просто на RJ45, з перемикачами живлення й передачі, власним стабілізатором 3,3 В та індикаторами. Розв'язаний порт контролера мотора PyPilot з власними 5 В. Розв'язаний послідовний порт до допоміжного мікроконтролера, що дає доступ до GPIO Pi, наприклад для виносного модуля кнопок. Два чотирипортові USB-хаби, разом 8 портів, кожен із захистом від статики 12 кВ, синфазними фільтрами і власним стабілізатором 2 А на групу. І два USB-порти лише для живлення, разом 1,5 А.

Ось справжній прототип і плата, встановлена на човні.

![Розводка базової плати KhatkaPi](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwkt1rcUeC1EALki4F36mmrsIqcPwe4NxArDa6MtXBEOqUTpg-EmIdYShXl22TQzu8aYp-WlFKsxHLP-QW_n0IKWG02SmqbIwCqjq5EFullP7KpLfqnkMMfhnt-bUZfKxz4kO4Yzy8f2OM_5rMyXrKO7-k7yS1CiGLykyxLY4zwT6wXbF7JVkaG1ZyMrxy/s1600/5908.png)
![Базова плата KhatkaPi з працюючим Raspberry Pi 5](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDISQp8fKd3wdyEauK5By6n9kwOg3wM9lpZgHxupcTVw_d5sU8bJBr5DTX0cuYpmaS5clgsjyNUUNf9lG_fRs8NCcQ7ccVKTR0lJLfagkZ8GR1HEilVxqmn0bYAynU_aDoSwdK6VTRy8q5D1dLjR2Ap9rf94b0tec7e8IfWdvWwuZRjOKDqzG5fOXg1LLx/s1600/59089.png)
![Коробка електроніки KhatkaPi за штурманським місцем](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbKxi_wnI-CDEV6IoMSZ4Zt_KII361qy2rYRKJ3wrTzlktjrGEvVc5rVKNdlrDyIdFiKZ7fh53nvmgQjf4dR5SSxkK7GGtv-PJ50xijgYeAH1nc-YND0x4KCtshUryltapZwoP2oc16Pt0GCqs2D6nOTwlg_8ut6yFbVYWp5qb7IUbbm4YYxdaklrp2pvE/s1600/IMG_0407.HEIC)

Story page: [KhatkaPi Baseboard](https://irwin34.blogspot.com/p/khatkapi-baseboard.html)
