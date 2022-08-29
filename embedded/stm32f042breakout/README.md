xml version="1.0" encoding="utf-8"?



STM32F042 Breakout




# STM32F042 Breakout


![STM32F042 Breakout](f042_breakout.jpg)


#### Assembled STM32F042 Breakout Board V0.1


### What is it?


This is a small (1.2" x 0.7") board with an STM32F042F6 MCU, 3.3V regulator,
reset button, power LED, user GPIO LED, SWD header USB connector and all I/O
pins brought out to SIP headers suitable for use in a solderless breadboard.
With this board one can easily prototype small ARM Cortex M0 applications with
minimum effort and expense.

### What it isn't


This is not a full development system - you'll have to gather your own
programming tools, power supply, I/O devices, etc. This is not an Arduino
clone with all the low-level stuff already done for you. If you want to get by
on the cheap you'll have to be familiar with setting up an ARM GCC toolchain
as well as using a JTAG/SWD debugger.

### Features:


* [STM32F042F6](http://www.st.com/web/catalog/mmc/FM141/SC1169/SS1574/LN1823/PF259617)
 CPU with:
	+ 32-bit ARM Cortex-M0 CPU rated for 48MHz clock
	+ 6kB SRAM
	+ 32kB Flash
	+ 6 Timers
	+ 1 SPI
	+ 1 I2C
	+ 2 USART
	+ 1 USB
	+ 1 CAN
	+ 1 CEC
	+ RTC
	+ Crystal-less USB operation
	+ 15 GPIO pins (4 are 5V tolerant)
	+ 1 12-bit SAR ADC with 11 input channels
* Onboard 3.3V Regulator (4.1V - 10V input range)
* Filtered Analog 3.3V Supply
* 8MHz crystal (not required)
* Power and User LEDs
* Reset button
* USB mini-B connector with ESD protection (optional)
* 5-pin ST-Link V2 SWD compatible programming interface
* Standard 24-pin 600-mil DIP form factor (Fits solderless breadboard
 with 2/3 rows exposed on each side


### Interfaces


* J1, J2: 24 pins of direct access to all of the pins of the MCU.
 In addition a 5V input and 3.3V output as well as 2 more GND pins
 are available.
* J3: USB mini-B connector.
* J4: 5-pin ST-Link V2 This connector provides the ST standard
 SWD debug/download connection. Note only pins 1-5 are used
 since this MCU doesn't provide the SWO normally present on pin 6.
* JP1: Select USB Bus power.
* S1: Reset button - tied directly to the MCU reset input. Handy way to
 quickly reboot your MCU after flashing new code into it.
* LED1: Power indicator - lights up when 3.3V is present.
* LED2: User GPIO - connected to PB8. Useful for diagnostics.


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


* Schematic: <stm32f042f_breakout_schematic.pdf>
* OSHpark board: [STM32F042 Breakout](https://oshpark.com/shared_projects/iOdnJ9Ie)
* BOM: <bom.xls>
* Basic blinky firmware: <f042_blinky.zip>
* USB CDC serial firmware: [f042\_blinky.zip](f042_usb_serial.zip)
* More to come...


### Revisions


* V0.1 was first board fabbed.


## Status


* 05-21-15 - Schematic and layout.
* 05-21-15 - PCB design sent to fab.
* 05-22-15 - Web page created.
* 05-26-15 - Added BOM, OSHpark board link.
* 06-02-15 - Boards received from fab.
* 06-10-15 - Assembled. Basic blinky light test passes.
* 06-11-15 - USB DFU bootloader works. USB CDC test works. Website updated.


[Return to Embedded page.](../index.html)
##### 
**Last Updated**


:2015-06-11
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)

[![Valid HTML 4.01 Transitional](http://www.w3.org/Icons/valid-html401)](http://validator.w3.org/check?uri=referer)








