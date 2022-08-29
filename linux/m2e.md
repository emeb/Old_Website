





m2e




## 
ESS Maestro 2E


### 
Background


[ESS](http://www.esstech.com) has been involved in PC sound
since the early 90s (remember the Disney Sound Source?). More recently,
they have been producing the ISA-based AudioDrive chips which are supported
by the OSS modular sound drivers included with the Linux kernel. As the
x86 PC world migrates away from the ISA bus and towards the PCI bus, ESS
has introduced the Maestro and Solo audio chipsets to address this market.
These chips are available on many add-in cards and are also included on-board
some Mainboards and in some laptops (such as the Micron [GoBook2](gobook2.html)).

### 
Resources


As is typical of most PC hardware manufacturers, ESS and their OEMs are
reluctant to respond to Linux coders looking for the information necessary
for writing drivers. Despite this, detailed documentation for their chips
is available from some less well publicized sites, such as their [ftp
site in Taiwan](ftp://ftp.esstech.com.tw). At this site you can find Adobe Acrobat files with
specifications for the chips as well as test and driver code for DOS/Windows/NT.
Unfortunately, some directories are hidden. To access information regarding
the PCI-based audio solutions, use this [link](ftp://ftp.esstech.com.tw/PCIAudio).
Access to this site is rather sporadic - sometimes you can get there, sometimes
you can't. If you find it unavailable, wait a while and try again later.

### 
Drivers


Zach Brown has completed a Linux OSS-Lite driver for the Maestro chips.
With a diverse ancestry, this code has its roots in Thomas Sailer's Sonicvibes
driver, with initial hacking by
[Alan
Cox](http://www.linux.org.uk/diary), maintainer of the OSS-Lite modular sound. Zach has brought this
effort to its full potential with support for 8/16 mono/stereo output,
including mmap() access. Input is 16/stereo only due to hardware constraints,
without mmap() support. The most current versions of this driver can be
found in both the 2.2 and 2.3 kernel.
Hurray! [Zach's website](http://www.zabbo.net/maestro/) is back!

#### 
Compatibility


This driver only works for the Maestro, Maestro2, and Maestro 2e chips. The
[Maestro3 and Allegro](m3.html) chips are supported by a separate
driver which Zach is also maintaining.

#### 
Versions


I've got a version of Zach's v0.13 driver which adds MPU401 MIDI functionality.
I can't do extensive testing on this code, but if someone has MIDI equipment
available, this code may provide basic serial I/O support. Be sure to look
at the README.MIDI file in the tarball for more info on setting up this
version of the driver.
  
[v0.13m2 with whitelist](maestro-19991128.tar.gz)
  
[v0.13m with loadtime flag](maestro-19991126.tar.gz)
Brett Saunders maintains a site
[here](http://www.cl.cam.ac.uk/users/bms20/esshack.html)
where you can find a few more Maestro related files.
An [ALSA](http://www.alsa-project.org) driver is also being
developed for the Maestro. It's not as functionally complete as the OSS/Free
driver, but suitable for simple audio output. Matze Braun has more details
[here](http://home.t-online.de/home/Braun_Homburg/essm2ee.html).
[Return to Linux page.](linux.html)
##### 
**Last Updated**


:11/04/00
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)
  
 










