A 40-year-old boat with 40-year-old wiring. Bare copper, twisted joints under electrical tape, a burned-out alternator and two dead batteries. I ended up replacing every wire on Vira, then built a panel, and then went into lithium, inverters and a lot of lessons about smart batteries.

## The alternator
January 2022 I took the alternator home to check it. I hoped it was just the regulator. Opening the case showed burned stator windings, so it's good only as a weight. I had a 63 A automotive alternator in the garage with a different mount, and with a hacksaw and my hands I adapted it to the Yanmar 2QM20. Later I'll take an AC signal for the tachometer and add voltage control so long engine runs don't overcharge the batteries. LATER.
@s126 s123:1-3
That month the new shore power cord went in, and the old one was retired.
@s131
And the steaming light mount. Really?
@s207

## Why does the wiring go around the boat?
June 2022, one more surprise: the original wiring goes down the starboard side, turns, and comes back along the port side. WHY?
@s193
September 2022: I know the original wiring is 40 years old, not tinned, not "marine", and that the 110 V outlets are corroded. But what I found under the ORIGINAL electrical tape made me feel I had to replace everything. Fun #1: during the build they apparently cut the wires in the head cabinet too short, added a piece with two loose twists and covered it with tape. I'm pretty sure it's original; it's the same tape as all the harnesses. Fun #2: the 110 V outlet by the nav desk had no box at all, just pushed into a hole in the liner.
@s253
In September a quick test of the house and start batteries: one had 5–6 Ah left, the other 10–15. Both on the edge of death, so I replaced them.
Then I found that ALL the original wiring was thick stranded copper, not tinned, and oxidized. Even inside the original harness there were twisted joints. And on my boat every port side wire goes from the main panel to the bow and back. I don't see why. There's a perfect path under the companionway step, and Irwin's own diagram shows the wires there, not around the whole boat. It's not just wire length; it also makes the system more vulnerable to lightning. Here's a nice example of an ORIGINAL power harness: looks like the wires came out a bit short and they extended them.
All the wiring is 40 years old and I don't trust it anymore, so I decided to replace everything. A couple of hours digging out space to route wires. Building the harness, every wire tagged at both ends. Mounting blocks glued to the hull every 18 inches to hold it.
@s257:1-6
Two observations not about wiring. There's lots of unused space in the corner left of the nav desk. My first thought: WOW, a nice place to hide electronics. But it'd be a nightmare to reach for maintenance. And the laminated plywood piece in the corner of the pilot berth is both inside and outside: not glassed on the outside, so water gets into it easily. When I removed it I got a "nice" opening from under the engine room hatch into the cabin. That should be glassed, not just plywood.
@s257:7-10
Then the new wiring system, following my wiring diagram.
@s260
Wires for an electric toilet, the refrigerator, the autopilot and pumps, all organized along the hull sides. I tested the original battery charger, and surprise, it was broken: no real charge current, just a little pulsing. A new 3x5 A charger went in, in a temporary place.
@s264
And in March 2023, at home, a small side project: one of my 18 V Bosch tool batteries had a broken latch cam. I broke it years ago and held it with masking tape, and it finally got too annoying. So I modeled and 3D printed a new cam.
@s359

## Inverters and lithium
October 2022 I dry-tested a 3,000 W inverter running the air conditioner from one dual-purpose battery. My lithium batteries were still being built. The AC ran well, maximum load 1,200 W. And a small 400 W inverter with the refrigerator. Works well; the fridge label says 0.8 A, way below.
@s272
To make the 3 kW inverter work with a 10.8 V lithium battery I had to change its low-voltage cutoff, by adjusting a 20 kΩ resistor on a small control board. The battery box fit exactly in the locker next to the original batteries.
@s283
Then a flat floor for the lithium battery in that compartment. Maybe I can fit a fifth pack there.
@s298

## Off the old panel
April 2023: terminal blocks on the back of the fuse box, and all the high-current and 110 V wiring terminated.
@s363 s366
May: the battery charger moved to its permanent place, the original panels came out, and temporary connections went in so I'd still have power: 15 A fuse on DC, 25 A on AC. And a shelf for the inverter.
@s371
A 110 V outlet in the front cabin, then a 12 V outlet and USB charger there too. A temporary switch for the nav lights. Time to build a switch panel.
@s376 s387 s390
Four galley outlets. A bottom plate separating the distribution panel compartment from the engine room. And the new electric panel design.
@s393

## A new panel
July 2023: the new panel design, garage manufacturing, assembly, first dry fit. Really tight, but it fits.
@s396
Then it was installed. All the old wiring is gone except one connection, the bow nav lights. The indicators are color-coded:
- Red: a problem, or something to pay attention to (bilge pump running, LPG, engine room light, service fuel pump).
- Yellow: circuits that run when someone's aboard or underway.
- Green: can or must stay on.
I replaced all the 110 V outlets and crimped proper ring terminals. For now they're simple household outlets. It would be nice to have something more "marine", but I didn't find anything reasonable. Main power is reconnected to the new wiring, with a 25 A GFCI in an IP68 box between the main inlet and the panel, 2 feet from the shore power port. It's very hard to meet the rule about distance from the wet exhaust hose. No idea what to do about that.
@s400

## The dock turned 90 degrees
October 2023. I usually get to the marina early, and that day I came about 7 AM and... didn't see my boat. Even more, I didn't see THE DOCK my boat was on. I called the marina owner, and of course he doesn't answer at 7 AM on a Saturday. Short story: they turned the whole dock, with all the boats, 90 degrees. Five very hard minutes, then I found my boat.
Second surprise: no electricity on the docks. Third: the boat was now somewhere almost impossible to get in and out of: about 10 feet from shore to the transom and 3 feet from the rudder to the rocks. Later the owner let me swap with a boat across the dock.
But no electricity. So I went home and got the inverter and my 2.5 kWh lithium battery.
@s433
That was the first time I ran the inverter on the boat. A "dry" install: inverter on a cardboard box, output to the wires I'd run for it, low-voltage cables to the battery, and start. Everything worked perfectly. The 110 V panel lit the inverter lamp and I switched the input to "inverter". With just one battery I could only use about 1 kW without tripping the BMS, but that was enough for the lead battery charger, lights, a fan, and now and then the big shop vac and some power tools.
I'd put a battery monitor screen on the DC panel, but it shows battery current, not the house loads. When anything charges the battery, you see the battery current, not what the house uses. So I added another meter next to the refrigerator thermostat, to see the real 12 V consumption. I'm not proud of this solution, but better now than later. I also dry-fit a battery monitor and shunt on the lead battery and left it a few days to see how much they drain: under 10 mA, so about 5,000 hours, or roughly 7 months, to drain the battery. I think that's OK for "self-discharge".
@s434

## The nav desk panel
January 2024: a panel at the nav table, with water and fuel tank gauges and a small 2.5-inch thermal printer, just in case I want to print a "ticket". The light over the desk dims from "good enough for surgery" to "hard to see anything". The black water gauge is where you'll check it before use.
@s461
I connected that black water gauge to an indicator in the head, powered from the "WC" breaker, so when you go to flush you can see how much room is left for "stuff". I powered up the thermal printer; it's always nice to have something aboard that can print. Then I got ready for the cold with the engine compartment heater. And then, COLD WEATHER: −5 °C outside, docks covered with ice, and the lake at about +15 °C, steaming like tea in a cup.
@s465:2-5

## New battery cables
I'd replaced all the wiring after the breaker panel with high-flex tinned wire to UL 1426, but left the battery side as it was. Now its time came. Three days: one to take apart the old wiring, one to look at the engine wiring and start building the new, and one to finish, tidy, label and zip-tie.
What I didn't like about the original battery wiring:
- Old wires heavily oxidized, with many broken strands.
- Low-quality crimps, strands sticking out of the terminals.
- The battery switch 7 feet from the batteries.
- 15 feet of positive cable from the battery to the starter, plus 4 feet of negative, all in 2 AWG.
- 10 AWG for the negative from the batteries to the DC panel, really undersized.
- No way to charge both batteries from the alternator without paralleling them, which should be a last resort.
- None of the extra features I wanted.
The goal: comfortable, safe, to standard, reliable, easy to fix if something fails, and all the bells and whistles I want. Sounds simple. The new wiring:
- Switches moved right next to the batteries. Three of them: start, house, and coupler (1+2).
- Starter cables down to 3 feet positive and 3 feet negative, upsized to 0 AWG, so it can take everything from both batteries if needed.
- A 50 A breaker on the house right after the switch.
- A dual battery isolator, so the alternator charges both batteries.
- An "ideal diode" module, so the house runs from a shore power 14 V supply when available. A battery charger gets confused when loads are on the battery while it tries to charge. No more confused charger.
- A smart monitor on each battery, two 400 A shunts and their electronics.
- Wiring for my 350 Ah 12 V lithium battery to the 3 kW inverter, with a fuse and switch. The lithium doesn't feed the 12 V system directly, only the inverter. A DC-DC charger to the house battery later.
- 4 AWG from the batteries to the DC panel, good for up to 130 A.
@s468:1
Ideas on paper, then counting every length and gauge. I ordered all the cables made up from Battery Cables USA and got them in three days, with very good crimps and real marine battery cable. Lots of planning to get everything right. I laid them out to check lengths and terminal sizes, then laid out the components. Switches, diodes and breakers are in the engine room, port side, right next to the batteries on the other side of the wall. In 2D it looks a bit messy; in 3D it's better. The battery compartment, with the monitors on the side wall, and a view toward the engine, with some wires still "flying" on day two.
@s468:2-9

## Priming the inverter
With the 3 kW inverter and lithium battery working, I wanted a switch for that "sweet couple". But the first time I connected the battery to the inverter, the BMS shut it off: a huge current spike from charging the inverter's input capacitors. So the capacitors have to be charged first. I added a button and a 100 Ω resistor across the main switch, with an LED showing the voltage across the resistor. Now I "prime" the inverter: press the button and wait until the LED goes out, then switch on. A new power switch panel, dry-fitted.
I also found something pressing on the back of the big cockpit screen, stressing the LCD. It was a USB extender box stuck between the plywood and the display. I cut a hole to take off the strain. It was like digging around a land mine: cut the plywood without breaking into the adapter. I scratched it a little, but it still works. A nice cover next time.
@s471
All the antenna cables joined with N-type connectors. Ready to close the headliner. Testing with a handheld VHF, the signal is much better from the masthead antenna. Unfortunately there's no radio check service in Austin, at least I didn't find one. And a "booster" battery, another 67 Ah, next to my 268 Ah inverter battery. The small wire powers the smart monitor. Still need to figure out how to secure the batteries in the locker.
@s497

## Mast cables
In February 2024 I sealed the last piece of wiring: where the mast cables come through the deck. For now three cables: nav and deck lights, VHF antenna, wind instrument. First, let's see what comes out of the mast. Just a 40-year-old boat: three connections for each wire hidden inside the mast, wrapped in layers of electrical tape, some crimped, some twisted.
I chose a single cable seal box made for 3+ cables, so I can add more later, the powder-coated stainless version. It's well designed, but I like to raise through-deck fittings a little so water flows around the seal. So a 6 mm G10 mounting plate laminated to the deck, which also gives a nice flat surface for the gland. 20 minutes in CAD and 15 minutes on the CNC. The plate glued on thickened epoxy with fillets around.
@s493:1-4
The cables got sleeved in polyester rope covers, for UV protection, and they look fun. You can see the raised plate, with about half an inch each side for water to go around. Patching and painting later.
By the way, the mast base looks cracked, but when I drilled the deck for the wires the core shavings were completely dry, so the cracks are probably only gelcoat deep. I'll fix them when the mast comes down. Not now.
Under the deck I tidied the wiring too. The wires dip to a low point before they connect, as a water trap in case of a leak. And a water test: a 2-inch masking tape dam around the seal, filled with water, left for 30 minutes. No drip inside, at least for now.
@s493:5-7
I routed the wind instrument cable to OpenPlotter, so now I have the instrument and the camera view on the dashboard. And a plug plate over the hole I'd cut to take the pressure off the cockpit LCD. Maybe later one single plate.
@s493:8-9
In February 2026, at the boatyard, the mast got all new cables, eight in total:
- Masthead: VHF/AIS antenna, tricolor/anchor light (16 AWG), wind sensor and camera (20 AWG).
- Radar level: the B&G radar cable, a spare Cat5 Ethernet for a 4G/Wi-Fi router, and a 4-wire 18 AWG power cable for the future.
- Steaming light: 2-wire 16 AWG.
- Spreaders: deck lights, 4-wire 16 AWG.
@s803
Connecting them under the deck: easy to say, two hours to play with. I still had to fish three wires to the nav desk: the radar, the Ring camera power and the spare Ethernet from mid-mast.
@s826

## Lithium lessons
March 2026: the new 100 Ah LiFePO4 house battery had been in for a few weeks without a proper fuse. A class-T fuse went on the battery cable. Breaker guards on the main panel. And a Victron 25 A charger for the inverter battery, wired behind the panel. Still to do: its 110 V feed, and a relay to block charging when the 110 V system runs from the inverter.
@s837 s848 s858
In April I added a dimmer for the indicator LEDs on the main panel.
@s872
I have a NOCO GEN5X3 three-bank charger for the start, house and windlass batteries. It worked well for about five years with lead-acid. Then the house battery became LiFePO4 and I switched that bank to lithium mode. Everything looked fine at first. I also had a 40 A, 14.2 V power supply running the 12 V system from shore power, joined to the battery through a 100 A ideal-diode module.
One night, sleeping aboard, I saw the lights blinking now and then and the nav computer rebooting every 10–15 seconds. A mystery. I checked for heavy loads, loose connections, bad wiring. Then I saw the NOCO showing "Overvoltage" on the lithium battery. Surprising. The BMS showed nothing suspicious: the battery was simply at 100%.
Then I found the BMS was a little too smart. At 100%, it simply disconnects the charging path. No fault, just discharge-only. After resting, the battery voltage dropped back to about 13.9–14.0 V. The charger saw that and decided to charge again. But the BMS had blocked charging, so the current had nowhere to go and made a short spike of about 16.5 V. The battery couldn't absorb it, so it went to the ideal-diode module. The module saw the battery side suddenly higher and switched sources, and because the pulse was so short, it confused the whole sharing arrangement and made a spike and then a dip on the 12 V bus. My computer's protection socket saw the bad voltage and shut the computer down. A few seconds later everything recovered, and then it all happened again.
That's what pushed me to design my own UPS-like power switch. It's in the small electronics story.
@s916

## A real ELCI
In May 2026 the shore power GFCI started tripping whenever the refrigerator compressor started. I'd checked the compressor pins to the case before and couldn't measure anything under several megohms, so I was sure it was fine. Maybe the GFCI got damp or too sensitive in the humidity. When it tripped again, I decided it was time for a real Equipment Leakage Circuit Interrupter made for boats.
Saying ELCIs are expensive is an understatement. You hardly find anything under $250, even on sale. But I hate the idea of 110 V on the boat without ground-fault protection, so I bit the bullet: a 30 A ELCI and an IP67 box, to replace the industrial DIN-rail GFCI.
It arrived, nice and shiny. I spent an hour putting proper terminals on the wires and figuring out the routing. Then, on the very last screw, I heard a "crack" and the terminal came loose. It wasn't secured properly inside. So no GFCI or ELCI until next time.
@s878
Thanks to Walmart for refunding the broken one, I ordered a new one, a Blue Sea A-Series 30 A double-pole. Now there's a proper ELCI on the shore power. I found an IP68 box as small as reasonable, and as usual it's "a little small", but the next size is really big. A panel-mount ELCI in a box with no front panel isn't simple: it's deep and doesn't fit in the base, so the panel has to stick out about 1/4 inch. I designed a panel that protrudes, with threaded inserts in the box, and a separate space for a ground terminal block behind a small wall. It's installed 10 inches from the shore power inlet, in the starboard cockpit locker, easy to reach. And the real label.
@s889:1-4
