xml version="1.0" encoding="utf-8"?



Cheep Mod




# Cheep Mod - a low cost platform for Euro-Rack digital audio.



![Cheep Mod](cheep_mod_hw_front.jpg)
![Cheep Mod](cheep_mod_hw_back.jpg)



#### Cheep Mod Front - fully assembled


### What is it?


This is a small 6HP Euro-Rack format module with 3 CV inputs, 3 pots, Digital
(Sync) input, 12-bit DAC Audio output and Digital (gate) output.

### Why?


I do a lot of development for various Euro-Rack manufacturers but I've never
built an entire module myself. This project was an experiment on several fronts -
what's the cheapest yet most capable MCU to use (the one used here costs $0.50)
while still providing features that allow advanced DSP, and how well does it work
to use PCB manufacturing processes to create a modular front panel? Considering
the advanced synthesis algorithms I've been running on this hardware and the
decent appearance and assembly of the panel I consider Cheep Mod a success on
both fronts.

### Features:


* [STM32F030F4](http://www.st.com/web/en/catalog/mmc/SC1169/SS1574/LN1826/PF258968)
 CPU with:
	+ 32-bit ARM Cortex-M0 CPU rated for 48MHz clock
	+ 4kB SRAM
	+ 16kB Flash
	+ 5 Timers
	+ 1 SPI
	+ 1 I2C
	+ 1 USART
	+ RTC
	+ 15 GPIO pins (4 are 5V tolerant)
	+ 1 12-bit SAR ADC with 11 input channels
* 3 front-panel pots
* 3-position toggle switch for mode selection
* 3 +/-5V CV inputs
* 1 digital (sync/trigger/gate) input
* 1 12-bit 200kHz DAC +/-5V (audio/CV) output
* 1 digital (sync/trigger/gate) output
* 1 6-pin ARM SWD connector (ST-Link V2 format) on back
* Standard 16-pin shrouded Euro-Rack power:
	+ +12V @ 28ma
	+ -12V @ 9ma
* 24mm deep


### Software Development


The STM32 family of parts are supported by a variety of commercial IDEs, all
of which are available in low-cost or limited free versions from the
[ST website](http://www.st.com/internet/mcu/class/1734.jsp).

I prefer to use open-source tools so I've set up a development environment
based on the GNU C compiler for ARM, available for free from the Launchpad
project. For downloading to the target I use OpenOCD and the ST-Link V2 SWD
interface that's available on most all of the inexpensive STM32 Discovery boards.
To accelerate development I also use the STM32 Standard Peripheral Library as
a starting point for my code and then optimize out the heavyweight functions
as required. Links to all of these are here:

* [Launchpad GCC](https://launchpad.net/gcc-arm-embedded): 
 ARM-supported GCC (somewhat newer than the CS version above).
* [OpenOCD](http://openocd.org/): JTAG/SWD interface for
 programming a debugging.
* [STM32F0 Discovery](http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/PF253215?sc=internet/evalboard/product/253215.jsp): Development board with USB flash programming
 and debugging.
* [STM32 Standard Peripheral Library for STM32F0xx](http://www.st.com/web/catalog/tools/FM147/CL1794/SC961/SS1743/LN1939/PF257884): Manufacturer's low-level C driver code.


### Design Resources


* Schematic: <cheep_mod_schematic.pdf>
* BOM: <cheep_mod_bom.xls>
* more to com...


### Project Status


* 2015-04-30: Started Schematic, order parts.
* 2015-05-02: Order PC boards.
* 2015-05-18: PC boards arrive, assembled, working.
* 2015-05-22: Created web page.
* 2015-05-26: Synth apps work. Added BOM.


[Return to Synth page.](../index.html)
##### 
**Last Updated**


:2015-05-26
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)

[![Valid HTML 4.01 Transitional](http://www.w3.org/Icons/valid-html401)](http://validator.w3.org/check?uri=referer)








