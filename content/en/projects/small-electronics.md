---
id: small-electronics
title: "Small electronics projects"
section: electric
order: 3
description: "Home-made controllers: KhatkaPi, LPG, shower, dry bilge, tank fill, lights."
cover: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGG2UhzxmaO5JBVW_bRLnzAqq2ZtpCX1HdFAoOOtKT-UNazweH0G8msNDuS98R5eTgbjbs7ZpmrZVlwrRNAonlhjDnZFlA6yT1RSY0oV-kG-QZzfXGdIKqJjRjdYyeYvnY2oWEJG-rfGXjpGV2jfyACkcXKhS1ux6YjNGJR3pG_qEzhUFKMqjPHHdG-uqB/s1600/5B20C409-8C04-48EB-8FA1-199F821AF230.jpg
---

I'm an electrical engineer, and at some point I stopped buying little boxes for the boat and started designing my own. Every one of these began with a real problem on Vira. Here they are, with all the details, in case somebody wants to build the same.

## The family

For each project there's a full page on the blog with design files. If you want to make something similar for your boat, just leave a comment. KhatkaPi baseboard, dry bilge timer, shower controller, LPG solenoid controller, water tank fill controller, panel light dimmer, masthead tricolor/anchor light control, and the PSU/battery power switch.

![KhatkaPi baseboard with Raspberry Pi 5 for OpenPlotter](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDISQp8fKd3wdyEauK5By6n9kwOg3wM9lpZgHxupcTVw_d5sU8bJBr5DTX0cuYpmaS5clgsjyNUUNf9lG_fRs8NCcQ7ccVKTR0lJLfagkZ8GR1HEilVxqmn0bYAynU_aDoSwdK6VTRy8q5D1dLjR2Ap9rf94b0tec7e8IfWdvWwuZRjOKDqzG5fOXg1LLx/s1600/59089.png)
![Dry bilge pump controller board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimUbYFpIufc7aYktP3IeO9BAqDa3Tk4PfOVuauAJFaslT6cPsK-rdJIgWYWh7Cte0Dg0hBd1QrmpPHkzWd7uyCTBmE34ro1l3JXsDs2kwmtD2hWJry8_COv-KjbEtWAAXx_VX7PxXEYS10yyA4y35N-3RIiZlku1g_2PhavcErNxkcpHaBdoMQVX7SkGTy/s1600/2.png)
![Shower controller board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjOxmhhVuM0w4lrJFe-Ow_rUpBGXRyLfUP3V0Gmaarfn9x6-rIYoC4OtONZ9LB8Cz4zRnlzBTVpTcUI8W9Unme3Pl09vU8MmyHC0npN9NLFBUhbOGEQCVeZsA0Fp_a9_LBh6MEtkGyX8-o9jkVXD1Ci2Miw-MbeVrjZMLRilqPS24t0bzeGSjPR7yKfgAc/s1600/1png.png)
![LPG solenoid controller in a sealed box](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnghRYkFJvTSNtbreVWL31m_R1QvQmWpf05KVSC_4X5qfULjWOlj6KJLaTUVZUMtFCVicL44NoNtb4JiUIr46FToxeYntxuezq7qbIhh-H5wnFJAzmTBOHydYDIgGq-azzLmuSsqO_ikKCeymFl6c_q1MtmuiWosoWWR_nVc9Tacg_GIPsMf7BVAsfpFb1/s1600/IMG_0960.HEIC)
![Water tank fill controller in a box with its level sensor](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVgwCyvanwmR5a8HBvjhbPOLkjJ2hFy2c0hfKuZdvMBq-cWzV5H0dPv33EXxUW09umL_BQSVeWr0CjL-aMWSiHbzx11R8RQfjrW33f_8vhmdo4uz7WkQTv1NdJF22-ljlnGfFIZs0MvdZBEqJXVv8C9XN2O4P4nnHOk_cIGwXouZMm8mYHh648rsGJymT5/s1600/IMG_1227.HEIC)
![Panel light dimmer board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![Panel light dimmer board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![PSU/battery power switch installed in the engine compartment](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgt5QwjQI8yvf35BI-HY8X9oEcSq8nT0desmzVDIegUHXxfsGRYYzFeRW6ar1hOSA1ylagUSRavgX0JD4jq2acwkUflqduDtikkB8BTMaQ2UPRN2a6kF1EytlzEzQZq6fEV1Ahh_JJXDvseHUeft9qVt1dNOodeF8Hd4oSJlJJ55ltFGw1L8KH00s8XmaDt/s1600/IMG_2341.HEIC)

Story page: [Small electronics projects](https://irwin34.blogspot.com/p/small-electronics-projects.html)

## KhatkaPi: a home for the Raspberry Pi

I designed and tested a baseboard for a Raspberry Pi 5 running OpenPlotter, built to really protect the electronics on a boat. The design files are public.

The main ideas:

- Made for the Pi 5, as a baseboard, not a HAT, so you can use any heatsink case and NVMe SSD adapter.
- Everything lives in an IP67 box (290 x 210 x 100 mm), and the board puts some distance between the outside world and the Pi.
- Every interface has ESD protection, 15 kV air and 8 kV contact.
- Built to lose as little as possible from a lightning strike, a user mistake or some other device going crazy. Mostly common ground rather than galvanic isolation, but the data lines to the Pi are isolated on most interfaces, and outside interfaces get their own power regulators.
- And of course, double conformal coating against moisture and salt air.

Power: over-voltage protection to 40 V, cut-off below 9 V so the battery doesn't get killed, with an override switch down to 6 V for emergencies. Its own 5 V, 6 A regulator for the Pi. Connectors for hard power on, hard power off and shutdown buttons. When the Pi finishes shutting down, everything turns off except the AIS. A switched 12 V output, up to 4 A, for other devices while the Pi runs. And a spot for an HDMI splitter, so two mirrored displays work without software tricks.

On the board: an ICM-20948 IMU, placed in the far corner away from magnetic fields. A PWM fan to stir the air in the box so the heat gets to the box walls. A socket for an Arduino Nano running the PyPilot weather sensors, with a BMP280 pressure sensor on board. Three 1-Wire connectors for temperature sensors.

Outside: I2C (protected, not isolated, so keep it short or inside the box). Two fully isolated NMEA 0183 ports, one meant for the depth sounder. A port for the Maiana AIS/GPS, straight on RJ45, with switches for power and transmit, its own 3.3 V regulator and indicators. An isolated PyPilot motor controller port with its own 5 V. An isolated serial port to a helper microcontroller that gives access to the Pi's GPIO, for example for a remote button module. Two four-port USB hubs, 8 ports total, each with 12 kV ESD protection, common-mode filters and its own 2 A regulator per group. And two power-only USB ports, 1.5 A total.

The real prototype, and installed on the boat.

![KhatkaPi baseboard layout](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwkt1rcUeC1EALki4F36mmrsIqcPwe4NxArDa6MtXBEOqUTpg-EmIdYShXl22TQzu8aYp-WlFKsxHLP-QW_n0IKWG02SmqbIwCqjq5EFullP7KpLfqnkMMfhnt-bUZfKxz4kO4Yzy8f2OM_5rMyXrKO7-k7yS1CiGLykyxLY4zwT6wXbF7JVkaG1ZyMrxy/s1600/5908.png)
![KhatkaPi baseboard with Raspberry Pi 5 running](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDISQp8fKd3wdyEauK5By6n9kwOg3wM9lpZgHxupcTVw_d5sU8bJBr5DTX0cuYpmaS5clgsjyNUUNf9lG_fRs8NCcQ7ccVKTR0lJLfagkZ8GR1HEilVxqmn0bYAynU_aDoSwdK6VTRy8q5D1dLjR2Ap9rf94b0tec7e8IfWdvWwuZRjOKDqzG5fOXg1LLx/s1600/59089.png)
![KhatkaPi electronics box installed behind the nav station](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbKxi_wnI-CDEV6IoMSZ4Zt_KII361qy2rYRKJ3wrTzlktjrGEvVc5rVKNdlrDyIdFiKZ7fh53nvmgQjf4dR5SSxkK7GGtv-PJ50xijgYeAH1nc-YND0x4KCtshUryltapZwoP2oc16Pt0GCqs2D6nOTwlg_8ut6yFbVYWp5qb7IUbbm4YYxdaklrp2pvE/s1600/IMG_0407.HEIC)

Story page: [KhatkaPi Baseboard](https://irwin34.blogspot.com/p/khatkapi-baseboard.html)

## Dry bilge

In January 2023 I tested the idea of a "dry bilge": a box with a sponge and a membrane pump. Works perfect. I also tested the manual pump. I could pump it out in a minute or two. Hard to prime, but doable.

![Dry bilge test: box with sponge and membrane pump](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgN-yYrILi2BXUa9z_kHLwogw2VM5mN4u0gMt9V_pvf5ohn9F_m5gstX2U_4tZ11sTIJryf7qMxaUWsWsLgEBBwAX7KpcomTSFu70yMbR4oR_37c1QaJ66FB0ZNh69xAzYpflIWVhxe0CcTMlDXQOQAWNxJtgPgIRxDsK7hZlDVWflxL3-VrrUt6bowbg/s1600/IMG_4595.HEIC)

Diary: [7 Jan 2023](https://irwin34.blogspot.com/2023/01/day-75-1723-shower-walls-gaps-glassing.html)

In April I installed a small self-priming pump for it on a plywood block glued to the engine room wall, with the output into the cockpit drain. I drilled a corner of the drain fitting and cut a tight 1/4 NPT thread for a barb. It dries a quarter-flooded bilge in under 3 minutes.

![Small self-priming dry bilge pump mounted in the bilge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibGcQ5YbhWqNXOgb1B_KDJmNEr7VGHefPQvfTHWL_nElsipHgPus1PM8GYM4M_vCUlsOkdc80Bj5mvjudpgszyPOcnME1zw4aOAoAdz-zdQhmzjbYrNUg0hb4l9AfTTsx54Qr8d0gYT908HIEcekPKpq3QmLE2NZlk4lEzYunkKVfA1Vm_bb4XLlEeuQ/s1600/IMG_5539.HEIC)
![Dry bilge pump hose and wiring in the bilge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj28yjQ6o6aFDGNbU2kILUkQ7-PDXJP7PCMmzRIXbMCMdrBkRY2Q6tMGa6Rkv08WWysGe_GiCmw4GyW9560kAusAiGpmQ3RQXqJu3Ulhxi2dlp4vf5iT7KUlBPZ16ZeaxP4JRy4of9b5LQ7bYgb74K6dOftLngZYJYsQYK7HbzG-X9h01pcqI6KeODvjA/s1600/IMG_5540.HEIC)

Diary: [8 Apr 2023](https://irwin34.blogspot.com/2023/04/day-84day-83-4823-rebuilt-ducting.html)

In March 2025 I 3D printed a new intake box from TPU. That one won't crack again.

![Dry bilge intake box in the bilge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCeccQKVbuCRbyujrC8knGKIJ9i8QoMlB4BTNpGln8GvMH-kOFpvNyfNNcJE7ph1748xrFbrftZZbFpI5En9tUaJ6Cp89A_bjcqzlKmm3GGDqCEndloOrJeJ6pp2L2ELDHjFOeK7pCDEDQqn3PFeTePpv9ZAtrjR580KRE3BtD2DgyMoQpnS3P2cpqPl8D/s1600/IMG_0227.HEIC)

Diary: [9 Mar 2025](https://irwin34.blogspot.com/2025/03/day-190-hvac-air-dirtribution-redo.html)

Then I designed a controller for it. When you switch the breaker on, it runs the pump for 3 minutes, about how long it takes to get the bilge dry after the main centrifugal pump, then waits 24 hours and repeats. It also has overheat and overcurrent protection. The light on the board is off with no power, on while pumping, and blinks slowly while waiting. In June 2025 I finally installed it, the small gray box on the wall.

![Dry bilge pump and wiring](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCxQEkJnMTwXxOngCsF8xUSsc5dtbBWS-uADjBzVXs0U8LQxDX7C16xYpiMgUNdECXhn_St9IH_9COMaDvv0QajPWGnSdi_wGYPYRoHhW_yk98qUN-Hsa0siFF-8UxafHeT2Vs8IK5KKy20vIt59kHqNcRnRlFAPEZxbGMxX2uxkNzfguK5bNQQf_Gu4sw/s1600/IMG_0828.HEIC)
![Dry bilge controller board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimUbYFpIufc7aYktP3IeO9BAqDa3Tk4PfOVuauAJFaslT6cPsK-rdJIgWYWh7Cte0Dg0hBd1QrmpPHkzWd7uyCTBmE34ro1l3JXsDs2kwmtD2hWJry8_COv-KjbEtWAAXx_VX7PxXEYS10yyA4y35N-3RIiZlku1g_2PhavcErNxkcpHaBdoMQVX7SkGTy/s1600/2.png)

Diary: [15 Jun 2025](https://irwin34.blogspot.com/2025/06/day-203-61425-engine-emergency-manual.html)
Story page: [Dry bilge controller (timer)](https://irwin34.blogspot.com/p/dry-bilge-controller-timer.html)

## LPG solenoid controller

This one adds convenience and safety to the propane. It switches the solenoid without sparks, protects the circuit if the cable shorts or breaks, and limits the holding current so the coil doesn't get hot and uses much less power. The valve closes itself after 60 minutes. One button with an LED, and it can work with a gas sensor to cut the gas if there's a leak.

The light: off means no power. A dim short blink every 2 seconds means the circuit is OK and the valve is closed. One second on, one off: open, more than 10 minutes left. Fast blinking: less than 10 minutes left. Three short blinks then 5 seconds on: the 24-hour timer (not recommended). And quick blinking, a second on and a second off, means a wiring problem.

Button: a short press toggles the valve, or restarts the timer when it's about to run out. Press and hold for a second, and it's off.

![LPG solenoid controller PCB layout](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5q57sCDrG3AN8PpW8LwqTGQbV-7s8qR_fw0IxQmZD0DW1XzmHn5XM_vxeGB41FDVHzbmwbguiauvTUsX8XGllGBm-ibBmdD8BQS_V2o24VDpbe9HrXeSXiFeP8sQmg8fuQ7z7dcOQVznDflz5G-Se8F7EGlmXlemD9xzoT0xk4Ag_w4afwaRUeUj5yaSo/s1600/lpg1.png)
![LPG solenoid controller board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVeI4Id9FiqPDblo3QlnJ7hTNEFCpda1Xbp6sQnsS72v1ofrxV09IgniRtwGDQQjg7Q9ZYkf2IAh9faF2-oB8rgsQepTAuewgUAZyv8YcI5WjSh45brU_Xb36hrgZh3G7aL4wf_GRial4y-QCJ7iaoakFPF-Qhb7XB7KdToRc2eK4wqhlsnBEzsH1JyTKz/s1600/lpg2.png)
![LPG solenoid controller in a sealed box](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnghRYkFJvTSNtbreVWL31m_R1QvQmWpf05KVSC_4X5qfULjWOlj6KJLaTUVZUMtFCVicL44NoNtb4JiUIr46FToxeYntxuezq7qbIhh-H5wnFJAzmTBOHydYDIgGq-azzLmuSsqO_ikKCeymFl6c_q1MtmuiWosoWWR_nVc9Tacg_GIPsMf7BVAsfpFb1/s1600/IMG_0960.HEIC)

Story page: [LPG solenoid controller](https://irwin34.blogspot.com/p/lpg-solenoid-controller.html)

## Shower controller

This is the one from the head story: it opens and closes the shower, and first pumps the cold water in the hot pipe back to the tank, so you get comfortable water almost right away and don't waste any. One button press gives one minute of water, and it can take a foot switch.

The light: dim red is standby (HOLD). Amber is priming the hot water. Green means ready. Green blinking slowly means the shower is running, and fast flashing means 10 seconds left; press again for another minute. A short press starts or stops priming, and opens or closes the water. Press and hold for a second to stop and go back to HOLD.

![Shower controller board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjOxmhhVuM0w4lrJFe-Ow_rUpBGXRyLfUP3V0Gmaarfn9x6-rIYoC4OtONZ9LB8Cz4zRnlzBTVpTcUI8W9Unme3Pl09vU8MmyHC0npN9NLFBUhbOGEQCVeZsA0Fp_a9_LBh6MEtkGyX8-o9jkVXD1Ci2Miw-MbeVrjZMLRilqPS24t0bzeGSjPR7yKfgAc/s1600/1png.png)
![Shower controller, mixing valve and solenoid valves, labeled](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0z-fG-i5amb1M4BWsHUWX9Ae4S4lVhDk4liUh7s0LyD6RHyO_BD_LyWmVTRYbpZN-PxaG1fc6ZUG6nAUEDMmT5bze2CHuv9mktbf5rO3gs7Z7qK_VQ1GJByF9wP3pEYv2oiALRVtNQaUYJgyLiupSmogg3GEMyfuoA4GXuDWCKLn0dsvoJX4vBsjO-3_m/s1600/2.png)

Story page: [Simple shower controller](https://irwin34.blogspot.com/p/simple-shower-controller.html)

## Panel light dimmer

When I built my breaker panel I added LEDs to show which circuits are on. After two night passages I found the problem: fine in the day, way too bright at night.

So I made a small board that dims them about 1:2000 by switching their common negative side with PWM. A tiny microcontroller does it, so I can change the ratio without changing parts. Four wires: the LEDs' common negative, 12 V (it uses about 0.01 mA), the nav lights wire (the signal for night mode), and ground. All the parts, PCB included, cost about $5.

![Main electric panel with indicator LEDs](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinzaTDDkSQleF2fN9sX3bn69EHannHGbfsYxEPxL2Df2vL4bB8K59bCmt1-Wdj6d_IBCgqWLny2xQlcX9W_31H87gEMgh-9LWdTdNYUdDBkRYM55LjMg-zNqHtq9DOF913JJOjIyjE5P8_I5lfRbLyJDLMh0V9X5YIn7XEUuMN3gDjE4JB4aHG8Vjqmeo2/s1600/IMG_0893.HEIC)
![Panel light dimmer schematic](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizu6zW7WiVyV0KU-DatDWrOA07a34J4u15TWWDS9_dNRQ-Kd_rPZOjt_a846FhYpxp4UIAy4bM9eFTxDztbecr0MWupPuQsTSsCwPRIvZP6YETHUdojqApv9ZYellyG2_UYHz_RFEoPutEwgwrr7HKCSC6YyARd7zRuSJcuXw9EjF88KIe55_A99E_4psJ/s1600/970002%20sch.png)
![Panel light dimmer board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![Panel light dimmer PCB layout](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8Ymr8mrerkf3aZhHPKdtM9KbntYVz4QsqNRMRoMx62KgDpHGZkJVzwSUS2HVrVshIHrZC0tAK3W9CRONTlCTRX0mK0IWs8FCKR4WmLmnBzB0l_XYvhRJnE6ipTkrithjS_YPZf3SlkT52A4R6ceDXIwo7P-lk8PFpPJgEaO_IIWcq3ThO2NB390bKnm8Y/s1600/970002-1.png)
![Main electric panel with dimmed indicator LEDs](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinzaTDDkSQleF2fN9sX3bn69EHannHGbfsYxEPxL2Df2vL4bB8K59bCmt1-Wdj6d_IBCgqWLny2xQlcX9W_31H87gEMgh-9LWdTdNYUdDBkRYM55LjMg-zNqHtq9DOF913JJOjIyjE5P8_I5lfRbLyJDLMh0V9X5YIn7XEUuMN3gDjE4JB4aHG8Vjqmeo2/s1600/IMG_0893.HEIC)
![Panel light dimmer schematic](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizu6zW7WiVyV0KU-DatDWrOA07a34J4u15TWWDS9_dNRQ-Kd_rPZOjt_a846FhYpxp4UIAy4bM9eFTxDztbecr0MWupPuQsTSsCwPRIvZP6YETHUdojqApv9ZYellyG2_UYHz_RFEoPutEwgwrr7HKCSC6YyARd7zRuSJcuXw9EjF88KIe55_A99E_4psJ/s1600/970002%20sch.png)
![Panel light dimmer board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOfC496h75ME4yxFZgDbHGNrHDXgeQTUIvOBahzhsQOyB8RY3xkUOF8LdJCLBh9Qak30WOYpz-uRfopOMf-q1VMkkyAZxfSmjY0IfY-ZzYmG0x5pROveKsVAbdafjnvhZvAZ1Fq1HxbDaN43VrkDhqAlgllMWS8yZ9fvmdDycesIfSlTHvbfQ4lfQDqoqG/s1600/970002-2.png)
![Panel light dimmer PCB layout](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8Ymr8mrerkf3aZhHPKdtM9KbntYVz4QsqNRMRoMx62KgDpHGZkJVzwSUS2HVrVshIHrZC0tAK3W9CRONTlCTRX0mK0IWs8FCKR4WmLmnBzB0l_XYvhRJnE6ipTkrithjS_YPZf3SlkT52A4R6ceDXIwo7P-lk8PFpPJgEaO_IIWcq3ThO2NB390bKnm8Y/s1600/970002-1.png)

Story page: [Electric panel lights brightness control](https://irwin34.blogspot.com/p/electric-panel-lights-brightness-control.html)
Diary: [14 Mar 2026](https://irwin34.blogspot.com/2026/03/new-small-electronics-for-my-boat-home.html)

## Masthead tricolor and anchor light

This board fixes two problems. First, when you upgrade a plain anchor light to a combined tricolor/anchor light, you normally need three wires up the mast. This lets you use the two you already have, so no new cable up the mast. Second, it switches between the deck-level side lights and the tricolor when you're motoring, without another switch on the panel.

Important: never show the tricolor at the top together with the steaming light. It's against the rules, and from the bow other boats would see just red or green above white.

The board has three inputs (masthead switch +12 V, nav lights switch +12 V, ground) and three outputs (masthead wire A, masthead wire B, and deck-level nav lights).

![Table of nav light switch positions and light configurations](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMLPpku84w7njPdvZtJGx1-Sjxmc50IB4Kh0Bz6FdcaNdXRxD7vXhCwuVPFKj6J1hSrl60Gw7mCj6b3M14Xq7kCxsk6yx4kgkv2Mn3HO0l6o5KtoEvGa5Iv8czaSZfTRmY6WAWw5-cwZYPJjUFTsErd7F_A_RodW6MOC6pggTgRTq_ikc1-51REjbi_3oy/s1600/Lights.png)
![Masthead light controller schematic](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXQ1HWYkpwx1IDxfp3GDOkKzXB4vMXEjrEv4Wczn6sizhZPY6wg408uIte2zwo54B_qaAZ-ha6JIkW9rbCqGFQ5nXJ0ubSZopVuqltPPrLK6KKgz6LEtCQ-inK_3C4q0LMJYBjIr7_uz2TcxO6AFGUrOPwgXQ9q-1fbHBB492Jo_XXiNtiK565-mjPmwkG/s1600/970001sch.png)
![Masthead light controller PCB layout](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj2bDOwub2y-XqAtEfBnRjyvCkPNIma0u5ebq0TC0UsvymiSWhRSXKhlNzpa4cB6EUij17GstMuIcvbADwDbngGOjmPTF5MoAye2LmDytLOpJdQFLmKAicEI5gEuJMVJToMUKeivAp0q4w12JkkYj2tQUr20xsyMw27IPgWXDAH4kgSXl_nO3GGmGK9F-g/s1600/970001-1.png)
![Masthead light controller board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiu0H6-_4UlvdV5OdbQ3BXshEZCsrrXCHRRogQgFn67jhqpfYMVESOjqYkOeoeGOVSgGAqgxzvfjpg_PIrrqCt8Ix0-JuO_buRljJHw_gAue55pXO5Aw8JCa6SkOesFklgYyXvkXlxAldPWhXUcEg0S4iLk2_H1KBx6N5BMbVLr01DlJ4p_VlTYoInz-XI/s1600/970001-2.png)
![Wiring diagram of the masthead light controller](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6bnkyQZrGaK8Do3xCjlJHLU7wZqY3H5z4HptgM0OwKl2clwlIIAg57J2GVuj9HSXpzRxeVPyysksx98ez13QCcFLTak5Bb2bSYLuE192lGnAnvhHgo4Hw_bgdwBqEF5JijIEW7lEGRuu1fk-zu3oduqG0JNc38EtyktnoIZz9TKsRchBvCMeRp84YLx9V/s1600/970001-3.png)
![Table of nav light switch positions and light configurations](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMLPpku84w7njPdvZtJGx1-Sjxmc50IB4Kh0Bz6FdcaNdXRxD7vXhCwuVPFKj6J1hSrl60Gw7mCj6b3M14Xq7kCxsk6yx4kgkv2Mn3HO0l6o5KtoEvGa5Iv8czaSZfTRmY6WAWw5-cwZYPJjUFTsErd7F_A_RodW6MOC6pggTgRTq_ikc1-51REjbi_3oy/s1600/Lights.png)
![Masthead light controller schematic](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXQ1HWYkpwx1IDxfp3GDOkKzXB4vMXEjrEv4Wczn6sizhZPY6wg408uIte2zwo54B_qaAZ-ha6JIkW9rbCqGFQ5nXJ0ubSZopVuqltPPrLK6KKgz6LEtCQ-inK_3C4q0LMJYBjIr7_uz2TcxO6AFGUrOPwgXQ9q-1fbHBB492Jo_XXiNtiK565-mjPmwkG/s1600/970001sch.png)
![Masthead light controller PCB layout](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj2bDOwub2y-XqAtEfBnRjyvCkPNIma0u5ebq0TC0UsvymiSWhRSXKhlNzpa4cB6EUij17GstMuIcvbADwDbngGOjmPTF5MoAye2LmDytLOpJdQFLmKAicEI5gEuJMVJToMUKeivAp0q4w12JkkYj2tQUr20xsyMw27IPgWXDAH4kgSXl_nO3GGmGK9F-g/s1600/970001-1.png)
![Masthead light controller board, 3D render](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiu0H6-_4UlvdV5OdbQ3BXshEZCsrrXCHRRogQgFn67jhqpfYMVESOjqYkOeoeGOVSgGAqgxzvfjpg_PIrrqCt8Ix0-JuO_buRljJHw_gAue55pXO5Aw8JCa6SkOesFklgYyXvkXlxAldPWhXUcEg0S4iLk2_H1KBx6N5BMbVLr01DlJ4p_VlTYoInz-XI/s1600/970001-2.png)
![Wiring diagram of the masthead light controller](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6bnkyQZrGaK8Do3xCjlJHLU7wZqY3H5z4HptgM0OwKl2clwlIIAg57J2GVuj9HSXpzRxeVPyysksx98ez13QCcFLTak5Bb2bSYLuE192lGnAnvhHgo4Hw_bgdwBqEF5JijIEW7lEGRuu1fk-zu3oduqG0JNc38EtyktnoIZz9TKsRchBvCMeRp84YLx9V/s1600/970001-3.png)

Story page: [Mast top Tri-color/Anchor light control](https://irwin34.blogspot.com/p/mast-top-tri-coloranchor-light-control.html)
Diary: [14 Mar 2026](https://irwin34.blogspot.com/2026/03/new-small-electronics-for-my-boat-home.html)

## Water tank fill controller

When you top up the tank from a hose you have to watch the level. On my boat, if it overfills, water goes into the vent and leaks into the bilge. And the vent line is too small to keep the tank from pressurizing, so I have to keep the fill cap open and watch. It takes attention and timing to shut the water off at the right moment.

So the shore water goes through a valve with a 12 V solenoid. Power the controller and it checks the level. If the tank isn't full, it opens the valve and waits for the sensor to say full, an inductive 5–12 V level sensor with NPN output. And it cuts the water after 15 minutes no matter what.

The sounds: one short beep at power-up. Filling: a short beep every 10 seconds. Full: a long beep every second. Timeout: a short beep every second. So it shuts the water off and keeps reminding you to disconnect the hose.

![Water tank fill controller in a box with the level sensor](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVgwCyvanwmR5a8HBvjhbPOLkjJ2hFy2c0hfKuZdvMBq-cWzV5H0dPv33EXxUW09umL_BQSVeWr0CjL-aMWSiHbzx11R8RQfjrW33f_8vhmdo4uz7WkQTv1NdJF22-ljlnGfFIZs0MvdZBEqJXVv8C9XN2O4P4nnHOk_cIGwXouZMm8mYHh648rsGJymT5/s1600/IMG_1227.HEIC)
![Water tank fill controller diagram](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXJPzSgla98ksHYznDPQVkwnDHzq0mQmsk2wlTKD1uYvaFAg6vSIlRlJ7Tu_N0thS3oWg9l2j9HLLl8HkyIjuJjfJWYSEB0lSyM-cz3Z9af3wSaeLtGmZk1AYmbiEsEfk_clCkuk0-G_9dZiTN7iiJBE7__tQng9grWRRG1mnZe-l3adhUhCW_OtTGC7mD/s1600/wc.png)
![Non-contact water level sensor](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFVsXLsztATJsBDES-a6KCX6q-NmfveUDVBbJ1LyJhhwjg8tVoAG00Rj9RwhVyOxI4l4o3DkkcVidpSj4w5PnCDCjKuJ0-tLGamUkl-Diatue9AGWtmdF2aqFoHFUtjErFk8LB5F1cBhvD61Utlcvj7LNJM5GHngzgvVb_Rkm97rB1cOci0V_DHmAxcQzU/s1600/k.png)

Story page: [Water tank fill controller](https://irwin34.blogspot.com/p/water-tank-fill-controller.html)

## PSU/battery power switch

I installed a separate 14.5 V, 40 A power supply on shore power, to take the boat's loads off the battery charger. Chargers get confused by a constant load during charging and can't tell when to switch to float.

At first I mixed the two sources with a dual ideal diode board. Very simple: whichever source has the higher voltage feeds the boat. All good until the battery is full. Then sometimes (I caught it happening) the power supply, the charger, the battery and the diode chip start a switching storm. Short drops on the 12 V bus, and the computer reboots several times in 10 minutes.

So the switch works like a UPS. It feeds the bus from the power supply if its output is between 12.5 and 16 V. If shore power is lost or the voltage is wrong, it switches the bus to the battery. When shore power comes back, it waits 10 seconds to be sure it's stable, then switches back. It also disconnects everything from the battery if the battery drops below 9 V.

It's microcontroller-based, so all the times and voltages are set in firmware. The transistors are rated 260 A continuous and 1.4 kA for a 10 µs pulse, two in parallel, 40 V max. I don't expect more than 80 A from the battery (the breaker is 80 A) and 40 A from the power supply (it limits itself). With 0.75 mΩ on-resistance, 80 A makes less than 5 W of heat, so a 70x70 mm heatsink is fine. It's installed, and after weekend sailing and a couple of nights aboard it works well.

![PSU/battery power switch board](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7xAQVy6DljfAUgnq1GcGpqNVPrBvVtEiC_WPas-U5Izpie-PDXelRZhlFlop1UJ__hf3d6AfA2Su09o61xwcuHIeI8JAbSkKq7lESXMWd2_e2IkZtALkpgnJY3sOakMVClZdjjxpgRMcDho7MGikdRUw4-whZWdNYm88jpP8cBt-aa138jMKRaJUuIjEL/s1600/IMG_2247.HEIC)
![PSU/battery power switch with heat sink](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjQnmoZKCEpC__wT2fDPDJT4d7X5n5SsrlxPkoxK8xgvjsJCXoU-IOQ55PXQjL1uLEgw-_m42MC-XxwYIeb1610fpaFtJDwnvQnCxz4q65FftoHv4rjZXi81_FR7hml9XLlNFNqVUGgn6F5utLgZk_OZGqPNbivkrTdyZF1nYX4x7wnKKuo-Mr6UrFJ0sU/s1600/IMG_2248.HEIC)
![PSU/battery power switch schematic](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQG5bGmGHIHbsJXaVyAOorUau9MRK_62uI2pZkWeyJw_tdRMUzkCmg0tG3aUB121825uWxUAAz8RSF7U7Z7ReVI7KbObPu9YDe7_0vpndYt3ClZrJ8yVKKbCapzusxQmmoZhZrt8eX8TKDN-_45CF593Giq5hyphenhyphenaqtyV8N4rtAKGGCeRlUkAlmiZ9ORtt-w/s1600/Untitled.jpg)
![Power switch installed next to the battery cables](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRW9bCoJdrEOEn7BHmSbHA5QnWYGRGXb57JZq-WNepXTwQqw2IJ2g7ZfSZjOITs81NSWGngKLbLIVZ-ZsJgRauoVc-I0wOdgDR6Y3ukUf44KeG3txp5RFEtLRfU7tHi7UMYJsfoYiMoBhRxAOHR0135kh2X3APBdE8jonBhCWVdwJC6kEbNhORoDDyfxVf/s1600/IMG_2341.HEIC)

Story page: [Power switch PSU/Battery](https://irwin34.blogspot.com/p/power-switch-psubattery.html)

The design rules I set: shore power has priority, so if the power supply is above about 12 V, the bus runs from it whatever the battery says. Complete isolation: each source has a dual-MOSFET switch arranged so that when it's off, no current flows either way, so the battery and the supply never see each other. A minimum battery time: once it switches to battery because the supply dropped, it stays there at least 10 seconds, so a shaky shore supply can't make it flip back and forth. And break-before-make: about 100 µs of dead time between disconnecting one source and connecting the other.

What started as some strange blinking lights became a whole engineering project: idea, research, schematic, PCB, parts, assembly, programming, function tests, stress tests, a 3D-printed enclosure, installation and testing aboard. About four weeks. Now, instead of trusting two power sources and an ideal-diode chip to negotiate with each other, I have power management whose behavior I actually understand. The board with conformal coating, and the module installed in the engine compartment.

![PSU/battery power switch board, top view](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEnlE_32drK1hdmFGTz4aBhUk5UmoZy8sfjHgZ-iZAtkMjAf19uUkC9d75uaEwwUYwy07kveDzeaKKU3AZfc15jjK1ht0fgWkJ9LHTVPYyyFEQ2AhPyC9GE6OZsudYgpxWMxcmDBB5oiyNxElkzKiRsDfXnFU2jGBvORWivmdva8LfG50z6Ck_qmvYxOLH/s1600/IMG_2247.HEIC)
![Power switch installed in the engine compartment](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgweNdbzCRoZBEq2-_umMFOJzdsszayKfr0iMLZ0OAze0SR4zJaULoYaJPQC1w44IAZ5EqVS7UN-y_aswOC7z1-YLvSw3dyH1isR1l6k7e-mfNWRKLsfnBA9YNQAyPY_nMZvkLhyET0Pc4xh2a6Rm4kIOUJDsXe_TgJsBcBDjJmw3CLs_Psv3_GtORKk_Q6/s1600/IMG_2341.HEIC)

Diary: [24 Aug 2026](https://irwin34.blogspot.com/2026/08/days-276-277-sailing-kemahtx-to.html)

## Battery monitor

October 2026: a monitor for my WattCycle batteries. It talks to them over Bluetooth, shows the current state, and sends the data to the Signal K server in OpenPlotter.

![WattCycle battery monitor showing two batteries](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhml60cJ2eyTEz4fk6Vo1EDjs62pEWRDHkr09-IgniENoSdHyR7k9-OYhIq1CUs9Wn1FOKVOaLEurlXtQBmyrWpKo_BfUF5dvpxR4tm3uZqK4qJaB4sApl1938sluqZN1lMt81DhwyNXbuWCNrkHemjTsqDqiPyZNtR1-dU2iCfZgxjWrMLtYyljd2hkdPE/s1600/09E31248-A495-48A6-85D7-CF81C8BF50F8.jpg)
![Battery monitor showing details of one battery](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGG2UhzxmaO5JBVW_bRLnzAqq2ZtpCX1HdFAoOOtKT-UNazweH0G8msNDuS98R5eTgbjbs7ZpmrZVlwrRNAonlhjDnZFlA6yT1RSY0oV-kG-QZzfXGdIKqJjRjdYyeYvnY2oWEJG-rfGXjpGV2jfyACkcXKhS1ux6YjNGJR3pG_qEzhUFKMqjPHHdG-uqB/s1600/5B20C409-8C04-48EB-8FA1-199F821AF230.jpg)

Diary: [5 Oct 2026](https://irwin34.blogspot.com/2026/10/days280-refrigerator-thermostat-bumpy.html)
