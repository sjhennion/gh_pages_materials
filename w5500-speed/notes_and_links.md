# Notes
- When switching between micropython and circuitpython, make sure to recopy your /lib/ directory on the circuit build.  I found that while the files were all still there, they were somehow corrupt and I was getting weird errors in Mu trying to run my code that hadn't changed
- 

# Links
These are in no particular order, but serve as basically a dumping ground for my research on this article
- [Micropython W5500 Page](https://micropython.org/download/W5500_EVB_PICO/)
- [Circuitpython Getting Started](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython)
- [Wiznet's Circuitpython Github](https://github.com/Wiznet/RP2040-HAT-CircuitPython) <- Here is where I found a working example for circuit
- [Wiznet's Micropython Github](https://github.com/Wiznet/RP2040-HAT-MicroPython) 
- [Wiznet's Micropython Releases](https://github.com/Wiznet/RP2040-HAT-MicroPython/releases)
- [Adafruit's Circuipython Wiznet Github](https://github.com/adafruit/Adafruit_CircuitPython_Wiznet5k) <- These examples had `board.Dx` configs that did not work out of the box for me
- [Adafruit Circuit Wiznet releases](https://github.com/adafruit/Adafruit_CircuitPython_Wiznet5k/releases)
- [Circuitpython Library Bundle releases](https://circuitpython.org/libraries)

