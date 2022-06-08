FDLOG = Field Day Logging Program                    6/2006 A K Biocca

FDLOG is distributed under the GNU Public License

$Revision: 1.23 $

  This program is designed to support Amateur Radio Field Day Operations by 
providing a robust multiplatform networked distributed logging database and
information service.


Introduction

  This is a complete rewrite of W6AKB/WB6ZQZ's Field Day Logging program.
It is nearly 20 years old (in 2002), but this new version has many new
features, primary of which is the ability to synchronize the logfile database
across a network in a peer to peer fashion, avoiding single points of failure. 
The expectation is that a wireless network will be used.

  To run this program you will need to install Python. The
development was done on win2k under Python 2.2-2.7 and Tkinter, but it also
runs on Linux and the Mac with most features. Python is available
from www.python.org. There was a directly executable version of FDLog called
fdlogexe.zip. This is a larger download but it works without Python installed.
It only works in Windows. It has not been built in some years.

  Networking is required to use the data sync features of the program. A
broadcast is used, so stations on the same subnet running the program will
sync databases.  An authentication code is used, so only stations with the
same auth code will be able to share data.

  Setting up ad-hoc or peer-peer 802.11 networking is beyond the scope of this 
note. This should be done prior to running the logging software. Note that each
station does need a distinct hostname for proper database synchronization. See
the separate note on wireless networking.

  The computer's clock accuracy is important, so set it before starting the log 
program. This will reduce the amount of correction the internal time sync has
to compensate for. Designate one computer as the master timekeeper (and set
this in FDLog). Then all program time clocks will track that one.

  Getting the latest version of the program on Field Day will at our site is 
handled by a small web server on one of the development machines. Other files 
like Python and FD rules will be available there as well. See the Help/802.11 
note for details. Python 2.2 to 2.7 have been used successfully with the
software. It is NOT Python 3 compatible!

  Installing the FDLOG program is straightforward - all that is needed is a
directory with the files in it. The program will create database and log files
in this directory. Unpack the zipfile in the directory you have chosen. If you
want access to the Field Day rules (a menu item under help) download the ARRL
Field Day Rules package and rename it to 'fdrules.pdf' and add it to the dir.
Viewing pdf files requires Adobe Acrobat, available from www.adobe.com.
Launching the pdf file from Python may only work on win32 systems.
The index.htm file contains links to all the documentation as well, so
launching your web browser (double click on index.htm) provides
program-independent access to the docs.  
  The FDLOG program is launched by double-clicking on the fdlog.py icon in the 
directory. For convenience you may want to create a shortcut on the desktop.

  Starting the program the first time will ask a few questions as it sets up.

  Visit the help menu 'Help/Getting Started' for further instructions.

Thanks, Alan Biocca, W6AKB at ARRL.net

eof
