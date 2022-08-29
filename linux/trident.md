




Trident 4DWave Sound




# 
Trident 4DWave


The Trident 4DWave DX/NX PCI Audio chips are found in a number of currently
available and inexpensive sound cards. ALSA had the original driver for
this architecture, thanks to some excellent support from Trident. 
Until recently however, OSS/Free did not support these chips. Fortunately,
the 4DWave is derived from an IP (intellectual property) core from an outfit
called T2 which is also used by SIS and ALi for their own audio
interfaces. Ollie Lho, working for SIS has combined code from the
original ALSA driver, as well as OSS/Free drivers from Zach Brown, Alan
Cox and Thomas Sailer to produce a fully functional OSS/Free driver for
the Trident 4DWave and SIS 7018. Ching Ling Lee has extended it to
support the ALi 5451, Aaron Holtzman cleaned it up some and I backported
it from the 2.3 development kernel to the 2.2 stable kernel.

To use this driver, you will need to be running at least the 2.2.16
stable kernel, or the latest development kernel (2.4.0test series at the
time of this writing). The driver is only available as a module (it
cannot be permanently compiled into the kernel) and supports no load-time
options. It will automatiically detect the type of chip you have and will
not load unless it finds a supported interface.

Currently, the driver supports only PCM audio I/O in all the standard
OSS/Free formats, as well as the standard OSS/Free mixer interface. Dual
AC97 codecs are supported for Dolby AC3 5.1 channel audio. MPU401 MIDI,
joystick and FM are not supported, but may be added in the future.

[Return to Linux page.](linux.html)
##### 
**Last Updated**


:06/10/00
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)








