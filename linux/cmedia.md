



CMedia AC97 Codec




# CMedia AC97 Codec


In late 2002 I upgraded my main desktop system to an Athlon XP1700+ on an
ECS K7S5A motherboard. This mobo has on-board sound through the SIS 7012
audio dma device built into the southbridge and a CMedia CMI9738 AC97 codec.

At the time I was running RedHat Linux 7.3 and the conversion
was seamless - I didn't have to make any changes to the OS other than to
allow Kudzu to detect the new hardware and enable it. The SIS 7012 audio
works well with the i810\_audio kernel driver. The CMI9738 codec, while not
explicitly supported by the ac97\_codec did function using the default
settings.

Recently, prompted by a hard drive crash, I upgraded to RH9. Again,
everything was working fine with the original kernel which shipped with RH9
(kernel-2.4.20-8). However, when RedHat Network pushed kernel 2.4.20-18.1
on me, my audio stopped working.

I went on a hunt and tracked the bug down to a change that Alan Cox had
made in his linux-2.4.21pre5-ac1 patch. He added explicit support for the
CMedia codecs, and noticing that they had non-functional PCM volume controls
added some code to disable the non-functioning registers in the OSS mixer
driver. This has the unintentional side-effect of disabling access to the
mute control for the PCM channel which prevents the driver (and userspace
applications as well) from un-muting the PCM. Hence, no sound.

I notified Alan and RedHat of the problem through Bugzilla (see entry
[97018](https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=97018))
and it is being addressed, but the bug also worked it's way into the official
kernel 2.4.21 before being caught. I've created a patch against 2.4.21 to
fix this bug, and if you're experiencing trouble with your CMedia-based audio
when running Linux kernel 2.4.21, you may want to try this patch to fix it.

### Update (02/11/04)


This bug was patched in kernel 2.4.22 and is back-ported to RedHat kernels
newer than 2.4.20-19.9. Please use these kernels if possible and patch only
if you cannot upgrade.

### Download


  

For 2.4.21 kernels: <cmedia-patch.2.4.21.gz>.
Please let me know if this is useful for you. 


[Return to Linux page.](linux.html)
##### 
**Last Updated**


:02/11/04
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)












