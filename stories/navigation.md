I didn't want to buy a plotter and a box of instruments. I wanted to build my own: a Raspberry Pi with OpenPlotter, a home-made autopilot from an old Autohelm, a wind instrument on a mount I cast on the mast, and in the end a "NavPod" with real buttons. It took four years, and it's still growing.

## The old compass
February 2022: I replaced the compass O-rings and membrane and refilled it with odorless mineral spirits. Looks like new.
@s138
In March the repaired compass and cup holder went back in place, thanks to my father. One more nice piece back on the boat.
@s153
On Day 5 I pulled the water speed sensor out of its housing. The boat didn't sink, the water coming in was nothing to talk about. Some growth on the paddle wheel; cleaned, now it'll be OK.
@s119

## A wind instrument mount, cast on the mast
June 2022 I made a fiberglass template of the mast side.
@s201
Then the mount: a "base" of three layers of 1708 cast right on the mast, a piece of 12.7 mm pipe shaped onto it with hot glue, a foam block to cast ribs, and 3–6 more layers of glass over everything. VERY solid. It still needs gelcoat, and a wire/drain hole so water can't sit in the cavity.
@s215
The Davis wind instrument mount for the masthead, screwed to the starboard side of the mast. Next: paint it, check the position, and make a Wi-Fi transmitter for the sensor.
@s221
In October I made a different mount for the masthead, cut from a solid 2x2x5-inch aluminum block. A few too many shavings. Main cut done, then the holes. The final product.
@s274:1-3

## Nav lights
In August 2022 I made back plates for the nav lights. Good try, but they came out about an inch too short. Redesign and cut again.
@s247:1-2
A week later I climbed the mast again. A piece of cake now, with steps. All the bulbs were dead, so I put in new LED lamps. As long as I was up there, the spreader lights became LED too, 2 x 18 W. The lights look good quality: powder-coated aluminum and stainless fasteners. But for some reason the brackets look like mild steel, so they'll need aluminum or stainless ones later. And new teak back plates for the bow nav lights.
@s256
Good night, marina. The one with the spreader lights on is my Vira.
@s311:4-5

## A screen in the cockpit
In May 2023 I took out a leaking port to make room for a 15-inch, 600–800 nit touchscreen. It works next to the main nav station; a second 7-inch, 1,200 nit screen will go on a nav pod, maybe with another Raspberry Pi. The port wasn't watertight at all: when I took out the screws, it just fell out of the hole. The cabin wall isn't flat, so to mount a screen I made a flat surface from the cabin side with thickened epoxy, pressed with a 3/4-inch MDF plate wrapped in freezer paper. A couple of wrinkles, but they shouldn't matter. The hole is closed with PVC tape for now. The inner rectangle is the display frame; the opening will grow about 2.5 inches. I don't expect structural problems.
@s367
June: dry fit, at 50% brightness. Clearly readable. The frame got a coat of gelcoat and a film over it against the coming rain.
@s380
Then I mounted the display with VHB tape to hold it and leave a 2 mm gap between the fiberglass and the glass for a layer of polyurethane rubber. The real bond and seal is 3M 08609 Window-Weld, the urethane used for car windshields. Hope it holds better than Sikaflex on the fixed ports. The next day I made a sun cover with phone pockets and snaps. The camera messed up the photo a little; it's readable on a sunny day. And a bonus: everything was sized for an iPhone 13, but one pocket UNEXPECTEDLY turned out to be the exact size for a flask of BLACK RUM.
@s385

## Planning the autopilot
September 2022, I measured the steering for an autopilot.
@s259
In February 2023 I did a lot of calculations. Final plan: close to a wheel drive, but "on steroids". The Irwin 34 steering: a wheel about 20 inches across, 2.5 turns lock to lock, so 900°. The rudder quadrant turns 80°. So the ratio is 900:80, about 11:1. Say 20 lb is the most you'd reasonably put on the wheel. On a 12-inch quadrant arm at 11:1 that's 2,640 lb-in, or 300 N·m.
I wanted a 300 mm wheel on the rudder stock driven by a timing belt. The force at 300 mm is 300 N·m / 0.15 m = 2,000 N, the starting point for picking a belt. I chose an 18 mm HTD belt with fiberglass cords: 130 N/mm x 18 mm = 2,340 N, 17% spare. The pulleys: a 300 mm wheel and a 37 mm, 24-tooth sprocket, for 8.1:1.
@s336:2-4 s337
The motor I had: a 200 W SIM motor. Big overkill, but I have two, and at 20% power it'll last forever. Maybe not efficient, we'll see. 4,300 RPM, 4 lb-in, 0.45 N·m. With a 100:1 gearbox and the 8.1:1 belt, 0.45 x 810 = 364 N·m, and 4,300 / 810 = 5 RPM at full power, 11 seconds per turn or 2.5 seconds lock to lock. I'll need to limit the speed.
@s338

## The wind instrument goes up
February 2024: the wind instrument is ready for the masthead. The small white box is a Wi-Fi camera looking ahead from the top, 120° view. It uses about 20 mA at 12 V, so it shares power with the instrument lines. The mount was made a year before. To install it I had to drill and tap the top joining plate and screw the mount on; its shape sits tight on the vertical bars with one vertical screw.
@s470:1-5
It didn't go easy. The first day my friend did his best; he's fitter for climbing the mast. But it was the first thread he ever tapped in his life, and we ended up with a broken tap at the top of the mast. The next day I went up and he belayed me. I broke the tap off flush, drilled a new hole 10 mm forward, tapped it, and screwed everything on as planned.
BUT then we spent about two hours fishing the wire down the mast. The cable isn't heavy enough, and it keeps touching something inside and coiling up. The hole at the top is maybe 6–7 mm, just bigger than the cable. The trick that worked: a long 10-inch drill bit as a weight. The grooves of the bit are perfect for hiding the thin wire, so the "weight" and the wire go through the hole together.
@s470:6-7

## OpenPlotter comes alive
January 2024, picture of the day: OpenPlotter running on the installed hardware. Inside the electronics compartment.
That weekend: power for the Raspberry box and the box installed. Tested the IMU, unsuccessfully; looks like a bad connection. Wires from the pedestal to the nav table. Resistor boards to keep the LEDs on the main switch box dimmer. A remote for the deck lights. A "secondary" GPS, in a spot where it works through the single-layer deck. I checked the dual-screen setup: I'll need an HDMI splitter to mirror the cockpit and nav table easily. Right now the cockpit display and the Pi power each other over HDMI; the splitter will fix that. I ran the engine to check RPM: idle 850, near-full throttle 2,800. It runs stable but with pretty strong white smoke. Need to check how it smells, oil or water. And I measured the fuel tank space. An off-the-shelf tank won't fit.
@s463
A "draft" electronics board for OpenPlotter. The wiring needs organizing, but first make it work, then make it pretty.
@s465:1

## A used Autohelm becomes a smart drive
In March 2024 I got a used Autohelm 6000 Type 2 (long) linear drive. It fits well in the lazarette, pointing at the transom. But I didn't want it there: it's easily exposed to salt water, and it takes locker space and needs a guard. So, the engine compartment. After an hour playing with that 20 lb toy, I found a spot: the port wall of the engine compartment, right above the cockpit drain hoses, clear of the steering, hoses, wires and cables. Next: a bracket, and a place for the motor controller.
@s506 s507
Then the mount was built. A dry-fit test under power: the drive moves the rudder end to end in 4 seconds, and the motor doesn't seem to feel the load at all. The top corner needs a spacer, because the wall isn't flat: the bottom is on a cored area, the top is just 1/8-inch liner, and not vertical.
To make it a smart drive I used Sean's mid-power motor controller instead of engineering my own. Two reasons: to support great work from an amazing person, and to save time for other projects. The conformal coating on the board was really poor, so I recoated it. Then I found the board fits perfectly inside the drive's own housing, which makes a much cleaner install. Only five holes in the aluminum cover: four 4 mm for the board screws and one 15 mm for a round connector to the end switches and rudder sensor. The motor temperature sensor connects inside. Six wires between the drive and the board: 2 motor, 2 clutch, 2 temperature. It looks like they left extra space beside the motor on purpose. Box closed, drive tested. Now I have a "smart linear drive" for PyPilot, with only power, serial and sensors to connect.
@s508:1-5
And I designed and printed flashlight holders, so I stop hunting for my "landing light".
@s509
April: the drive wired to the Raspberry Pi. It turns the rudder easily and fast. No end switches or rudder sensor yet, so no wild play. In the video the motor power is at 10% and the wheel turns by itself from the computer. Can't wait for the safety switches and a full-speed test.
@s514
May: the IMU on a gimbaled mount, the small black box.
@s528

## First test on the water
June 2024, the first PyPilot test on the water. It worked relatively well on all courses with default settings. I tested compass and wind modes, under sail and motor. Auto-tack, in wind mode only: the port tack worked reasonably, but the drive turned very slowly, and on the starboard tack the autopilot turned the boat all the way around. After a couple of tries I went back to tacking by hand. Need to figure out what I'm doing wrong.
The autopilot in charge, Eugene on watch, and I'm having fun. Wing on wing downwind, then beating back to the marina.
@s541

## End switches from a home alarm
In July 2024, sailing with the autopilot, it twice drove past the rudder's travel and the steering arm slipped on the rudder shaft. I left the key out of the shaft on purpose, so nothing breaks if the autopilot goes crazy without end switches. I'll cut a keyway when I'm 100% sure of it. For now slipping is better than fighting.
For end switches I first planned industrial heavy-duty ones, and even bought them. But I ended up with simple magnetic switches from home security systems. Why: they're fully sealed, so weather can't get to them. No moving parts touching anything, so nothing gets stuck, and reliable by design. And dirt cheap, easy to find anywhere on the planet.
The downsides and what I did. They're not made to mount on metal, so I made mounting plates for the steering cross member. They're fragile, so they sit where nothing can hit them. And magnets can bother a compass, so I tested: no deviation at all on the pedestal compass.
A few things I still don't love. Each sensor bracket is held by one screw; I put super glue on the thread and under the bracket so it can't loosen, though maybe Loctite is enough. The wires have no outer jacket, but they're zip-tied to the cross member, and they're just sensor wires, current-limited by the motor controller, so no fire risk. And the bolt from the steering arm to the linear drive is nut-up: if the nut loosens the bolt could drop out. I should drill it for a pin or at least Loctite it.
@s546 s547

## Cleaning up the rat's nest
By April 2025 the electronics had been in "temporary mode" for a year: flying wires, not organized, just working for day sails on the lake. More for fun than need. Everything sat on a plywood board with Velcro. Between the fuse panel and the switch panel it was a total rat's nest; to remove the switch panel I'd have to unscrew 15 wires. Nothing was protected except the boards' conformal coating. Not a big deal in a fresh lake, but I was going to salt water at the end of the year. What you can't see in the picture: three USB-serial adapters and the Arduino "weather sensors" hanging on wires below the frame.
@s642 s645
That day: the OpenPlotter electronics box installed, a connector between the switch panel and everything else, all the wires between the switch panel and the fuse box organized, a terminal block for power to the peripherals, wiring to the tank gauges (two water and the fuel), coolant temperature sensors and a shaft packing temperature sensor connected to the engine monitor, and the engine monitor grounded and connected to the alternator.
@s646 s647
The box is IP68, with IP68 connectors, and holds the most sensitive parts: my baseboard, the Raspberry Pi and the HDMI splitter. The baseboard is like a big HAT, except the Pi mounts on it instead of the other way around. It protects the Pi's interfaces from the marine environment and from mild static discharge. A direct lightning hit you can't really protect against; it's cheaper to keep a spare set of electronics in a Faraday box.
Inside the box:
- Raspberry Pi 5, 8 GB, mechanically secured.
- Two 4-port USB 2.0 hubs, 8 well-protected ports with 2 A, from two Pi ports.
- A direct RJ45 port for the Maiana AIS.
- IMU, and the PyPilot weather sensor with a barometric sensor and a direct connection for the Davis anemometer.
- Two galvanically isolated NMEA 0183 ports.
- A port for the PyPilot motor controller.
- Pi power control.
- A remote keyboard interface for controlling PyPilot (software not ready yet).
- Two USB power ports.
- The HDMI splitter copying the nav desk screen to the cockpit.
And the connector pinouts.
@s648
The secondary switch panel at the nav desk includes a small 2.5-inch thermal printer, to quickly print the position, course or anything else. The wires on it are organized now, with a 24-pin connector between the panel and the rest of the system. The back of the installed panel, and the pinout.
@s644 s649

## The NavPod idea
At my desk in April 2025 I started on a "navpod": an OpenPlotter dashboard on the pedestal guard, shaped like a navpod, with buttons instead of touch. For me buttons are much easier in the cockpit. A script will switch apps to the front and back, and arrow buttons can work as a mouse if I need something "non-standard", but mostly it'll be a dashboard. The modes:
- Map (an OpenCPN preset).
- VNC, a copy of the main nav screen.
- Sailing dashboard: big wind instrument, SOG, STW, day log, depth, position, COG.
- Engine dashboard: small wind instrument, tachometer, coolant out temperature, oil pressure, the other temperatures (coolant in, exhaust, gearbox, shaft packing, raw water after the exchanger), and SOG, STW, log, depth, position, COG.
- Autopilot controls and anchor/windlass control with a chain counter, as pop-up overlays.
- The masthead camera.
@s650
July: NavPod dry fit.
@s697
The front part I ordered from JLCPCB before the tariffs; the back I printed at home on a resin printer from "ABS-like" resin. The box dry-fitted on the boat. Then the real build: prototyping frames for the Pi, the display adapter board and the backlight power supply.
@s65
Inside, in layers: the display controller (HDMI to LVDS) and backlight power, the Pi on top, and its mounting frame. The face panel with the keyboard boards.
The software is standalone Python apps. navpod_manager talks to the keyboard, switches between apps and maps the physical buttons to them: OpenCPN, navpod_dashboard, Engine_control and Anchor_control. navpod_dashboard shows the sailing dashboard from Signal K and PyPilot. Engine_control shows a detailed motoring dashboard. Anchor_control is an anchor alarm that can also run the windlass, with its own dashboard.
Finally on the boat. A clean install: all wires inside the guard rail, the box screwed to the rail with machine screws (the rail drilled and tapped) and backing plates inside the plastic. And the real-world view.
@s66
How the buttons work. Left module: MOB (works whenever powered); power (one second to turn on and start the apps; when on, one second to toggle the display and backlight, double click for minimum brightness, triple for full, single click one step brighter; hold 3 seconds to shut down, 10 seconds to cut power); VNC/MAP (click for OpenCPN, double click for VNC to the main computer); sail/motor dashboards; auto/anchor (click for the autopilot dashboard, double click for anchor and windlass, with the right panel in keyboard mode); and the autopilot keys: mode, tack (with the ±10 buttons), STBY and AUTO.
Right module: mouse mode, lock, and KEY/NUM. In mouse mode the arrows move the cursor, OK is the left button, ESC/Return is Esc on a click, Enter on a double click and turns the arrows into scroll when held, and Right/Space is the right button. In keyboard mode the arrows are cursor keys and Right/Space and Tab/Next send Space and Tab. In NUM mode the autopilot buttons become digits.
@s64

## A radar from my son
August 2025 I got a great present from my son: a radar, a B&G (Navico) Halo20+. I don't need it on the lake, but since the boat was going to big water, it'll be a very good add-on to my navigation setup. No point making a real mount before transport, but I wanted to test it with my OpenCPN setup. So I designed a "cheap and dirty" bracket to tie it to the mast, cut from plywood on my CNC and glued.
@s705
Paying $300–500 or more for a piece of aluminum, even one holding a $2K radar, is insane, I think. And off-the-shelf mounts are "universal", with small hinges and small stainless pins: weak points and a place for galvanic corrosion. So, my own design.
Design zero was plywood, VERY temporary. I needed a two-hour lifetime. The boat was still on the lake, but I wanted to test the radar with OpenPlotter and OpenCPN before West Marine's return window closed.
@s94 s95 s96 s97
Then the real mount. My requirements:
- Take 10x the radar's weight both down and sideways without damage. Say 100 kg down plus 100 kg sideways. I think the radar would come apart before 200 kg got to the mount bolts.
- Made for my radar and my boat.
- As few parts as possible, ideally one, simple to build or order.
- Aluminum, like the mast. Minimum fasteners.
- Under $130.
My design is one piece of 3/16-inch (4.7 mm) 5052-H32 aluminum, as simple as possible. SendCutSend quoted $114, plus $15–20 of primer and paint I already had.
@s98 s99
In simulation it survived 200 kg with less than 2 mm of deformation. That's only a 20% margin at 200 kg, but a load like that means 25 G or a direct hit. Normally I expect no more than 5 G even in extreme working conditions, so about 4x margin. The flattened design and some 3D views.
@s100
Then the test on the water: the Halo20+ on the mast in its temporary mount, Vira with radar. Dual mode on the OpenCPN screen, and the overlay on the external OpenCPN screen. For some reason auto-targeting turned land into blobs and made a mess on the screen.
@s707

## Kemah: radar, AIS and a router
March 2026, 24 small things in two weekend days. The radar went on the mast. Simple, except the bracket had bent a little and the rear holes didn't line up, so I drilled them out a bit for the bolts. The other challenge was lifting the radar up the mast safely. It's round, with nothing to tie a rope to. And I riveted a plate for a Ring camera on the radar mount, to watch the docks, especially in really bad weather.
@s818 s822
The VHF antenna went back: SWR 1.3. The wind instrument and masthead camera hadn't worked last time. I suspected the wiring, but the masthead connector was plugged in the wrong way around. I still spent about 40 minutes at the top checking every wire, took the instrument down, rechecked it, and my son put it all back. Mission completed.
@s821 s825
I planned to splice the halyard to its shackle, but after three tries I gave up and tied a knot. I think the rope got hardened from climbing on it so many times. A reminder for myself: I need a pin for the main tack, 5/16, 1-3/4 working length. The injector tubes are 6.4 mm. The USCG garbage sticker went up.
@s827 s828 s830 s836 s838
The Maiana AIS went together, mounted on 6 feet of stainless tube on the back rail, the cable protected with heat shrink and run into the cabin. And a MikroTik router. I switched the 4G router to modem-only mode for internet; the MikroTik is the Ethernet switch for the radar, and I prefer it for Wi-Fi too. The masthead camera started working once I switched to it.
@s841 s844 s845 s846
See you in two weeks.
@s850

## AIS troubles and a 3D-printed steel clamp
In April 2026 I added a switch for the big cockpit touchscreen, so rain stops "touching" it. And the AIS transponder, repaired, went back and was tested. Now people can see me, if I transmit my position.
@s870 s871
Then a puzzle. Right after I installed the AIS transponder, the autopilot wouldn't stay running. I didn't connect the dots until later: PyPilot's control program was rebooting every 30 seconds, but only when the AIS was on. Long story short, the Maiana sends GPS data to Signal K as another GPS source, and PyPilot crashes because it can't parse it. I tried pointing PyPilot at the Linux GPSD daemon with a separate GPS. It worked fine at the dock, BUT underway GPSD locked onto stale positions, giving wrong position and speed, and I had to restart it every time it went into the weeds. Back to the drawing board.
@s878
The Maiana sits on the end of a 1-inch tube. To attach it to the stern rail I tried aluminum clamps from Amazon, and they were completely wrong for a boat. This is what one looked like after two weeks in Houston. Clamps for two parallel 1-inch tubes are almost impossible to find, so I designed my own and ordered them printed in 316L stainless from JLC3DP in China, four for $40. A week later they arrived, and I was surprised how well they were printed. After sanding they look like solid metal, and they are solid metal. Clamps in place.
@s889:5-8

## The NavPod is finished
May 2026, a weekend of NavPod software. It's a second Raspberry Pi head unit at the helm, with a 7-inch, 2,000-nit display, adjustable from 0.005% to 100%, talking to the main computer's Signal K, PyPilot and other apps. It has 26 buttons and mouse simulation. The left panel: power, a dedicated MOB button (saves the position, opens OpenCPN and drops a MOB mark), AIS TX on/off, three app buttons, and the autopilot: mode (compass, wind, GPS, true wind, nav), AUTO/STBY, ±1°, ±10° and tack. The right panel: mode buttons (keyboard, numpad, mouse, lock), arrows with OK, and Enter, Esc and Tab.
The sailing screen: a wind/compass instrument with apparent wind (orange arrow), true wind (blue marker), set and drift (green teardrop), heading, the autopilot mode, the rudder position on a hull outline, and a red dot toward the next waypoint. The side panels are fully configurable: on the left SOG, STW, depth, water temperature (:-)) and rudder; on the right time on each tack, and the next waypoint's direction, distance and speed. It will have sailing and motoring modes, and maybe day and night, but first I want to see it in bright sun.
@s880 s881 s882 s883 s884 s885
June: dry fit and sea trial. The front panel still needs paint and the buttons redoing.
@s898
July: the final install. It's not a brand-name Navpod; it just looks like one, so I call it NavPod. A full boat dashboard with physical buttons: sailing, motoring, OpenCPN and the anchor alarm, all running on the Pi inside and talking over Ethernet to the main OpenPlotter computer. I took the guard rail home and drilled and tapped it for screws.
@s906

## Small fixes
August 2026 the wind sensor showed nothing on the dashboards. A quick check: the small sacrificial resistor on the sensor board's power was blown. Probably a discharge to the mast, or lightning close enough to do that little damage. A soldering iron and a piece of wire fixed it.
@s913
September: one more GPS, 10 Hz, mainly for the autopilot's GPS mode. A faster GPS lets the autopilot work more precisely. Nothing fancy, a standard u-blox 10 module, but in a custom outdoor housing for the back rail.
@s938
