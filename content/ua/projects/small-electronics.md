---
id: small-electronics
title: "Маленькі електронні проєкти"
section: electric
order: 3
description: "Саморобні контролери: KhatkaPi, газ, душ, сухий трюм, заповнення бака, підсвітка."
cover: "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhml60cJ2eyTEz4fk6Vo1EDjs62pEWRDHkr09-IgniENoSdHyR7k9-OYhIq1CUs9Wn1FOKVOaLEurlXtQBmyrWpKo_BfUF5dvpxR4tm3uZqK4qJaB4sApl1938sluqZN1lMt81DhwyNXbuWCNrkHemjTsqDqiPyZNtR1-dU2iCfZgxjWrMLtYyljd2hkdPE/s1600/09E31248-A495-48A6-85D7-CF81C8BF50F8.jpg"
---
Я інженер-електрик, і в якийсь момент перестав купувати для човна маленькі коробочки й почав проєктувати свої. Так дешевше, вони роблять саме те, що мені треба, і, чесно кажучи, так цікавіше. Кожна з цих плат почалася зі справжньої проблеми на «Вірі». Ось вони всі, з подробицями, на випадок, якщо хтось захоче зібрати таке саме.

## Родина

Для кожного проєкту в блозі є окрема сторінка з файлами. Якщо хочете зробити щось подібне для свого човна, просто залиште там коментар. Родина: базова плата KhatkaPi, таймер сухого трюму, контролер душу, контролер газового соленоїда, контролер наповнення бака водою, диммер підсвітки щитка, керування топовим триколірним/якірним вогнем і перемикач живлення «блок живлення/батарея».

![Базова плата KhatkaPi з Raspberry Pi 5 для OpenPlotter](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDISQp8fKd3wdyEauK5By6n9kwOg3wM9lpZgHxupcTVw_d5sU8bJBr5DTX0cuYpmaS5clgsjyNUUNf9lG_fRs8NCcQ7ccVKTR0lJLfagkZ8GR1HEilVxqmn0bYAynU_aDoSwdK6VTRy8q5D1dLjR2Ap9rf94b0tec7e8IfWdvWwuZRjOKDqzG5fOXg1LLx/s1600/59089.png)
![Плата контролера сухого трюму, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimUbYFpIufc7aYktP3IeO9BAqDa3Tk4PfOVuauAJFaslT6cPsK-rdJIgWYWh7Cte0Dg0hBd1QrmpPHkzWd7uyCTBmE34ro1l3JXsDs2kwmtD2hWJry8_COv-KjbEtWAAXx_VX7PxXEYS10yyA4y35N-3RIiZlku1g_2PhavcErNxkcpHaBdoMQVX7SkGTy/s1600/2.png)
![Плата контролера душу, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjOxmhhVuM0w4lrJFe-Ow_rUpBGXRyLfUP3V0Gmaarfn9x6-rIYoC4OtONZ9LB8Cz4zRnlzBTVpTcUI8W9Unme3Pl09vU8MmyHC0npN9NLFBUhbOGEQCVeZsA0Fp_a9_LBh6MEtkGyX8-o9jkVXD1Ci2Miw-MbeVrjZMLRilqPS24t0bzeGSjPR7yKfgAc/s1600/1png.png)
![Контролер газового соленоїда в герметичній коробці](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnghRYkFJvTSNtbreVWL31m_R1QvQmWpf05KVSC_4X5qfULjWOlj6KJLaTUVZUMtFCVicL44NoNtb4JiUIr46FToxeYntxuezq7qbIhh-H5wnFJAzmTBOHydYDIgGq-azzLmuSsqO_ikKCeymFl6c_q1MtmuiWosoWWR_nVc9Tacg_GIPsMf7BVAsfpFb1/s1600/IMG_0960.HEIC)
![Контролер наповнення бака води в коробці з датчиком рівня](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVgwCyvanwmR5a8HBvjhbPOLkjJ2hFy2c0hfKuZdvMBq-cWzV5H0dPv33EXxUW09umL_BQSVeWr0CjL-aMWSiHbzx11R8RQfjrW33f_8vhmdo4uz7WkQTv1NdJF22-ljlnGfFIZs0MvdZBEqJXVv8C9XN2O4P4nnHOk_cIGwXouZMm8mYHh648rsGJymT5/s1600/IMG_1227.HEIC)
![Плата димера підсвітки щита, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![Плата димера підсвітки щита, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![Перемикач живлення блок/батарея в моторному відсіку](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgt5QwjQI8yvf35BI-HY8X9oEcSq8nT0desmzVDIegUHXxfsGRYYzFeRW6ar1hOSA1ylagUSRavgX0JD4jq2acwkUflqduDtikkB8BTMaQ2UPRN2a6kF1EytlzEzQZq6fEV1Ahh_JJXDvseHUeft9qVt1dNOodeF8Hd4oSJlJJ55ltFGw1L8KH00s8XmaDt/s1600/IMG_2341.HEIC)

Story page: [Small electronics projects](https://irwin34.blogspot.com/p/small-electronics-projects.html)

## KhatkaPi: хатка для Raspberry Pi

Найбільша з них — базова плата для Raspberry Pi 5 з OpenPlotter, зроблена, щоб справді захистити електроніку на човні. Я її спроєктував, перевірив, і файли проєкту відкриті. («Хатка» — це маленький будиночок, і для Pi вона саме такою і є.)

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

## Сухий трюм

У січні 2023-го я перевірив ідею «сухого трюму»: коробка з губкою і мембранна помпа. Працює ідеально. Ще перевірив ручну помпу: відкачати трюм нею можна за хвилину-дві. Запускається вона важко, але можна.

![Тест сухого трюму: коробочка з губкою і мембранна помпа](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgN-yYrILi2BXUa9z_kHLwogw2VM5mN4u0gMt9V_pvf5ohn9F_m5gstX2U_4tZ11sTIJryf7qMxaUWsWsLgEBBwAX7KpcomTSFu70yMbR4oR_37c1QaJ66FB0ZNh69xAzYpflIWVhxe0CcTMlDXQOQAWNxJtgPgIRxDsK7hZlDVWflxL3-VrrUt6bowbg/s1600/IMG_4595.HEIC)

Diary: [7 Jan 2023](https://irwin34.blogspot.com/2023/01/day-75-1723-shower-walls-gaps-glassing.html)

У квітні я поставив для цього невелику самовсмоктувальну помпу на фанерному бруску, приклеєному до стінки моторного відсіку, з виходом у злив кокпіту. Я просвердлив кут зливного штуцера й нарізав щільну різьбу 1/4 NPT під штуцер для шланга. Чверть залитого трюму вона осушує менш ніж за 3 хвилини.

![Маленька самовсмоктувальна помпа сухого трюму в трюмі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibGcQ5YbhWqNXOgb1B_KDJmNEr7VGHefPQvfTHWL_nElsipHgPus1PM8GYM4M_vCUlsOkdc80Bj5mvjudpgszyPOcnME1zw4aOAoAdz-zdQhmzjbYrNUg0hb4l9AfTTsx54Qr8d0gYT908HIEcekPKpq3QmLE2NZlk4lEzYunkKVfA1Vm_bb4XLlEeuQ/s1600/IMG_5539.HEIC)
![Шланг і проводка помпи сухого трюму](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj28yjQ6o6aFDGNbU2kILUkQ7-PDXJP7PCMmzRIXbMCMdrBkRY2Q6tMGa6Rkv08WWysGe_GiCmw4GyW9560kAusAiGpmQ3RQXqJu3Ulhxi2dlp4vf5iT7KUlBPZ16ZeaxP4JRy4of9b5LQ7bYgb74K6dOftLngZYJYsQYK7HbzG-X9h01pcqI6KeODvjA/s1600/IMG_5540.HEIC)

Diary: [8 Apr 2023](https://irwin34.blogspot.com/2023/04/day-84day-83-4823-rebuilt-ducting.html)

У березні 2025-го я надрукував з TPU нову забірну коробку. Ця вже не трісне.

![Забірна коробочка сухого трюму в трюмі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCeccQKVbuCRbyujrC8knGKIJ9i8QoMlB4BTNpGln8GvMH-kOFpvNyfNNcJE7ph1748xrFbrftZZbFpI5En9tUaJ6Cp89A_bjcqzlKmm3GGDqCEndloOrJeJ6pp2L2ELDHjFOeK7pCDEDQqn3PFeTePpv9ZAtrjR580KRE3BtD2DgyMoQpnS3P2cpqPl8D/s1600/IMG_0227.HEIC)

Diary: [9 Mar 2025](https://irwin34.blogspot.com/2025/03/day-190-hvac-air-dirtribution-redo.html)

Потім я спроєктував для неї контролер. Коли вмикаєш автомат, він ганяє помпу 3 хвилини, приблизно стільки треба, щоб осушити трюм після основної відцентрової помпи, потім чекає 24 години й повторює. Ще він має захист від перегріву й перевантаження за струмом. Світлодіод на платі не світиться без живлення, світиться під час відкачування і повільно блимає під час очікування. У червні 2025-го я його нарешті встановив: це маленька сіра коробочка на стінці.

![Помпа сухого трюму і проводка](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCxQEkJnMTwXxOngCsF8xUSsc5dtbBWS-uADjBzVXs0U8LQxDX7C16xYpiMgUNdECXhn_St9IH_9COMaDvv0QajPWGnSdi_wGYPYRoHhW_yk98qUN-Hsa0siFF-8UxafHeT2Vs8IK5KKy20vIt59kHqNcRnRlFAPEZxbGMxX2uxkNzfguK5bNQQf_Gu4sw/s1600/IMG_0828.HEIC)
![Плата контролера сухого трюму, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimUbYFpIufc7aYktP3IeO9BAqDa3Tk4PfOVuauAJFaslT6cPsK-rdJIgWYWh7Cte0Dg0hBd1QrmpPHkzWd7uyCTBmE34ro1l3JXsDs2kwmtD2hWJry8_COv-KjbEtWAAXx_VX7PxXEYS10yyA4y35N-3RIiZlku1g_2PhavcErNxkcpHaBdoMQVX7SkGTy/s1600/2.png)

Diary: [15 Jun 2025](https://irwin34.blogspot.com/2025/06/day-203-61425-engine-emergency-manual.html)
Story page: [Dry bilge controller (timer)](https://irwin34.blogspot.com/p/dry-bilge-controller-timer.html)

## Контролер газового соленоїда

Цей додає зручності й безпеки газовій системі. Він вмикає соленоїд без іскор, захищає коло, якщо кабель закоротить чи обірветься, і обмежує струм утримання, тож котушка не гріється і споживає значно менше. Клапан сам закривається через 60 хвилин, на випадок, якщо кок забуде. Одна кнопка зі світлодіодом, і він може працювати з датчиком газу, щоб перекрити газ при витоку.

Світлодіод: не світиться — немає живлення. Тьмяний короткий спалах кожні 2 секунди — коло в порядку, клапан закритий. Секунда світиться, секунда ні — відкрито, лишилося більше 10 хвилин. Часте блимання — лишилося менше 10 хвилин. Три короткі спалахи, потім 5 секунд світиться — 24-годинний таймер (не рекомендується). А швидке блимання, секунда світиться і секунда ні, означає проблему з проводкою.

Кнопка: коротке натискання перемикає клапан або перезапускає таймер, коли той добігає кінця. Натиснути й потримати секунду — вимкнено.

![Розводка плати контролера газового соленоїда](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5q57sCDrG3AN8PpW8LwqTGQbV-7s8qR_fw0IxQmZD0DW1XzmHn5XM_vxeGB41FDVHzbmwbguiauvTUsX8XGllGBm-ibBmdD8BQS_V2o24VDpbe9HrXeSXiFeP8sQmg8fuQ7z7dcOQVznDflz5G-Se8F7EGlmXlemD9xzoT0xk4Ag_w4afwaRUeUj5yaSo/s1600/lpg1.png)
![Плата контролера газового соленоїда, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVeI4Id9FiqPDblo3QlnJ7hTNEFCpda1Xbp6sQnsS72v1ofrxV09IgniRtwGDQQjg7Q9ZYkf2IAh9faF2-oB8rgsQepTAuewgUAZyv8YcI5WjSh45brU_Xb36hrgZh3G7aL4wf_GRial4y-QCJ7iaoakFPF-Qhb7XB7KdToRc2eK4wqhlsnBEzsH1JyTKz/s1600/lpg2.png)
![Контролер газового соленоїда в герметичній коробці](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnghRYkFJvTSNtbreVWL31m_R1QvQmWpf05KVSC_4X5qfULjWOlj6KJLaTUVZUMtFCVicL44NoNtb4JiUIr46FToxeYntxuezq7qbIhh-H5wnFJAzmTBOHydYDIgGq-azzLmuSsqO_ikKCeymFl6c_q1MtmuiWosoWWR_nVc9Tacg_GIPsMf7BVAsfpFb1/s1600/IMG_0960.HEIC)

Story page: [LPG solenoid controller](https://irwin34.blogspot.com/p/lpg-solenoid-controller.html)

## Контролер душу

Це той, що з історії про гальюн. Він відкриває й закриває душ, але спершу відганяє холодну воду з гарячої труби назад у бак, тож комфортна вода йде майже одразу й жодна крапля не марнується. Одне натискання дає хвилину води, і до нього можна під'єднати ножний перемикач.

Світлодіод: тьмяний червоний — очікування (HOLD). Бурштиновий — прогрів гарячої води. Зелений — готово. Зелений, що повільно блимає, — душ працює, а швидкі спалахи — лишилося 10 секунд; натисніть ще раз, щоб отримати ще хвилину. Коротке натискання запускає чи зупиняє прогрів і відкриває чи закриває воду. Натиснути й потримати секунду — зупинити й повернутися в HOLD.

![Плата контролера душу, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjOxmhhVuM0w4lrJFe-Ow_rUpBGXRyLfUP3V0Gmaarfn9x6-rIYoC4OtONZ9LB8Cz4zRnlzBTVpTcUI8W9Unme3Pl09vU8MmyHC0npN9NLFBUhbOGEQCVeZsA0Fp_a9_LBh6MEtkGyX8-o9jkVXD1Ci2Miw-MbeVrjZMLRilqPS24t0bzeGSjPR7yKfgAc/s1600/1png.png)
![Контролер душу, змішувач і соленоїдні клапани з підписами](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0z-fG-i5amb1M4BWsHUWX9Ae4S4lVhDk4liUh7s0LyD6RHyO_BD_LyWmVTRYbpZN-PxaG1fc6ZUG6nAUEDMmT5bze2CHuv9mktbf5rO3gs7Z7qK_VQ1GJByF9wP3pEYv2oiALRVtNQaUYJgyLiupSmogg3GEMyfuoA4GXuDWCKLn0dsvoJX4vBsjO-3_m/s1600/2.png)

Story page: [Simple shower controller](https://irwin34.blogspot.com/p/simple-shower-controller.html)

## Диммер підсвітки щитка

Збираючи свій щиток автоматів, я додав світлодіоди, що показують, які кола ввімкнені. Після двох нічних переходів знайшлася проблема: удень нормально, а вночі занадто яскраво. Як новорічна ялинка в каюті.

Тож я зробив маленьку плату, що приглушує їх приблизно 1:2000, комутуючи їхній спільний мінус ШІМом. Робить це крихітний мікроконтролер, тож співвідношення можна змінити без заміни деталей. Чотири дроти: спільний мінус світлодіодів, 12 В (споживає близько 0,01 мА), дріт ходових вогнів (сигнал для нічного режиму) і земля. Усі деталі разом з платою коштують близько $5.

![Головний електрощит зі світлодіодними індикаторами](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinzaTDDkSQleF2fN9sX3bn69EHannHGbfsYxEPxL2Df2vL4bB8K59bCmt1-Wdj6d_IBCgqWLny2xQlcX9W_31H87gEMgh-9LWdTdNYUdDBkRYM55LjMg-zNqHtq9DOF913JJOjIyjE5P8_I5lfRbLyJDLMh0V9X5YIn7XEUuMN3gDjE4JB4aHG8Vjqmeo2/s1600/IMG_0893.HEIC)
![Схема димера підсвітки щита](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizu6zW7WiVyV0KU-DatDWrOA07a34J4u15TWWDS9_dNRQ-Kd_rPZOjt_a846FhYpxp4UIAy4bM9eFTxDztbecr0MWupPuQsTSsCwPRIvZP6YETHUdojqApv9ZYellyG2_UYHz_RFEoPutEwgwrr7HKCSC6YyARd7zRuSJcuXw9EjF88KIe55_A99E_4psJ/s1600/970002%20sch.png)
![Плата димера підсвітки, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![Розводка плати димера підсвітки](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8Ymr8mrerkf3aZhHPKdtM9KbntYVz4QsqNRMRoMx62KgDpHGZkJVzwSUS2HVrVshIHrZC0tAK3W9CRONTlCTRX0mK0IWs8FCKR4WmLmnBzB0l_XYvhRJnE6ipTkrithjS_YPZf3SlkT52A4R6ceDXIwo7P-lk8PFpPJgEaO_IIWcq3ThO2NB390bKnm8Y/s1600/970002-1.png)
![Головний щит із приглушеними індикаторами](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinzaTDDkSQleF2fN9sX3bn69EHannHGbfsYxEPxL2Df2vL4bB8K59bCmt1-Wdj6d_IBCgqWLny2xQlcX9W_31H87gEMgh-9LWdTdNYUdDBkRYM55LjMg-zNqHtq9DOF913JJOjIyjE5P8_I5lfRbLyJDLMh0V9X5YIn7XEUuMN3gDjE4JB4aHG8Vjqmeo2/s1600/IMG_0893.HEIC)
![Схема димера підсвітки щита](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizu6zW7WiVyV0KU-DatDWrOA07a34J4u15TWWDS9_dNRQ-Kd_rPZOjt_a846FhYpxp4UIAy4bM9eFTxDztbecr0MWupPuQsTSsCwPRIvZP6YETHUdojqApv9ZYellyG2_UYHz_RFEoPutEwgwrr7HKCSC6YyARd7zRuSJcuXw9EjF88KIe55_A99E_4psJ/s1600/970002%20sch.png)
![Плата димера підсвітки, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![Розводка плати димера підсвітки](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8Ymr8mrerkf3aZhHPKdtM9KbntYVz4QsqNRMRoMx62KgDpHGZkJVzwSUS2HVrVshIHrZC0tAK3W9CRONTlCTRX0mK0IWs8FCKR4WmLmnBzB0l_XYvhRJnE6ipTkrithjS_YPZf3SlkT52A4R6ceDXIwo7P-lk8PFpPJgEaO_IIWcq3ThO2NB390bKnm8Y/s1600/970002-1.png)

Story page: [Electric panel lights brightness control](https://irwin34.blogspot.com/p/electric-panel-lights-brightness-control.html)
Diary: [14 Mar 2026](https://irwin34.blogspot.com/2026/03/new-small-electronics-for-my-boat-home.html)

## Топовий триколірний і якірний вогонь

Ця плата вирішує дві проблеми. По-перше, коли міняєш звичайний якірний вогонь на комбінований триколірний/якірний, зазвичай потрібні три дроти на щоглу. Ця плата дає змогу обійтися двома, що вже є, тож жодного нового кабелю на щоглу. По-друге, вона перемикає з триколірного вогню на бортові вогні на рівні палуби, коли йдеш на моторі, без ще одного перемикача на щитку.

Важливо: ніколи не вмикайте триколірний на топі разом з ходовим топовим вогнем. Це суперечить правилам, і з носа інші човни бачитимуть лише червоний або зелений над білим.

У плати три входи (вимикач топового вогню +12 В, вимикач ходових вогнів +12 В, земля) і три виходи (дріт на топ A, дріт на топ B і ходові вогні на рівні палуби).

![Таблиця положень вимикачів і конфігурацій ходових вогнів](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMLPpku84w7njPdvZtJGx1-Sjxmc50IB4Kh0Bz6FdcaNdXRxD7vXhCwuVPFKj6J1hSrl60Gw7mCj6b3M14Xq7kCxsk6yx4kgkv2Mn3HO0l6o5KtoEvGa5Iv8czaSZfTRmY6WAWw5-cwZYPJjUFTsErd7F_A_RodW6MOC6pggTgRTq_ikc1-51REjbi_3oy/s1600/Lights.png)
![Схема контролера вогнів на топі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXQ1HWYkpwx1IDxfp3GDOkKzXB4vMXEjrEv4Wczn6sizhZPY6wg408uIte2zwo54B_qaAZ-ha6JIkW9rbCqGFQ5nXJ0ubSZopVuqltPPrLK6KKgz6LEtCQ-inK_3C4q0LMJYBjIr7_uz2TcxO6AFGUrOPwgXQ9q-1fbHBB492Jo_XXiNtiK565-mjPmwkG/s1600/970001sch.png)
![Розводка плати контролера вогнів на топі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj2bDOwub2y-XqAtEfBnRjyvCkPNIma0u5ebq0TC0UsvymiSWhRSXKhlNzpa4cB6EUij17GstMuIcvbADwDbngGOjmPTF5MoAye2LmDytLOpJdQFLmKAicEI5gEuJMVJToMUKeivAp0q4w12JkkYj2tQUr20xsyMw27IPgWXDAH4kgSXl_nO3GGmGK9F-g/s1600/970001-1.png)
![Плата контролера вогнів на топі, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiu0H6-_4UlvdV5OdbQ3BXshEZCsrrXCHRRogQgFn67jhqpfYMVESOjqYkOeoeGOVSgGAqgxzvfjpg_PIrrqCt8Ix0-JuO_buRljJHw_gAue55pXO5Aw8JCa6SkOesFklgYyXvkXlxAldPWhXUcEg0S4iLk2_H1KBx6N5BMbVLr01DlJ4p_VlTYoInz-XI/s1600/970001-2.png)
![Схема підключення контролера вогнів на топі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6bnkyQZrGaK8Do3xCjlJHLU7wZqY3H5z4HptgM0OwKl2clwlIIAg57J2GVuj9HSXpzRxeVPyysksx98ez13QCcFLTak5Bb2bSYLuE192lGnAnvhHgo4Hw_bgdwBqEF5JijIEW7lEGRuu1fk-zu3oduqG0JNc38EtyktnoIZz9TKsRchBvCMeRp84YLx9V/s1600/970001-3.png)
![Таблиця положень вимикачів і конфігурацій ходових вогнів](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMLPpku84w7njPdvZtJGx1-Sjxmc50IB4Kh0Bz6FdcaNdXRxD7vXhCwuVPFKj6J1hSrl60Gw7mCj6b3M14Xq7kCxsk6yx4kgkv2Mn3HO0l6o5KtoEvGa5Iv8czaSZfTRmY6WAWw5-cwZYPJjUFTsErd7F_A_RodW6MOC6pggTgRTq_ikc1-51REjbi_3oy/s1600/Lights.png)
![Схема контролера вогнів на топі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXQ1HWYkpwx1IDxfp3GDOkKzXB4vMXEjrEv4Wczn6sizhZPY6wg408uIte2zwo54B_qaAZ-ha6JIkW9rbCqGFQ5nXJ0ubSZopVuqltPPrLK6KKgz6LEtCQ-inK_3C4q0LMJYBjIr7_uz2TcxO6AFGUrOPwgXQ9q-1fbHBB492Jo_XXiNtiK565-mjPmwkG/s1600/970001sch.png)
![Розводка плати контролера вогнів на топі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj2bDOwub2y-XqAtEfBnRjyvCkPNIma0u5ebq0TC0UsvymiSWhRSXKhlNzpa4cB6EUij17GstMuIcvbADwDbngGOjmPTF5MoAye2LmDytLOpJdQFLmKAicEI5gEuJMVJToMUKeivAp0q4w12JkkYj2tQUr20xsyMw27IPgWXDAH4kgSXl_nO3GGmGK9F-g/s1600/970001-1.png)
![Плата контролера вогнів на топі, 3D-рендер](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiu0H6-_4UlvdV5OdbQ3BXshEZCsrrXCHRRogQgFn67jhqpfYMVESOjqYkOeoeGOVSgGAqgxzvfjpg_PIrrqCt8Ix0-JuO_buRljJHw_gAue55pXO5Aw8JCa6SkOesFklgYyXvkXlxAldPWhXUcEg0S4iLk2_H1KBx6N5BMbVLr01DlJ4p_VlTYoInz-XI/s1600/970001-2.png)
![Схема підключення контролера вогнів на топі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6bnkyQZrGaK8Do3xCjlJHLU7wZqY3H5z4HptgM0OwKl2clwlIIAg57J2GVuj9HSXpzRxeVPyysksx98ez13QCcFLTak5Bb2bSYLuE192lGnAnvhHgo4Hw_bgdwBqEF5JijIEW7lEGRuu1fk-zu3oduqG0JNc38EtyktnoIZz9TKsRchBvCMeRp84YLx9V/s1600/970001-3.png)

Story page: [Mast top Tri-color/Anchor light control](https://irwin34.blogspot.com/p/mast-top-tri-coloranchor-light-control.html)
Diary: [14 Mar 2026](https://irwin34.blogspot.com/2026/03/new-small-electronics-for-my-boat-home.html)

## Контролер наповнення бака водою

Коли доливаєш бак зі шланга, треба стежити за рівнем. На моєму човні, якщо перелити, вода йде у вентиляцію й протікає в трюм. А вентиляційна лінія надто тонка, щоб у баку не наростав тиск, тож доводиться тримати кришку горловини відкритою і дивитися. Треба уваги й точного моменту, щоб вчасно перекрити воду, а увага біля причалу закінчується першою.

Тож тепер берегова вода йде через клапан із соленоїдом на 12 В. Подаєш живлення на контролер, і він перевіряє рівень. Якщо бак не повний, він відкриває клапан і чекає, поки датчик скаже «повний». Датчик — індуктивний датчик рівня на 5–12 В з виходом NPN. А через 15 хвилин контролер перекриває воду хоч би що.

Звуки: один короткий сигнал при ввімкненні. Наповнення: короткий сигнал кожні 10 секунд. Повний: довгий сигнал щосекунди. Тайм-аут: короткий сигнал щосекунди. Тож він перекриває воду й постійно нагадує від'єднати шланг.

![Контролер наповнення бака в коробці з датчиком рівня](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVgwCyvanwmR5a8HBvjhbPOLkjJ2hFy2c0hfKuZdvMBq-cWzV5H0dPv33EXxUW09umL_BQSVeWr0CjL-aMWSiHbzx11R8RQfjrW33f_8vhmdo4uz7WkQTv1NdJF22-ljlnGfFIZs0MvdZBEqJXVv8C9XN2O4P4nnHOk_cIGwXouZMm8mYHh648rsGJymT5/s1600/IMG_1227.HEIC)
![Схема контролера наповнення бака води](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXJPzSgla98ksHYznDPQVkwnDHzq0mQmsk2wlTKD1uYvaFAg6vSIlRlJ7Tu_N0thS3oWg9l2j9HLLl8HkyIjuJjfJWYSEB0lSyM-cz3Z9af3wSaeLtGmZk1AYmbiEsEfk_clCkuk0-G_9dZiTN7iiJBE7__tQng9grWRRG1mnZe-l3adhUhCW_OtTGC7mD/s1600/wc.png)
![Безконтактний датчик рівня води](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFVsXLsztATJsBDES-a6KCX6q-NmfveUDVBbJ1LyJhhwjg8tVoAG00Rj9RwhVyOxI4l4o3DkkcVidpSj4w5PnCDCjKuJ0-tLGamUkl-Diatue9AGWtmdF2aqFoHFUtjErFk8LB5F1cBhvD61Utlcvj7LNJM5GHngzgvVb_Rkm97rB1cOci0V_DHmAxcQzU/s1600/k.png)

Story page: [Water tank fill controller](https://irwin34.blogspot.com/p/water-tank-fill-controller.html)

## Перемикач живлення «блок живлення/батарея»

Я поставив окремий блок живлення 14,5 В, 40 А від берегової мережі, щоб зняти навантаження човна із зарядного пристрою. Зарядні пристрої плутаються, коли під час зарядки висить постійне навантаження, і не можуть зрозуміти, коли переходити в режим підтримки.

Спершу я поєднував два джерела платою з двома ідеальними діодами. Дуже просто: човен живить те джерело, де напруга вища. Усе добре, доки батарея не зарядиться повністю. Тоді іноді (я це впіймав) блок живлення, зарядний пристрій, батарея і мікросхема діода влаштовують шторм перемикань. Короткі провали на шині 12 В, і комп'ютер перезавантажується кілька разів за 10 хвилин.

Тож я спроєктував перемикач, що працює як ДБЖ. Він живить шину від блока живлення, якщо на його виході від 12,5 до 16 В. Якщо берегове живлення зникло або напруга неправильна, він перемикає шину на батарею. Коли берегове живлення повертається, він чекає 10 секунд, щоб переконатися, що воно стабільне, і перемикає назад. А ще відключає все від батареї, якщо вона просідає нижче 9 В.

Він на мікроконтролері, тож усі часи й напруги задаються у прошивці. Транзистори розраховані на 260 А тривало і 1,4 кА в імпульсі 10 мкс, по два паралельно, до 40 В. Я не чекаю більше 80 А від батареї (автомат на 80 А) і 40 А від блока живлення (він сам обмежує струм). З опором у відкритому стані 0,75 мОм 80 А дають менш ніж 5 Вт тепла, тож радіатора 70x70 мм досить. Він встановлений, і після вихідних під вітрилами й кількох ночей на борту працює добре.

![Плата перемикача живлення блок/батарея](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7xAQVy6DljfAUgnq1GcGpqNVPrBvVtEiC_WPas-U5Izpie-PDXelRZhlFlop1UJ__hf3d6AfA2Su09o61xwcuHIeI8JAbSkKq7lESXMWd2_e2IkZtALkpgnJY3sOakMVClZdjjxpgRMcDho7MGikdRUw4-whZWdNYm88jpP8cBt-aa138jMKRaJUuIjEL/s1600/IMG_2247.HEIC)
![Перемикач живлення з радіатором](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjQnmoZKCEpC__wT2fDPDJT4d7X5n5SsrlxPkoxK8xgvjsJCXoU-IOQ55PXQjL1uLEgw-_m42MC-XxwYIeb1610fpaFtJDwnvQnCxz4q65FftoHv4rjZXi81_FR7hml9XLlNFNqVUGgn6F5utLgZk_OZGqPNbivkrTdyZF1nYX4x7wnKKuo-Mr6UrFJ0sU/s1600/IMG_2248.HEIC)
![Схема перемикача живлення блок/батарея](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQG5bGmGHIHbsJXaVyAOorUau9MRK_62uI2pZkWeyJw_tdRMUzkCmg0tG3aUB121825uWxUAAz8RSF7U7Z7ReVI7KbObPu9YDe7_0vpndYt3ClZrJ8yVKKbCapzusxQmmoZhZrt8eX8TKDN-_45CF593Giq5hyphenhyphenaqtyV8N4rtAKGGCeRlUkAlmiZ9ORtt-w/s1600/Untitled.jpg)
![Перемикач живлення біля батарейних кабелів](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRW9bCoJdrEOEn7BHmSbHA5QnWYGRGXb57JZq-WNepXTwQqw2IJ2g7ZfSZjOITs81NSWGngKLbLIVZ-ZsJgRauoVc-I0wOdgDR6Y3ukUf44KeG3txp5RFEtLRfU7tHi7UMYJsfoYiMoBhRxAOHR0135kh2X3APBdE8jonBhCWVdwJC6kEbNhORoDDyfxVf/s1600/IMG_2341.HEIC)

Story page: [Power switch PSU/Battery](https://irwin34.blogspot.com/p/power-switch-psubattery.html)

Правила, які я заклав у проєкт: берегове живлення має пріоритет, тож якщо блок живлення видає понад приблизно 12 В, шина живиться від нього, хоч би що казала батарея. Повна розв'язка: кожне джерело має подвійний MOSFET-ключ, увімкнений так, що у вимкненому стані струм не тече в жодний бік, тож батарея і блок живлення ніколи не бачать одне одного. Мінімальний час на батареї: перемкнувшись на батарею через провал живлення, він лишається на ній щонайменше 10 секунд, тож хитке берегове живлення не змусить його стрибати туди-сюди. І «спершу розімкни, потім замкни»: близько 100 мкс мертвого часу між відключенням одного джерела і підключенням іншого.

Те, що почалося з дивного мерехтіння світла, стало цілим інженерним проєктом: ідея, дослідження, схема, плата, деталі, складання, програмування, функціональні тести, стрес-тести, корпус з 3D-принтера, монтаж і випробування на борту. Близько чотирьох тижнів. Тепер, замість довіряти двом джерелам живлення і мікросхемі ідеального діода домовлятися між собою, у мене керування живленням, поведінку якого я справді розумію. Ось плата з захисним покриттям і модуль, встановлений у моторному відсіку.

![Плата перемикача живлення, вигляд зверху](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEnlE_32drK1hdmFGTz4aBhUk5UmoZy8sfjHgZ-iZAtkMjAf19uUkC9d75uaEwwUYwy07kveDzeaKKU3AZfc15jjK1ht0fgWkJ9LHTVPYyyFEQ2AhPyC9GE6OZsudYgpxWMxcmDBB5oiyNxElkzKiRsDfXnFU2jGBvORWivmdva8LfG50z6Ck_qmvYxOLH/s1600/IMG_2247.HEIC)
![Перемикач живлення в моторному відсіку](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgweNdbzCRoZBEq2-_umMFOJzdsszayKfr0iMLZ0OAze0SR4zJaULoYaJPQC1w44IAZ5EqVS7UN-y_aswOC7z1-YLvSw3dyH1isR1l6k7e-mfNWRKLsfnBA9YNQAyPY_nMZvkLhyET0Pc4xh2a6Rm4kIOUJDsXe_TgJsBcBDjJmw3CLs_Psv3_GtORKk_Q6/s1600/IMG_2341.HEIC)

Diary: [24 Aug 2026](https://irwin34.blogspot.com/2026/08/days-276-277-sailing-kemahtx-to.html)

## Монітор батарей

Найновіший, з жовтня 2026-го, — монітор для моїх батарей WattCycle. Він спілкується з ними через Bluetooth, показує їхній поточний стан і відправляє дані на сервер Signal K в OpenPlotter. Тепер батареї звітують комп'ютеру, а комп'ютер — мені.

![Монітор батарей WattCycle показує дві батареї](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhml60cJ2eyTEz4fk6Vo1EDjs62pEWRDHkr09-IgniENoSdHyR7k9-OYhIq1CUs9Wn1FOKVOaLEurlXtQBmyrWpKo_BfUF5dvpxR4tm3uZqK4qJaB4sApl1938sluqZN1lMt81DhwyNXbuWCNrkHemjTsqDqiPyZNtR1-dU2iCfZgxjWrMLtYyljd2hkdPE/s1600/09E31248-A495-48A6-85D7-CF81C8BF50F8.jpg)
![Монітор батарей із деталями однієї батареї](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGG2UhzxmaO5JBVW_bRLnzAqq2ZtpCX1HdFAoOOtKT-UNazweH0G8msNDuS98R5eTgbjbs7ZpmrZVlwrRNAonlhjDnZFlA6yT1RSY0oV-kG-QZzfXGdIKqJjRjdYyeYvnY2oWEJG-rfGXjpGV2jfyACkcXKhS1ux6YjNGJR3pG_qEzhUFKMqjPHHdG-uqB/s1600/5B20C409-8C04-48EB-8FA1-199F821AF230.jpg)

Diary: [5 Oct 2026](https://irwin34.blogspot.com/2026/10/days280-refrigerator-thermostat-bumpy.html)
