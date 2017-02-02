Title: Mount CloneZilla Image
Id: 6
Date: 2017-02-02 08:00
Author: aidanharris
Slug: mount-clonezilla-image
Status: published
HeadingTheme: light
HeadingIconFont: fa fa-hdd-o
BeforeHeading: &nbsp;

The contents of this article are taken from [blog.christosoft.de](http://blog.christosoft.de/2012/05/mount-clonezilla-image-to-restore-single-file-browse) which I'm referencing for future use.

<blockquote cite="http://blog.christosoft.de/2012/05/mount-clonezilla-image-to-restore-single-file-browse/" style="display: block;font-style: normal;letter-spacing: 0;font-weight: 400;font-size: 16px;margin: 0 auto;width: 75%;white-space: pre-wrap;">

<h3>Mount clonezilla image to restore single file (browse)</h3>

[Clonezilla](http://clonezilla.org/) is a fine tool to backup/restore/clone partitions or drives. It is very powerful, can handle both Linux and Windows partitions and so on. If you do not know it, you should really give it a try. It is really free software (open source), which means it is also free to use for commercial purposes.

By the way, if you want to backup/restore images of Windows partitions/drives, I’d also recommend [DriveImage XML](http://www.runtime.org/driveimage-xml.htm) which is also very powerful yet simple (only free for private use). Windows 7 has also built-in backup and imaging tools, which you can give a try. But this post is about Clonezilla.

One important feature that Clonezilla does not offer out of the box is browsing images to restore single files. You can only restore complete partitions or drives.

But there is a way around this, which is [discussed in this forum thread](http://ubuntuforums.org/showthread.php?t=872832), although not perfect as it requires lots of time and disk space as well.

The basic approach is to convert the whole image into a (probably huge) img-file that can be easily mounted. In the forum post linked above several different commands are discussed depending on your image file.
Here I’d like to show you what worked for me.

In my case, the file was compressed using gzip and it was an image of a linux partition (ext3). I used Ubuntu Linux to mount the image. The steps I took:

Install partclone (sudo apt-get install partclone)
Prepare an img-file somewhere where enough free disk space is available:

<div class="highlight"><pre><span></span><span class="highlight kd">touch</span>/dir-to-new-image/partition.img
</pre></div>

You should have at least as much free disk space as the size of the image there.
Convert the clonezilla-image into the img-file:

<div class="highlight"><pre><span></span><span class="hightlight kd">sudo cat</span> /dir-to-images/partition.ext3.ptcl-img.gz.*
<span class="o">|</span><span class="highlight kd" style="background: transparent;">sudo gzip</span>-d -c
<span class="o">|</span><span class="highlight kd" style="background: transparent;">sudo partclone.restore</span>-C -s - -O /dir-to-new-image/partition.img</pre></div>

(This is one line. Note the minus after -s. I overlooked it when I tried this first.)
This will take some time, dependent on how big the image and how fast your drive(s).
There are other commands in the forum thread for NTFS images and other compression formats.

Mount the img-file:

<div class="highlight"><pre><span></span><span class="highlight kd">sudo mount</span>-o loop -t ext3 /dir-to-new-image/partition.img /mnt</span>
</pre></div>

Thanks a lot to all posters of the forum mentioned above for these hints, especially bfitzhugh, nutria007, ttguy and gaebriel!

P.S.: It’s always good to have a (recent) backup 😉 One drive of mine just crashed after about two years in operation, so I know what I am talking about…

Think about what pain it would be if the drive of your laptop / desktop would crash just right now. If you get a bad feeling thinking about this, you should make a backup now.
</blockquote>

<hr/>

<em>NOTE: </em> In my case I had to use the excellent [testdisk](http://www.cgsecurity.org/wiki/TestDisk) to restore the NTFS boot sector. Without this the image wouldn't mount.
