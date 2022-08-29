xml version="1.0" encoding="utf-8"?



dsPIC FPGA



# dsPIC FPGA board


![dsPIC_fpga PCB](dsPIC_fpga_full.jpg)


#### Assembly progress: complete


## Hardware


This is a small project focused on CV-based signal generation using the
Microchip dsPIC and a mid-range Xilinx Spartan 3A FPGA. It provides the
following features:

* Microchip [dsPIC33FJ128GP204](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en532297) Microcontroller with 128kB Flash, 16kB SRAM, ADC, Codec interface, I2C, SPI, etc.
* Xilinx [XC3S200AVQ100](http://www.xilinx.com/products/spartan3a/) Spartan 3A FPGA with 200kgates, 16 Multipliers and 288kb RAM.
* Cirrus Logic [CS4344](http://www.cirrus.com/en/products/pro/detail/P1050.html) stereo audio DAC with up to 192kHz / 24-bit sampling.
* Atmel [AT45DB321D](http://www.atmel.com/dyn/products/product_card.asp?part_id=3818) SPI 32Mb Flash.
* Micro SD flash memory socket.
* Off board analog/control port with:
	+ stereo audio output (+/-5Vpp, DC-coupled).
	+ 4 x 10V CV + offset pot inputs.
	+ 3 x 3.3V logic inputs to FPGA.
	+ 1 x wide-range buffered logic input to FPGA>
* Off board digital expansion port with 6 MCU I/O.
* 3 x Digilent-compatible I/O ports with 4 FPGA I/O, 3.3V and GND.
* ISP port for MCU development and debugging.
* JTAG port for FPGA development and debugging.
* +12V, +5V, GND, -12V power connector.


### Motivation


The impetus for this board is to experiment with audio
FPGA-based audio synthesis algorithms, voltage control and SD memory
concepts.


Potential applications include:


* Wavetable oscillators
* Field upgradable MCU firmware
* Flash-based FPGA configuration
* Voltage Controlled digital hardware
* Granular Synthesis
* etc


### Processor


The dsPIC line of 16-bit processors from Microchip provides excellent
performance in embedded applications, coupled with a strong lineup of on-chip
peripherals. The device chosen for this board has plenty of flash memory for
complex applications and is available for a reasonable price even in small
quantities. Software development tools are freely available and provide
good results for both assembly and C source code.


### FPGA


The Spartan3A line of FPGAs from Xilinx are inexpensive and easy to use.
The architecture has been refined over years from prior Xilinx parts and these
parts provide plenty of useful features, including dedicated on-chip RAM, clock
management, multipliers and flexible I/O. In addition to being available in a
DIY-friendly 100-pin flatpack package, the 200kgate part chosen for this board
also requires only two supply voltages, making it somewhat easier to use
than the previous generation Spartan3E devices which needed 3 supplies.


### Storage


FPGA configuration bitstreams typically require several hundred kilobytes
of storage. Additionally, firmware updates, wavetables and other data may
also require large, removable storate. SD Flash memory is a major advance
in portable storage and is now available on many new PCs, Laptops and Netbooks
as standard equipment. The electrical interfaces required to access SD memory
in DIY applications are fairly simple if one is satisfied to use the slower SPI
method, and many processor manufacturers including Microchip provide free
libraries to enable SD interfaces. For this project, I've chosen the Micro SD
format primarily for its size and simplicity. Data may be formatted using
standard FAT16 or FAT32 specifications for compatibility with all current
operating systmes (Windows, MAC OS X, Linux).


While the SD card interface is directly connected to the dsPIC processor,
another serial flash memory is directly connected to the FPGA. This will allow
direct hardware interfacing to large amounts of non-volatile storage for such
things as samples, wavetables, etc. Although there is a slight bottleneck due
to the 1-bit SPI connection, this memory will still support sufficient bandwidth
to allow 16-bit interpolated samples at up to 384kHz rates, which should allow
fairly complex wavetable oscillator applications. By designing SPI muxing logic
into the FPGA, this memory may be written directly from the dsPIC via the same
SPI interface used to control the FPGA, then connected to custom read logic
in the FPGA for realtime readout.


### Interfaces


Multiple digital and analog interfaces are present on this board which
should enable its use in a variety of applications. While my primary goal
is for a board that could be used in a modular synthesis context, this
system is flexible enough to be used stand-alone as well. Multiple digital
connections will support off-board displays, buttons and encoders, as well
as common interfaces such as RS-232, SPI and others with appropriate
hardware. 4x 10V analog interfaces with offset pots digitized to 12-bit
resolution via the dsPIC on-chip ADC will support voltage control, while
a 24-bit 192kHz stereo audio DAC with +/-5V output buffers provides for
high quality output.


### Configuration


Based on previous experiments with ARM processors, loading
the FPGA bitstream from SD flash via a SPI port and slave serial mode
is a workable approach. This design goes beyond that to provide an option
to load using the dsPIC PMP (byte-wide parallel port). This may accellerate
boot times, as well as provide more CPU/FPGA bandwidth for the final
application. Additionally, if parallel mode is not used the additional
dedicated lines between the dsPIC and FPGA, coupled with the flexibility
of the dsPIC I/O pin muxing will allow more dsPIC peripherals to be
routed to the auxiliary I/O connectors.


### Design Collateral


* [schematic PDF](dsPIC_fpga_pg1-3.pdf)
* [Bill of Materials](bom.txt)
* [gEDA/gschem schematic](dsPIC_fpga_v0.1_schematic.zip)
* [gEDA/PCB design file](dsPIC_fpga_v0.1_pcb.zip)
* [Gerbers](dsPIC_fpga_v0.1.zip)
* [Test firmware](fpga1.zip)
* [Test FPGA design](spi_tst.zip)
* More to come as developement continues


## Firmware


dsPIC code for this will be developed using the freely available Microchip MPLAB IDE, including an assembler
and GCC-based C compiler, as well as mass storage and flash access libraries. FPGA designs will be created with the
Verilog Hardware Description Language under the free Xilinx Webpack ISE development environment. Once the basic hardware
is checked out I'll post skeleton C projects and FPGA designs that can be used for individual development.


## Status


* 10-25-09 - Start schematics.
* 11-01-09 - Start Layout.
* 11-15-09 - Submit rev 1.0 board layout to fab.
* 11-18-09 - Create Web page.
* 12-04-09 - PCBs arrive in mail.
* 12-19-09 - Assemble SD, Power, dsPIC. Confirm Power, dsPIC.
* 12-26-09 - SD filesystem works.
* 12-27-09 - Assemble FPGA. JTAG config works.
* 01-01-10 - FPGA serial config from SD works.
* 01-03-10 - Debugged DAC output drive issue.
* 01-16-10 - Added UART command line firmware and FPGA SPI port.
* 01-17-10 - Assemble CV inputs.
* 01-19-10 - Test dsPIC ADC driver code.
* 01-21-10 - Assemble SPI Flash. Test command line read/write.
* 02-02-10 - All hardware tested. Post design materials.


[Return to Synth page.](../index.html)
##### 
**Last Updated**


:2010-02-02
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)

[![Valid HTML 4.01 Transitional](http://www.w3.org/Icons/valid-html401)](http://validator.w3.org/check?uri=referer)







