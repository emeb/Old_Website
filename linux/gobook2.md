





gobook2




# 
Micron GoBook2


In the spring of 1999, I bought a Micron GoBook2.  It came with Win98
pre-loaded, but being a Linux weenie, I decided to load up RedHat and see
how it worked. With some assistance from the excellent [Linux
on Laptops](http://www.cs.utexas.edu/users/kharker/linux-laptop/) site I have it going and it works very well. I use Linux
at work on some rather high-end PIII systems, and Linux on the GoBook is
an excellent adjunct to that environment.
## 
RH 7.1


Starting out with RedHat 5.2 I've kept the system current with the latest
releases and now I'm running 7.1 (Seawolf). I'm quite pleased with the
overall performance and it just keeps getting better as more of the system's
features are supported with each revision.   Here are the details:
### 
X Server


This time around, the installer figured out my video subsystem and set
up the correct driver without any guidance from me.
### 
Sound


RedHat's Soundconfig utility finds the Maestro2e sound subsystem without
difficulty and sets up the modules.conf correctly with [Zach's
driver](http://www.zabbo.net/maestro/) from the kernel. You do need to run sndconfig by hand - it's
not part of the normal install process.
### 
PCMCIA


PCMCIA card services work out of the box without modification. They even
found my [802.11(b)](80211b.html) card and started it up without
assistance!
### 
Power Management


The installer sets up apmd, but it doesn't seem to have particularly agressive
defaults. The hard-drive stays spun up continuously, and the laptop doesn't
suspend during long periods of no use. I'm going to have to look at this
more closely.
### 
Modem & Ethernet


See below - I've not used the modem or Ethernet cards for a while now that
I'm using 802.11(b).
### 
IR


The installer found the IR subsystem and seems to have set up the kernel
IRDA drivers, but I haven't bothered trying to do anything with it yet.
See below for my previous forays into this area.
### 
USB


This is the reason to go to a 2.4 kernel! The USB subsystem in the GoBook
is not properly initialized by the BIOS, so unless you have the 2.4 kernel's
new PCI subsystem, the USB controller doesn't come up right. With 2.4,
the GoBook's USB is all there and working fine. I've used it to hook up
an Ezonics EZCam-USB using the kernel [CPIA](http://webcam.sourceforge.net/)
drivers and [gqcam](http://cse.unl.edu/~cluening/gqcam/).
### 
SCSI


See below.
### 
Hotkeys


Still no word on how to get these bad boys working.
## 
RH 6.2


### 
X Server


Standard RedHat CDs don't include the correct X Server for the Neomagic
chipset that the GoBook2 uses. You'll need to get the XFCom\_Neomagic server
from Precision Insight's ftp site [here.](ftp://ftp.precisioninsight.com/pub/pi/XFCom/)
For those who want it, here's the <XF86Config>
file I've set up for my machine.
### 
Sound


I've been helping with the developemnt of a device driver for the ESS Maestro
2E sound system in the GoBook2. It works well on my laptop and is quite
functional. Although still in development, it is nearly complete and is
currently included with the 2.2 and 2.3 kernels. For more info, check out
my Maestro web page [here](m2e.html).
### 
PCMCIA


RH 6.2 has excellent support for PCMCIA. You'll find it works best with
some slight modifications to the /etc/pcmcia/config.opts file. I've included
mine [here](config.opts).
### 
Power Managment


It appears that Power Managment is enabled by default in the standard kernel
shipping with RH 6.2. APM works correctly on my GoBook2 without recompiling
the kernel. You will need to use Linuxconf to enable APMD which controls
sleep/wakeup etc.
### 
Modem


The GoBook2 comes with a 3Com/MHz 56K PCMCIA WinModem. As all informed
Linux users should know, most WinModems are not well supported by Linux,
so I ended up swapping this card for another I had which works just fine.
(For the curious, its a 3Com 3CXM056-BNW Noteworthy modem. I haven't seen
this sold anywhere - it came bundled with another machine I have.)
### 
Ethernet


Adding Ethernet access was painless. I bought a D-Link DE-660 for about
$50.00, fiddled with the PCMCIA (see above), plugged it in, configured
the interface in Linuxconf and it worked.
### 
IR


The GoBook has an IR port and the 2.2.x kernel has IRDA built in. After
some fiddling I've sent some data between the GoBook and my Palm III. Check
the excellent
[IRDA
Homepage](http://www.cs.uit.no/linux-irda/index.html) for more details.
### 
USB


A USB port is present on the GoBook, and USB drivers are under development
in the 2.3 kernel. Until this is in the stable kernel I haven't tried messing
with it.
### 
SCSI


I know, the GoBook doesn't have a SCSI port, but that can be fixed! I picked
up a Zip Card - a SCSI PCMCIA card that is sold by Iomega for use with
their Zip drives. It turns out to be a re-labled Adaptec 1460 which is
supported by the PCMCIA drivers. I was able to mount PC formatted Zip disks
with no fuss whatsoever, and I'm looking forward to trying out some other
peripherals I have laying about.
### 
HotKeys


The GoBook2 has a set of three HotKeys across the top of the keyboard.
Under Win98 these can be used to launch applications. I'd be interested
in writing a device driver for these, similar to that available for some
Toshiba models. If you have any info on the hardware behind these keys,
drop me a line.
[Return to Linux page.](linux.html)
##### 
**Last Updated**


:05/20/01
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)
  
 






