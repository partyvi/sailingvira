---
id: navpod
title: "NavPod"
search_title: "Саморобний NavPod: дисплей біля штурвала на Raspberry Pi"
section: electric
order: 3
related: [navigation, khatkapi]
description: "Блок біля штурвала з 7-дюймовим екраном і 26 справжніми кнопками, що говорить з OpenPlotter, Signal K і PyPilot."
cover: "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeW_Ub1562uLkio219CyFr11SFzcktXplddLgQGq0wwOwFdv49VCkQSAyphmLo3NYXEtQuod5oR6DLCAbqlw2D7KdFXBtEYT4gJk3AYhTAF1hl9k7tz1REF1Szyvfht1z72WBUFBYZd6yKczcJYQ1x41WxqEfJGtAiLB98brBWeEI8SorbjiVxm9aYUk2x/s1600/IMG_2272.HEIC"
---
Сенсорні екрани й мокрі пальці не дружать. Тож я зробив для штурвала «NavPod»: другий Raspberry Pi з яскравим 7-дюймовим екраном і справжніми кнопками, що сидить на огорожі педесталу й говорить з головним комп'ютером OpenPlotter. Це не фірмовий NavPod, він лише схожий. Решта навігаційної системи — у [Навігаційних приладах і авторульовому](../navigation/).

## Ідея NavPod

У квітні 2025-го за своїм столом я взявся за «navpod»: панель OpenPlotter на огорожі колонки штурвала, у формі навігаційної консолі, з кнопками замість сенсора. Для мене кнопки в кокпіті значно зручніші. Скрипт перемикатиме застосунки на передній план і назад, а кнопки-стрілки можуть працювати як миша, якщо знадобиться щось «нестандартне», але здебільшого це буде панель приладів. Режими:

- Карта (передналаштування OpenCPN).
- VNC, копія головного навігаційного екрана.
- Вітрильна панель: великий вітровий прилад, SOG, STW, денний лаг, глибина, позиція, COG.
- Моторна панель: малий вітровий прилад, тахометр, температура охолоджувальної рідини на виході, тиск масла, інші температури (охолоджувальна рідина на вході, вихлоп, редуктор, сальник валу, забортна вода після теплообмінника), а також SOG, STW, лаг, глибина, позиція, COG.
- Керування авторульовим і якорем/брашпилем з лічильником ланцюга, як спливні вікна поверх.
- Камера з топу щогли.

![3D-модель NavPod](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj2boAxQ_qniiTozrH4ndJi_oTBMcr43tb50vrI2VDOCTbChLA_hDCrT2G9tzcndrOT-pNuMhyDI_7ICG6sQBAcN7IgKiJMIFymb-IZF5-PgM8D0XgBZPymA53hIklsB0mGL3-1RXxiGW5H5LfqWXGigRD4SJ9xnCQR51t-G9pzhW1dBIJGBcB93gIDA_-/s1600/1.png)
![3D-модель NavPod збоку](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb1xJ08sMaI04XOUs6L8xzD5RVzIN81EWkAedlC7AzX9PXYXugRjBcGrC0Sr4gemsUM6wshBAkKyefOMKkTj8isRY787A3b80D8h9z9T0PmKrkLtig3jK2Ck6AG43iSLvdBzWn0wi-2wPFyKRbKVLqMeNLYNKXip16cOn1MCabxZH3RV8mhr1o9f8mni5u/s1600/2.png)

Diary: [22 Apr 2025](https://irwin34.blogspot.com/2025/04/day-196-at-desk-navpod-design.html)

У липні — примірка NavPod.

![Примірка корпусу NavPod на тумбі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-63vqt8nugM7KxG7k52U_V96JZWZ9It8AOBvmdnKINlNccnDivMDvsHU4gTWsamRfub6xkl3iA-mk1qBfJZL2WNjc-Fx59MKB4Oz7gRgnpdNIH1rZHhW_aQotrX9KuqgZ1EH6Lb-gc9OVEWE8WpP1OaSqadWeIEaIc-EVWoTbeGLTRcZoMKG9YxqHiG6v/s1600/IMG_1038.HEIC)
![Корпус NavPod на тумбі, вигляд збоку](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn3f5z76nlAvdd31b8rva7-h4i46OG12u0l-QYev2dpXP2VppPp8-AxkdGSNTVMlB-TM18gF5B5ozyR2CqW7DeK4G5DRM0x5-xnxANAQPgw2FLaLKQpNIqqyysf0xLROsvfjAzRCcBMxXhbx3GB76Uye-DiVA3TVZPYBhQ6aK_FqPrZwIWt2lYV2zAmra3/s1600/IMG_1040.HEIC)
![Корпус NavPod і дуга ззаду](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3JvAuwGoOwN7CCH125mnxq2ES5cChlxHqdE8BklILJQw2Z2MefWqM0AI0TuvXPjHYYvCN8U3i5obdAJfxvHQ0yNqiwiPM5_ujBLfFqIwWStFW4HhhK-95MKbgW7kLhBpT5sL8Nxyt5kdoF_ArM0tXjZD6AUbvQ2voZByc3-zSXNR39ZsWzMFGaYoyriIb/s1600/IMG_1039.HEIC)

Diary: [19 Jul 2025](https://irwin34.blogspot.com/2025/07/day-208-autopilot-arm-reinstallation.html)

Передню частину я замовив у JLCPCB ще до мит; задню надрукував удома на смоляному принтері, зі смоли «на кшталт ABS». Ось коробка на примірці на човні. Потім справжнє збирання: макетні рамки для Pi, плати-адаптера дисплея і блока живлення підсвітки.

![Задня частина NavPod друкується на смоляному принтері](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizvWM2RegnSHUOEUdu_hDxvvYg_LS05drSip01nqgAHGt0KYvNbFtbqK2hOZaPuOLMmSZTkvxz-cNjYXQOgLkGE7qW9B35mnViP3X-xzAIfu0BdNDGcfPMNPVoRG1PMjOquh_XTrWRGA6BjmFey824ZdVxWuJp655Ybw4pL8wWLj6XWZTYPh1rQqC3yGmi/s1600/IMG_1016.HEIC)
![Корпус NavPod на тумбі, інший ракурс](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoLz_sbPGMFEuMUHtNRLDcvXvEm-eIVc3k08MJXyTy-HCoMs_Wzn8LEzKIxeXC7Jrm-qM9Kj7nXSBUx2_ifBCQqUAftlTrvyergtMUzPSLtYRdP_7Xhwn74FMJUG5jqJe_bxTDNs64055IU8O3nxrKFqqIWuHBxZm3zvNV83OE0dGDnOIj4GhLZijPGsLO/s1600/IMG_1040.HEIC)
![Примірка NavPod на тумбі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWZuhZisGIfPoSxFjdBETB_d13g0JFK5Lgzk3PsScbw5L6lUmm2yEUgh_1Ayw3p9uRGuFO6X_oqnFMq7upkWO7U4DKRPpe3pPm0D1KgF4bQ9eLuUe50NGhGrTZy9UfwIy-Q-n5bGJFtBu8IxrbI_yWZBh6TLm-_AVdoO3DuJ_e8v0tJg91GBplHsLezfeu/s1600/IMG_1038.HEIC)
![Корпус NavPod, вигляд із носа](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-z8gR9u2m9JGBfR8G7aOzJJvaTI_8PyZxysVm9Rx6pKGH-HlDi_8KnwXOo3O2wD7xJatA04HG47LLd1BwkVwf_BMs6k5hTZY6vQTVTT_cDBL3Eac1KueDScrvsaEGwGL6bkmgw2kQ2j7uUdEUS-4TOkzPS8Ej2URqIcRd9WL8HrwqP68FAD1F613FsFTn/s1600/IMG_1039.HEIC)

Story page: [Helm instrument console](https://irwin34.blogspot.com/p/pedestal-helm-instrument-console.html)

Усередині, шарами: контролер дисплея (HDMI на LVDS) і живлення підсвітки, Pi згори і його монтажна рамка. Потім лицьова панель з платами клавіатури.

Програма — набір окремих застосунків на Python. navpod_manager спілкується з клавіатурою, перемикає застосунки й прив'язує до них фізичні кнопки: OpenCPN, navpod_dashboard, Engine_control і Anchor_control. navpod_dashboard показує вітрильну панель із Signal K і PyPilot. Engine_control показує детальну моторну панель. Anchor_control — якірна тривога, яка також уміє керувати брашпилем, з власною панеллю.

Нарешті — на човні. Чиста установка: усі дроти всередині поручня огорожі, а коробка прикручена до поручня машинними гвинтами (поручень просвердлений, з нарізаною різьбою), з опорними пластинами всередині пластику. І вигляд у реальному світі.

![3D-розріз деталей NavPod](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEit-3C_4ulmZdICEZhOSKm36R6nrh9_yeDSY7i3IaEMhkjqrIOiZiAuB3wRqqc4yppd1nYf5p1N_n_0txw9wmYpYxhXQqJCunpIy0o54UDNhHH0qXMmIqQEEoSur3zL-X4it4lnbtGxDTKfZlgfNfjRL_goQzOYImEhgFeJlsrIgVYSw62kpzmcHRgHiP0N/s1600/Components%20inside%20the%20box.png)
![Переріз NavPod](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpZNaQ6P4RGmW3Psa2JlHTG8qGLAEaMBLvwjE6Qu0ixBu9D53wt3Xa5NNm5TlYNr8kgkE8JvQC66IvUvB9O7WjjacPInYIu-3wzAnk9kh14i0MVhH9-h6IM8m2V-o9Riba4bwR4HR1fILP3k4RdvpOTG-3khQZ6O8KKZVYy2uS5Mjw8108iXN0SaMPGRUq/s1600/navpod%20section%20view.png)
![Контролер дисплея і живлення підсвітки](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFUEVjUJbOGnnZRl-R-5cipa2_ZvLA-zyPemNWSS0Vl-h6cJggxMU7POd8946OMAfmnpkiYzifxf0TQswMT_8pFQjwFEzgrJ9thmyTAedHyHS7_cc6-vNjWxf3kosuZityO4VETaUi6zIo3I8xymPjCL9wv-6ttARZk1Vp35PqxXdXh1cm813ufXqPmfMZ/s1600/IMG_1294.HEIC)
![Шар Raspberry Pi над платою дисплея](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggzxf5MDJ_g2bScwfem3DSG-iI2CwrUr2rnsem4htt1LvAGOA94EwC7At3L2COl5RDVQe4dbK8CITm2ZdbX1OKz_2UUS7Z-3lnYVB_C6rL_r57Yz58Wap4faNXMRYbFG5fpxmZBGdqUeHw0bTj_VC8z-r1aX0sSMHvsf4SJaAjtQ8t-L_vhYW24j-I3Iei/s1600/IMG_1309.HEIC)
![Стос із Raspberry Pi і дисплеєм на столі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjP6egf4w6MgvQMhttv5E4KwmFnoktuorHA9U-nJTYUJ-AVVj_UTTngps1TY0oPRs5GHCS7I9nVvLwf106eJ3TSOmjqqslJMj8WYeOexnQUDOss9mg4TFmsz4auBsjpDbNFRJ3BQwh5mpkEBqifkTf3pWXCo4cDrwedq7UOzoEeK3krajZ_FE2VTg8Hq3S/s1600/IMG_1295.HEIC)
![Лицьова панель NavPod із клавіатурою](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxVdL4PzMS6v5MQnwBJwSYUnKQYjz2bYKGGLMN8bAqa36YOKoIupoXsYX_toOCOci7D_c44HnjWWqVCGQ2i0vBTuZ8uAb8-GArcOQnxSETB4d7__E7WckW9ElZFW1DEZn56BSzJJ8Zq1QYPYYCek9-_O0uVHvzmdAfWLeaw201FEmZVqklG1YQShPwljvC/s1600/IMG_1293.HEIC)
![Передня частина NavPod з увімкненим екраном](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXpNdqLpaIjEVJK2jE5RXKq7UNMiTUkT68-VNKZKzsN4Y2sk0JcsJxJrIHU8CyjNT5qfw2PEH1OsFHLAYQ0CPUlQg72ennduUB_va0tEIWL2YdzMB3FO3Mztk83ryJqR9QThO71KZllWxEikO-FzQ50GDEk-BxBKtWq6Ynqn2AI9qpAgBY8K3b-GE73jgw/s1600/IMG_1299.HEIC)
![Вітрильний дашборд NavPod](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKpewpIL_BDwdigud9aVC_Bt8wNRNqMOiUOrfhOSnJO694kAbRd4t-7sMQDyuKbDajLb6cl95-gVGo13ZFTi7-UgOZjtfxyGn_NtyO4BnulBfIqGUyjJ8idCI3Ecv7Lzxw6jZVbVx-bvWwoF4ZZYcssk0gku_8wB2w-RujjywxqH_V96p1muU9yByXqQyK/s1600/Sailing_dashboard-day.png)
![Вітрильний дашборд NavPod з авторульовим](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjL8oCp8M5NXQIGs4l76g9XkMucxb4HJiq4sG3WneJjYLYK5zyoJEl8A7gkeiUO-QnMUhuHFdKRi67NhaNQmvT8zCaf-SI41mw1uwd-MOQF8fzW2s1f8I50tgFkL0huYM_QyRRgoMM2bC_P4oH-uaB7Cxf3pjeaYjAv7yx-VOmHd-psNbJZH57JYfpP1Box/s1600/Sailing_dashboard-night.png)
![Моторний дашборд через VNC](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLfaOz1g-FaFc7Q25dBeK0iTUf4WAoUjc67MDazSU2xdtaHULW0ZXxnthSX5i6w4K2ihKEunyahPTXoKR5ZGP3J7azD3v3QNeFpmNbiMqiw_f0FOt49YsR1M5zbouy56M94EWVdg7kT7OIoYGg3HNDjbOcajg2b7YewWJ1HlErVXl6_sUgvPOH6UyDRwZW/s1600/engine_dashboard-day.png)
![Моторний дашборд на NavPod](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxMo0H4OX3tReXbfAuG0DlO1IsD5kX2UO9xFk5NVPWDrEBmQL5cYUrG5Frkhyphenhyphenrn2uZ-Mkj9jjjFDkC1OWZv_aIz-DBCjFOEuR03AfoTh8Cq2H9BRFHTIuWOe_LwMc9nxjzt5WTVAEEGN3GS2kZxwtUtmoyFFrxHyplYlduzqrBOU0rjbxewZ6BbT1lak-2/s1600/engine_dashboard-night.png)
![Екран керування якорем](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikptJ-HTeuFJTaK0xqJh4Ij5CYvjmVjCK5v0sU2dpKXaWo9wuZBu65l2jURTe2CG1rF-vuuhSpvGS1IpMDVfglAewJpAPMTFSeOgX8IXZkETj-lz_prvZx051wNp3r0-HMaYIs5m-MbcMv4aBRZq061xMYrE0hc1PqUU3iXRnbcGPo8HqvTdqVfbgSaMTF/s1600/Anchor_control-day.png)
![Екран керування якорем, якірна тривога активна](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfXDetB9CmEJNnGXeN3ssjhemFyHT34KIv90zKc5TJCQLmanb4fMcpVFDWA9G0bw-n4Hl6pYDCKwTiaSZZYi9lJq_3r66TfVFxm5IsG0QU8CqFNv0f0KtcUbQR3g_vzQLRhYskVMxl4fATusjXxqYgaR9FboKvM2BZQxG2W2TAxMDXc_O5p0kpHS8SczcM/s1600/Anchor_control-night.png)
![NavPod на тумбі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn9W5OMGHdWik__1JWnp7svdHSM4QtdkLXyFOVN-tJ-13kV1_EuJSB9SpF72W39bwZ0MAWnyzqz0UvZdfcq5mb09v4vRf7saYhT0i5kLHxrzI6nXOr3tfK9uajnosgqQ4vjaH8k4M7Us8dfJQLYpG4VaU_0_elG39CC_a52KnnMQvdbBM7qOO1E9IjwO5B/s1600/IMG_2271.HEIC)
![NavPod показує моторний дашборд](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeW_Ub1562uLkio219CyFr11SFzcktXplddLgQGq0wwOwFdv49VCkQSAyphmLo3NYXEtQuod5oR6DLCAbqlw2D7KdFXBtEYT4gJk3AYhTAF1hl9k7tz1REF1Szyvfht1z72WBUFBYZd6yKczcJYQ1x41WxqEfJGtAiLB98brBWeEI8SorbjiVxm9aYUk2x/s1600/IMG_2272.HEIC)
![NavPod ззаду на захисній дузі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpNWFIchwDPYXwotNISFtmRDNx6E_BWbCvwXmJFHfLST7GayDng8wGxzoPtQ_PwDdenr7KOe7KrYok5TQd-oyoUeoRIE4ePVPTna9PCFbA9B5U-QfXlskxvBpm0bZKj4ukjy3rWueB0s3SMlqA89UEhjY5fNxQmaUQaYAwCOabLwA8EIg7fWZa0BKLhsJI/s1600/IMG_2269.HEIC)
![NavPod у роботі біля причалу](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJ8HJ3NHymmC8Zid07n4PzTcBBHmHjgBTwLy7aqGM4Y0EYO45WEpTm55a5jdShx5kAfgwR6DNxvptP6EIrestXQlckhD4PxflVYNm9CFy7VtclcyI8ARVopJJFi_x5HaNWVuVQ8aizfl1I2vBSUGlneT-T4zdzzZnzLOjaEeI0uvCT9M63Z1invuNSZWQH/s1600/IMG_2607.HEIC)

Story page: [Helm instrument console](https://irwin34.blogspot.com/p/pedestal-helm-instrument-console.html)

Як працюють кнопки. Лівий модуль: MOB (працює завжди, коли є живлення); живлення (одна секунда — увімкнути й запустити застосунки; коли ввімкнено — одна секунда перемикає дисплей і підсвітку, подвійне натискання — мінімальна яскравість, потрійне — повна, одинарне — на крок яскравіше; утримання 3 секунди — вимкнення, 10 секунд — знеструмлення); VNC/MAP (натискання — OpenCPN, подвійне — VNC до головного комп'ютера); вітрильна/моторна панелі; auto/anchor (натискання — панель авторульового, подвійне — якір і брашпиль, з правою панеллю в режимі клавіатури); і клавіші авторульового: mode, tack (з кнопками ±10), STBY і AUTO.

Правий модуль: режим миші, блокування і KEY/NUM. У режимі миші стрілки рухають курсор, OK — ліва кнопка, ESC/Return — Esc при натисканні й Enter при подвійному, а при утриманні перетворює стрілки на прокрутку, а Right/Space — права кнопка. У режимі клавіатури стрілки — клавіші курсора, а Right/Space і Tab/Next надсилають Space і Tab. У режимі NUM кнопки авторульового стають цифрами.

![3D-модель NavPod на дузі](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQu3O8YG_f7kx0jblnZdMRTWMdv-6VQU5K7kMieP0IPyLcuBIuH5vZZb1jltBYlQex5ErKJHU9rqYLm7GNzrWEfPGs7cVV3rFvgjyPPOq6LcftIWEA-iuN3CkURhrp4hqinw_tAkdHj4s7LsJiLqeXiIn8NVxRYEe0FRfjl9qQ_bYvWIS4KGxF0i5blwDI/s1600/Pedestal%20top2.png)
![Розташування кнопок NavPod](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUyuJ2U8j__wvfr_7SHeJ8UhgbDT_iZ57EdfUwgw4YEm1PfdJRVbwAxjk3CEkAyZPJViKIxRHdalVmoT2NLFq9cNqH8A1ySZ4XbqZDb0sOtuPNVT2SSuBkO9gPFLttlFtjROOt4Qz8H66JK2ySbZjO7LJQ3mr2vrO_E13DtUlKvQZ5FP-TiTeEPLPaeaau/s1600/0.png)

Story page: [Helm instrument console](https://irwin34.blogspot.com/p/pedestal-helm-instrument-console.html)

## NavPod завершено

Травень 2026-го: вікенд програмування NavPod. Це другий головний блок на Raspberry Pi біля штурвала, з 7-дюймовим дисплеєм на 2 000 ніт, що регулюється від 0,005% до 100% і спілкується з Signal K, PyPilot та іншими застосунками головного комп'ютера. У нього 26 кнопок і симуляція миші. Ліва панель: живлення, окрема кнопка MOB (зберігає позицію, відкриває OpenCPN і ставить мітку MOB), увімкнення/вимкнення передачі AIS, три кнопки застосунків, і авторульовий: режим (компас, вітер, GPS, справжній вітер, навігація), AUTO/STBY, ±1°, ±10° і поворот. Права панель: кнопки режимів (клавіатура, цифри, миша, блокування), стрілки з OK, і Enter, Esc та Tab.

Вітрильний екран: прилад вітру/компаса з вимпельним вітром (помаранчева стрілка), справжнім вітром (синя позначка), течією і знесенням (зелена крапля), курсом, режимом авторульового, положенням стерна на силуеті корпусу і червоною крапкою в бік наступної точки маршруту. Бічні панелі повністю налаштовуються: ліворуч SOG, STW, глибина, температура води (:-)) і стерно; праворуч час на кожному галсі, а також напрям, відстань і швидкість до наступної точки маршруту. Будуть вітрильний і моторний режими, а може, денний і нічний, але спершу хочу побачити його на яскравому сонці.

![Вітрильний екран NavPod](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7FgVmXgMaP-EaGI-kHqKLydqmJ7feMSUpsWRVZdvQ00iNc6bhYoY3ThhwBtZStQimMHF63uanml1TUYk-2-NuSRTZcEbZGfTy_n0vwooglKqG05pL7UmwrjwrJnJtIUj4ZJc2OqU_DemkxpzjReLssrlw2Vodmhsn9qZ50C1sv1P93IqeKgV9JAXxfCmt/s1600/att.6pjuSwuoicNWNgp9kRaK3r857K-U9u67dJDKs1kxdbs.jpg)

Diary: [18 May 2026](https://irwin34.blogspot.com/2026/05/homework-navpod-software.html)

У червні: примірка й ходові випробування. Передню панель ще треба пофарбувати, а кнопки переробити.

![Примірка NavPod під вітрилами](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpKEIwz53hsvAWbUhZvaGKJkFsB6oqQxtACw52lRQ_G-WhdqNiIqJ8rd8ErmZxtWoh0NMrUFpvzPIddDqenVtO85XATJtIZUnJ3wa59hR-ggi-S1UOOawdiD-6d5muTE1SiOPuFdqDlxSFDYsxTRvboGxhL2Ov-i-P-I0o4RP60z1_pBvDPNZDtVP2RwIG/s1600/IMG_1579.HEIC)
![Екран NavPod під вітрилами](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4WPy2xaOe11ocqeYjaR_8iruVwo9_FYJ0iMULeqSy4Qr785WDOL3QilXC7cbDIDaEw23Ex-zzrkm7PeK3q9lHolCl1LN76HXBfzafNJZt1RCGE6iP4pCdAS2p8VMwpitqaYdGJHJveT1FOt4zjYMnE8VM7j0AjWQjUM9Ms_NNK1GDsTNHnZdTOpkl4FYX/s1600/IMG_1570.HEIC)

Diary: [14 Jun 2026](https://irwin34.blogspot.com/2026/06/days-269-270-new-mainsail-variable.html)

У липні — остаточна установка. Це не фірмовий NavPod; він лише схожий на нього, тож я називаю його NavPod. Повна панель приладів човна з фізичними кнопками: вітрила, мотор, OpenCPN і якірна тривога, усе працює на Pi всередині й спілкується через Ethernet з головним комп'ютером OpenPlotter. Поручень огорожі я забрав додому, просвердлив і нарізав різьбу під гвинти.

![Готовий NavPod біля штурвала](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIT_VuxfScw_W-akH8YxaTFf5WNvnYTx0QdB99wE3QRHsoZL7timHYxT11sDSrVN6DE0_uIfDF2DybIWGahm84gswugyPZ5eqGkwxnCevvBsMhl_-E7MD6whuWaNaZVaL-DMHRzy5mSdWN7J64QPeJB4XzphtZRa-g_ZYpJ_-zQoNWEZO8wHBcW3Pm-PBh/s1600/IMG_2272.HEIC)
![NavPod із вітрильним дашбордом](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiY-0i8lb4bnc-k3Gw-qoKVozJghKjjHzxxauqCYHabLrpdjc3RS-KNHxhgFNCwSJ9B7mxEPZqOnGIp4e4ChvBmsQ_txV04_Qs0YBWHLjgv5fQ3jtX5foFGcTvduaGM20T-3fwmfhufqWare-KwnVsghJpZnQOvAMIxXH_q0uQrfNfErABj4KRKHFRkTF7c/s1600/IMG_2271.HEIC)
![NavPod ззаду: дуга і проводка](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6aRBS89VleNcHl8A1PnTAuJYyyUuVF1XgU1PdFIpmTwA99cwa4YtV8f1Xsb2V5w3CzuQo2bABfpnqY2QIcmuDRFQja1Lw2qKlGeC5-UicjXBTbnXUckLWu1l4hAK4kDmkZ-nWCTrv5SWMllMcVAi8m2zOptKvlGLctiH1bPKJ4KjQelG9TquOHK2XLOM_/s1600/IMG_2269.HEIC)

Diary: [30 Jul 2026](https://irwin34.blogspot.com/2026/07/day-272-273-new-outhull-line-setup.html)
