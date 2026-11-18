---
id: khatkapi
title: "Baseboard for a Raspberry Pi based OpenPlotter computer"
search_title: "Raspberry Pi 5 baseboard for OpenPlotter: KhatkaPi"
section: electric
order: 5
description: "KhatkaPi: the baseboard I designed to protect a Raspberry Pi 5 running OpenPlotter on a boat. The design files are public."
cover: "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDISQp8fKd3wdyEauK5By6n9kwOg3wM9lpZgHxupcTVw_d5sU8bJBr5DTX0cuYpmaS5clgsjyNUUNf9lG_fRs8NCcQ7ccVKTR0lJLfagkZ8GR1HEilVxqmn0bYAynU_aDoSwdK6VTRy8q5D1dLjR2Ap9rf94b0tec7e8IfWdvWwuZRjOKDqzG5fOXg1LLx/s1600/59089.png"
---
This board is the home of Vira's navigation computer: a Raspberry Pi 5 running OpenPlotter. I call it KhatkaPi. The design files are public, you can [download them here](https://drive.google.com/drive/folders/1qK_36HSr0MhrJ2yZK5vT_KGrrQ-0Dkhr), and the full description is in my original diary article: [KhatkaPi Baseboard](https://diary.sailingvira.com/p/khatkapi-baseboard.html).

## KhatkaPi: a home for the Raspberry Pi

KhatkaPi is a baseboard for a Raspberry Pi 5 running OpenPlotter, built to really protect the electronics on a boat. I designed it, tested it, and the design files are public. ("Khatka" is a little house in Ukrainian, and that's exactly what it is for the Pi.)

The main ideas:

- Made for the Pi 5, as a baseboard, not a HAT, so you can use any heatsink case and NVMe SSD adapter.
- Everything lives in an IP67 box (290 x 210 x 100 mm), and the board puts some distance between the outside world and the Pi.
- Every interface has ESD protection, 15 kV air and 8 kV contact.
- Built to lose as little as possible from a lightning strike, a user mistake or some other device going crazy. Mostly common ground rather than galvanic isolation, but the data lines to the Pi are isolated on most interfaces, and outside interfaces get their own power regulators.
- And of course, a double conformal coating against moisture and salt air.

Power: over-voltage protection up to 40 V, and a cut-off below 9 V so the battery doesn't get killed, with an override switch down to 6 V for emergencies. Its own 5 V, 6 A regulator for the Pi. Connectors for hard power on, hard power off and shutdown buttons. When the Pi finishes shutting down, everything turns off except the AIS. A switched 12 V output, up to 4 A, for other devices while the Pi runs. And a spot for an HDMI splitter, so two mirrored displays work without software tricks.

On the board: an ICM-20948 IMU, placed in the far corner, away from magnetic fields. A PWM fan to stir the air in the box, so the heat gets to the box walls. A socket for an Arduino Nano running the PyPilot weather sensors, with a BMP280 pressure sensor on board. Three 1-Wire connectors for temperature sensors.

To the outside world: I2C (protected, not isolated, so keep it short or inside the box). Two fully isolated NMEA 0183 ports, one meant for the depth sounder. A port for the Maiana AIS/GPS, straight on RJ45, with switches for power and transmit, its own 3.3 V regulator and indicators. An isolated PyPilot motor controller port with its own 5 V. An isolated serial port to a helper microcontroller that gives access to the Pi's GPIO, for example for a remote button module. Two four-port USB hubs, 8 ports in total, each with 12 kV ESD protection, common-mode filters and its own 2 A regulator per group. And two power-only USB ports, 1.5 A total.

Here's the real prototype, and the board installed on the boat.

![KhatkaPi baseboard layout](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwkt1rcUeC1EALki4F36mmrsIqcPwe4NxArDa6MtXBEOqUTpg-EmIdYShXl22TQzu8aYp-WlFKsxHLP-QW_n0IKWG02SmqbIwCqjq5EFullP7KpLfqnkMMfhnt-bUZfKxz4kO4Yzy8f2OM_5rMyXrKO7-k7yS1CiGLykyxLY4zwT6wXbF7JVkaG1ZyMrxy/s1600/5908.png)
![KhatkaPi baseboard with Raspberry Pi 5 running](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDISQp8fKd3wdyEauK5By6n9kwOg3wM9lpZgHxupcTVw_d5sU8bJBr5DTX0cuYpmaS5clgsjyNUUNf9lG_fRs8NCcQ7ccVKTR0lJLfagkZ8GR1HEilVxqmn0bYAynU_aDoSwdK6VTRy8q5D1dLjR2Ap9rf94b0tec7e8IfWdvWwuZRjOKDqzG5fOXg1LLx/s1600/59089.png)
![KhatkaPi electronics box installed behind the nav station](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbKxi_wnI-CDEV6IoMSZ4Zt_KII361qy2rYRKJ3wrTzlktjrGEvVc5rVKNdlrDyIdFiKZ7fh53nvmgQjf4dR5SSxkK7GGtv-PJ50xijgYeAH1nc-YND0x4KCtshUryltapZwoP2oc16Pt0GCqs2D6nOTwlg_8ut6yFbVYWp5qb7IUbbm4YYxdaklrp2pvE/s1600/IMG_0407.HEIC)

Story page: [KhatkaPi Baseboard](https://irwin34.blogspot.com/p/khatkapi-baseboard.html)
