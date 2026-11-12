I'm an electrical engineer, and at some point I stopped buying little boxes for the boat and started designing my own. Every one of these began with a real problem on Vira. Here they are, with all the details, in case somebody wants to build the same.

## The family
For each project there's a full page on the blog with design files. If you want to make something similar for your boat, just leave a comment. KhatkaPi baseboard, dry bilge timer, shower controller, LPG solenoid controller, water tank fill controller, panel light dimmer, masthead tricolor/anchor light control, and the PSU/battery power switch.
@s101

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
@s36 s37 s38 s39 s40 s41

## Dry bilge
In January 2023 I tested the idea of a "dry bilge": a box with a sponge and a membrane pump. Works perfect. I also tested the manual pump. I could pump it out in a minute or two. Hard to prime, but doable.
@s322 s323
In April I installed a small self-priming pump for it on a plywood block glued to the engine room wall, with the output into the cockpit drain. I drilled a corner of the drain fitting and cut a tight 1/4 NPT thread for a barb. It dries a quarter-flooded bilge in under 3 minutes.
@s356
In March 2025 I 3D printed a new intake box from TPU. That one won't crack again.
@s632:1
Then I designed a controller for it. When you switch the breaker on, it runs the pump for 3 minutes, about how long it takes to get the bilge dry after the main centrifugal pump, then waits 24 hours and repeats. It also has overheat and overcurrent protection. The light on the board is off with no power, on while pumping, and blinks slowly while waiting. In June 2025 I finally installed it, the small gray box on the wall.
@s671 s73 s74 s75

## LPG solenoid controller
This one adds convenience and safety to the propane. It switches the solenoid without sparks, protects the circuit if the cable shorts or breaks, and limits the holding current so the coil doesn't get hot and uses much less power. The valve closes itself after 60 minutes. One button with an LED, and it can work with a gas sensor to cut the gas if there's a leak.
The light: off means no power. A dim short blink every 2 seconds means the circuit is OK and the valve is closed. One second on, one off: open, more than 10 minutes left. Fast blinking: less than 10 minutes left. Three short blinks then 5 seconds on: the 24-hour timer (not recommended). And quick blinking, a second on and a second off, means a wiring problem.
Button: a short press toggles the valve, or restarts the timer when it's about to run out. Press and hold for a second, and it's off.
@s67 s68 s69 s70 s71 s72

## Shower controller
This is the one from the head story: it opens and closes the shower, and first pumps the cold water in the hot pipe back to the tank, so you get comfortable water almost right away and don't waste any. One button press gives one minute of water, and it can take a foot switch.
The light: dim red is standby (HOLD). Amber is priming the hot water. Green means ready. Green blinking slowly means the shower is running, and fast flashing means 10 seconds left; press again for another minute. A short press starts or stops priming, and opens or closes the water. Press and hold for a second to stop and go back to HOLD.
@s76 s77 s78 s79 s80 s81 s82 s83 s84

## Panel light dimmer
When I built my breaker panel I added LEDs to show which circuits are on. After two night passages I found the problem: fine in the day, way too bright at night.
So I made a small board that dims them about 1:2000 by switching their common negative side with PWM. A tiny microcontroller does it, so I can change the ratio without changing parts. Four wires: the LEDs' common negative, 12 V (it uses about 0.01 mA), the nav lights wire (the signal for night mode), and ground. All the parts, PCB included, cost about $5.
@s103 s851 s852

## Masthead tricolor and anchor light
This board fixes two problems. First, when you upgrade a plain anchor light to a combined tricolor/anchor light, you normally need three wires up the mast. This lets you use the two you already have, so no new cable up the mast. Second, it switches between the deck-level side lights and the tricolor when you're motoring, without another switch on the panel.
Important: never show the tricolor at the top together with the steaming light. It's against the rules, and from the bow other boats would see just red or green above white.
The board has three inputs (masthead switch +12 V, nav lights switch +12 V, ground) and three outputs (masthead wire A, masthead wire B, and deck-level nav lights).
@s102 s853

## Water tank fill controller
When you top up the tank from a hose you have to watch the level. On my boat, if it overfills, water goes into the vent and leaks into the bilge. And the vent line is too small to keep the tank from pressurizing, so I have to keep the fill cap open and watch. It takes attention and timing to shut the water off at the right moment.
So the shore water goes through a valve with a 12 V solenoid. Power the controller and it checks the level. If the tank isn't full, it opens the valve and waits for the sensor to say full, an inductive 5–12 V level sensor with NPN output. And it cuts the water after 15 minutes no matter what.
The sounds: one short beep at power-up. Filling: a short beep every 10 seconds. Full: a long beep every second. Timeout: a short beep every second. So it shuts the water off and keeps reminding you to disconnect the hose.
@s104 s105 s106 s107

## PSU/battery power switch
I installed a separate 14.5 V, 40 A power supply on shore power, to take the boat's loads off the battery charger. Chargers get confused by a constant load during charging and can't tell when to switch to float.
At first I mixed the two sources with a dual ideal diode board. Very simple: whichever source has the higher voltage feeds the boat. All good until the battery is full. Then sometimes (I caught it happening) the power supply, the charger, the battery and the diode chip start a switching storm. Short drops on the 12 V bus, and the computer reboots several times in 10 minutes.
So the switch works like a UPS. It feeds the bus from the power supply if its output is between 12.5 and 16 V. If shore power is lost or the voltage is wrong, it switches the bus to the battery. When shore power comes back, it waits 10 seconds to be sure it's stable, then switches back. It also disconnects everything from the battery if the battery drops below 9 V.
It's microcontroller-based, so all the times and voltages are set in firmware. The transistors are rated 260 A continuous and 1.4 kA for a 10 µs pulse, two in parallel, 40 V max. I don't expect more than 80 A from the battery (the breaker is 80 A) and 40 A from the power supply (it limits itself). With 0.75 mΩ on-resistance, 80 A makes less than 5 W of heat, so a 70x70 mm heatsink is fine. It's installed, and after weekend sailing and a couple of nights aboard it works well.
@s109
The design rules I set: shore power has priority, so if the power supply is above about 12 V, the bus runs from it whatever the battery says. Complete isolation: each source has a dual-MOSFET switch arranged so that when it's off, no current flows either way, so the battery and the supply never see each other. A minimum battery time: once it switches to battery because the supply dropped, it stays there at least 10 seconds, so a shaky shore supply can't make it flip back and forth. And break-before-make: about 100 µs of dead time between disconnecting one source and connecting the other.
What started as some strange blinking lights became a whole engineering project: idea, research, schematic, PCB, parts, assembly, programming, function tests, stress tests, a 3D-printed enclosure, installation and testing aboard. About four weeks. Now, instead of trusting two power sources and an ideal-diode chip to negotiate with each other, I have power management whose behavior I actually understand. The board with conformal coating, and the module installed in the engine compartment.
@s917 s918

## Battery monitor
October 2026: a monitor for my WattCycle batteries. It talks to them over Bluetooth, shows the current state, and sends the data to the Signal K server in OpenPlotter.
@s942
