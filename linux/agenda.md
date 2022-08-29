




Agenda VR3 PDA




## Agenda VR3 PDA


### Introduction


In the fall of 2001, I picked up an Agenda VR3 PDA at Fry's in Phoenix. At the
time, the VR3 was made by Agenda Computing, a subsidiary of a worldwide company
with locations in Asia, Europe and the US. Since then, the parent coproration
has shut the company down and the VR3 can now be obtained from
[Softfield](http://www.softfield.com) who started out as the contract
manufacturers of the device and have since obtained the rights to build/sell it.

The VR3 is unique in that it started out as a user supported platform. The
designers opened up the architecture and firmware to such an extent that it
is possible to continue to improve it long after the original developers have
scattered. Aside from the folks at Softfield who still support the hardware,
the Linux kernel and GNU-based OS are still under development by a small but
fanatical group of folks who gather at
[Agenda Wiki](http://www.agendawiki.com) to exchange tips and
techniques for using and improving this device.

###  Kernel Upgrades


As originally shipped, the Linux kernel for the VR3 had some shortcomings.
The hardware platform includes a wide array of peripherals, such as digital
audio I/O, infrared I/O, Consumer IR (remote control), dual-color LEDs,
a buzzer and numerous buttons and sensors. Not all of these were actively
supported by the kernel though, leaving a plethora of opportunities for
those of us interested in kernel hacking.

###  Audio


Since audio applications are one of my interests, I gravitated to the
audio input features nearly from the start. Not long after getting
my VR3, I started trying to play and record digital audio. I was pleased
to see that the common application 
[Sox](http://sox.sourceforge.net) was included in the OS, and
that copying a standard WAV formatted file to the VR3 allowed me to play
it through the mono mic/headphone that is included with the device. Sox
also supports recording, but every time that I tried this, it would hang
the machine. Obviously there was something wrong.

Browsing through the mail archives, it became clear that I was not the
first to discover this. Further discussions with the original developers
revealed that after getting the audio output working, other priorities had
forced them to abandon work on the audio input code, and it hadn't progressed
since. Shortly thereafter, Agenda went out of business and the world of the
VR3 became very quiet.

###  What's new


Recently though, VR3 development has begun to heat up. Several folks have
set up a range of Sourceforge depots to maintain the VR3 kernel, and a new
package-based system has sprung up to maintain the OS. The Wiki is active,
and the mail list is fairly busy. When the issue of audio input came around
on the mail list again, several of us volunteered to work on it. As a result,
I've got a few things to contribute.

####  Updated Kernel Sound Driver


I've done a fair bit of work on the drivers/sound/vr4181.c kernel sound driver.
The current version can be found on [Agenda OS at Sourceforge](http://sourceforge.net/projects/agos).

Milan Pikula has a much better driver available at his [agenda website](http://www.terminus.sk/~www/agenda/) which I reccomend instead of mine.

####  Audio Tools


To test the audio driver as I work on it, I rely on a few home-made userland
tools.

[oss-beep](oss-beep.tar.gz) is a simple little digital audio
output tester which allows me to quickly generate sinewaves at various
frequencies, channels and word-lengths. This is important in testing output
quality, as well as driver capabilities.

[ramrec](ramrec.tar.gz) is a RAM-buffered recording application
that is needed to test input quality. Sox can't be used due to the way it writes
to the disk.

[rec-test](rec-test.tar.gz) is a simplified app that can record
a few DMA buffers worth of audio data and dump the results to stdout. I use
this as a quick check when banging on the driver.

[wavedump](wavdump.tar.gz) is a host application that assists
me in analyzing the audio input in greater detail. I use it in conjunction with 
[Octave](http://www.octave.org) to do spectral analysis.

[record](vru-record-0.1.tar.gz) is a FLTK/FLPDA GUI application
for the VR3 which allows you to record and playback .WAV files. Here's a [snow 1.2 binary](vru-record_snow_1.2_binary.tar.gz) as well.

####  Audio Hardware Mods


As part of my work on the VR3 audio driver, I cleaned up the bypassing on the
audio input preamp. Here's a [tarball](audio_fix.tar.gz) describing
the changes I had to make.

####  Address Database Conversion


Although I do a fair amount of hacking on the VR3, I also use a Sharp Zaurus
for day to day PDA functions. Recently, I lost my Z, so I needed a way to
convert the Qtopia Desktop Contacts database to a format the VR3 could use.
The result is [z2a](z2a.tar.gz), a perl script which parses the
Qtopia XML format and spits out a GnomeCard compatible database that you can
load into your VR3.

Please let me know if this is useful for you. 


[Return to Linux page.](linux.html)


##### **Last Updated**


:2003-7-19
##### **Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)  

   























