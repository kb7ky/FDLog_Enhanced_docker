# fdlog.py Copyright Alan K Biocca (W6AKB) www.fdlog.info

print "\nHigh Sierra Field Day Log Program\n"

prog = "FDLog v4-1-154c-dev 2016/07 distributed under the GNU Public License\n"\
       "  Copyright 2002-2017 by Alan Biocca (W6AKB) (www.fdlog.info)\n"

print prog,

about = """

FDLog = Field Day Log Program (www.fdlog.info)
  Distributed Synchronized Database Log System

Copyright by Alan.Biocca@gmail.com (W6AKB, formerly WB6ZQZ)
  High Sierra Field Day Group www.hsfdg.org
  Rewritten to Python/Tkinter 2.7 (not 3.x)

"""

# Current Problems, Issues and Plans
#
# mike found that in vhf mode changing callsign case doesn't get considered
#   to be a dup, also happens in fd mode
#
# need to update the installer to pick up key items from the files tree
#
# update is occasionally throwing a disk i/o error in tkinter callback,
#   around update/updateqct/adjust/put, may be dropbox related
#   have not seen this bug for a long time now in 6/2016
#
# qso/data broadcasts do not seem to be received, they are always fixed
#   by 'fills' afterward so not noticed, except when filling is broken
#   low priority since it works anyway, but good to fix
#
# testq seems to be sending both q broadcasts and status broadcasts for each q
#   but the broadcasts don't seem to fill the log for some reason
#   would rather it didn't send the broadcasts
#   but since it does why don't they enter the log?)
#
# the new 6/2016 complex callsigns don't dup check correctly
#
# udp occasionally lethargic, packets missing unexpectedly
#
# on Mac adding participants doesn't add them to pulldown (only on wa6fxp's mac?)
#
# qso broadcasts rcvd may not be getting to database (maybe)
#
# .ba command not showing stations on the bands (improving in 4-1-152)(fixed?)
#
# would be nice to discard the poor large status updates for time when possible
#
# debug rapid repeat of fills and broadcasts not making database
#
# make short status packets have better time levels
# have nodes with better time send short status packets, and a little more often
#   this is already done but more improvement in time logic should be considered
#
# might want option flag on bells to enable/disable
#
# edit save dialog has lots of diagnostic printing left in


# Version Numbering
#
#   FDLog-<major>-<minor>-<release>-<type>
#   and release is monotonic integer, increased when released or checkpointed
#   release may be optionally followed by single letter for finer control
#   and major and minor are manually managed
#   minor is for protocol changes, and other significant changes
#   type is for dev, beta, rc, release as needed to clarify the status
#   note this does not affect files, fdlog.py is still the executable
#
# Major Versions
#
#   1 Bilofsky small C version 1984 (CP/M) (H89 single user w/CW,
#       then 3 terminal multiuser w/o CW) (written by Alan WB6ZQZ)
#   2 OS9 port (multiuser) (ported by Eric WD6CMU)
#       RS232 through the forest via haywired power cords...
#   3 MSDos port (single user) (ported by Steve KA6S, WD6CMU et al?)
#       (who all worked on this?)
#   4 Complete rewrite to Python/Tkinter 2.2-2.7 2002-2016 (networked)
#       (by Alan WB6ZQZ who changed callsigns to W6AKB)
#   5 Future major restructuring - Python 3 / Qt rewrite, coming soon...
#
# Release Log follows, then code, then the Suggestion List and Code Parking
#
#
release_log = """\

4-1-154c-dev 6/2017

    7/2016
    Major comment and commented out material purge, almost 600 lines deleted
    Note - development is taking place on Python 2.7.11 (Python 2.7 support ending mid 2020)
    12/2016
    Added code to ignore shift key message 65505
    6/2017
    TimeSync Bug noted by Mike and Glenn on VHF contest recently - clock sync failing.
    Actually it is diverging when there is no GPS FD Clock and when .timeok is not set.
    The time master is apparently chasing itself. This bug is also in recent versions,
    perhaps all starting with 152j (fd clock support). The 152i version seemed to work.
    Found the timesync bug. Workaround is on time master set ".timeok 1". or use FD GPS Clock.
    But note that 154a and 154b are not searching for the GPS clock (testing speedup).
    Re-enable searching for GPS clock in this 154c version.
    Fixed TimeSync Bug. Don't allow time master to adjust its clock unless it has GPS FD Clock
    or timeok is set. If neither, then time master (tmast) just leaves its time offset
    and uses it. So if GPS goes offline, it will continue to use the time offset it
    already has developed, which is as close to GPS time as is available at that point.
    developing using Python 2.7.11

4-1-154b-dev bb873b 7/19/2016

    2016-7-19 20:32:26
    Program: fdlog.py 262182 4071 bb873b e8bc8746200e2a052e5198d200bb873b
    Archive: fdlog154b-dev.zip 97656 d0d880 b29ce3b488021df6dcc09a40ebd0d880

    Bug found in 154b - fdclock searching is disabled, line 1582 is a return that skips the checking,
    comment it out to enable fdclock searching. This was used to speed up testing, but was accidentally
    left in on the development release. No downside for users unless they have a FD GPS Clock,
    which is based on a Teensy CPU and a GPS receiver. See the separate project for further info.

    Bugfix, rover contacts were being filtered out, now fixed
    Requirements Bug: /R needed to be logged/in Cabrillo output, fixed
    Now VHF contest Grid is a separate item (not part of callsign), and can be before or after callsign
    Callsign can have /r for rover, but the program doesn't look at whether /r is used or not when
      doing dup checks, all stations are dup checked as if they are rovers, and the source is
      assumed to NOT be a rover

4-1-154a-dev e24448 7/19/2016

    2016-7-19 11:20:40
    Program: fdlog.py 260386 4063 e24448 28278eb0609fef72048bbbd345e24448
    Archive: fdlog154a-dev.zip 97109 ca649b e7e8ab2933a09ab4831b73f194ca649b

    NOTE temporarily disabled gps clock searching to speedup testing, restore later
    
    Major Changes this version!
    
    Indicator "RCVP FAIL" changed to "STANDALONE"
    Added Docs menu, dynamically built from what it finds in ../files
    Added key decoding for arrow keys (not used yet, for future)
    Fixed a bug in the Time Zone Conversion Chart, Mountain Time was omitted
    
    Field Day Reporting Improved
        Added Solar power
        Added Wind power
        Added Educational Activity bonus
        Added Social Media bonus
        Added Safety Officer bonus
    
    Moved wireless_net.txt, NTS example, Frequencies list, etc to the files folder
        these are picked up by the new Docs menu (packager will need fixing)

    V4 out of order input parser installed
        includes forcing time and grid square parsing with VHF/FD modes
    Starting to add VHF contest back in
    Major re-ordering of code to get things in the proper order, or at least better
    Contest mode added to startup dialog, contst switch removed from db
    Documentation adjusted for this new location of the contest selection
    VHF/UHF/etc bands added via a new vhfBands.dat file that can be edited
        to adjust the band buttons and log labelling
    Changed call parsing .xprefix to .aprefix (ancillary prefix for complex callsigns)
    Struggling with the new syntax for VHF:
        reverting to wa6zty/cm98 format
        call grid comment (future)
        grid call comment (future)
        order not important aside from comment (future)
        extended calls should work (prepended with ")
        regular calls allow /cm98 postfixes
    Parser now checking ARRL section letter by letter for correctness
    FD Parser now allows regular calls to have postfixes /...
    Force Date works, prefix :dd.hhmm ... to force time in for paper logs
    Shortened 1.25cm VHF band to 1.25c to avoid problems with log and editing Q's
    VHF Contest seems to be working in terms of logging, dup checking and generating
      the proper Cabrillo file.
    Fixed bug allowing separate phone and cw contacts per band.
    Title Bar Adjusted for VHF Contest
    Filtered reporting to drop the FD related items
    Commented out qparse as it is no longer used
    Commented out ooiParser V3 as it is no longer used
    VHF Scoring now working
    Packager adjusted for file reduction, but not for new shape, for now it
      will ignore the files outside the fdlog folder
    Fixed editor recognizing VHF bands problem
    Filter out mode in cleanlog to drop dup contacts on same band but different modes
      These are already prevented by dupck, but if any get into the journal they
      are filtered out and one is quietly ignored by cleanlog, that is used
      to drive scoring and Cabrillo / ADIF outputs


    As I work on this code it becomes increasingly clear that it is time for a rewrite
    It is also Python's intention to stop support of 2.7 in less than 4 years (around mid 2020).
    So after these bugfixes I think it is time to stop updating FDLog in 2.7 and pause
    for a complete rewrite with Python 3 and Qt. No major new functionality in
    FDLog after this parser replacement, unless it is to test out components being
    built for the new logger.

4-1-153d-beta 57c6e9 6/2016

    2016-6-28 15:20:23
    Program: fdlog.py 227450 3860 57c6e9 0fae364fd54db0374771825c2c57c6e9
    Archive: fdlog153d-beta.zip 92185 ca8bdd 5e656fb5a9c687df022215e2fbca8bdd

    This version has very minor changes after Field Day 2016 usage
    with 153c-beta:
    Fixed space after contact info but empty comment preventing logging
    Also fixed spaces in comment causing repeat log lookups
    Adding packager log info comments below
    Adding results from using on FD 2016 comments below

    This version published at www.FDLog.info
    
4-1-153c-beta fcd66a 6/2016

    New Packager Log Info:
        2016-6-21 13:12:43
        Program: fdlog.py 225302 3824 fcd66a 5276c6bba07d5d4afbc3cc335dfcd66a
        Archive: fdlog153c-beta.zip 91336 ba1d83 516711b9a59055798a4156c5feba1d83

    Packager Log Info Format:
        date time (local)
        Program: filename bytes linesOfCode short, full fingerprint
        Archive: filename bytes short, full fingerprint

    Exit button (upper right corner) in startup dialog box now quits FDLog
        entirely rather than just quitting the box and then starting FDLog.
        This protects against bad data in the input fields as well as reducing
        confusion about the meaning of the exit button.
        Fixed the packager to move the completed zipfile to the enclosing dir

    153c-beta was used on FD 2016 by the High Sierra FD Group
        No major problems
        Time master failed to sync with gps clock, probably started too fast,
            restarting fixed it. Clock/time code should be revisited.
        Program hung once on 2.7.8 python on time master / station logging machine,
            restarted fine.
        MikeF's netbook got a database error the next morning when he worked Q's after
            the net was shut down. Copying his folder to another machine
            (my i7 w newer Python),
            it worked just fine. Might by related to 2.7.8 Python.
        One minor bug noted, typing a space after all info (leading into a
            comment, but with no comment) prevents return being used, need to
            either type a comment character or back out of the space to log the Q.
            This was fixed in 'd'.

    This version published at www.FDLog.info
    
4-1-153b-beta 6/20/2016

    2016-6-20 22:42:6
    Program: fdlog.py 223943 3807 333487 a8e0a2e1a044e19c0150f85543333487
    Archive: fdlog153b-beta.zip 90811 541a6a 7c2b30bfcf870c0846f6a7b8e8541a6a

    Added Graphical Startup Dialog Box
    Time Master dialog message fixed, master node id was checked too early
    Documentation cleaned up for new GUI box and other minor items
    Changed .ba node info title from min ago to seconds
    Fixed vhf cabrillo splitting on '/' to be more reliable
    Skip vhf cabrillo output unless contest is vhf 
    Time on Band in title bar shortened to TimeOnBand
    Made a cleanup pass through the manual (which is in this file)
    Made .ba report to separate window instead of diagnostic window
    Added Complex Call entry info to the manual
    Added version number to root window title
    Cleaned up packager and added lines of code to log
        lines of code counts lines with code or text, not blank or comment only
        about 3750 lines of code at this time, out of 5708 total

4-1-153a-beta 6/2016

    2016-6-18 22:57:40
    Program fdlog.py 219040 a8341c be29cfc641d85b075a49961de5a8341c
    Archive: fdlog153a-beta.zip 88751 4e02c1 f9ab3586a1b81c3a5da284d4064e02c1

    Fixed bug in new packager, have it move the zipfile to the parent dir
    Added help/FDLog Version (info was already in help/FDLog Release Log)

4-1-153-beta 6/2016

    Packager changes had problems, didn't release

    Disabled most new diagnostic printing (still some left in edit)

    Getting ready for Field Day 2016

    Armored ival against improper types, should fix the occasional .ba
    error that might be related to editing

    Clipped log power level print field to 4 chars to avoid edit problems.
    This doesn't affect the real database but does make the 'n' for natural
    power disappear on 1000W stations, which should not be common. :)

    Packager.py upgraded to fingerprint both fdlog.py and the zip archive
    also makes a logfile
    and avoids re-using the version
    and gets the version from the sourcefile prog = line
    dowrite flag added for testing
        packager.py broken by using ../ in the path

    Inspected all print statements looking for debug remainders
    only ones noted are in edit Q submit, left those alone, rarely used

    Note that FDLog is looking for a file called 'bands.pdf' for the ARRL
    band chart. This must be downloaded from ARRL and renamed and placed
    in the FDLog directory for this help menu item to work.

4-1-152n-dev 83af07 6/16/2016

    Added validation of ARRL Section abbreviations using section data file

    Added extended callsign parsing prefaced with " (doublequote)
        It doesn't dupcheck quite right, but logs ok

    Fixed many bugs

    Disabled much of the testing diagnostic printing

4-1-152m-dev 936e1c 6/16/2016

    Fixed two bugs in parsing

    In program fingerprint display now shows long and short versions
        the short version is in the version line above
        after that version releases (cannot put in same version
        as this would not converge :)
        Also fingerprints are kept in Hg and in Evernote notes

    Built in Getting Started text updated, cleaned up, and some
    info on Out of Order Entry was added

    Imported 2014 152 "it" changes for controlling GPS FDClock debug mode
        .gpsclock [0-1]
        Note that due to bug in GPSClock code may need to do a .gpsclock command
        twice to clean the display

4-1-152k 1f2e1c 6/15/2016

    Added Out of Order Input (new parser)

    The first FOUR Input Elements can be in ANY ORDER
        Call Prefix
        Call Suffix
        Field Day Class
        Section (MUST be prefaced with ';' if before callsign)

    The comment can only be entered after all other fields:
        Comment (always last)

    Spaces are normally entered after each field except the call prefix.
    The Suffix may directly follow the Call Prefix. Or a Call Suffix
    may be entered without prefix which triggers Quick DUP that displays
    calls matching the suffix on this Band/Mode. Entering a Prefix and
    then a Space brings in the previously entered Suffix.

    This breaks VHF contest, and postfix (/r). This will be fixed later.
    Use version 'j' for now.

    .set ckslew 10-500 mS/S time correction slew rate limit

    section spelling correction attempt parked
    added a column to section data file with corrected abbreviation
    (primarily for alias entries) this is not working well, going to
    leave the bits around but they are presently commented out

    FDLog GPS Clock time used directly for time broadcasts if available
    very prompt time to network broadcast

    New Time Levels
    0 Master with GPS
    1 Non Master with GPS
    2 Master without GPS
    3 Locked to 0
    ...

    limited class integer to 39

4-1-152j 7a63e8 5/2014

    added 900 to .band command
    added .timeok to .h help command
    added ? help note to startup
    compacted startup lines on GUI
    adjusted comments
    added signature to console QSTs -logger
    display UDP and TCP ports (only showed UDP before and didn't note protocol)

    This version published at www.FDLog.info
    
4-1-152i 9738da

    added QST bells (noise) and copy to console
    this was used in FD2014 (also an 'it' version used)

    This version published at www.FDLog.info
    
4-1-152h 62169f

    made a new packaging program (packager.py), added fingerprinting to it
    reduced writes of offset to database
    added more info at shutdown time, directed user to close console after app finishes
    added more delays during shutdown
    tightened tdwin default to 5 (even over internet 2 is enough)
    added os exit call after shutdown to clear dangling items

4-1-152g 146e5 2014

    preparing for FD2014, shared this version to HSFDG for testing 5/26
    added W6AKB's GPS Station Clock
      this is a GPS with PPS, a Teensy2 with USB, a ChronoDot and some displays
      design and PC boards will be available
      it delives millisecond accurate time via USB
      and provides readouts of UTC and Local Time on several displays
      FDLog searches the first 20 COM channels for it
        if either there is no serial library or it doesn't find it
        the GPS Clock it gives up
        FDLot will only use the GPS Clock time when locked to GPS
    separated time master from how the station gets time
      only one master, it advertises level 0
        set by .set tmast <nodeid> as before
        regardless of how the master node gets time
        master node sends time only status broadcasts at 1hz
      if a station is not master and has a GPS clock it can advertise level 1
      if a station has a defined accurate clock it can advertise 2
        turn on with .timeok 1, off with .timeok 0, stored in local database
      stations add 3 to their source to report their own time level
    added defined accurate time flag for each station (.timeok 0/1)
      indicates system time is accurate (and offset is zero)
      stored in local database like operator, logger, power, debug
      smoothly transitions to offset zero
    add gps clock flag for each station (did auto find instead)
      drives local offset from gps clock readings
    it doesn't make sense to have both as this would drive
      the offset to zero and to a value...
      so one must take priority over the other
      the gps clock takes priority since it is verifiable..
      then drops to timeok if true and gps clock not locked
    time master now sends out time-only broadcasts at 1hz
      in addition to the usual 10 second full info status broadcast
    fixed startup clock offset read from database (old bug fixed)
    makes smooth transition between modes (offset transitions at most 0.1s per second


4-1-152f added 900mhz

    added 900 to .ba command
    band command titles fixed
    comments updated
    probably FD2013 version (for many to most stations)

4-1-152e vhf cabrillo output 5/30/2013

    making ba command smarter, filtering for newest info on each station
    limit age growth on info to 999 min (999 minutes old max)
    .ba command shows time since last Q (tslq) in minutes instead of time of last Q (tmlq)
    .ba command tslq now in hhmm units
    added cabrillo for vhf contest to saved entry file
    added .set grid <grid> for 4 character grid entry

4-1-152d port change and cleanup 5/2013

    changed shutting down comment
    edited other comments
    added startup info about remote mode capable
    fixing date
    note that dates on version line were 2013/05/12, forgot to edit that
    .ba command formatting improved and information filtered
    changed to tcp port 5100 (yahoo webcam) to be compatible with work firewall
    changed indicatoron in band buttons to 1 which changes look but works better on mac
    detected os.name and made indicatoron for posix os (mac and likely linux)

4-1-152c minor cleanup 5/2013

    made storing globals to database automatic when commands processed
    made shutdown closing socket activity ignore exceptions
    clock tracking is jumping
      slowing clock slew to 0.1s/s
      target half the error each 30 seconds (instead of all)

4-1-152b clock slewing 5/2013

    fixed clock slew (was frozen)
    added fingerprint

4-1-152a remote TCP beta 5/2013

    adding TCP remote synchronization in this version.
    cleaning out old remote sync code
    changing threads to use threading library (slightly higher level)
    reinstated rem_adr and added flags for tcp server and client
    replacing and rewriting network sections to add TCP
    updated to ADIF 2.27
    added countdown to testQ reports
    filtered response of RCVP FAIL (STANDALONE) as it would flicker in some cases
      when there was no problem
    added "NET OK" when GOTA Q's are zero
    adapted versioning in messages to new scheme (broken since after x.y versions)
    improving .ba command
    problems with utf strings, sockets traced to sqlite unicode, useful article:
      http://stackoverflow.com/questions/2392732/sqlite-python-unicode-and-non-utf-data
    problems with windows firewall, make sure python is allowed
    broadcasts working over tcp
    filling working over tcp, slowed it from 10hz to 5hz to reduce repeats
    added fingerprint function to output md5 hexdigest of fdlog.py at startup
    changed to use real 'from' address for fills to avoid NAT issues
    testing progress thanks to W6AKB and N6OI:
      1-146, 1-149, 4-152a FDLog versions with python 2.6 and 2.7, UDP and TCP
      up to 4 stations at once
      FDGroup testing further
      one problem noted on Mac by RichF, adding participants doesn't add to pulldown
        not reproduced on w6akb mac

4-1-151 more sqlite beta 5/12/2013

    make database fdlog.sq3 for global value storage (replacing textfile)
    store time offset in global database so a restart doesn't jump the time
    added in memory cache for global database to reduce file i/o
    changing build to release, only increments when
      released to others or checkpointed
    added code to ignore short w1aw file placeholder in scoring final entry
    changed FDLOG to FDLog
    various general tidying up (minor)
    changed (c) to Copyright since (c) is not legal
    commented out remote UDP broadcast code (unfinished code)
    considering putting in remote TCP code instead - soon

4-1-150 sqlite beta 2013/05/11 database upgrade

    adding sqlite log database (keeping text file journal, but db is primary)
    conforming to proposed new version numbering system

1-149-02 2011/07/11 bug fix

    allow lowercase contest names
    added 900 mhz to editing validation
    note that report requires 4 chars in editor to save
    editor shows unvalidated fields in yellow after save attempt
    edit dialog box disappears on successful save, else stays with yellow
    fields that need fixing.
    note that this version is not reporting version number in the
      status packets correctly, shows up as 'v' with no value
      likely has been this way since 1.147 due to old regexp

1-149 2011/07/02 contest set version

    adding .set contst menu for (FD,VHF)
        set global to contest type .set contst FD|VHF
        adjust dup check to call for FD, and include /<grid> for VHF
    adjust bands for VHF, include 900, (drop below 6m?)
        dropping bands is tricky, leave for later.
        did add 900 band however

    setup for mercurial, opened Google Code project

1-148vf 2011/06/25 fd version

    commented out VHF code but kept other changes for 2011 fday

1-148v 2010/08/18 vhf version

    dup checking includes call/grid
    call column widened by 1 char to handle additional width
    still need to enter something in the report, such as signal strength
    fixed some small bugs in log color and editing due to dependence
    on data in the scrollbox. May be only one line change to
    make compatible with standard Field Day.

    q just needs call/grid & band (use same mode for all Qs)
    got it to work.
    added a column to make call/grid fit
    fixed a few bugs
    newline on log missing, added it, later removed again

    now two bugs. (fixed)
    local log color=blue not working
    - always black
    edit left mouse click for edit on log not working
    - probably getting error at some point and killing that thread/window
    - problem was two functions that pick up chars from msg buffer
    - adjust them by 1 char, worked

    note that python is complaining about md5 and using hashlib instead.
    snap 9, release 3 at this point

    also after space input didn't echo call with full grid. Fixed.
    converted from md5 library to hashlib. done.
    snap 10 release 4

    made call box in edit dig wider to accommodate 11 char call/grid
    added code to disallow editing another node's Qs
    after changing node id and restarting the q's still came up blue? bug?
    test code was still in. fixed.
    snap 11

    comment cleanup. added more notes detail.


1.147 2009/06/20 pre fd (used on FD 2009,2010)

    changed GOTA Q limit from 400 to 500
    demo modes commented out
    80 meter cw frequency for w1aw changed (w1aw.txt)

    qrp 5W from mains or generator has a multiplier 2 - same as 150W.
        This is not scored properly by the program yet.
    max of 20 transmitters is not enforced by the program
    educational activity is not scored by the program.
    complex GOTA bonus points are not handled by the program

1.146B has GOTA call fixed. 6/15/2008 AKB
        gcall will accept a proper call with number, somewhere prior to this
        the number part of the regex got lost. This affects log output.

Revision 1.146  2006/06/11 22:00:57  Alan Biocca
    Documentation - minor cleanup.
    Setup - added web push dir support. (also upload)
    TimeSync - new program derived from Eric's that syncs system time from GPS.

Revision 1.145  2005/09/12 03:41:23  Alan Biocca
    Minor Comment Edits

Revision 1.144  2005/09/12 03:17:11  Alan Biocca
    Added Q Edit Dialog Box. Major Effort

Revision 1.143  2005/07/06 17:26:13  Alan Biocca
    Added Time Zone Chart

Revision 1.142  2005/07/01 12:58:56  Alan Biocca
    Documentation updated, minor edits to prog comments.

Revision 1.141  2005/07/01 05:13:03  Alan Biocca
    Log autolookups added
    Displays log lines matching the current call when duplicates found,
    or by typing in <call><return>
    This shows the info for this callsign collected on the other bands
    Stubbed in the beginnings of the .edit command

Revision 1.140  2005/06/29 22:44:48  Alan Biocca
    Color log text from this node
    Restrict node to lowercase

Revision 1.139  2005/06/29 20:22:56  Alan Biocca
    Youth updated to take 1-2 digits
    Fixing case on set variables like callsigns initials etc

Revision 1.138  2005/06/28 16:25:09  Alan Biocca
    Adjusted Add Participant dialog box.

Revision 1.137  2005/06/28 16:22:06  Alan Biocca
    Add participants case problem fixed
    Added synonyms for ARRL sections for WAS

Revision 1.136  2005/06/26 19:01:10  Alan Biocca
    Fixed time level display. 3500 lines now.
    I ran this version FD 2005 on one node (changed during).

Revision 1.135  2005/06/19 03:44:56  Alan Biocca
    Minor changes to message in fdlog.
    Major upgrades to group_plan.
    Minor updates to group_handbook.

Revision 1.134  2005/06/17 23:56:23  Alan Biocca
    Preparing for 2005-1 release.
    This version used on FD 2005.

Revision 1.133  2005/06/17 23:24:32  Alan Biocca
    Updates to accomodate ARRL rule changes over the past couple of years
    including GOTA, new bonuses, etc. Minor other cleanup. No substantive
    changes.

Revision 1.132  2005/06/13 23:45:20  Alan Biocca
    Fixed power type-in bug (text vs number).
    Changed power var to keep it a string at all times to fix typed-in power
    anomalies. Improved the Add Participants dialog box.
    Moved to new laptop.

Revision 1.131  2004/07/05 18:48:43 akbiocca
    prep for release to web.

Revision log redux - Thinning.

Revision 1.130  2004/07/05 04:15:58  akbiocca
    Time Synch added. Clients track master node. Designate with .set tmast <node>

Revision 1.128  2004/06/29 23:52:43  akbiocca
    Plans for time sync made. some vars defined. minor misc cleanup.

Revision 1.127  2004/06/29 15:51:13  akbiocca
    Natural power bug fixed. My val() function is apparently a subtle problem
    but only in the tkinter case. Perhaps a conflict with TCL? Changed my func
    to ival().

Revision 1.126  2004/06/28 18:42:56  akbiocca
    Comments from FD 2004 added.

Revision 1.125  2004/06/14 02:13:12  akbiocca
    added seed to authkey. updated group handbook. Used for FD 2004

Revision 1.124  2004/06/13 15:19:52  akbiocca
    improving documentation on reporting. fixed power command updating screen.
    some testing. no substantive changes.

Revision 1.122  2004/06/10 20:42:46  akbiocca
    adjusting messages. testing.

Revision 1.121  2004/06/10 03:39:38  akbiocca
    including c.bat and setup.py for the py2exe config. updated handbook.
    minor edits elsewhere.

Revision 1.120  2004/06/10 02:37:24  akbiocca
    Setup for py2exe, which appears to work.

Revision 1.119  2004/06/09 18:15:53  akbiocca
    Added GPL. minor doc edits.

Revision 1.118  2004/06/09 16:38:54  akbiocca
    renaming group files. fdlog startup improvement continues. documentation
    cleanup continues. testing continues, is partial at this time. no substantive
    changes have been made.

Revision 1.116  2004/06/09 02:59:21  akbiocca
    checkpoint. fdlog startup altered to be more interactive, straightforward.
    testing minimal at this point, but changes not fundamental. text files
    edited for some 2004 info, but not final.

Revision 1.115  2003/07/20 21:39:15  akbiocca
    WAS Logic improved to handle can, dx. This likely vsn for 2003 submittal.

Revision 1.114  2003/07/19 05:39:43  akbiocca
    Improved Worked All States display. Fixed bug in Vermont.

Revision 1.113  2003/07/18 21:37:55  akbiocca
    Updating old comments, removing some old code. Improvement in recognizing
    worked all states. Improving report for FD Entry. Partially tested.

Revision 1.112  2003/07/17 05:26:22  akbiocca
    WAS rpt added to fd log.

Revision 1.111  2003/07/16 14:08:20  akbiocca
    Changed text inputs such as w1aw message, nts messages, etc to 'file input'.
    These fixed filenames are searched for and if existing they are included
    in the FD report.

    w1aw_msg.txt
    nts_msg.txt
    nts_rly0.txt to nts_rly9.txt (one msg per file)
    soapbox.txt
    media.txt

    Added example of nts messages in nts_eg.txt to copy and modify.

Revision 1.110  2003/07/15 03:55:06  akbiocca
    Linux improvement. Changed font calcs. Linux needs about size 20,
    Windoze 10. Changed grid argument col to column for increased
    portability. This after FD03, previous vsn was used for FD03.

Revision 1.109  2003/06/22 17:13:27  akbiocca
    Updated for 2003. Authkey sets data filename and port. Used for FD 2003.

Revision 1.108  2003/06/10 13:49:54  akbiocca
    Prep for FD 2003. GOTA bonus changed. Class F added. Untested.

Revision 1.107  2002/06/22 07:01:13  akbiocca
    Rich found bug in socket addr list. Tested partially w Mac, Sony laptops.

Revision 1.106  2002/06/15 16:11:21  akbiocca
    checkpoint. minor changes to prog, plan, handbook. moved manuals to
    subdir. make this beta 6.

Revision 1.105  2002/05/28 13:36:50  akbiocca
    fdlog fixes to help buttonsize. adding remote bcast (incomplete?).
    changed station to node.. prog seems to run, not well tested.

Revision 1.103  2002/05/13 12:23:46  akbiocca
    small mods to handbook & plan.
    addded grid.sticky=NSEW to all buttons hoping to fix the mac.

Revision 1.102  2002/05/12 22:29:25  akbiocca
    updated group plan with meeting info. first draft.
    update group handbook.
    updated program somewhat. chop print fields that were overflowing.
    improved parsing to reject some bad calls. fixed .h command triggering
    on kh6 callsigns. changed a lot of re.search to re.match calls.
    started to work on internet test feature, not complete.
    this version not significantly tested, but probably works.

Revision 1.101  2002/05/11 03:17:00  akbiocca
    Eric fixed linux fail to bcast. Prelim tests on Linux passed. Win2k tested.
    This was Beta 5, tested at the FD 2002 mtg.

Revision 1.99  2002/05/09 05:01:54  akbiocca
    testing. fixed bug w power on first startup. cleaned comments.
    tested w 2 stations wireless. ok so far. fixed site info typo.

Revision 1.97  2002/05/08 13:55:52  akbiocca
    op, log pulldowns. fixed global sets. testing not complete. docn upgraded.
    cleaned up data handling. lots of code commented out in cleanup, will be
    deleted soon. changed to initials for op, log. added space to other column.
    added dialog for adding participants. power select menu and entry w check
    for natural. converted stub view funcs to lambdas. added online equipment
    manuals, 746 and pro. upgraded site info file.

Revision 1.95  2002/04/23 03:30:04  akbiocca
    added ARRL band plan in help menu.

Revision 1.94  2002/04/22 14:51:52  akbiocca
    lots of edits. reorganized revision history, made a menu to display it.
    added equipment help submenu. reorg help menu. reorg and update of much
    of the doc'n. not complete. expanded site info. added access point to
    wireless doc. added root window titles to subwindows.

Revision 1.93  2002/04/21 08:33:30  akbiocca
    dialog + wasrpt cleanup. sfx report improved.

Revision 1.92  2002/04/20 22:36:34  akbiocca
    added Worked All States Report. measures progress to worked all states.
    requires correct abbreviations to be used for ARRL sections.

Revision 1.91  2002/04/19 03:41:30  akbiocca
    added a few files. propagation, site info, nts manual. cleaned up docs
    regarding control-c and control-z. note that the new text files need
    a bit of work, they are frameworks at this time.

Revision 1.90  2002/04/19 03:16:16  akbiocca
    added python web help menu item. disabled control-c,z (suggested by Weo WN6I).
    added set cursor on mouse-1-up to keep it where it belongs.

Revision 1.86  2002/04/17 12:47:06  akbiocca
    improved time on band accuracy. cleanup.

Revision 1.85  2002/04/15 12:38:34  akbiocca
    added time on band indicator in root title bar.

Revision 1.84  2002/04/15 12:09:30  akbiocca
    view text boxes made resizable, and independent (not transient).
    this allows them to be iconified and not on top.

Revision 1.83  2002/04/15 05:28:30  akbiocca
    made main window resizable.

Revision 1.82  2002/04/15 00:30:58  akbiocca
    release prep beta 4. tagged beta 4.

Revision 1.81  2002/04/14 21:26:26  akbiocca
    added bands.pdf, imported group_handbook.txt.

Revision 1.80  2002/04/14 18:46:41  akbiocca
    w1aw schedule added.
    improved set command help.

Revision 1.79  2002/04/14 16:53:29  akbiocca
    changed to UTC time.

Revision 1.78  2002/04/14 15:42:15  akbiocca
    added .testq test qso generator.

Revision 1.75  2002/04/14 02:21:54  akbiocca
    fixed bug in delete, present in beta 3.
    added more .set commands.

Revision 1.74  2002/04/13 20:32:11  akbiocca
    .set commands added. global data sharing, load/reloading.

Revision 1.73  2002/04/13 13:50:47  akbiocca
    prep for beta-3. (Tagged Beta-3)

Revision 1.71  2002/04/12 17:16:39  akbiocca
    fixed bug in qst to allow question mark in char set there without
    triggering help. improved age out message to include both from and
    station the info is about.

Revision 1.70  2002/04/12 13:17:55  akbiocca
    qst messaging working, added to docn, qst log report added.

Revision 1.67  2002/04/12 03:21:19  akbiocca
    improved net error indicators. working fairly well.

Revision 1.66  2002/04/11 13:51:39  akbiocca
    added logs menu w per band/mode filtering.

Revision 1.64  2002/04/11 05:39:19  akbiocca
    changed to age timeout of band data. pkt struct chgd slightly.

Revision 1.62  2002/04/09 23:37:02  akbiocca
    added need fill message on CW/D button when fill list length is nonzero.
    this and the NO PKTS indicators are on a 10 second update cycle.

Revision 1.57  2002/04/08 14:22:54  akbiocca
    included about and getting started into the prog file. plan is to keep
    the program self contained in one file for basic minimal doc'n and
    executable in one file. added cvs log into source. improved root title

1.56 redup on sta chg. getting good!

1.54 band buttons hooked to real data. chg station goes to band off
     exits set band off

1.52 exit button cleans up, launches pdf arrl rules (prob only win32)
     most help menus work. properties made larger. single property diags
     added many text doc files. band button array

1.49 win vsn working, property dialogs working. tk continues.

1.46 tk integration begins..

1.44 contest entry to file. effort est 10d. 1500 lines. beta-2?

1.41 many changes. wireless tested. fd entry report output in work
     mac/unix port changes started. dup reports. 1500 lines

1.30 fixed start date conflict in comments. dug out 1984 start date!
     mv todo, etc to notes.txt file. approx 7 days effort in. 915 lines

1.8  sped up fill and rcvr threads
     rcvr blocked on read - no delay. filling works fast now
     debug mode slows fill requestor, otherwist fills at 10hz
     fixed propagation of broadcast info. works fairly well..

1.4  (in cvs) net sync works! approx 5 days fte effort so far

1.1  2002/03/18 23:35:15  akbiocca
     Initial revision (to CVS)

-------------------------------------------------------------

Program Early History (Pre-CVS)

Re-coding started 3/6/2002 Alan K Biocca WB6ZQZ (wb6zqz@arrl.net)
Design based on fdlog.c, by same author starting in 1984 for CP/M.

Goal: a minimum keystroke field day logging program supporting
      a group of users (a whole FD site) simultaneously

The original program was multitasking and supported multiple
stations on serial terminals, 2000 lines of small C and asm.
With help from Eric Williams WD6CMU and Steve Wilson KA6S, it
devolved to MSDOS but there supported only one user, so the
database had to be manually collated to include all stations.

Plan: use networking, usually 802.11b peer-to-peer wireless,
   to interconnect the stations. use a flood/fill algorithm
   to share data. avoid single point failure, stations can join
   and depart the network with minimal effect.

v0.01 started 3/2002. chose Python as it has the features
   to do this project well and efficiently
   after 2.5 days of effort the program is working for a
   single station. useful for single station logging
   
-------------------------------------------------------------------

"""

key_help = """
FDLog.py Help       File/Exit or Exit Button to Quit
                    ESC to abort input line
                    .h<return> for command help

<suffix><space>                 look up dups by suffix
<prefix><space>                 add prefix to previous suffix
<call><space><report><return>   log a contact

#<message>                      send qst message to all stations

:<dd.hhmm><space><call><space><report><return>  to force a date/time

<call> is <letters><digits><letters>

<suffix> is <letters>
<prefix> is <letters><digit>

To edit click on QSO in the Log window (must be node that made entry)
"""

def mhelp():
    viewtextv(key_help)

getting_started = """
FDLog = Field Day Logging Program            Copyright 2002-2016 Alan K Biocca

  Welcome to the W6AKB (formerly WB6ZQZ) High Sierra Field Day Group
FDLog program. This getting started dialog will review the essentials
and get you started using the program.

  FDLog is distributed under the GNU Public License. A copy is included
in the distribution package (gnu.txt) or can be found at www.gnu.org.

New Features and Changes

  The new Docs Menu allows a collection of files to be accessed from FDLog.
When FDLog is starting up it looks for a 'files' directory alongside the
program directory. If it finds one it creates a menu tree for the text,
pdf and image files it finds there to make them easily accessible from
FDLog. Operating aids, Field day rules, and equipment manuals are examples
of things you might want to have handy there.

  Note there is a new graphical startup dialog box, which allows the
user to input the Node ID and the Database Authorization Key. They
have defaults, but can be changed at this startup dialog. Then click
either Run FDLog or ABORT as desired.

  Note there is a new Out of Order entry capability, as well as a new
Complex Callsign entry feature, see the end of this document under
"Advanced Techniques". New users can focus on the basics before getting
into those features.

  VHF Mode is back, select it when starting the program, then enter the
four character grid either before or after the callsign. Use a /r postfix
on rovers (not enforced). Qs BandMode Grids and Score is displayed.
The Score Weighting and Band Selection is determined by the vhfBands.dat
CSV textfile which you can edit.

  Starting the program by either double clicking on fdlog.py, or typing
it on the command line. It will come up and display a dialog box to select
the contest type between Field Day and VHF Contest mode, and get
the Node ID and Authorization key. Subsequent launches will default to
the previous node ID and database authorization key, so clicking Run FDLog
is all that's required to get going again. We typically use two databases
on Field Day, one for practice (tst) and the other for the actual contest.
Your group will choose the name of the contest database they wish to use.

  The node id is used to identify the database records for each node in
the network of logging computers. These names must be unique - no two nodes
may use the same id at the same time. The suggested id is the callsign
of the equipment owner followed by a dash and a single digit, similar
to packet radio id's. An example would be: wb6zqz-1. Valid characters
include lowercase letters, numbers, and dash. An alternate form is to use
suffix-digit or just suffix such as 'zqz-1' or just zqz.

  The node id is requested as input during the startup and remembered for
future restarts. Thereafter if it need be changed it may be altered from
the Properties menu.

  The database authentication key is used to both select the database
and validate packets. Outgoing packets are digitally signed, and incoming
packets are checked for correct signatures. Invalid packets are not
processed. Set the authentication key to the same value for all nodes during
startup.  The filename and authentication key is made up of three components.
The first 3 characters are used as part of the logfile name.
Typically these are set to 'tst' for testing, or the two digit year and a
letter, such as '04a' for 2004, log file 'a'. This allows multiple logfiles
if desired. The next 3 digits are the port number factor. Characters beyond
that are used for the digital signature hash: 'yycppphhh...'

  The authentication key can be changed at each program startup. To change it
after the program is running, quit and restart the program. The value
used the previous time will be presented as the default, so normal startup
requires just clicking the Run FDLog button.

  Host based firewalls can be used with FDLog.
The program needs to be a server and client on the internet, so give it
that access (if network/wireless synchronization between stations is
desired). The port number used by FDLog is calculated from the Auth Key
so multiple FDLog working groups can be used on the same network.

  The display consists of several areas. The Menu Bar, the Button area,
the scrolling Log area and the Input area.

  The Window Title Bar displays a lot of information. Some items may not have
values and so will not display until they do. From left to right:

    FDLog154b                   program name and version
    N6OI                        group callsign
    39A SV-Sacramento Valley    field day class and section (the report)
    Node: w6akb-1               node id
    TimeOnBand 0:23             time on this band in hours, minutes
    13:35 UTC 06/25             UTC time and date

  The Menu has many options which will be covered later. In particular,
there are many useful items under the Help menu.

  The Band Buttons are used to set the band of this station. They are in
wavelength (meters) from 160 through 2, and then in frequency from 220
through 1200. Satellite is abbreviated 'sat'. Cw, Digital and Phone are
indicated by a single postfix letter; 'c', 'd', and 'p'. Thus Satellite
Phone is 'satp' and twenty meter cw is '20c'.

  The 'off' selections are to be selected when the station is not on a
band. This allows other stations to use the band.

  The Class indicator shows the number of stations on vs the number allowed.
Thus 0/2 is none on, two allowed. The VHF label indicates the number of
stations on VHF, and the number of Free stations available. Thus 1/1 shows
one station on VHF, one free allowed. Similarly, 2/1 indicates two stations
on, and one free is allowed. The second VHF station will count against the
Class transmitter count.

  The FonQ indicator shows the number of phone contacts. The GOTAq indicator
shows the number of Get On The Air station contacts. This lower right label
gets overwritten with error messages regarding the networking when needed.
These errors are described later.

  This section has color coding. In the Band columns Gray indicates
available bands, Yellow is on occupied bands, Orange an over-occupied
band, White the band this station is on, and Red an over-occupied
band this station is on. In the Class column White indicates no stations,
Yellow is some but not all that are allotted, and Green is full usage of that
station type. Red or Orange indicates too many stations for the current Class.

  Just below the Band Button block is the Operator/Logger/Power button
row. These Menu buttons allow selecting from the participants for Operator and
Logger, Adding new Participants, and entering the Power Level. Participants
are indexed by initials, so they must be unique. The power level may be
selected from the pulldown menu, or typed in. The Natural checkbox is used
to designate Natural Power for proper bonus credit.

  The Central window displays the current log entries. It may be scrolled
back to inspect earlier entries. Log entries and QSTs from other stations
are included in this display.

  The Lower window is the input window. Log Entries are typed there, and it
can be scrolled back to inspect earlier entries. Only local input data
appears in the lower display.

  The computer's clock accuracy is important for sorting of reports. The
program uses UTC time, so incorrect time zone settings can cause apparent time
errors. The '.tdwin' command sets the tolerance for time difference in seconds.
Incoming packets showing time differences exceeding this number of seconds
are displayed in the Command Window. One computer on the network can be
designated the time master (.set tmast <nodeid>). This machine should have
good time, all the other FDLogs will measure a time offset and apply this
to their system clocks to make FDLog time. An optional GPS Clock can be
USB connected that will synchronize FDLog to much better than one second.
If the system time is okay to use directly, enable ".timeok 1" to transition
local time offset to zero. This is used for system clocks sync'ed to good
time already.

  The output power in (watts) is recorded in the log. An output power of
0 watts indicates a test, so it will not be included in the final logs. Use
the Power button or Power Entry box to set the power level. Check the Natural
checkbox if the station is using natural power (to get credit for the extra
points).

  The operator and logger are recorded in the log. Use the Operator and Logger
buttons to select.

  The power, operator, logger, and authentication data are stored in a database
with the log program on normal exit, and reloaded on restart to minimize
re-entering. The band is not restored, so it will have to be re-selected after
restarting the program.

  Band is set by clicking on the desired gray band button.
Bands are 160/80/40/20/15/10/6/2 meters or 220/440/900/1200 mhz or sat
(for satellite) followed by a mode letter c, d or p for cw, digital
or phone. It will warn you if there is another station on that band by turning
RED, but it will allow the change anyway. Make sure the other station is not
using the band before making contacts.

  There is a special switch for VHF contests that changes a few things.
The main changes are a different set of bands, and dup checking includes grid.
The QSO modes are reduced to just one per band, stations are worked once per
band and grid. There is also a Cabrillo output in the result file. There
is no Cabrillo format defined for Field Day. ADIF output is generated in both
cases.

  For the VHF Contest Cabrillo File to be valid, the .set grid and .set fdcall
commands need to be entered. The vhfBands.dat text file can be edited to select
the bands that will appear on buttons and in the log. CW and Phone button rows
are available to populate the Cabrillo form appropriately. The scoring column
in the vhfBands file will allow different point values to be selected for each
band. Contacts may be entered with the grid first or the callsign first, and
the callsign should have postfix '/r' for rovers. Dupe checking is done on
return.

  Testing can be done with the band set to 'off' (or by using the 'tst'
authentication code and database). Contacts made to band 'off' are not
counted in the various scoring outputs, and will be filtered from the final
log. Use the auth key 'tst' to share data with test stations. In this
configuration the band and mode can be set as if operating to fully exercise
the system since the test log is separate from the contest log. When ready
to join the actual field day data net, shut down the fdlog program. Restart
the program and use the key that the group is using for the contest. Note
that two groups in the same physical area can use keys with differing port
fields to avoid authentication error warnings.

  Logging contacts is optimized for minimum keystrokes. Enter the call suffix
followed by a space to do a quick dup check. This will list any calls on this
band/mode  that have that same suffix. To log that call enter the prefix and
a space, and it will automatically pick up the earlier suffix and be ready for
the report. After typing the report, wait for the actual QSL confirmation
before hitting return. Return logs the Q into the database. Study the ARRL
section abbreviations to use the correct ones. This will als enable the worked
all states function to be accurate.

  Here is an example using 12 keystrokes to log a Q:

  aw<space> ==> ['w2aw']         <Quick DUP shows stations worked on this band>
  w1<space> ==> w1aw<space>_     <waiting for report, not a DUP>
  <report>  ==> w1aw 2a nc_      <waiting for return to LOG the Q>
  <return>  ==> w1aw 2a nc QSL   <LOGGED the Contact>

  ESCape will cancel an entry in progress and clear the input line.

  WAIT to hit <return> until tho QSO has been confirmed.

  An incorrectly entered Q can be edited or deleted by: clicking on the log entry
in the upper scrolling window (from the computer that entered it)and select edit
the fields. Select SAVE to preserve the changes, DELETE to delete the Q, or QUIT
to cancel changes.

  When taking a break in operations, set the band to 'off' with the "off"
button or the ".off" command. This makes the band available to others.

  If a node is just joining the net, or was off for awhile, it will take time
for it to 'catch up' to the full database. It attempts to do this at 5 items
per second, so it should not take long. It will display the data as it comes in,
so when it stops streaming data it is probably caught up. The 'Need Fill'
indicator will appear until it is caught up.

  QST broadcast messages can be sent to all nodes and entered into the log
by typing '#<message>' starting in column one. These are visible in the upper
window and scan be reviewed by selecting the log for band *QST, so watch for
them!

Platform Issues

  This program was developed and tested under Windows 2k to 10. It also
works on Linux, Unix, and Macintosh due to the portability of Python and
Tkinter. There are some issues that will affect portability, and some
functions may not work. For example, launching the ARRL Rules pdf file
may only work on Windows. Font sizes may be an issue on Linux.

Troubleshooting

  The program checks the networking and if any problems are noted they are
displayed on the lower right button (that usually reads GOTAq), turning it
yellow and putting a short message in it. These messages and what they mean
are detailed below. Note that it will display "NET OK" instead of a zero
GOTA Q count.


  NO NODE    The node identification is missing. This is necessary
             to identify the database records when they are shared.
             It is recommended to set this to the callsign of the owner
             of the station radio or computer (or the suffix), optionally
             followed by a dash and a single digit number if more than one
             id is needed. THIS MUST BE UNIQUE. DO NOT GIVE TWO NODES THE
             SAME NODE ID at the same time. Restart the program
             and answer the query during initialization to set it.

  NO AUTHKEY The authentication key is missing. Restart the program
             and answer the query during initialization to set it.
             It must match the other nodes you are sharing data with.

  SNDP FAIL  The Packet Sender has received an error from the operating
             sytem. This may occur when there is a network problem.
             Restarting the program or rebooting may cure it.

  STANDALONE Twenty seconds have passed without receiving any packets. This
             indicates that no other packets from an FDLog program are
             being received within the time window. This could indicate
             a problem with the network or auth key, or it could be normal
             if this is the only computer on this network running the
             program. It may occur occasionally if there are only two
             computers on the network running FDLog. Try restarting the
             program after the network is known to be working.

  AUTH FAIL  A packet has been received (on the port) that has the incorrect
             authentication code. It will not be processed. All nodes
             participating must use the same authentication key. Refer to
             the command window for more information about this error. It
             is best if test and production modes use different ports to
             avoid seeing each others packets which have differing
             authentication codes.

  NEED FILL  A node status broadcast has been received, and one or more
             of these nodes have data that this node's database does
             not have. This node will request the missing data until
             it is caught up. The new database items will be displayed in
             the upper display as they come in. If the NEED FILL is
             indicated, and no data is flowing into the upper display,
             the requests for data are not being answered.

  The incoming packets are checked for time skew. If it exceeds '.tdwin'
seconds a message is displayed in the command window. The default is 10
seconds. The message is 'tdel <diff> <host> <ip> <node> <utc date.time>'.
The window can be adjusted with the '.tdwin <seconds> command. (Note -
set the tmast variable to select a time master node - see the .set menu).

Reports

File / Save Entry File    - writes the complete Entry file to the file named
                            'fdlog.log' (including ADIF format log)

File / Preview Entry File - preview the existing entry file.

File / View Raw Logfile   - view the raw database file ('fdlog.fdb')

The following reports are generated from keyboard commands (starting with
'.' (period)). They respond to the command window.

.st     this station's status
.ba     station and band status
.re     log summary report
.pr     save contest entry textfile to file 'fdlog.log'


Keyboard Input Syntax for QSOs

call is
  <prefix><suffix><tag>

prefix is
  <letters><digits> or <digits><letters>

suffix is
  <letters or digits>  (different from end of prefix)

tag is
  /<letters or digits>

qso is
  <call> <report>

report is
  <letters or digits or spaces>

commands are
  .help
  .pow <digits><optional 'n'>
  .band <band><mode>           bands are 160..2m, 220..1200, modes are c d p
  .st                          this node's status
  .ba                          station and band report
  .re                          summary
  .pr                          generate contest entry

Forcing a Contact into the database at a specific time (eg: from paper logs):
  :dd.hhmm <call> <report> (picks up band/mode/oper/log/power)
  (this feature has been temporarily disabled)

QST messages to all nodes:
  #<message>

Advanced Techniques - Out of Order Input

    These FOUR Input Elements can be typed in ANY ORDER
        Call Prefix
        Call Suffix
        Field Day Class
        ARRL Section (MUST be prefaced with ';' if before callsign
            or prefix or suffix)

    The comment can only be entered after all other fields:
        Comment (always last)

    Normally a space is used to separate elements, however the prefix may be
    followed directly by the suffix. Typing <suffix><space> triggers a quick
    DUP check. Typing <prefix><space> brings in the previously typed suffix.
    (Note that < > and ' are just for document clarity and should not be typed)

    Call Prefix is one or two letters and one digit
    Call Suffix is one to three letters
    Field Day Class is 1..39 followed by a-f (either upper or lowercase)
    Section is two or three letters (see ARRL section abbreviation list)

Advanced Techniques - Complex Callsign Entry

    FDLog can now accept complex callsigns - those with one or two '/'
    characters, such as "VE7/WA6NHC or "N6OI/7 or "VE6/WB6ZQZ/MM. This also
    includes calls with multiple digits, or calls that start with digits.
    These calls will not DUP check at the present time, but they will
    go in the log. To enter these special callsigns start with a double
    quote, like "KH6/W6AKB/QRP. No closing quote is used.

Advanced Techniques - Port numbers and TCP/UDP

    The Remote IP command allows connecting to a remote FDLog. The remote TCP
    server is built into FDLog. The command is .remip 0.0.0.0 to turn the
    connection off, or enable it if the values are nonzero. In the address
    field use 0.0.0.0:123 instead of 0.0.0.0 to denote TCP
    on port 123 instead of the default port. If there is no ':' then it is
    UDP on standard port if there is a ':' then it uses TCP on the port
    following the ':'. Local UDP is always enabled independently of the remote.

eof
"""

import os,sys,time,calendar,string,re,time,thread,threading,socket,hashlib,random,math
from Tkinter import *

def fingerprint():
    t = open('fdlog.py').read()
    h = hashlib.md5()
    h.update(t)
    f = h.hexdigest()
    print "  FDLog Fingerprint",f,f[-6:]
fingerprint()


# Time Zone Conversion Chart
#000 0000 0000 0000 0000
#000  -8   -7   -6   -5
tzchart = """
 UTC       PDT  MDT  CDT  EDT
 GMT  PST  MST  CST  EST

"""

for g in range(0,2400,100):
    p = g - 800
    if (p < 0): p += 2400
    m = p + 100
    if (m < 0): m += 2400
    c = m + 100
    if (c < 0): c += 2400
    e = c + 100
    if (e < 0): e += 2400
    x = e + 100
    if (x < 0): x += 2400
    tzchart += "%04d %04d %04d %04d %04d %04d\n"%(g,p,m,c,e,x)

#print tzchart

# font setups (needs different fonts for Linux and Macintosh)
# fontsize on linux works around 18-20 (from Bob W9YA)
# fontsize default was 10 on windoze, interval 2
# fontsize of 18 won't fit on many windoze systems
# should make this user configurable. akb. xx

fontsize = 10
fontinterval = 2
typeface = 'Courier'

fdfont  = (typeface,fontsize)                  # regular fixwidth font
fdmfont = (typeface,fontsize+fontinterval)     # medium  fixwidth font
fdbfont = (typeface,fontsize+fontinterval*2)   # large   fixwidth font


# integer value utility

def ival(s):
    "return value of leading int"
    r = 0
    try:
        if s != "":
            m = re.match(r' *(-?[0-9]*)',s)
            if m and m.group(1):
                r = int(m.group(1))
    except:
        pass
    return r

def getver():
    "get version info"
    m = re.search(r'v[0-9]-[0-9]+-([0-9]+[a-zA-Z]{0,1})',prog)
    version = "v"
    if m: version += m.group(1)
    print "  FDLog Version",version[1:],"\n"
    return version
version = getver()



# feature request - built in time correction - use 'master' and offsets
#
# we can no longer easily adjust the system time, so instead we apply
# an offset to it when computing the time we use for FDLog.
#
# master is designated. marks time as level '0'
#
# time offset is stored in local database, so will return after reboot
# time master designation stored in db as a .set
# move gradually into correct time. speed up or slow by 25% max.
#
# master has zero correction factor - broadcasts system time
#
# local clock adjust procedure is - shutdown fdlog, change, start fdlog
#
# at broadcast reception:
#   if at level then average
#   if above level then restart average with this
#
# every minute:
#   look at what we know and do time correction
#
# time quality levels (0..9)
#   0 = designated master
#   1 = sync'd to master
#   2 = sync'd to level 2
#   ..
#   9 = not sync'd
#
#   consider self synchronized when error <= 2s?
#     then set level to src+1
#
#   new and other nodes will go to level 9
#

# 2016 comments
#
# windoze time jerks the clock and occasionally makes a mess
# especially when it jerks the time master's GPS locked clock?
# this is hard to recognize and adapt for
# perhaps a timer master GPS locked clock should sendout real GPS time
# rather than its own, and avoid the local jerk going out
#
# more info in separate note in W6AKB's Evernotes
#
# the thing we trust most is a master with FDLog GPS CLock which tells us when it is locked
# and only the freshly read time messages from this are level 0
# next we trust one or more non-masters with FDLog GPS Clock at level 1
# the master's other messages are level 1 or 2 as they are not fresh GPS clocks
# next we trust a timeok host that supposedly has NTP or GPS set system time at level 3
# the master we follow if it is there

timeok = 0              # system time is defined to be trusted (NTP etc)

class clock_class:

    level = 9           # my time quality level
    offset = 0          # my time offset from system clock, add to system time, sec
    adjusta = 0         # amount to adjust clock now (delta)
    errors = 0          # current error sum wrt best sources, in total seconds
    errorn = 0          # number of time values in errors sum
    srclev = 900        # current best time source level observed
    clockser = None     # fdlog gps clock serial

    # level 0 is time master (with locked gps clock, time fresh from GPS)
    # level 1 is have gps clock, locked, tracking it
    # level 2 is time master w/o gps
    # level 3 is has timeok (moved from 2)
    # +3 is tracking, within 2S
    # +6 is tracking, not within 2S

    #offset = globDb.get('toffset',4)  # get initial from global database
    #print "Initial Time Offset",offset

    lock = threading.RLock()    # sharing lock, to protect against overlapping

    def update(self):
        "periodic clock update every 30 seconds"

        gpstm,gpslock,gpserr = self.gpsclock()          # check for gps clock

        tmast =  node == gd.getv('tmast')               # if we are master

        self.lock.acquire()                             # take semaphore

        if  gpslock:                                    # if we have locked clock (takes priority)
            self.srclev = 1                             #   follow it instead of what we heard
            self.errorn = 1
            self.errors = gpserr*2                      # take the gps error

        elif timeok:                                    # if system time defined accurate, use it
            if self.srclev > 3:                         # if nothing better is heard
                self.srclev = 3
                self.errorn = 1
                self.errors = -self.offset              # go gently to zero

        if self.errorn > 0:                             # calc error average if data
            error = float(self.errors)/self.errorn
        else: error = 0


        # if we are the time master, we should only follow gps clock or timeok (2017 154c)
        if self.srclev <= 3 or not tmast:
            self.adjusta = error*0.5                    # adjust half of the error
        mag = abs(error)

        if mag < 2:                                     # set our level
            if gpslock: self.level = 1
            elif tmast: self.level = 2
            elif timeok: self.level = 3
            else: self.level = self.srclev + 3          # sync'd with something
        else:
            self.level = self.srclev + 50               # following but not yet sync'd

        if abs(self.adjusta) > 0.1:
            print "Adjusting Clock %.1f S, src level %d, total offset %.1f S, at %s"%\
                  (self.adjusta,self.level,self.offset+self.adjusta,now())
##            print self.srclev,"src level"
##            print gpslock,"gps lock"
##            print tmast,"time master"
##            print timeok,"time ok"
##            print self.errorn,"corrections count"
##            print self.errors,"corrections sum"
##            print error,"time error"
##            print gpserr,"gps error"
##            print self.offset,"time offset"

        self.srclev = 900                               # reset for next search cycle

        self.lock.release()                             # release sem


    def calib(self,fnod,stml,td):
        "process time info in incoming pkt"
        if fnod == node: return                       # ignore self data (UNLESS GPS??)
        self.lock.acquire()                           # take semaphore
    #    print "time fm",fnod,"lev",stml,"diff",td
        stml = int(stml)                              # src time level
        if stml < self.srclev:                        # find the best time data
            self.errors,self.errorn = 0,0
            self.srclev = stml
        if stml == self.srclev:                       # average data at same level
            self.errorn += 1
            self.errors += td                         # time difference
        self.lock.release()                           # release sem

    def adjust(self):
        "slew the clock each second as needed (called /sec)"

                                                        # clock tuning
        srt = gd.getv('ckslew')                         # get slew rate
        if srt[:5] == 'error': rate = 100               # default 100 mS / S
        else:
            try: rate = ival(srt)
            except: rate = 100
        if rate < 10: rate = 10
        if rate > 500: rate = 500
        rate = rate / 1000.0
        #print "slew rate",srt,rate

        self.lock.acquire();
        #rate = 0.1                                    # delta seconds per second limit
        adj = self.adjusta
        #if abs(adj) < 0.001: return                   # close enough, quit NO, WATCH LOCK

        if adj > rate: adj = rate                     # adjustment rate limit
        elif adj < -rate: adj = -rate

        self.offset = float(globDb.get('toffset',0))  # get from global database/cache
        self.offset += adj

        if abs(adj) > 0.0005:                         # reduce sqlite writes
            globDb.put('toffset',self.offset)         # save in global database

        self.adjusta -= adj                           # account for slewing progress

        self.lock.release();

        if abs(adj) > 0.5: print "Slewing clock",adj,"to",self.offset


    def offsetinit(self):
        self.offset = float(globDb.get('toffset',0))  # set up offset
        print "    time offset restored",self.offset


    def gpsclockinit(self):
        "find and initialize for gps clock"
##        return  # temporarily bypass to save time during testing, may want to make a control
    
        try:
            import serial
        except:
            print "warning - serial import failed (only needed for gps clock)"
            return
        print "  Searching for W6AKB FDLog GPS USB Clock"
        for i in range(22):
            if i == 21:
                print "    failed to find GPS clock"
                break
            try:
                clockser = None
                clockser = serial.Serial(port=i,baudrate=9600,timeout=2)
                #print "  found serial",i+1
                for j in range(2):
                    clockser.write("t\n")
                    line = clockser.readline()
                    #print "   ",line
                    p = line.split()
                    if p[0] == 'g' or p[0] == 'u':
                        print "    found GPS clock on COM%d\n"%(i+1)
                        #print "     ",line
                        self.clockser = clockser
                        return
                clockser.close()
            except:
               # print "  fail",i
                if clockser: clockser.close()

        print

    # gpsclock() read gps clock hardware
    #
    # usb serial hardware returns indication of lock condition g/u
    # and gmt time in 7 integers to milliseconds
    #
    # gpsclock could have a race condition if it was called from two threads at once
    # we may be calling it from two places but they are part of the same thread
    # so this won't be an issue. If this changes it should get a protective lock
    #
    def gpsclock(self):                         # read serial gps clock
        g,gpslock,gpserr = 0,0,0                # initialize gps time, lock, error
        if self.clockser:                       # if there is one, read gps clock
            self.clockser.write("m\n")          # warm the link
            self.clockser.readline()            # discard the first reading
            self.clockser.write("t\n")          # get gps seconds and milliseconds
                                                # delays are worst on way in
                                                # return msg is very prompt
            l1 = self.clockser.readline()       # gather the result
            t2 = time.time()                    # system time again (old code location)

            t2 += self.offset                   # apply current time adjustment

            p = l1.split()                      # 8 parts: g/u y m d h m s ms
            if p[0] == 'g' and len(p) == 8:     # if locked g, if not u
                gpslock = 1
                gt = "%02d%02d%02d %02d%02d%02d GMT"% \
                    ( int(p[1]),int(p[2]),int(p[3]),int(p[4]),int(p[5]),int(p[6]) )
                g = calendar.timegm(time.strptime(gt,"%y%m%d %H%M%S %Z")) + int(p[7])/1000.0
                gpserr = g - t2                  # calc clock error
                if debug: print "  gpsClockDbg %.3f %.3f %.3f"%(g-t2,self.offset,t2-self.offset-t)
                else:
                    print "  gpsClock %.3f %.3f"%(g-t2,self.offset)
        return g,gpslock,gpserr                 # return gps time, lock, time error

    def gpsclockDebug(self,v):
        if v == "1": self.clockser.write("D\n") # put clock in debug mode
        if v == "0": self.clockser.write("d\n") # take clock out of debug mode

mclock = clock_class()                          # set up clock class
mclock.gpsclockinit()                           # search for gps clock hardware

def exin(op):
    "extract operator or logger initials"
    r = ""
    m = re.match(r'([a-z0-9]{2,3})',op)
    if m:
        r = m.group(1)
    return r


# sqlite database upgrade
#
# use sqlite as the primary journal file database
# do the various important transactions there
# should avoid the locking needed now, the database has the locks
# write it out and then read it back from there
# so the database becomes the central collaboration point
#
# do db in parallel w ascii journal file, ascii journal becomes a write only file
#   some folks use this file for other purposes


import sqlite3

class SQDB:
    def __init__(self):
        self.dbPath = logdbf[0:-4] + '.sq3'
        print "Using database",self.dbPath

        self.sqdb = sqlite3.connect(self.dbPath)  # connect to the database
        self.sqdb.row_factory = sqlite3.Row   # namedtuple_factory
        self.curs = self.sqdb.cursor()      # make a database connection cursor
        sql = "create table if not exists qjournal(src text,seq int,date text,\
            band text,call text,rept text,powr text,oper text,logr text,\
            primary key (src,seq))"
        self.curs.execute(sql)
        self.sqdb.commit()
        #create table qsos, index by call,band,mode (varies by contest)
        #create table score phone, cw, data
        #create table station, operator, logger, power,
        #return self
    def readLog(self): # ,srcId,srcIdx):            # returns list of log journal items
        print "Loading log journal from sqlite database"
        sql = "select * from qjournal"
        result = self.curs.execute(sql)
        nl = []
        for r in result:
            nl.append("|".join(('q',r['src'],str(r['seq']),r['date'],r['band'],\
                                r['call'],r['rept'],r['powr'],r['oper'],r['logr'],'')))
        return nl
    def next(self):                         # get next item from db in text format
        n = self.result
        nl = "|".join(n.src,n['seq'],n['date'],n['band'],n['call'],\
                      n['rept'],n['powr'],n['oper'],n['logr'])
        return nl
    def log(self,n):                        # add item to journal logfile table (and other tables...)
        parms = (n.src,n.seq,n.date,n.band,n.call,n.rept,n.powr,n.oper,n.logr)

        sqdb = sqlite3.connect(self.dbPath)  # connect to the database
#        self.sqdb.row_factory = sqlite3.Row   # namedtuple_factory
        curs = sqdb.cursor()      # make a database connection cursor

        # start commit, begin transaction
        sql = "insert into qjournal (src,seq,date,band,call,rept,powr,oper,logr) values (?,?,?,?,?,?,?,?,?)"
        curs.execute(sql,parms)
        # update qso count, scores? or just use q db count? this doesn't work well for different weights
        # update sequence counts for journals?
        sqdb.commit()                       # do the commit

        if n.band == '*QST': print("QST\a "+n.rept+" -"+n.logr) # emit BEEP sound on QST

        # might want to use one fixed database, add a column for the sub-set that we're using
        # have a pulldown to select the particular contest/db to use


class D:  # method free data class
    pass

# interesting idea for future, store sql in the journal...
# probably a subset, but basically ready to execute sql with some encapsulation
# for the arguments
# OR perhaps JSON dictionaries or method free classes instead?


# qso database class

class qsodb:
    byid = {}                   # qso journals by src.seq
    bysfx = {}                  # call list by suffix.band
    hiseq = {}                  # high sequence number by node
    lock = threading.RLock()    # sharing lock

    def new(self, source):
        n = qsodb()
        n.src = source          # source id
        return n

    def tolog(self):            # make log file entry
        sqdb.log(self)          # to database
        self.lock.acquire()     # and to ascii journal file as well
        fd = file(logdbf,"a")
        fd.write("\nq|%s|%s|%s|%s|%s|%s|%s|%s|%s|" % \
            (self.src,self.seq,
             self.date,self.band,self.call,self.rept,
             self.powr,self.oper,self.logr))
        fd.close()
        self.lock.release()

    def ldrec(self,line):       # load log entry fm text
        (typ,self.src,self.seq,
             self.date,self.band,self.call,self.rept,
             self.powr,self.oper,self.logr,eol) = string.split(line,'|')
        self.seq = int(self.seq)
        self.dispatch('logf')

    def loadfile(self):
        print "Loading Log File"
        i,s,log = 0,0,[]
        global sqdb                         # setup sqlite database connection
        sqdb = SQDB()
        log = sqdb.readLog()                # read the database

        for ln in log:
            if ln[0] == 'q':                # qso db line
                r = qdb.new(0)
                try:
                    r.ldrec(ln)
                    i += 1
                except ValueError,e:
                    print "  error, item skipped: ",e
                    print "    in:",ln
                    s += 1
        if i == 0 and s == 1:
            print "  Log file not found, must be new"
        else:
            print "  ",i,"Records Loaded,",s,"Errors"

    def cleanlog(self):
        "return clean filtered dictionaries of the log"
        d,c,g = {},{},{} # log by id, main by dupkey, gota by dupkey; dupkey is call.band
        fdstart,fdend = gd.getv('fdstrt'),gd.getv('fdend')
        self.lock.acquire()
        for i in self.byid.values():        # copy, index by node, sequence
            k = "%s|%s"%(i.src,i.seq)
            d[k] = i
        self.lock.release()
        for i in d.keys():                  # process deletes
            if d.has_key(i):
                iv = d[i]
                if iv.rept[:5] == "*del:":
                    j,st,sn,r = iv.rept.split(':')   # extract deleted id
                    k = "%s|%s"%(st,sn)
                    if k in d.keys():
##                        print iv.rept,; iv.pr()
                        del(d[k])               # delete it
##                    else: print "del target missing",iv.rept
                    del(d[i])
        for i in d.keys():                  # filter time window
            iv = d[i]
            if iv.date < fdstart or iv.date > fdend:
##                print "discarding out of date range",iv.date,iv.src,iv.seq
                del(d[i])
        for i in d.values():                # re-index by call-band
            #s,t,p,x,call,x,r = self.qparse(i.call)    # extract call (not /...)
            s,t,p,x,call,xc,r = qparse3('"'+i.call+' ')    # extract call (not /...)
##            print "cleanlog call",call,"xc",xc,"band",i.band,i.band[:-1]
##            if contest == "VHF": call = xc
            k = "%s-%s"%(call,i.band)
            if contest == "VHF": k = "%s-%s-%s"%(call,i.band[:-1],i.rept[:4]) # drop out mode for VHF, include grid
##            print "cleanlog",k
                                            # filter out noncontest entries
            if ival(i.powr) == 0 and i.band[0] != '*': continue
            if i.band == 'off': continue
            if i.band[0] == '*': continue   # rm special msgs
            if i.src == 'gota': g[k] = i    # gota is separate dup space
            else: c[k] = i
        return (d,c,g)                      # Deletes processed, fully Cleaned
                                            # by id, call-bnd, gota by call-bnd

    def prlogln(s):
        "convert log item to print format"
        # note that edit and color read data from the editor so
        # changing columns matters to these other functions.
        if s.band == '*QST':
            ln = "%8s %5s %-41s %-3s %-3s %4s %s"%\
                (s.date[4:11],s.band,s.rept[:41],s.oper,s.logr,s.seq,s.src)
        elif s.band == '*set':
            ln = "%8s %5s %-11s %-29s %-3s %-3s %4s %s"%\
                (s.date[4:11],s.band,s.call[:10],s.rept[:29],\
                 s.oper,s.logr,s.seq,s.src)
        elif s.rept[:5] == '*del:':
            ln = "%8s %5s %-7s %-33s %-3s %-3s %4s %s"%\
                (s.date[4:11],s.band,s.call[:7],s.rept[:33],\
                 s.oper,s.logr,s.seq,s.src)
        else:
            ln = "%8s %5s %-11s %-24s %4s %-3s %-3s %4s %s"%\
                (s.date[4:11],s.band,s.call[:11],s.rept[:24],\
                 s.powr[:4],s.oper,s.logr,s.seq,s.src)
        return ln

    def prlog(self):
        "print log in time order"
        l = self.filterlog("")
        for i in l:
            print i


# adif specs for eqsl.org   http://www.eqsl.cc/qslcard/adifcontentspecs.cfm ver 2.27
#
# problems - adif digital modes and satellite modes don't fit the fd model
#   even voice.. need 'real' mode field. pulldown menu.
#     add outgoing report to comments in parens
#
# <QSO_DATE:8> YYYYMMDD
# <TIME_ON:4> HHMM only HH and MM are used
# <CALL:6> up to 13 chars
# <BAND:3>
# <MODE:3>
# <SAT_MODE:>
# <LOG_PGM:15>FDLog by WB6ZQZ
# <COMMENT:> up to 240 chars
# <EOR>
#
# .ADI extension

    def pradif(self):
        "print clean log in adif format"
        pgm = "FDLog by W6AKB (formerly WB6ZQZ) (www.fdlog.info)"
        print "<PROGRAMID:%d>%s"%(len(pgm),pgm)
        m,n,g = self.cleanlog()
        for i in n.values() + g.values():
            dat = "20%s"%i.date[0:6]
            tim = i.date[7:11]
            cal = i.call
            bnd = "%sm"%i.band[:-1]
            mod = i.band[-1:]
            if mod == 'p': mod = 'SSB'
            elif mod == 'c': mod = 'CW'
            elif mod == 'd': mod = 'RTTY'
            com = i.rept
            print "<QSO_DATE:8>%s"%(dat)
            print "<TIME_ON:4>%s"%(tim)
            print "<CALL:%d>%s"%(len(cal),cal)
            print "<BAND:%d>%s"%(len(bnd),bnd)
            print "<MODE:%d>%s"%(len(mod),mod)
            print "<QSLMSG:%d>%s"%(len(com),com)
            print "<EOR>"
            print


# vhf contest cabrillo qso output (must be in chronological order)
#
#QSO: freq  mo date       time call              grid   call              grid
#QSO: ***** ** yyyy-mm-dd nnnn *************     ****** *************     ******

    def vhf_cabrillo(self):
##        for i in self.byid.values():
##            print "byidValues %-8s %5d %s"%(i.src,i.seq,i.call)
        "output VHF contest cabrillo QSO data (no such for Field Day)"
        #band_map = {'6':'50','2':'144','220':'222','440':'432','900':'902','1200':'1.2G'}
        band_map = bandToCabrillo
        m,n,g = self.cleanlog()
##        print "len byid, by callband after cleanlog",len(m),len(n)
        mycall = string.upper(gd.getv('fdcall'))    # my call
        mygrid = gd.getv('grid')                    # my grid
##        print "len n.values",len(n.values())
        l = []
        #                mode                 my                my  contacted      destination
        print "QSO: freq  mo date       time call              grid   call              grid "
        for i in n.values():                            # + g.values(): no gota in vhf contest
            freq = "%s"%i.band[:-1]                     # band
            if freq in band_map: freq = band_map[freq]  # remap some bands
            else: continue                              # ignore entries it cannot map
            mod = i.band[-1:]                           # mode recoded
            if mod == "c": mod = "CW"
            elif mod == "p": mod = "PH"
            elif mod == "d": mod = "RY"                   # this assumes RTTY is the digital mode
            else: mod = "PH"
            date = "20%2s-%2s-%2s"%(i.date[0:2],i.date[2:4],i.date[4:6])
            tim = i.date[7:11]
            call = i.call.upper()
            grid = i.rept[:4]
            l.append("%sQSO: %-5s %-2s %-10s %4s %-13s     %-6s %-13s     %-6s"%\
                     (i.date,freq,mod,date,tim,mycall,mygrid,call,grid))
        l.sort()                    # sort data with prepended date.time
        for i in l: print i[13:]    # strip prepended sort key date.time

    def filterlog(self,filt):
        "list filtered (by bandm) log in time order, nondup valid q's only"
        l = []
        m,n,g = self.cleanlog()
        for i in n.values() + g.values():
            if filt == "" or re.match('%s$'%filt,i.band):
                l.append(i.prlogln())
        l.sort()
        return l

    def filterlog2(self,filt):
        "list filtered (by bandm) log in time order, including special msgs"
        l = []
        m,n,g = self.cleanlog()
        for i in m.values():
            if filt == "" or re.match('%s$'%filt,i.band):
                l.append(i.prlogln())
        l.sort()
        return l

    def filterlogst(self,filt):
        "list filtered (by nod) log in time order, including special msgs"
        l = []
        m,n,g = self.cleanlog()
        for i in m.values():
            if re.match('%s$'%filt,i.src):
                l.append(i.prlogln())
        l.sort()
        return l

    def qsl(self,time,call,bandmod,report):
        "log a qsl"
##        lookupSection(report)
        return self.postnewinfo(time,call,bandmod,report)

    def qst(self,msg):
        "put a qst in database + log"
        return self.postnewinfo(now(),'','*QST',msg)

    def globalshare(self,name,value):
        "put global var set in db + log"
        return self.postnewinfo(now(),name,'*set',value)

    def postnewinfo(self,time,call,bandmod,report):
        "post new locally generated info"
        return self.postnew(time,call,bandmod,report,exin(operator),\
                            exin(logger),power)

    def postnew(self,time,call,bandmod,report,oper,logr,powr):
        "post new locally generated info"
        s = self.new(node)
        s.date,s.call,s.band,s.rept,s.oper,s.logr,s.powr = \
            time,call,bandmod,report,oper,logr,powr
        s.seq = -1
        return s.dispatch('user')

    def delete(self,nod,seq,reason):
        "rm a Q by creating a delete record"
##        print "del",nod,seq
        a,b,c = self.cleanlog()
        k = "%s|%s"%(nod,seq)
        if a.has_key(k) and a[k].band[0] != '*':        # only visible q
            tm,call,bandmod = a[k].date,a[k].call,a[k].band
            rept = "*del:%s:%s:%s"%(nod,seq,reason)
            s = self.new(node)
            s.date,s.call,s.band,s.rept,s.oper,s.logr,s.powr = \
               now(),call,bandmod,rept,exin(operator),exin(logger),0
            s.seq = -1
            s.dispatch('user')
            text.insert(END," DELETE Successful %s %s %s\n"%(tm,call,bandmod))
        else:
            text.insert(END," DELETE Ignored [%s,%s] Not Found\n"%\
                        (nod,seq))

    def todb(self):
        "Q record object to db"
        r = None
        self.lock.acquire()
        current = self.hiseq.get(self.src,0)
        self.seq = int(self.seq)
        if self.seq == current+1:       # filter out dup or nonsequential
            self.byid["%s.%s"%(self.src,self.seq)] = self
            self.hiseq[self.src] = current+1
##            if debug: print "todb:",self.src,self.seq
            r = self
        elif self.seq == current:
            if debug: print "dup sequence log entry ignored"
        else:
            print "out of sequence log entry ignored", self.seq,current+1
        self.lock.release()
        return r

    def pr(self):
        "print Q record object"
        sms.prmsg(self.prlogln())

    def dispatch(self,src):
        "process new db rec (fm logf,user,net) to where it goes"
        self.lock.acquire()
        self.seq = int(self.seq)
        if self.seq == -1:                              # assign new seq num
            self.seq = self.hiseq.get(self.src,0) + 1
        r = self.todb()
        self.lock.release()
        if  r:                                          # if new
            self.pr()
            if src != 'logf': self.tolog()
            if src == 'user': net.bc_qsomsg(self.src,self.seq)
            if self.band == '*set':
                m = gd.setv(r.call,r.rept,r.date)
                if not m: r = None
            else:
                self.logdup()
        return r

    def bandrpt(self):
        "band report q/band pwr/band, q/oper q/logr q/station"
        qpb,ppb,qpop,qplg,qpst,tq,score,maxp = {},{},{},{},{},0,0,0
        cwq,digq,fonq = 0,0,0
        qpgop,gotaq,nat,sat = {},0,[],[]

        x,c,g = self.cleanlog()

        for i in c.values()+g.values():

            if re.search('sat',i.band): sat.append(i)
            if 'n' in i.powr: nat.append(i)

# GOTA q's stop counting over 500 (2009)
            if i.src == 'gota':                     # analyze gota limits
                qpgop[i.oper] = qpgop.get(i.oper,0)+1
                qpop[i.oper] = qpop.get(i.oper,0)+1
                qplg[i.logr] = qplg.get(i.logr,0)+1
                qpst[i.src]  = qpst.get(i.src,0) +1
                if gotaq >= 500: continue           # stop over 500 total
                gotaq += 1
                tq += 1
                score += 1
                if 'c' in i.band:
                    cwq   += 1
                    score += 1
                    qpb['gotac'] = qpb.get('gotac',0)+1
                    ppb['gotac'] = max(ppb.get('gotac',0),ival(i.powr))
                if 'd' in i.band:
                    digq  += 1
                    score += 1
                    qpb['gotad'] = qpb.get('gotad',0)+1
                    ppb['gotad'] = max(ppb.get('gotad',0),ival(i.powr))
                if 'p' in i.band:
                    fonq  += 1
                    qpb['gotap'] = qpb.get('gotap',0)+1
                    ppb['gotap'] = max(ppb.get('gotap',0),ival(i.powr))
                continue

            qpb[i.band] = qpb.get(i.band,0)+1
            ppb[i.band] = max(ppb.get(i.band,0),ival(i.powr))
            maxp = max(maxp,ival(i.powr))
            qpop[i.oper] = qpop.get(i.oper,0)+1
            qplg[i.logr] = qplg.get(i.logr,0)+1
            qpst[i.src]  = qpst.get(i.src,0) +1
            score += 1; tq += 1
            if 'c' in i.band:
                score += 1    # extra cw and dig points
                cwq   += 1
            if 'd' in i.band:
                score += 1
                digq  += 1
            if 'p' in i.band:
                fonq  += 1

        return (qpb,ppb,qpop,qplg,qpst,tq,score,maxp,cwq,digq,fonq,qpgop,gotaq,nat,sat)

    def vhfrpt(self):
        "vhf report counts VHF scoring"
        res = D()  # an empty data container instance
        res.qcount,res.grids,res.score,grid = 0,0,0,{}
        x,c,g = self.cleanlog()

        for i in c.values():                # by id clean dictionary of Q's
            band = i.band[:-1]              # trim off c/p mode
            pv = bandToScore.get(band,0)    # lookup point value for this Q
            if pv > 0:                      # count this Q only if it is in table
                res.qcount += 1      
                res.score += pv             # weighted contact value
                g = i.rept[:4]
                bg = ('/').join((band,g))   # band/grid
                grid[bg] = 1                # band grid dictionary deduplicates
##            print "band",band,"pv",pv,"grid",g,"bg",bg # debug

        res.grids = len(grid)           # size of grid dictionary is unique count
        res.score *= res.grids          # apply grid multiplier to accumulated points
        
        return res

    def bands(self):      # .ba command band status station on, q/band, xx needs upgd
        qpb,tmlq,nod = {},{},{}
        self.lock.acquire()
        for i in self.byid.values():
            if ival(i.powr) < 1: continue
            if i.band == 'off': continue
            v = 1
            if i.rept[:5] == '*del:': v = -1
            qpb[i.band] = qpb.get(i.band,0)+v               # num q's
            tmlq[i.band] = max(tmlq.get(i.band,''),i.date)  # time of last (latest) q
        self.lock.release()

        tx = []  # list of lines for output
        #print
        tx.append("Stations this node is hearing:\n")
        # scan for stations on bands
        for s in net.si.nodes.values():   #xx
##            print dir(s)
            tx.append("%s %s %s %s"% (s.nod,s.host,s.ip,s.stm))
##            nod[s.bnd] = s.nod_on_band()
##            print "%8s %4s %18s %s"%(s.nod,s.bnd,s.msc,s.stm)

        d = {}
        #print
        tx.append("\nNode Info")
        tx.append("--node-- band opr lgr pwr---  seconds\n")
        for t in net.si.nodinfo.values():
            x1,x2,age = d.get(t.nod,('','',9999))
            if age > t.age: d[t.nod] = (t.bnd,t.msc,t.age)
        for t in d: # fresh ones first
            if d[t][2] < 999:
                tx.append("%8s %4s %-18s %4s"%(t,d[t][0],d[t][1],d[t][2]))
                #t.bnd,t.msc,t.age)
        for t in d: # then the rest
            if d[t][2] >= 999:
                tx.append("%8s %4s %-18s %4s"%(t,d[t][0],d[t][1],d[t][2]))
                #t.bnd,t.msc,t.age)


        #print
        tx.append("\n Band  -------- CW ----- ------- Dig ----- ------- Fon -----\n")
        tx.append(  "         Nod  Q's  TsLQ    Nod  Q's  TsLQ    Nod  Q's  TsLQ\n")
        #      xxxxxx yyyyyy xxxx xxxxx yyyyyy xxxx xxxxx yyyyyy xxxx xxxxx

        t1 = now()
        for b in (160,80,40,20,15,10,6,2,220,440,900,1200,'Sat'):
            s1 = "%5s"%b
            for m in 'cdp':
                bm = "%s%s"%(b,m)
                # be nice to do min since q instead of time of last q DONE
                t2 = tmlq.get(bm,'')                # time since last Q minutes
                if t2 == '':
                    tdif = ''
                else:
                    tdif = int(tmsub(t1,t2)/60.)
                    tmin = tdif%60
                    tdhr = tdif/60
                    if tdhr > 99:
                        tdhr = 99
                        tmin = 59
                    tdif = tdhr*100 + tmin
               #     if tdif > 9999: tdif = 9999
               #     tdif = str(int(tdif))           # be nice to make this hhmm instead of mmmm

##                t = ""                            # time of latest Q hhmm
##                m = re.search(r"([0-9]{4})[0-9]{2}$",tmlq.get(bm,''))
##                if m: t = m.group(1)
                nob = net.si.nod_on_band(bm) # node now on band
                if len(nob) == 0: nob = ''   # list take first item if any
                else: nob = nob[0]
                s1 += " %6s %4s %5s"%(nob[0:6],qpb.get(bm,''),tdif)  # was t
##                      (nod.get(bm,'')[0:5],qpb.get(bm,''),t),
            tx.append('%s'%s1)

        tx.append("\nTsLQ is in HHMM format")
        viewtextl(tx,"Station and Band Report")

    def sfx2call(self, suffix, band):
        "return calls w suffix on this band"
        x = self.bysfx.get(suffix+'.'+band,[])
        if contest == "VHF": # vhf gets both contact types
            if band[-1:] == 'c': band = band[:-1] + 'p'
            else: band = band[:-1] + 'c'
            print "band",band
            x += self.bysfx.get(suffix+'.'+band,[])
        #print "sfx2call",suffix,band,x
        return x


##    def dupck(self, wcall, band):
    def dupck(self,call,band,grid):
        "check for duplicate call on this band"
        stat,tm,pfx,sfx,call,xcall,rept = qparse3(call)
##        stat,tm,pfx,sfx,call,xcall,rept = qparse3(buf)
##        print "qparse call '%s' stat '%s' pfx '%s' sfx '%s' call '%s' xcall '%s' rept '%s'"%\
##              (call,stat,pfx,sfx,call,xcall,rept)  # debug
        if contest == "VHF":
            #print "dupck",xcall
            a,b,c = self.cleanlog()
            k = "%s-%s-%s"%(call,band[:-1],grid)
##            print "call",call,"band",band[:-1],"grid",grid  # no rept here, need more info to do this
            return k in b
        return call in self.sfx2call(sfx,band) # field day

    def logdup(self):
        "enter into dup log"
        #stat,tm,pfx,sfx,call,xcall,rept = self.qparse(self.call)
        stat,tm,pfx,sfx,call,xcall,rept = qparse3(self.call+' ')
        key = sfx + '.' + self.band
        self.lock.acquire()
        if self.rept[:5] == "*del:":   # check for delete journal entry
            self.redup()               # and rebuild the dup database (wow)
##            print "proc del",self.rept,self.call,self.band
##            try:
##                self.bysfx[key].remove(call)
##            except:
##                pass
##                print " rm fm dupdb failed -%s-%s-%s-"%(call,sfx,band)
        else:
            # duplog everything with nonzero power, or on band off (test)
            if (self.band == 'off')|(ival(self.powr) > 0):
                # dup only if Q and node type match (gota/not)
                if (node == 'gota') == (self.src == 'gota'):
##                    self.dupdic[call + dupstr] = 1
                    if self.bysfx.has_key(key):     # add to suffix db
                        self.bysfx[key].append(xcall)
                    else:
                        self.bysfx[key] = [xcall]
##                else: print "node type mismatch",node,self.src
        self.lock.release()

    def redup(self):
        "rebuild dup db"
        d,c,g = self.cleanlog()
        self.lock.acquire()
#        print self.bysfx
        qsodb.bysfx = {}                # why not self.?
        for i in c.values()+g.values():
#            print i.call,i.band
            i.logdup()
        self.lock.release()
#        print qsodb.bysfx

    def wasrpt(self):
        "worked all states report"
        sectost,stcnt,r,e = {},{},[],[]

        try:
            fd = file("arrl_sect.dat","r")  # read section data
            while 1:
                ln = fd.readline()          # read a line and put in db
                if not ln: break
                #if ln == "": continue
                if ln[0] == '#': continue
                try:
                    sec,st,canum,desc = string.split(ln,None,3)
                    sectost[sec] = st
                    stcnt[st] = 0
##                    print sec,st,desc
                except ValueError,e:
                    print "rd arrl sec dat err, itm skpd: ",e
            fd.close()
        except IOError,e:
            print "io error during arrl section data file load", e

        a,b,c = self.cleanlog()
        for i in a.values():
            sect,state = "",""
            if i.rept[:1] == '*': continue
            if i.band[0] == '*': continue
            if i.band == 'off': continue
            if i.powr == '0': continue
            m = re.match(r' *[0-9]+[a-fA-F] +([A-Za-z]{2,4})',i.rept)
            if m:
                sect = m.group(1)
                sect = string.upper(sect)
                state = sectost.get(sect,"")
#                print "sec",sect,"state",state
                if state: stcnt[state] += 1
            if not state:
##                print "section not recognized in:\n  %s"%i.prlogln()
##                print "sec",sect,"state",state
                e.append(i.prlogln())

        h,n = [],[]                         # make have and need lists
        for i in stcnt.keys():
            if i != "--":
                if stcnt[i] == 0: n.append("%s"%i)
                else: h.append("%s"%i)
        n.sort()
        r.append("Worked All States Report\n%s Warning(s) Below\nNeed %s States:"%(len(e),len(n)))
        for i in n:
            r.append(i)
        h.sort()
        r.append("\nHave %s States:"%len(h))
        for i in h:
            r.append("%s %s"%(i,stcnt[i]))
        if len(e) > 0:
            r.append("\nWarnings - Cannot Discern US Section in Q(s):\n")
            for i in e:
                r.append(i)
        return r


# NOTE sqlite limitation:
# cannot use sqlite object created in a different thread
# all sqlite access must be from one thread


# threads and networking section

class node_info:
    nodes = {}
    nodinfo = {}
    lock = threading.RLock()                    # reentrant sharing lock

    def sqd(self,src,seq,t,b,c,rp,p,o,l):
        "process qso data fm net into db"       # excessive cohesion?
        s = qdb.new(src)
        s.seq,s.date,s.call,s.band,s.rept,s.oper,s.logr,s.powr = \
               seq,t,c,b,rp,o,l,p
        s.dispatch('net')

    def netnum(self,ip,mask):
        "extract net number"
        i,m,r = [],[],{}
        i = string.split(ip,'.')
        m = string.split(mask,'.')
        for n in (0,1,2,3):
            r[n] = ival(i[n]) & ival(m[n])
        return "%s.%s.%s.%s"%(r[0],r[1],r[2],r[3])

    def ssb(self,pkt_tm,host,sip,nod,stm,stml,ver,td):
        "process status broadcast (first line)"
        self.lock.acquire()
        if not self.nodes.has_key(nod):      # create if new
            self.nodes[nod] = node_info()
            if nod != node:
                print "New Node Heard",host,sip,nod,stm,stml,ver,td
        i = self.nodes[nod]
##        if debug: print "ssb before assign",i.nod,i.stm,i.bnd
        i.ptm,i.nod,i.host,i.ip,i.stm,i.age = \
                pkt_tm,nod,host,sip,stm,0
        self.lock.release()
     #   if debug:
      #  print "ssb:",pkt_tm,host,sip,nod,stm,stml,ver,td

    def sss(self,pkt_tm,fnod,sip,nod,seq,bnd,msc,age):
        "process node status bcast (rest of bcast lines)"
        self.lock.acquire()
        key = "%s-%s"%(fnod,nod)
        if not self.nodinfo.has_key(key):
            self.nodinfo[key] = node_info()  # create new
##            if debug: print "sss: new nodinfo instance",key
        i = self.nodinfo[key]
        i.tm,i.fnod,i.fip,i.nod,i.seq,i.bnd,i.msc,i.age = \
              pkt_tm,fnod,sip,nod,seq,bnd,msc,int(age)
        self.lock.release()
##        if debug:
      #  print "sss:",i.age,i.nod,i.seq,i.bnd

    def age_data(self):
        "increment age and delete old band"
        t = now()[7:] # time hhmmss
        self.lock.acquire()
        for i in self.nodinfo.values():
            if i.age < 999: i.age += 1
##            if debug: print "ageing nodinfo",i.fnod,i.nod,i.bnd,i.age
            if i.age > 55 and i.bnd:
                print t,"age out info from",i.fnod,"about",i.nod,"on",i.bnd,"age",i.age
                i.bnd = ""
        for i in self.nodes.values():
            if i.age < 999: i.age += 1
        self.lock.release()

    def fill_requests_list(self):
        "return list of fills needed"
        r = []
        self.lock.acquire()
        for i in self.nodinfo.values():     # for each node
            j = qdb.hiseq.get(i.nod,0)
            if int(i.seq) > j:              # if they have something we need
                r.append((i.fip,i.nod,j+1)) # add req for next to list
##                if debug: print "req fm",i.fip,"for",i.nod,i.seq,"have",j+1
        self.lock.release()
        return r                            # list of (addr,src,seq)

    def node_status_list(self):
        "return list of node status tuples"
        sum = {}                            # summary dictionary
        self.lock.acquire()
        i = node_info()                  # update our info
        i.nod,i.bnd,i.age = node,band,0
        i.msc = "%s %s %sW" % (exin(operator), exin(logger), power)
        sum[node] = i

        for i in qdb.hiseq.keys():          # insure all db nod on list
            if not sum.has_key(i):          # add iff new
                j = node_info()
                j.nod, j.bnd, j.msc, j.age = i, '', '', 999
                sum[i] = j
##                if debug: print "adding nod fm db to list",i

        for i in self.nodinfo.values():     # browse bcast data
            if not sum.has_key(i.nod):
                j = node_info()
                j.nod, j.bnd, j.msc, j.age = i.nod, '', '', 999
                sum[i.nod] = j
            j = sum[i.nod]                  # collect into summary
##            if debug:
##                print "have",      j.nod,j.age,j.bnd,j.msc
##                print "inspecting",i.nod,i.age,i.bnd,i.msc
            if i.age < j.age:              # keep latest wrt src time
##                if debug:
##                    print "updating",j.nod,j.age,j.bnd,j.msc,\
##                                "to",      i.age,i.bnd,i.msc
                j.bnd,j.msc,j.age = i.bnd,i.msc,i.age
        self.lock.release()

        r = []                              # form the list (xx return sum?)
        for s in sum.values():
            seq = qdb.hiseq.get(s.nod,0)    # reflect what we have in our db
            if seq or s.bnd:                # only report interesting info
                r.append((s.nod,seq,s.bnd,s.msc,s.age))
        return r                            # list of (nod,seq,bnd,msc,age)

    def nod_on_band(self,band):
        "return list of nodes on this band"
        r = []
        for s in self.node_status_list():
##            print s[0],s[2]                 # (nod,seq,bnd,msc,age)
            if band == s[2]:
                r.append(s[0])
        return r

    def nod_on_bands(self):
        "return dictionary of list of nodes indexed by band and counts"
        r,hf,vhf,gota = {},0,0,0
        for s in self.node_status_list():
##            print s[0],s[2]
            if not r.has_key(s[2]):
                r[s[2]] = []
            r[s[2]].append(s[0])
            if s[2] == 'off' or s[2] == "": continue
            if s[0] == 'gota': gota += 1
            else:
                b = ival(s[2])
                if b > 8 and b < 200: hf  += 1
                if b < 8 or  b > 200: vhf += 1

        return r,hf,vhf,gota


# new message class
# needed for filler to work with tcp

class MESSAGE:
    def __init__(self,host,port,mode,mesg):
        "construct a message"
        self.time = now()               # arrival/creation time
        self.host = host                # remote host dotted ip text
        self.port = port                # remote port text
        self.mode = mode                # tcp or udp or bcast text
        self.mesg = mesg                # message content text
        self.authok = self.ckauth(mesg) # authorization check boolean

        if mode == 'udp': self.adr_str = host
        else:             self.adr_str = "%s:%s"%(host,port)

        # might want a processing status indicating where the meesage came from, what has been
        # done to it, what needs to be done; has it been broadcast, has it been logged to the journal,
        # etc.

    def reply(self,reply_mesg):
        "construct a reply message"
        reply = MESSAGE(self.host,self.port,self.mode,reply_mesg)
        return reply
    def send(self):
        net.send_msg(self)
    def bcast(self):
        self.mode = 'bcast'
        self.send()

# copied the auth methods here, probably will move them
# or set up a relationship between message and network classes
##    def setauth(self,newauth):
##        "set authentication key code base, copy on use"
##        global authk
##        authk = newauth
##        seed = "2004070511111akb"               # change when protocol changes
##        self.authkey = hashlib.md5(newauth+seed)

    def auth(self,msg):
        "calc authentication hash"
        h = net.authkey.copy()
        h.update(msg)
        return h.hexdigest()

    def ckauth(self,msg):
        "check authentication hash"
        h,m = msg.split('\n',1)
##        print h; print self.auth(m); print
        return h == self.auth(m)


class netsync:
    "network database synchronization"

    netmask = '255.255.255.0'

    authkey = hashlib.md5()
    pkts_rcvd,fills,badauth_rcvd,send_errs = 0,0,0,0
    hostname = socket.gethostname()
    my_addr = socket.gethostbyname(hostname)                # fails on some systems
    bc_addr = '<broadcast>'                                 # udp broadcast address
    udp_skt = None
    pkts_prev = 0

##    if my_addr[:3] == '10.':
##        bc_addr = '10.255.255.255'
##        netmask = '255.0.0.0'
##    else:
##        bc_addr = re.sub(r'[0-9]+$','255',my_addr)          # calc bcast addr

    si = node_info()                                        # create node info object



    # new tcp/udp code section
    #
    # tcp penetrates home routers more conveniently
    # so handle remote stations with tcp
    # server listens for any connections, logs them,
    # deletes on error
    # this will retire some of the old code when placed in service
    # reorganizes the flow of data from network sockets of both types
    # refactored old code

    rem_host = "0.0.0.0"                                    # remote tcp address
   # rem_host = "192.168.1.107"                              # test

    #rem_cli = 0                                             # tcp client enable flag
    #rem_srv = 0                                             # tcp server enable flag

    tcp_conn = {} # tcp connection dictionary, index by socket_str, store (socket,(host,port))

    def socket_str(self,addr):
        "convert address tuple to string"
        # use this for tcp addresses, if no :port then must be udp
        host,port = addr
        str_addr = '%s:%s'%(host,port)

    def tcp_manager(self):
        "tcp service manager thread"
        # this thread should just accept connections and make threads to respond
        self.tcp_thread = {}  # service threads
        time.sleep(1)
        print "starting TCP service manager on",self.my_addr
        while 1:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.bind(("", tcp_port))
            s.listen(1)
            while 1: # incoming tcp connection, launch a handler
                c = s.accept()   # returns socket object and (host,port) tuple
                sock,addr = c
                addr_str = "%s:%d"%addr #self.socket_str(addr)
                self.tcp_conn[addr_str] = c         # store socket and addr tuple
                print "launching TCP service thread",addr_str
                th = threading.Thread(target=self.tcp_server,args=(addr_str,))
                th.start()
                self.tcp_thread[addr_str] = th
            s.close()
            time.sleep(13)
            print "remote TCP service manager restarting"

    def tcp_server(self,addr_str):
        "receive tcp stream and process them for one client"
        print "TCP service thread starting on",addr_str
        skt,addr = self.tcp_conn[addr_str]          # get connection socket
        while 1:
            if not self.rcv_tcp(addr_str): break    # quit on error
        del(self.tcp_conn[addr_str])                # socket deleted fm table
        skt.close()                                 # cleanup lost connection
        print "TCP server quitting"

    def tcp_client(self):
        "launch client thread and connect to remote TCP server"
        # only one of these, only one remote connection establishment per client
        # this thread which keeps connecting
        # until the remote client mode is disabled
        time.sleep(3)
        while 1:
            rem_host = self.rem_host
            if rem_host == '0.0.0.0':
                time.sleep(11)
                continue
            rem_adr = (rem_host,tcp_port)
            adr_str = "%s:%s"%rem_adr
            print "TCP client connecting to",rem_adr
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.bind(('',self.port+1))
            try:
                s.connect(rem_adr)
                print "TCP client connected to",rem_adr
                self.tcp_conn[adr_str] = s,(rem_adr)        # add to connection list
                print len(self.tcp_conn),"tcp connections"
                while rem_host == self.rem_host:
                    if not self.rcv_tcp(adr_str):           # receive and process messages
                        break
            except:
                print "TCP client exception to",rem_host
                #raise  # normally this is commented out but can be useful for test
            try: del(self.tcp_conn[adr_str])                # indicate connection disabled
            except: pass
            s.close()
            time.sleep(19)                                  # retry interval
        print "tcp_client quitting"


    def rcv_tcp(self,adr_str):
        "receive and process one TCP message"
        s,adr = self.tcp_conn.get(adr_str,None)
        mode,msg,hdr = "tcp","",""
       # print "rcv_tcp",adr_str
        if s == None:
            print "rcv_tcp on bad socket"
            return False
        try:
            while len(hdr) < 3:                             # get header
                hdr += s.recv(3-len(hdr))
            if ord(hdr[0]) ^ ord(hdr[1]) != ord(hdr[2]):
                print "rcv_tcp bad header", ord(hdr[0]),ord(hdr[1]),ord(hdr[2])
                return False
            len_read = ord(hdr[0]) + 256*ord(hdr[1])
            if debug: print "rcv_tcp length",len_read
            if len_read > 8200:
                print "rcv_tcp msg too long",len_read
                return False
            while len(msg) < len_read:
                msg += s.recv(len_read-len(msg))            # read exact until have it all
            if debug: print "rcv_tcp msg",adr_str #,msg
           # print msg
        except:
            print "rcv_tcp exception",adr_str,msg
            #raise
            return False
        self.pkts_rcvd += 1
        host,port = adr
        message = MESSAGE(host,port,mode,msg)
        return self.proc_message(message)                   # process if valid

    def rcv_udp(self):
        "receive and process UDP messages"
        # replaces old rcvr thread below
        # need to start this before sending UDP messages
        if debug: print "UDP receiver thread starting"
        r = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        r.bind(('',self.port))
        mode = 'udp'
        while 1:
            # need to handle errors and clean shutdown of ports during exit
            # perhaps terminating the threads will be sufficient if the
            # connections are not cached, have to test it
            # hard to force shutdown since threads are blocked
            # no easy way to terminate threads either
            # so try closing sockets even though threads are waiting
            msg,addr = r.recvfrom(800)                      # get a message
            host,port = addr
            if host != self.my_addr: self.pkts_rcvd += 1    # count other machine pkts
            message = MESSAGE(host,port,mode,msg)
            self.proc_message(message)

    def proc_message(self,message):
        "process received message object"
        pkt_tm = message.time                                   # time of receipt
        msg = message.mesg
        addr = message.adr_str
        host,sip,fnod,stm = '','','',''
        if debug: print "proc_message: %s  %s\n"%(addr,msg)
        if not self.ckauth(msg):                                # authenticate packet
            #if debug: sms.prmsg("bad auth from: %s"%addr)
            print "bad auth from:",addr
            self.badauth_rcvd += 1
            return False
        lines = msg.split('\n')                                 # decode lines
        for line in lines[1:-1]:                                # skip auth hash, blank at end
##            if debug: sms.prmsg(line)
            fields = line.split('|')
            # if message came from tcp the sip (src ip) needs to have port added
            # but this has to be done for each message type
            # in the appropriate place. WRONG, need to pick up
            # real from address and ignore the one in the packet!

            if fields[0] == 'b':                                # status bcast
                host,sip,fnod,stm,stml,ver = fields[1:]
                # hostname, source ip, from node, source time, source time level, version

##                if message.mode == 'tcp':                       # fix tcp src ip
##                    sip += ":"+str(message.port)
                    #print "tcp sip",sip
               # else:
                    #print "udp sip",sip
##                print
##                print "processing broadcast"
##                print "addr",addr
##                print "sip",sip
##                print
                sip = addr # the real deal
                td = tmsub(stm,pkt_tm)                          # time subtract for error
                self.si.ssb(pkt_tm,host,sip,fnod,stm,stml,ver,td)
                mclock.calib(fnod,stml,td)                      # clock calibration
                if abs(td) >= tdwin:
                    print 'clock err',td,host,sip,fnod,pkt_tm
                if showbc:
                    print "bcast",host,sip,fnod,ver,pkt_tm,td
            elif fields[0] == 's':                              # source status
                nod,seq,bnd,msc,age = fields[1:]
                #if debug: print pkt_tm,fnod,sip,stm,nod,seq,bnd,msc
                self.si.sss(pkt_tm,fnod,sip,nod,seq,bnd,msc,age)
            elif fields[0] == 'r':                              # fill request
                destip,src,seq = fields[1:]
##                if message.mode == 'tcp':                       # if tcp add port
##                    destip += ":"+str(message.port)
                destip = addr
                #if debug: print destip,src,seq
                self.send_qsomsg(src,seq,destip)
            elif fields[0] == 'q':                              # qso data
                src,seq,stm,b,c,rp,p,o,l = fields[1:]
                #if debug: print src,seq,stm,b,c,rp,p,o,l
                self.si.sqd(src,seq,stm,b,c,rp,p,o,l)
            else:
                sms.prmsg("msg not recognized %s"%addr)
                return False
        return True


# another interesting issue (several actually)
#
# fill requests
#   need to pass more info about address and transport (port,...)
#
# status info
#   status needs to store more info about address and transport (port,...)
#
# note that both above issues solved by using addr:port for tcp and addr for udp
#
#
# message info
#   wondering if the message info should be broken down into fields or a sub dictionary of them
#   made to be part of the message object
#   so perhaps 'contents' would be a dictionary of the key,values of a message
#   might want to use json to package up a dictionary as the message instead of the
#   present text format?
#
# JSON thoughts
#   good for encoding dictionary to/from the network
#   could store JSON in the journal directly (maybe better than SQL)
#   short keys would be advisable as they are always sent
#   the JSON should be ADIF compatible, if that makes any sense
#     it may make sense to map the common ADIF field names to shorter values for the JSON efficiency
#
# JSON over TCP/IP only? (possible future idea, didn't do this yet)
#   why JSON?
#     easier to add fields
#     better compatibility with different versions (maybe, somewhat)
#
# JSON keys brainstorming (try to keep to 1/2/3 letters per key)
#
#   S,N   source journal identifier, journal sequence number
#   T   timestamp when sent?
#   q   qso callsign
#   t   qso time/date
#   b   band
#   f   frequency
#   m   operating mode (see ADIF format)
#   p   power
#   r   report
#   c   notes, comments
#   o   operator
#   l   logger
#
#   I,P,X   message received from ip,port,transport
#
#
# it begins to look as though the infrastructure for storing this host info should be reworked
#   perhaps we should have a memory based sqlite database for storing transient info?
#   this would have the advantage of avoiding explicit locks in python, allowing transactions
#   to be used instead, if they are needed
#     or just use objects...


    def send_msg(self,message):
        "route and send network message from a message object"
        # form tcp and udp messages
        msg = message.mesg
        if type(msg) == type(u'unicode'):       # convert unicode to ascii
            msg = msg.encode('utf-8')
     #   print "type msg",type(msg)
        adr_str = message.adr_str
        host = message.host
        umsg = self.auth(msg)+'\n'+msg          # make udp message
        tlen = len(umsg)                        # make tcp message
        if tlen > 8200:
            print "error, send_msg too long",tlen,"dropping to",adr_str
            return
        # making 3B header for tcp with two byte length, lsB first, and
        # third byte xor of first two
        i = tlen&255
        j = tlen>>8
        tmsg = chr(i) + chr(j) + chr(i^j) + umsg # umsg must be ascii
        # where did umsg become unicode and what have you done with my ascii?
        # sockets can't take unicode, will convert to bytes, not good if it crashes
        if message.mode == 'bcast':
            if debug: print
##            if len(self.tcp_conn) > 0:
##                print "broadcasting (tcp:%d)"%len(self.tcp_conn)
            if debug: print msg,
            self.send_udp(self.bc_addr,umsg)    # send to udp broadcast
            for a in self.tcp_conn:             # send to tcp clients
                self.send_tcp(a,tmsg)
        elif message.mode == 'tcp':
            if self.tcp_conn.get(adr_str,None):
                self.send_tcp(adr_str,tmsg)     # if in tcp list, send to tcp (priority)
            else:
                print "tcp send fail no conn",adr_str
        else:
            self.send_udp(host,umsg)            # otherwise send to udp

    def send_tcp(self,adr_str,tmsg):
        "send a TCP message"
        c = self.tcp_conn.get(adr_str,None)
        if c == None:                           # dead connection
            print "sent_tcp fail to conn None",adr_str
            return
        skt,adr = c
        if debug: print "send_tcp to ",adr_str,len(tmsg)
        try:
            skt.sendall(tmsg)                   # send all the bytes of the message
        except socket.error,e:
            self.send_errs += 1
            print "error, send_tcp failed %s %s [%s]"%(now(),e.args,adr_str)

# udp and tcp are fundamentally different (even though they share a lot)
# we do udp on one port, one host per ip
# tcp may be using different ports on the same ip for different hosts (NAT routing)
# how does filler get back to the right host in the tcp case? FIXED
# new message object solves this problem by carrying the extra info needed

    def send_udp(self,host,umsg):
        "send a UDP message either a broadcast or a unicast"
        # two cases, broadcast or directed UDP (fill request response)
        # this is determined by the sender and encoded in the host address
        # the host address is in the x.x.x.x format

        #return # TCP test, silently disable udp transmissions

        if debug: print "send_udp to ",host #,self.port #; print umsg

##        print "  udp transmission skipped for debug" # testing
##        return # testing

        if self.udp_skt == None:
            print "uninit UDP socket"
            return
        try:
            self.udp_skt.sendto(umsg,(host,self.port))
        except socket.error,e:
            self.send_errs += 1
            print "error, send_udp failed %s %s [%s]"%(now(),e.args,host)

    def close_all(self):
        "close all network sockets"
        print "  closing udp"
        if self.udp_skt:                    # close the shared udp socket if it is open
            s = self.udp_skt
            self.udp_skt = None
            try: s.close()
            except: pass
        print "  closing tcp"
        for a,s in self.tcp_conn.items():   # close all the open tcp sockets
            del(self.tcp_conn[a])
            try: s.close()
            except: pass


    # old udp code from here on

    def setport(self,useport):
        "setup network udp port"
        self.port = useport
        self.udp_skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   # send socket
        self.udp_skt.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) # Erics linux fix
        try:
            self.udp_skt.bind((self.my_addr,self.port+1))                # outbound udp port
        except:
            print "ERROR - failed to bind UDP port"

# seem to be having a new problem 5/2013
#   error: [Errno 10048] Only one usage of each socket address
#     (protocol/network address/port) is normally permitted
#   perhaps due to a recent windoze update that changed port behavior
#   seems to require a reboot to clear the port
#   or killing pythonw process tree after closing the interpreter
#   this was improved by closing the socket when exiting the program,
#   need to do this for all the sockets that are open
#   this is mostly an IDLE deugger problem
# added the try/except 6/2016, this allows FDLog to run but some threads fail,
#   useful for testing at least

    def setauth(self,newauth):
        "set authentication key code base, copy on use"
        global authk
        authk = newauth
        seed = "2004070511111akb"               # change when protocol changes
        self.authkey = hashlib.md5(newauth+seed)

    def auth(self,msg):
        "calc authentication hash"
        h = self.authkey.copy()
        h.update(msg)
        return h.hexdigest()

    def ckauth(self,msg):
        "check authentication hash"
        h,m = msg.split('\n',1)
##        print h; print self.auth(m); print
        return h == self.auth(m)


# sndmsg must be taught to send tcp to remote sites
# probably should be split for sending both udp and tcp message types
# will be replaced by new version above

    def sndmsg(self,msg,addr):
        "send message to address replacing old version"
        # interface old messaging to new, handles tcp
        if ':' in addr:                           # tcp addresses include port
            host,port = addr.split(':')
            mode = 'tcp'
        elif addr == 'bcast':
            host,port,mode = '','','bcast'
        else:
            host,port,mode = addr,self.port,'udp' # udp addresses are host only, port is fixed
        message = MESSAGE(host,port,mode,msg)
        message.send()

    def sndmsgX(self,msg,addr):
        "send message to address"
        if authk != "" and node != "":
            amsg = self.auth(msg)+'\n'+msg
            #print "auth len",len(self.auth(msg))
            addrlst = []
            if addr == 'bcast':
                addrlst.append(self.bc_addr)
##                addrlst.append(self.rem_adr)
##                for a in node_info.rembcast.keys():
##                    if debug: print "adding dyn remaddr",a
##                    addrlst.append(a)
            else: addrlst.append(addr)
            for a in addrlst:
                if a == "": continue
                if a == '0.0.0.0': continue
                if debug: print "send to ",a ; print msg
                try:
                    self.skt.sendto(amsg,(a,self.port))
                except socket.error,e:
                    self.send_errs += 1
                    print "error, pkt xmt failed %s %s [%s]"%(now(),e.args,a)

    def send_qsomsg(self,nod,seq,destip):
        "send q record"
        key = nod + '.' + str(seq)
        if qdb.byid.has_key(key):
            i = qdb.byid[key]
            msg = "q|%s|%s|%s|%s|%s|%s|%s|%s|%s\n"%\
                (i.src,i.seq,i.date,i.band,i.call,i.rept,i.powr,i.oper,i.logr)
            self.sndmsg(msg,destip)

    def bc_qsomsg(self,nod,seq):
        "broadcast new q record"
        self.send_qsomsg(nod,seq,self.bc_addr)

    def bcast_now(self):
        "broadcast node status message now"
        tm,lev = nowms()
        msg = "b|%s|%s|%s|%s|%s|%s\n"%\
              (self.hostname,self.my_addr,node,tm,lev,version)
       # print "node",type(node)  # node is unicode, causing problems, probably from dbase
        for i in self.si.node_status_list():
            msg += "s|%s|%s|%s|%s|%s\n" % i     # nod,seq,bnd,msc,age
            #if debug: print i
       # print msg
        self.sndmsg(msg,'bcast')                # broadcast it

    def bcast_time(self):
        "broadcast brief and prompt time message"
        # used by time master only, at 1hz intervals for better time sync
        tm,lev = nowms()
        msg = "b|%s|%s|%s|%s|%s|%s\n"%\
              (self.hostname,self.my_addr,node,tm,lev,version)
       # print "node",type(node)  # node is unicode, causing problems, probably from dbase
##        for i in self.si.node_status_list():
##            msg += "s|%s|%s|%s|%s|%s\n" % i     # nod,seq,bnd,msc,age
##            #if debug: print i

        self.sndmsg(msg,'bcast')                # broadcast it

        #print msg


# requesting fills is about to get more complicated
# with tcp involved we need to know not just which host requested the fill
# but also which port
# two ways to go, one is to break the protocol,
#   but there is a non protocol breaking alternative
# the other is to carry the requesting host, port and mode clear through
# tempting to make a message class to handle this sort of thing
# for now, if the port is there it is tcp otherwise it is udp

    def fillr(self):
        "filler thread requests missing database records"
        time.sleep(5.0)#0.2)
        if debug: print "filler thread starting"

        while 1:
            time.sleep(.2)                      # periodically check for fills (5 hz)
            if debug: time.sleep(2)             # slow for debug
            r = self.si.fill_requests_list()
            self.fills = len(r)
            if self.fills:
                p = random.randrange(0,len(r))                  # randomly select one
                c = r[p]
                msg = "r|%s|%s|%s\n"%(self.my_addr,c[1],c[2])   # (addr,src,seq)
                self.sndmsg(msg,c[0])                           # send a fill request
                print "req fill",c

    def start(self):
        "launch all net threads"
        global fillrThread,rcvrThread
##        global node
        print "This host:", self.hostname, "IP:",self.my_addr#, "Mask:",self.bc_addr
##        if (self.hostname > "") & (node == 's'):
##            node = self.hostname             # should filter chars
##        print "Node ID:",node
        print "Launching threads"
##        thread.start_new_thread(self.fillr,())
##        thread.start_new_thread(self.rcvr,())
        fillrThread = threading.Thread(target=self.fillr,name="filler")
        fillrThread.start()
#        rcvrThread = threading.Thread(target=self.rcvr,name="receiver")
        rcvrThread = threading.Thread(target=self.rcv_udp,name="udp receiver")
        rcvrThread.start()
        tcpSvcMgrThread = threading.Thread(target=self.tcp_manager,name="tcp manager")
        tcpSvcMgrThread.start()
        tcpClientThread = threading.Thread(target=self.tcp_client,name="tcp client")
        tcpClientThread.start()
        time.sleep(4)                         # let em print
        print "Startup complete"


class global_data: # global data stored in the journal

    byname = {}

    def new(self,name,desc,defaultvalue,okgrammar,maxlen):
        i = global_data()                       # create
        i.name = name                           # set
        i.val = defaultvalue
        i.okg = okgrammar
        i.maxl = maxlen
        i.ts = ""
        i.desc = desc
        self.byname[name] = i
        return i

    def setv(self,name,value,timestamp):
        if node == "":
            text.insert(END,"error - no node id\n")
            return
        if name[:2] == 'p:':                    # set oper/logr
            i = self.byname.get(name,self.new(name,'','','',0))
        else:
            if not self.byname.has_key(name):   # new
                return "error - invalid global data name: %s"%name
            i = self.byname[name]
            if len(value) > i.maxl:             # too long
                return "error - value too long: %s = %s"%(name,value)
            if not re.match(i.okg,value):       # bad grammar
                return "set error - invalid value: %s = %s"%(name,value)
        if timestamp > i.ts:                    # timestamp later?
            i.val = value
            i.ts = timestamp
            if name[:2] == 'p:':
                ini,name,call = string.split(value,', ')
                participants[ini] = value
                if name == 'delete':
                    del(participants[ini])
                buildmenus()
        #else: print "set warning - older value discarded"

    def getv(self,name):
        if not self.byname.has_key(name):       # new
            return "get error - global data name %s not valid"%name
        return self.byname[name].val

    def sethelp(self):
        l = ["   Set Commands\n\n    eg: .set <parameter> <value>\n"]  # spaced for sort
        for i in self.byname.keys():
            if i[:2] != 'p:':                   # skip ops in help display
                l.append("  %-6s  %-43s  '%s'"%(i,self.byname[i].desc,self.byname[i].val))
        l.sort()
        viewtextl(l)

gd = global_data()
for name,desc,default,okre,maxlen in (
        ('class', '<n><A-F>       FD class (eg 2A)','2A',r'([1-9]|[1-3][0-9])[a-fA-F]$',3),
        ('fdcall','<CALL>         FD call','',r'[a-zA-Z0-9]{3,6}$',6),
        ('gcall', '<CALL>         GOTA call','',r'[a-zA-Z0-9]{3,6}$',6),
        ('sect',  '<CC-Ccccc...>  ARRL section','<section>',r'[A-Z]{2,3}-[a-zA-Z ]{2,20}$',24),
        ('grid',  '<grid>         VHF grid square','',r'[A-Z]{2}[0-9]{2}$',4),
        ('grpnam','<text>         group name','',r'[A-Za-z0-9 #.:-]{4,35}$',35),
        ('fmcall','<CALL>         entry from call','',r'[a-zA-Z0-9]{3,6}$',6),
        ('fmnam', '<name>         entry from name','',r'[A-Za-z0-9 .:-]{0,35}$',35),
        ('fmad1', '<text>         entry from address line 1','',r'[A-Za-z0-9 #.,:-]{0,35}$',35),
        ('fmad2', '<text>         entry from address line 2','',r'[A-Za-z0-9 #.,:-]{0,35}$',35),
        ('fmem',  '<text>         entry from email','',r'[A-Za-z0-9@.:-]{0,35}$',35),
        ('public','<text>         public location desc','',r'[A-Za-z0-9@.: -]{0,35}$',35),
        ('infob', '0/1            public info table','0',r'[0-1]$',1),
        ('svego', '<name>         govt official visitor name','',r'[A-Za-z., -]{0,35}$',35),
        ('svroa', '<name>         agency site visitor name','',r'[A-Za-z., -]{0,35}$',35),
        ('youth', '<n>            participating youth','0',r'[0-9]{1,2}$',2),
        ('websub','0/1            web submission bonus','0',r'[0-1]$',1),
        ('psgen', '0/1            using generator power','0',r'[0-1]$',1),
        ('pscom', '0/1            using commercial power','0',r'[0-1]$',1),
        ('psbat', '0/1            using battery power','0',r'[0-1]$',1),
        ('pssolar', '0/1            using solar power','0',r'[0-1]$',1),
        ('pswind', '0/1            using wind power','0',r'[0-1]$',1),
        ('psoth', '<text>         desc of other power','',r'[A-Za-z0-9.: -]{0,35}$',35),
        ('educate', '0/1            educational activity','0',r'[0-1]$',1),
        ('social', '0/1            social media','0',r'[0-1]$',1),
        ('safety', '0/1            safety officer','0',r'[0-1]$',1),
        ('fdstrt','yymmdd.hhmm    FD start time (UTC)','020108.1800',r'[0-9.]{11}$',11),
        ('fdend', 'yymmdd.hhmm    FD end time (UTC)',  '990629.2100',r'[0-9.]{11}$',11),
        ('ckslew','<n>            max clock skew mS/S',  '100',r'([1-9][0-9]|[1-4][0-9][0-9]|500)$',3),
        ('tmast', '<text>         time master node','',r'[A-Za-z0-9-]{0,8}$',8) ):
    gd.new(name,desc,default,okre,maxlen)

class syncmsg:
    "synchronous message printing"
    lock = threading.RLock()
    msgs = []

    def prmsg(self,msg):
        "put message in queue for printing"
        self.lock.acquire()
        self.msgs.append(msg)
        self.lock.release()

    def prout(self):
        "get message from queue for printing"
        self.lock.acquire()
        while self.msgs:
            #print self.msgs[0]
            logw.configure(state=NORMAL)
            logw.see(END)
            nod = self.msgs[0][70:81]               #color local entries
#            print nod,node
            if nod == node:
                logw.insert(END,"%s\n"%self.msgs[0],"b")
#                print "blue '%s' '%s'\n"%(nod,node)
            else:
                logw.insert(END,"%s\n"%self.msgs[0])
            logw.configure(state=DISABLED)
            del self.msgs[0]
        self.lock.release()


# global functions

def now():
    "return current time in standard string format yymmdd.hhmmss"
    n = time.gmtime(time.time()+mclock.offset) # time in utc, with offset to correct to master/gps clock
    t = time.strftime("%y%m%d.%H%M%S",n)       # compact version YY
    return t

def nowms():
    "return best current time in standard string format yymmdd.hhmmss.mmm with milliseconds"

    # update 6/2016 - added 'best' feature to get GPS time if available
    # note that using GPSClock is subject to potential race condition
    # and should only be called from one thread

    gpstm,gpslock,gpserr = mclock.gpsclock()    # try to get GPS time
    if gpslock:                                 # if locked GPS time, use it
        n = time.gmtime(gpstm)                  # convert epoch time to gmt utc
        t = time.strftime("%y%m%d.%H%M%S",n)    # compact version YY
        f,i = math.modf(gpstm)                  # extract milliseconds
        t2 = "%s.%03d"%(t,f*1000)               # apply ms
        if mclock.level == 0: level = 0
        else: level = 1
        #print "nowms gpsclock",gpstm,gpslock,gpserr
        #print "nowms gps",t2,level
        return t2,level

    # no locked gps clock, so use system clock and offset
    x = time.time()+mclock.offset               # epoch time plus offset to correct to master/gps clock
    n = time.gmtime(x)                          # convert epoch time to gmt utc time structure
    t = time.strftime("%y%m%d.%H%M%S",n)        # compact version YY
    f,i = math.modf(x)                          # extract milliseconds
    t2 = "%s.%03d"%(t,f*1000)                   # apply ms
    if mclock.level < 2: level = 2
    else: level = mclock.level
    #print "nowms x",x
    #print "nowms n",n
    #print "nowms t",t
    #print "nowms system",t2,mclock.level
    #print
    return t2,level

def tmtofl(a):
    "time to float in seconds, allow milliseconds"

    #print "tmtofl",a
    return calendar.timegm((2000+int(a[0:2]),int(a[2:4]),int(a[4:6]),\
                       int(a[7:9]),int(a[9:11]),float(a[11:]),0,0,0))

def tmsub(a,b):
    "time subtract in seconds"
    return tmtofl(a) - tmtofl(b)

def testcmd(name, rex, default):
    "set global from command, return value and change status"
    global kbuf
    value = default
    s = "%s +(%s)$"%(name,rex)
    m = re.match(s,kbuf)
    if m:
        value = m.group(1)
        text.insert(END,"\n%s set to %s\n"%(name,value))
        kbuf = ""
    return value,default != value


# new sqlite globals database fdlog.sq3 replacing globals file
#
class GlobalDb:
    def __init__(self):
        self.dbPath = globf[0:-4] + '.sq3'
        print "  Using local value database",self.dbPath

        self.sqdb = sqlite3.connect(self.dbPath)  # connect to the database
        self.sqdb.row_factory = sqlite3.Row       # row factory
        self.curs = self.sqdb.cursor()            # make a database connection cursor
        sql = "create table if not exists global(nam text,val text,primary key(nam))"
        self.curs.execute(sql)
        self.sqdb.commit()
        self.cache = {}                           # use a cache to reduce db i/o
    def get(self,name,default):
        if name in self.cache:
            #print "reading from globCache",name
            return self.cache[name]
        sql = "select * from global where nam == ?"
        results = self.curs.execute(sql,(name,))
        value = default
        for result in results:
            value = result['val']
            #print "reading from globDb", name, value
            self.cache[name] = value
        return value
    def put(self,name,value):
        now = self.get(name,'zzzzz')
        #print now,str(value),now==str(value)
        if str(value) == now: return              # skip write if same
        sql = "replace into global (nam,val) values (?,?)"
        self.curs.execute(sql,(name,value))
        self.sqdb.commit()
        #print "writing to globDb", name, value
        self.cache[name] = str(value)



def loadglob():
    "load persistent local config to global vars from file"
    global globDb,node,operator,logger,power,tdwin,debug,authk,timeok,contest
    globDb = GlobalDb()
    node = globDb.get('node','')
    operator = globDb.get('operator','')
    logger = globDb.get('logger','')
    power = globDb.get('power','100')
    authk = globDb.get('authk','tst')
    tdwin = int(globDb.get('tdwin',5))
    debug = int(globDb.get('debug',0))
    timeok = int(globDb.get('timeok',0))
    netsync.rem_host = globDb.get('remip','0.0.0.0')
    contest = globDb.get('contest','FD')

    mclock.offsetinit()

    if debug: print "  debug:",debug

def saveglob():
    "save persistent local config global vars to file"
    globDb.put('node',node)
    globDb.put('operator',operator)
    globDb.put('logger',logger)
    globDb.put('power',power)
    globDb.put('authk',authk)
    globDb.put('tdwin',tdwin)
    globDb.put('debug',debug)
    globDb.put('timeok',timeok)
    globDb.put('contest',contest)



# contest log section

def getfile(fn):
    "get file contents"

    data = ""
    try:
        fd = file(fn,"r")
        data = fd.read()
        fd.close()
    except:
        pass
    if data != "":
        print "Found file",fn
        #print data
    return data


participants = {} # participants dictionary

def contestlog(pr):
    "generate contest entry and log forms"

    w1aw_msg = getfile("w1aw_msg.txt")          # w1aw bulletin copy


    # National Traffic System Messages

    nts_orig_msg = getfile("nts_msg.txt")       # status message

    nts_msg_relay = []
    for i in range(0,10):                        # relayed messages
        fn = "nts_rly%d.txt"%i
        msg = getfile(fn)
        if msg != "":
            nts_msg_relay.append(msg)

    media_copy = getfile("media.txt")           # media activity

    soapbox = getfile("soapbox.txt")            # soapbox commentary

    fd_call = string.upper(gd.getv('fdcall'))   # prep data
    xmttrs = ival(gd.getv('class'))
    gota_call = string.upper(gd.getv('gcall'))
    if xmttrs < 2: gota_call = ""


    if pr == 0: return                          # only define variables return

    # output the entry, adif & cabrillo log file

    datime = now()
    byid,bycall,gotabycall = qdb.cleanlog()     # get a clean log

    qpb,ppb,qpop,qplg,qpst,tq,score,maxp,cwq,digq,fonq,qpgop,gotaq,nat,sat = \
        qdb.bandrpt()                           # and count it

    print "..",

    sys.stdout = file(logfile,"w")              # redirect output to file

    if contest == "FD":
        
        print "Field Day 20%s Entry Form"%datime[:2]
        print
        print "Date Prepared:              %s UTC"%datime[:-2]
        print
        print "1.  Field Day Call:         %s"%fd_call
        if gota_call != "":
            print "    GOTA Station Call:      %s"%gota_call
        print "2.  Club or Group Name:     %s"%gd.getv('grpnam')
        print "3.  Number of Participants: %s"%len(participants)
        print "4.  Transmitter Class:      %s"%xmttrs
        print "5.  Entry Class:            %s"%string.upper(gd.getv('class'))[-1:]
        print
        print "6.  Power Sources Used:"
        if int(gd.getv('psgen')) > 0:
            print "      Generator"
        if int(gd.getv('pscom')) > 0:
            print "      Commercial"
        if int(gd.getv('psbat')) > 0:
            print "      Battery"
        if int(gd.getv('pssolar')) > 0:
            print "      Solar"
        if int(gd.getv('pswind')) > 0:
            print "      Wind"
        if gd.getv('psoth') != '':
            print "      Other: %s"%(gd.getv('psoth'))
        print
        print "7.  ARRL Section:           %s"%gd.getv('sect')

        print
        print "8.  Total CW QSOs:      %4s  Points: %5s"%(cwq,cwq*2)
        print "9.  Total Digital QSOs: %4s  Points: %5s"%(digq,digq*2)
        print "10. Total Phone QSOs:   %4s  Points: %5s"%(fonq,fonq)
        qsop = cwq*2 + digq*2 + fonq
        print "11. Total QSO Points:                 %5s"%qsop

        print "12. Max Power Used:     %4s  Watts"%maxp
        powm = 5
        if int(gd.getv('psgen')) > 0 or int(gd.getv('pscom')) > 0: powm = 2
        if maxp > 5: powm = 2
        if maxp > 150: powm = 1
        if maxp > 1500: powm = 0
        print "13. Power Multiplier:                  x %2s"%powm

        qso_scor = qsop * powm
        print "14. Claimed QSO Score:                %5s"%qso_scor

        print
        print "15. Bonus Points:"

        tot_bonus = 0

        emerg_powr_bp = 0       # emergency power
        if gd.getv('pscom') == '0':
            emerg_powr_bp = 100 * xmttrs
            if emerg_powr_bp > 2000:
                emerg_powr_bp = 2000
            tot_bonus += emerg_powr_bp
            print "   %4s 100%s Emergency Power (%s xmttrs)"%(emerg_powr_bp,'%',xmttrs)

        media_pub_bp = 0        # media publicity
        if media_copy > "":
            media_pub_bp = 100
            tot_bonus += media_pub_bp
            print "    %3s Media Publicity (copy below)"%media_pub_bp

        public_bp = 0           # operation in a public place
        public_place = gd.getv('public')
        if public_place != "":
            public_bp = 100
            tot_bonus += public_bp
            print "    %3s Set-up in a Public Place (%s)"%(public_bp, public_place)

        info_booth_bp = 0       # public information table
        if int(gd.getv('infob')) > 0 and public_bp > 0:
            info_booth_bp = 100
            tot_bonus += info_booth_bp
            print "    %3s Public Information Table"%info_booth_bp

        nts_orig_bp = 0         # originate Field Day message
        if nts_orig_msg > "":
            nts_orig_bp = 100
            tot_bonus += nts_orig_bp
            print "    %3s Formal message Originated to ARRL SM/SEC (copy below)"%nts_orig_bp

        w1aw_msg_bp = 0         # copy field day message from W1AW or alternate
        if len(w1aw_msg) > 30:  # ignore short file place holder
            w1aw_msg_bp = 100
            tot_bonus += w1aw_msg_bp
            print "    %3s W1AW FD Message Received (copy below)"%(w1aw_msg_bp)

        n = len(nts_msg_relay)  # formal messages handled
        nts_msgs_bp = 10 * n
        if nts_msgs_bp > 100:
            nts_msgs_bp = 100
        if nts_msgs_bp > 0:
            tot_bonus += nts_msgs_bp
            print "    %3s Formal messages handled (%s) (copy below)"%(nts_msgs_bp,n)

        sat_qsos = len(sat)     # satellite QSOs
        sat_bp = 0
        if sat_qsos > 0:
            sat_bp = 100
            tot_bonus += sat_bp
            print "    %3s Satellite QSO Completed (%s/1) (list below)"%(sat_bp,sat_qsos)

        natural_q = len(nat)    # natural power QSOs
        natural_bp = 0
        if natural_q >= 5:
            natural_bp = 100
            tot_bonus += natural_bp
            print "    %3s Five Natural power QSOs completed (%s/5) (list below)"%(natural_bp,natural_q)

        site_visited_ego_bp = 0 # site visits - elected government official
        if gd.getv('svego') > "":
            site_visited_ego_bp = 100
            tot_bonus += site_visited_ego_bp
            print "    %3s Site Visited by elected govt officials (%s)"%(site_visited_ego_bp,gd.getv('svego'))

        site_visited_roa_bp = 0 # site visits - agency representatives
        if gd.getv('svroa') > "":
            site_visited_roa_bp = 100
            tot_bonus += site_visited_roa_bp
            print "    %3s Site Visited by served agency official (%s)"%(site_visited_roa_bp,gd.getv('svroa'))

        gota_max_bp = 0         # GOTA station (GOTA coach needed also?)
        if gotaq >= 100:
            gota_max_bp = 100
            tot_bonus += gota_max_bp
            print "    %3s GOTA Station 100 QSOs bonus achieved"%(gota_max_bp)

        youth_bp = 0            # youth participation
        if int(gd.getv('youth')) > 0:
            youth_bp = 20 * int(gd.getv('youth'))
            if youth_bp > 5 * 20:
                youth_bp = 5 * 20
            tot_bonus += youth_bp
            print "    %3s Youth Participation Bonus"%(youth_bp)

        educ_activ_bp = 0       # educational activity
        if int(gd.getv('educate')) > 0:
            educ_activ_bp = 100
            tot_bonus += educ_activ_bp
            print "    %3s Educational Activity"%educ_activ_bp

        soc_media_bp = 0        # social media
        if int(gd.getv('social')) > 0:
            soc_media_bp = 100
            tot_bonus += soc_media_bp
            print "    %3s Social Media"%soc_media_bp

        safety_bp = 0           # safety officer
        if int(gd.getv('safety')) > 0:
            safety_bp = 100
            tot_bonus += safety_bp
            print "    %3s Safety Officer"%safety_bp

        web_sub_bp = 0          # web submission bonus (keep this one last)
        if gd.getv('websub') == "1":
            web_sub_bp = 50
            tot_bonus += web_sub_bp
            print "    %3s Web Submission Bonus"%(web_sub_bp)
        print
        print "    Total Bonus Points Claimed: %5s"%tot_bonus
        print
        tot_scor = qso_scor + tot_bonus
        print "    Total Claimed Score:        %5s"%tot_scor
        print
        print "16. We have observed all competition rules as well as all regulations"
        print "    for amateur radio in our country. Our report is correct and true"
        print "    to the best of our knowledge. We agree to be bound by the decisions"
        print "    of the ARRL Awards Committee."
        print
        print "Submitted By:"
        print
        print "    Date:     %s UTC"%datime[:-2]
        print "    Call:     %s"%string.upper(gd.getv('fmcall'))
        print "    Name:     %s"%gd.getv('fmnam')
        print "    Address:  %s"%gd.getv('fmad1')
        print "    Address:  %s"%gd.getv('fmad2')
        print "    Email:    %s"%gd.getv('fmem')
        print
        print
        print "Field Day Call: %s"%string.upper(fd_call)
        print

        print "17. QSO Breakdown by Band and Mode"
        print
        print "        ----CW----  --Digital-  ---Phone--"
        print "  Band  QSOs   PWR  QSOs   PWR  QSOs   PWR"
        print
        qsobm, pwrbm = {}, {}
        for b in (160,80,40,20,15,10,6,2,220,440,1200,'sat','gota'):
            if b == 'gota' and gota_call == "": continue
            print "%6s"%b,
            for m in 'cdp':
                bm = "%s%s"%(b,m)
                print "%5s %5s"%(qpb.get(bm,0),ppb.get(bm,0)),
                qsobm[m] = qsobm.get(m,0) + qpb.get(bm,0)
                pwrbm[m] = max(pwrbm.get(m,0), ppb.get(bm,0))
            print
        print
        print "Totals",
        print "%5s %5s"%(qsobm['c'],pwrbm['c']),
        print "%5s %5s"%(qsobm['d'],pwrbm['d']),
        print "%5s %5s"%(qsobm['p'],pwrbm['p'])
        print
        print

        if gota_call:
            print "18. Callsigns and QSO counts of GOTA Operators"
            print
            print "      Call  QSOs"
            for i in qpgop.keys():
                print "    %6s   %3s"%(i,qpgop[i])
            print "    %6s   %3s"%("Total",gotaq)
            print
            print

        print "Dupe Lists sorted by Band, Mode and Call:"
        print

    print "  Main Station(s) Dupe List (%s)"%fd_call
    l = []
    for i in bycall.values():
        l.append("    %4s %s"%(i.band,i.call))
    l.sort()
    b2,n = "",0
    for i in l:
        b,c = i.split()
        if (b == b2) & (n < 5):         # same band, 5 per line
            print "%-10s"%c,
            n += 1
        else:
            print
            print "    %4s   %-10s"%(b,c),
            b2 = b
            n = 1
    print
    print
    print

    if gota_call > "":
        print "  GOTA Station Dupe List (%s)"%gota_call
        l = []
        for i in gotabycall.values():
            l.append("    %4s %s"%(i.band,i.call))
        l.sort()
        b2,n = "",0
        for i in l:
            b,c = i.split()
            if (b == b2) & (n < 5):     # same band
                print "%-10s"%c,
                n += 1
            else:
                print
                print "    %4s   %-10s"%(b,c),
                b2 = b
                n = 1
        print
        print
        print

    if len(w1aw_msg) > 30:
        print "W1AW FD Message Copy"
        print
        print "%s"%w1aw_msg
        print
        print

    if nts_orig_msg != "":
        print "Originated NTS Message"
        print
        print nts_orig_msg
        print
        print

    if len(nts_msg_relay) > 0:
        print "RELAYED NTS Messages"
        print
        for i in nts_msg_relay:
            print i
            print
        print

    if media_copy != "":
        print "Media Copy"
        print
        print media_copy
        print
        print

    if len(nat) > 0:
        print "Natural Power QSOs (show first 10 logged)"
        print
        l = []
        for i in nat:
            ln = "%8s %5s %-10s %-18s %4s %-6s %-6s %4s %s"%\
                 (i.date[4:11],i.band,i.call,i.rept[:18],i.powr,i.oper,i.logr,i.seq,i.src)
            l.append(ln)
        l.sort()
        j = 0
        for i in l:
            print i
            j += 1
            if j > 9: break
        print
        print

    if len(sat) > 0:
        print "Satellite QSOs (show 5)"
        print
        l = []
        for i in sat:
            ln = "%8s %5s %-10s %-18s %4s %-6s %-6s %4s %s"%\
                 (i.date[4:11],i.band,i.call,i.rept[:18],i.powr,i.oper,i.logr,i.seq,i.src)
            l.append(ln)
        l.sort()
        j = 0
        for i in l:
            print i
            j += 1
            if j > 4: break
        print
        print

    if soapbox != "":
        print "Soapbox Comments"
        print
        print soapbox
        print
        print

    print "Logging and Reporting Software Used:\n"
    print prog

    if contest == "FD":
        
        print "===================== CLIP HERE ============================"
        print
        print "(do not include below in ARRL submission)"

        print
        print "Submission Notes"

        print """

        email files as attachments to FieldDay@arrl.org within 30 days!!!
        web entry at www.b4h.net/cabforms

            fdlog.log log file, less log detail below 'CLIP HERE'
            proof of bonus points, as needed:
                public info booth picture, visitor list, info
                visiting officials pictures
                media visiting pictures
                natural power pictures
                demo stations pictures
            plus other interesting pictures

        """

    print "Participant List"
    print
    l = []
    for i in participants.values():
        l.append(i)
    l.sort
    n = 0
    for i in l:
        n += 1
        print "  %4s %s"%(n,i)
    print

    print
    print "QSO breakdown by Station"
    print
    for i in qpst.keys():
        print "  %4s %s"%(qpst[i],i)
    print
    print
    print "QSO breakdown by Operator"
    print
    for i in qpop.keys():
        print "  %4s %s"%(qpop[i],i)
    print
    print
    print "QSO breakdown by Logger"
    print
    for i in qplg.keys():
        print "  %4s %s"%(qplg[i],i)
    print
    print

    if contest == "FD":
        
        print "Worked All States during FD Status"
        print
        r = qdb.wasrpt()
        for i in r:
            print i
        print
        print

    print "Detailed Log"
    print
    print "  Date Range",gd.getv('fdstrt'),"-",gd.getv('fdend'),"UTC"
    print
    qdb.prlog()
    print
    print

    print "ADIF Log"
    print
    qdb.pradif()
    print

    if contest == "VHF":
        print "VHF Cabrillo"
        print
        qdb.vhf_cabrillo()
        print

    print "eof"

    sys.stdout = sys.__stdout__                 # revert print to console
    print
    print "entry and log written to file",logfile

# end of report generation


# global section, main program

# setup persistent globals before GUI

suffix   = ""
call     = ""
band     = "off"
power    = "0"
operator = ""
logger   = ""
node     = ""
authk    = ""
tcp_port = 5100                 # yahoo webcam port, allowed thru work firewall
port_base = 7373
tmob     = now()                # time started on band in min
tdwin    = 10                   # time diff window on displaying node clock diffs
showbc   = 1                    # show broadcast
debug    = 0

logdbf   = "data/fdlog.fdd"          # persistent file copy of log database
logfile  = "data/fdlog.log"          # printable log file (contest entry)
globf    = "data/fdlog.dat"          # persistent global file

kbuf     = ""                   # keyboard line buffer

loadglob()                      # load persistent globals from file


# FDLog GUI Startup Dialog Window

print

runfdlog = 0  # keep track of Run FDLog button

def doCmd(self):
    global node,authk,runfdlog,contest
    node = nodeEntry.get().strip()
    authk = keyEntry.get().strip()
    contest = contestBox.get()
    #print contest
    #print "doCmd",node,authk
    if not re.match(r'[-a-zA-Z0-9]{3,8}$',node):
        print "error, Node ID not valid: '%s'"%node
        return
    if not re.match(r'[-a-zA-Z0-9]{3,12}$',authk):
        print "error, Authorization Key not valid: '%s'"%authk
        return
    runfdlog = 1 # *0 # for testing
    self.root.destroy()  # kill the startup window

if node == '':
    node = socket.gethostname()
    node = node.replace(' ','')
    node = node[:8]
    
if authk == '':
    authk = 'tst' # default auth key

k = authk

import Tkinter #(double import?) don't like this, the original Tkinter import is *
# eventually should be cleaned up one way or the other

contestType = ["FD","VHF"]

class myApp(Tkinter.Frame):
    def __init__(self,title):
        #self.frame = Tkinter.Frame()
        self.root = Tkinter.Tk()
        self.frame = Tkinter.Frame()
        self.frame.grid()
        self.frame.master.title(title)
        global nodeEntry,keyEntry,contestBox
        Tkinter.Label(self.frame,text=title).grid(sticky=Tkinter.EW)
        Tkinter.Label(self.frame,text="Select Contest").grid(sticky=Tkinter.EW)
        contestBox = Tkinter.Spinbox(self.frame,values=contestType)
        contestBox.grid(sticky=Tkinter.EW)
        contestBox.delete(0,"end")
        contestBox.insert(0,contest)
        Tkinter.Label(self.frame,text="This Node ID").grid(sticky=Tkinter.EW)
        nodeEntry = Tkinter.Entry(self.frame)
        nodeEntry.grid(sticky=Tkinter.EW)
        nodeEntry.insert(0,node)
        Tkinter.Label(self.frame,text="Authorization Key").grid(sticky=Tkinter.EW)
        keyEntry = Tkinter.Entry(self.frame)
        keyEntry.grid(sticky=Tkinter.EW)
        keyEntry.insert(0,authk)

        Tkinter.Button(self.frame,text="Run FDLog",\
            command=lambda : doCmd(self)).grid(sticky=Tkinter.EW)

        Tkinter.Button(self.frame,text="ABORT",\
            command=lambda : os._exit(1)).grid(sticky=Tkinter.EW)


# comment out this region (next 3 lines of code) to make FDLog bypass the input dialog for testing
app = myApp("FDLog Version "+version[1:])
app.frame.mainloop()

# if the RunFDLog button was not pressed, exit FDLog
# this insures that the conditions are met before running FDLog
if not runfdlog: os._exit(1)

if k != authk:
    print "New Key entered, operator and logger cleared"
    operator = ""
    logger   = ""
    print

print "Using Authentication Key: '%s'"%authk
print "Using",authk[0:3],"for setting port, file"
port_offset = ival(authk[3:6])*7
if port_offset == 0: port_offset = ival(authk[0:3])*7

port_base += port_offset
print "Using Network UDP Port:",port_base
print "Using Network TCP Port:",tcp_port
logdbf = "data/fdlog%s.fdd"%(authk[0:3])
print "Writing Log Journal file:",logdbf

print "Starting Network"
net = netsync()                 # setup net (may want to do an init method xx)
net.setport(port_base)
net.setauth(authk)
print "Saving Persistent Configuration in",globf
saveglob()

print "Time Difference Window (tdwin):",tdwin,"seconds"


# getting set up for the main GUI

# band set buttons
# this can be customized, don't forget the editor needs them also

bands = ('160','80','40','20','15','10','6','2','220','440','900','1200','sat','off')
modes = ('p','c','d')

if contest == "VHF":
##    bands = ('6','4','2','1.25','70c','33c','23c','13c','9c','6c','3c','1.25c','6m',\
##             '4m','2.5m','2m','1m','off')
    modes = ('p','c')

    # read vhfBands.dat CSV file: button/log, Cabrillo, ADIF, Score
    bands,bandToCabrillo,bandToADIF,bandToScore = [],{},{},{}
    with open("vhfBands.dat") as f:
        for ln in f:
            if ln[:1] != '#':
                x,y,z,s = ln.strip().split(',')
                #print x,y,z
                bands.append(x)
                bandToCabrillo[x] = y
                bandToADIF[x] = z
                bandToScore[x] = int(s)
    f.close()       

bandb = {}  # band button handles

def bandset(b):
    global band,tmob
    if node == "":
        b = 'off'
        text.insert(END,"err - no node\n")
    if operator == "":
        b = 'off'
        text.insert(END,"err - no operator\n")
    if b != 'off':
        s = net.si.nod_on_band(b)
        if s: text.insert(END," Already on [%s]: %s\n"%(b,s))
    text.see(END)
    if band != b: tmob = now()      # reset time on band
    band = b
    bandb[b].select()
    renew_title()

def bandoff():
    bandset('off')


# new participant setup

class newparticipantdialog:

    def lookup(self):
        # constrain focus to initials until they are ok
        #print "lookup"
        #print self.initials.get()
        initials = string.lower(self.initials.get())
        # if not re.match(r'[a-zA-Z]{2}[a-zA-Z0-9]?$',initials):
        if not re.match(r'[a-zA-Z]{2,3}$',initials):
            #self.initials.delete(0,END)
            self.initials.configure(bg='yellow')
            self.initials.focus()
        else:
            self.initials.configure(bg='white')
            ini,name,call = string.split(participants.get(initials,', , '),', ')
            self.name.delete(0,END)
            self.name.insert(END,name)
            self.call.delete(0,END)
            self.call.insert(END,call)
        return 1

    def applybtn(self):
        global participants
        #print "store"
        initials = self.initials.get().lower()
        name = self.name.get()
        call = string.lower(self.call.get())
        self.initials.configure(bg='white')
        self.name.configure(bg='white')
        self.call.configure(bg='white')
        if not re.match(r'[a-zA-Z]{2,3}$',initials):
            text.insert(END,"error in initials\n")
            text.see(END)
            self.initials.focus()
            self.initials.configure(bg='yellow')
            #self.initials.delete(0,END)
        elif not re.match(r'[A-Za-z ]{4,20}$',name):
            text.insert(END, "error in name\n")
            text.see(END)
            self.name.focus()
            self.name.configure(bg='yellow')
            #self.name.delete(0,END)
        #elif not re.match(r'([a-z]{1,2}[0-9][a-z]{1,3})?$',call):
        elif not re.match(r'([a-zA-Z0-9]{3,6})?$',call):
            text.insert(END, "error in call\n")
            text.see(END)
            self.call.focus()
            self.call.configure(bg='yellow')
            #self.call.delete(0,END)
        else:
            initials
            nam = "p:%s"%initials
            v = "%s, %s, %s"%(initials,name,call)
            participants[initials] = v
            n = qdb.globalshare(nam,v)  # store + bcast
            self.initials.delete(0,END)
            self.name.delete(0,END)
            self.call.delete(0,END)
            self.initials.focus()
            buildmenus()

    def quitbtn(self):
        #print "quit"
        self.t.destroy()

    def dialog(self):
        if node == "":
            text.insert(END,"err - no node\n")
            return
        s = newparticipantdialog()
        s.t = Toplevel(root)
        s.t.transient(root)
        s.t.title('FDLog Add New Participant')
        f1 = Frame(s.t)
        f1.grid(row=0,column=0)
        Label(f1,text='Initials',font=fdbfont).grid(row=0,column=0,sticky=W)
        s.initials = Entry(f1,width=3,font=fdbfont,\
                           validate='focusout',validatecommand=s.lookup)
        s.initials.grid(row=0,column=1,sticky=W)
        s.initials.focus()
        Label(f1,text='Name',font=fdbfont).grid(row=1,column=0,sticky=W)
        s.name = Entry(f1,width=20,font=fdbfont)
        s.name.grid(row=1,column=1,sticky=W)
        Label(f1,text='Call',font=fdbfont).grid(row=2,column=0,sticky=W)
        s.call = Entry(f1,width=6,font=fdbfont)
        s.call.grid(row=2,column=1,sticky=W)
        f2 = Frame(s.t)
        f2.grid(row=1,column=0,sticky=EW,pady=3)
        f2.grid_columnconfigure((0,1),weight=1)
        Button(f2,text='Save',font=fdbfont,command=s.applybtn)\
                                        .grid(row=3,column=1,sticky=EW,padx=3)
        Button(f2,text='Quit',font=fdbfont,command=s.quitbtn)\
                                        .grid(row=3,column=0,sticky=EW,padx=3)


newpart = newparticipantdialog()

# property dialogs

cf = {}

def renew_title():
    "renew title and various, called at 10 second rate"
    if node == 'gota': call = string.upper(gd.getv('gcall'))
    else: call = string.upper(gd.getv('fdcall'))
    clas = string.upper(gd.getv('class'))
    sec = gd.getv('sect')
    grid = gd.getv('grid')
    t = now()
    sob = tmsub(t,tmob)
    mob = sob/60
    h = mob/60
    m = mob%60
    if contest == "FD":
        root.title('FDLog%s %s %s %s (Node: %s TimeOnBand: %d:%02d) %s:%s UTC %s/%s'%\
           (version[1:],call,clas,sec,node,h,m,t[-6:-4],t[-4:-2],t[2:4],t[4:6]))
    if contest == "VHF":
        root.title('FDLog%s %s %s (Node: %s TimeOnBand: %d:%02d) %s:%s UTC %s/%s'%\
           (version[1:],call,grid,node,h,m,t[-6:-4],t[-4:-2],t[2:4],t[4:6]))
    net.bcast_now()   # this is periodic bcast...

def setnode(new):
    global node
    bandoff()
    node = string.lower(new)
    qdb.redup()
    renew_title()

def applyprop(e=''):
    "apply property"
    global operator,logger,power,node
    new = cf['e'].get()
    if re.match(cf['vre'],new):
##        if   cf['lab'] == 'Operator': operator = new
##        elif cf['lab'] == 'Logger':   logger = new
##        elif cf['lab'] == 'Power':    power = new
        if cf['lab'] == 'Node':  setnode(new)
##        elif cf['lab'] == 'AuthKey':  reauth(new)    #net.setauth(new)
        else: print 'error, no such var'
        saveglob()
        renew_title()
        cf['p'].destroy()
    else:
        print 'bad syntax',new

def pdiag(label,value,valid_re,wid):
    "property dialog box"
    cf['p'] = Toplevel(root)
    cf['p'].transient(root)
    Label(cf['p'],text=label,font=fdbfont).grid(sticky=E,pady=20)
    if label == 'AuthKey':
        cf['e'] = Entry(cf['p'],width=wid,font=fdbfont,show='*')
    else:
        cf['e'] = Entry(cf['p'],width=wid,font=fdbfont)
    cf['e'].grid(row=0,column=1,sticky=W)
    cf['e'].insert(END,value)
    Button(cf['p'],text="Apply",command=applyprop,font=fdbfont)\
                                .grid(sticky=W,padx=20)
    Button(cf['p'],text="Cancel",command=cf['p'].destroy,font=fdbfont)\
                                .grid(padx=20,pady=20,row=1,column=1,sticky=E)
    cf['vre'] = valid_re
    cf['lab'] = label
    cf['e'].bind('<Return>',applyprop)
    cf['p'].bind('<Escape>',lambda e:(cf['p'].destroy()))
    cf['e'].focus()

def noddiag():
    pdiag('Node',node,r'[A-Za-z0-9-]{1,8}$',8)

##def authdiag():
##    pdiag('AuthKey',authk,r'.{3,12}$',12)


# view textdocs

def viewprep(ttl=''):
    "view preparation core code"
    w = Toplevel(root)
##    w.transient(root)
    w.title("FDLog - %s"%ttl)
    t = Text(w,takefocus=0,height=20,width=85,font=fdfont,\
             wrap=NONE,setgrid=1)
    s = Scrollbar(w,command=t.yview)
    t.configure(yscrollcommand=s.set)
    t.grid(row=0,column=0,sticky=NSEW)
    s.grid(row=0,column=1,sticky=NS)
    w.grid_rowconfigure(0,weight=1)
    w.grid_columnconfigure(0,weight=1)
    t.bind('<KeyPress>',kevent)
    return t

def viewtextv(txt,ttl=''):
    "view text variable"
    w = viewprep(ttl)
    w.insert(END,txt)
    w.configure(state=DISABLED)

def viewtextl(l,ttl=''):
    "view text list"
    w = viewprep(ttl)
    for i in l:
        w.insert(END,"%s\n"%i)
    w.configure(state=DISABLED)

def viewtextf(fn,ttl=''):
    "view text file"
    if ttl == "": ttl = "file %s"%fn
    try:
        fd = file(fn,'r')
        l = fd.read()
        viewtextv(l,ttl)
        fd.close()
    except:
        viewtextv("read error on file %s"%fn)

def viewlogf(bandm):
    "view log filtered by bandmode"
    lg = qdb.filterlog2(bandm)
    viewtextl(lg,"Log Filtered for %s"%bandm)

def viewlogfs(nod):
    "view log filtered by node"
    lg = qdb.filterlogst(nod)
    viewtextl(lg,"Log Filtered for %s"%nod)

def viewwasrpt():
    r = qdb.wasrpt()
    viewtextl(r,"Worked All States Report")

def updatebb():
    "update band buttons"

    r,cl,vh,go = net.si.nod_on_bands()      # r,cl,vhf,gota

    for i in bands:
        b = 0
        for j in modes:
            bm = "%s%s"%(i,j)
            if i == 'off': continue
            bc = 'gray'
            n = len(r.get(bm,''))
            sc = 'white'
            if   n == 0: bc = 'gray'
            elif n == 1: bc = 'yellow'
            else:        bc = 'orange'; sc = 'red'
            bandb[bm].configure(background=bc,selectcolor=sc)

    cltg = ival(gd.getv('class'))           # class target

    if cltg > 1: vht = 1                    # handle free vhf xmttr
    else: vht = 0

    ts = cl + max(0,vh-vht)                 # total sta = class + excess vhf stations

    if contest == "VHF": ts = cl + vh

    clc = 'white'
    if ts >  0   : clc = 'yellow'
    if ts == cltg: clc = 'green'
    if ts >  cltg: clc = 'red'
    if contest == "FD":
        bandb['Class'].configure(text='Class %s/%s'%(ts,cltg),background=clc)
    if contest == "VHF":
        bandb['Class'].configure(text='Xmtrs %s'%(ts),background=clc)

    vhc = 'white'
    if vh > 0: vhc = 'green'
    if vh > vht and ts > cltg: vhc = 'orange'  # 2 vhf is okay, only 1 is free..
    if contest == "FD":
        bandb['VHF'].configure(text='VHF %s/%s'%(vh,vht),background=vhc)

    if cltg > 1: gotatg = 1
    else: gotatg = 0
    goc = 'white'
    if go == gotatg: goc = 'green'
    if go >  gotatg: goc = 'red'
    if contest == "FD":
        bandb['GOTA'].configure(text='GOTA %s/%s'%(go,gotatg),background=goc)

def updateqct():
    "update contact count"
    
    if contest == "FD":
        qpb,ppb,qpop,qplg,qpst,tq,score,maxp,cwq,digq,fonq,qpgop,gotaq,nat,sat = \
            qdb.bandrpt()  #xx reduce processing her
        for i,j in (('FonQ','FonQ %4s'%fonq),\
                    ('CW/D','CW/D %4s'%(cwq+digq)),\
                    ('GOTAq','GOTAq %3s'%gotaq)):
            bandb[i].configure(text=j,background='gray')

            
    if contest == "VHF":
        r = qdb.vhfrpt()
        for i,j in (('FonQ','Qs %4s'%r.qcount),\
                    ('CW/D','BGs %3s'%r.grids),\
                    ('GOTAq','NetStat'),\
                    ('NET','%s'%r.score)):
            bandb[i].configure(text=j,background='gray')
        gotaq = 0

    # network status display update
    if gotaq == 0:
        bandb['GOTAq'].configure(text='NET OK')
    t = ""                      # check for net config errors
    if net.fills: t = "NEED FILL"
    if net.badauth_rcvd:
        net.badauth_rcvd = 0
        t = "AUTH FAIL"
    if net.pkts_prev == 0 and net.pkts_rcvd == 0:
##        t = "RCVP FAIL"
        t = "STANDALONE"
    net.pkts_prev = net.pkts_rcvd
    net.pkts_rcvd = 0
    if net.send_errs: t = "SENDP FAIL"; net.send_errs = 0
    if authk == '':   t = "NO AUTHKEY"
    if node == '': t = "NO NODE"
    if t: bandb['GOTAq'].configure(text=t,background='yellow')


# band button problems on mac xx (old news, probably fixed from Tk upgrades long ago)
# buttons too small, probably fixed from Tk upgrades
# local band button is also yellow (backgrounds on buttons problematic on mac)


def bandbuttons(w):
    "create band buttons"
    global sv
    a = 0
    sv = StringVar()                # variable to make radiobuttons cooperate
    sv.set(band)
    mac = os.name == 'posix'        # detect the mac
    for i in bands:
        b = 0
        for j in modes:
            bm = "%s%s"%(i,j)
            if i == 'off': bm = 'off'   # indicatoron = 0 makes square button with text inside but
                                        # doesn't work well on mac, with value 1 it makes a
                                        # circle alongside the text and works on both
                                        # so detect mac and change it for mac only
            bandb[bm] = Radiobutton(master=w,text=bm,font=fdfont,indicatoron=mac,\
                variable=sv,value=bm,
                command=lambda b=bm:(bandset(b)))
            bandb[bm].grid(row=b,column=a,sticky=NSEW)
            b += 1
        a += 1

    # looks like px is no longer used?
    if contest == "FD":
        for i,j,px in (('Class',0,5),\
                       ('VHF',1,13),\
                       ('GOTA',2,9)):
            bandb[i] = Button(w,text=i,font=fdfont)
            bandb[i].grid(row=j,column=a,sticky=NSEW)
    if contest == "VHF":
        for i,j,px in (('Class',0,5),\
                       ('VHF',1,13),\
                       ('NET',2,9)):
            bandb[i] = Button(w,text=i,font=fdfont)
            bandb[i].grid(row=j,column=a,sticky=NSEW)
    w.grid_columnconfigure(a,weight=1)

    a += 1
    for i,j in (('FonQ',0),\
                ('CW/D',1),\
                ('GOTAq',2)):
        bandb[i] = Button(w,text=i,font=fdfont)
        bandb[i].grid(row=j,column=a,sticky=NSEW)
    w.grid_columnconfigure(a,weight=1)


def rndlet():
    return chr(random.randrange(ord('a'),ord('z')+1))

def rnddig():
    return chr(random.randrange(ord('0'),ord('9')+1))

def testqgen(n):
    while n:
        call = rndlet()+rndlet()+rnddig()+rndlet()+rndlet()+rndlet()
        rpt = rnddig()+rndlet()+' '+rndlet()+rndlet() + ' testQ ' + str(n)
        print call,rpt
        n -= 1

        qdb.qsl(now(),call,band,rpt)
        time.sleep(0.1)

##def reauth(nkey):
##    "reset authentication key, reload, set port"
##    net.setauth(nkey)
##    port = 7373 + ival(nkey[0:4])
##    #xx net.set_port(port)
##    print "port",port
##    logf = "fdlog%s.fdd"%(nkey[0:2])
##    #xx flush & reload log  loadlog(logf)
##    print "new file",logf
# the above is hard, and not correct. have to restart network thread..
# solve this for now by restarting the program..


print "Starting Main GUI"

root = Tk()                     # setup main Tk GUI

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Save Entry File",command=lambda:contestlog(1))
filemenu.add_command(label="View Saved Entry File",\
                     command=lambda:viewtextf('fdlog.log'))
filemenu.add_command(label="View Log Data File",\
                     command=lambda:viewtextf(logdbf))
filemenu.add_command(label="Exit",command=root.quit)

propmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Properties",menu=propmenu)
propmenu.add_command(label="Set Node ID",command=noddiag)
##propmenu.add_command(label="Set AuthKey",command=authdiag)
propmenu.add_command(label="Add Participants",command=newpart.dialog)

logmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Logs",menu=logmenu)
logmenu.add_command(label='Full Log',command=lambda:viewlogf(""))
logmenu.add_command(label='QSTs',command=lambda:viewlogf(r"[*]QST"))
logmenu.add_command(label='GOTA',command=lambda:viewlogfs("gota"))
logmenu.add_command(label='WAS',command=viewwasrpt)

for j in modes:
    m = Menu(logmenu,tearoff=0)
    if   j == 'c': lab = 'CW'
    elif j == 'd': lab = 'Digital'
    elif j == 'p': lab = 'Phone'
    elif j == 'm': lab = 'm'
    elif j == '' : lab = 'all'
    logmenu.add_cascade(label=lab,menu=m)
    for i in bands:
        if i == 'off': continue
        bm = "%s%s"%(i,j)
        m.add_command(label=bm,command=lambda x=bm:(viewlogf(x)))

#menu.add_command(label="Status",command=exit)
#toolsmenu = Menu(menu,tearoff=0)
#menu.add_cascade(label="Tools",menu=toolsmenu)
#toolsmenu.add_command(label="Status",command=exit)
#toolsmenu.add_command(label="Properties",command=propbox)
#toolsmenu.add_command(label="Network",command=exit)
##toolsmenu.add_command(label="Node",command=exit)
##toolsmenu.add_command(label="Authentication",command=exit)
#toolsmenu.add_command(label="Notes",command=exit)
#toolsmenu.add_command(label="Delete Log Entry",command=exit)


# Prepare Docs Menu
#   this menu populates automatically for specific file types it finds

start = '../../../files'            # eventual home
if not os.path.isdir(start):
    start = '../files'              # current home
if os.path.isdir(start):
    docmenu = Menu(menu,tearoff=0)  # add a Docs menu to the menu bar
    menu.add_cascade(label="Docs",menu=docmenu)

    menus = {}                      # store menu objects to add to
    menus[start] = docmenu

    for r,dirs,files in os.walk(start):
        for d in dirs:              # directories get cascades
            xmenu = Menu(menu,tearoff=0)
            menus[r].add_cascade(label=d,menu=xmenu)
            menus[os.path.join(r,d)] = xmenu
        for f in files:                                 # files get commands
            b,x = os.path.splitext(f)                   # check the extension
            x = x.lower()
            p = os.path.join(r,f)
            if x == ".txt":                             # text files view in window
                menus[r].add_command(label=b,\
                    command=lambda z1=p,z2=b:viewtextf(z1,z2))
            elif x in (".pdf",".jpg",".gif",".png"):    # other file types can be launched
                menus[r].add_command(label=b,\
                    command=lambda z=p:os.startfile(z))

# build help menu

helpmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Help",menu=helpmenu)

helpmenu.add_command(label="ReadMe",command=lambda:viewtextf('readme.txt'))
helpmenu.add_command(label="Getting Started",\
            command=lambda:viewtextv(getting_started,'Getting Started'))

##helpmenu.add_command(label="Wireless Network",\
##            command=lambda:viewtextf('wireless_net.txt','Wireless Network'))

##helpmenu.add_command(label="Group Meeting Agenda",\
##                command=lambda:viewtextf('group_agenda.txt','Group Plan'))
##helpmenu.add_command(label="Group Plans",\
##                command=lambda:viewtextf('group_plan.txt','Group Plan'))
##helpmenu.add_command(label="Group Site Info",\
##                command=lambda:viewtextf('group_site_info.txt','Site Info'))
##helpmenu.add_command(label="Group Handbook",\
##                command=lambda:viewtextf('group_handbook.txt','Group Handbook'))

##helpmenu.add_command(label="ARRL FD Rules (pdf)",\
##            command=lambda:os.startfile('fdrules.pdf'))
##helpmenu.add_command(label="ARRL Sections",\
##            command=lambda:viewtextf('arrl_sect.txt','ARRL Sections'))
##helpmenu.add_command(label="W1AW Schedule",\
##            command=lambda:viewtextf('w1aw.txt','W1AW Schedule'))
##helpmenu.add_command(label="ARRL Band Chart (pdf)",\
##            command=lambda:os.startfile('bands.pdf'))
##helpmenu.add_command(label="ARRL Band Plan",\
##            command=lambda:viewtextf('ARRL_Band_Plans.txt',"ARRL Band Plan"))
##helpmenu.add_command(label="FD Frequency List",\
##            command=lambda:viewtextf('frequencies.txt',"FD Frequency List"))
##helpmenu.add_command(label="Propagation Info",\
##            command=lambda:viewtextf('propagation.txt',"Propagation Info"))

helpmenu.add_command(label="Time Zone Chart",\
            command=lambda:viewtextv(tzchart,"Time Zone Chart"))

##helpmenu.add_command(label="NTS Info",\
##                     command=lambda:viewtextf('nts_info.txt',"NTS Info"))
##helpmenu.add_command(label="NTS Manual (pdf)",\
##                     command=lambda:os.startfile('pscm.pdf'))

helpmenu.add_command(label="FDLog Release Log",\
                     command=lambda:viewtextv(release_log,"Release Log"))
helpmenu.add_command(label="FDLog Set Commands",command=gd.sethelp)
helpmenu.add_command(label="FDLog Manual",\
                     command=lambda:viewtextf('fdlogman.txt',"Manual"))
helpmenu.add_command(label="FDLog Version",\
                     command=lambda:viewtextv(prog,"FDLog Version"))
helpmenu.add_command(label="About FDLog",\
                     command=lambda:viewtextv(about,"About"))

f1 = Frame(root,bd=1)                           # band buttons
bandbuttons(f1)
f1.grid(row=0,columnspan=2,sticky=NSEW)


def setoper(op):
    "set operator"
    global operator
    #print "setoper",op
    ini,name,call = string.split(op,', ')
    operator = "%s: %s, %s"%(ini,name,call)
    opds.config(text=operator)
    saveglob()

def setlog(logr):
    "set logger"
    global logger
    #print "setlog",logr
    ini,name,call = string.split(logr,', ')
    logger = "%s: %s, %s"%(ini,name,call)
    logds.config(text=logger)
    saveglob()

f1b = Frame(root,bd=1)                          # oper logger power window

# Operator
opmb = Menubutton(f1b,text="Operator",font=fdfont,relief='raised',\
                  background='gray')
opmb.grid(row=0,column=0,sticky=NSEW)

opmu = Menu(opmb,tearoff=0)
opmb.config(menu=opmu,direction='below')
opmu.add_command(label="Add New Participant",command=newpart.dialog)

op = operator
if op == "": op = '<select operator>'
opds = Menubutton(f1b,text=op,font=fdfont,relief='raised',\
                  background='gray')
opds.grid(row=0,column=1,sticky=NSEW)
opdsu = Menu(opds,tearoff=0)
opds.config(menu=opdsu,direction='below')

f1b.grid_columnconfigure(1,weight=1)

# Logger
logmb = Menubutton(f1b,text="Logger",font=fdfont,relief='raised',\
                   background='gray')
logmb.grid(row=0,column=3,sticky=NSEW)

logmu = Menu(logmb,tearoff=0)
logmb.config(menu=logmu,direction='below')
logmu.add_command(label="Add New Participant",command=newpart.dialog)

log = logger
if log == "": log = '<select logger>'
logds = Menubutton(f1b,text=log,font=fdfont,relief='raised',\
                   background='gray')
logds.grid(row=0,column=4,sticky=NSEW)

f1b.grid_columnconfigure(4,weight=1)

logdsu = Menu(logds,tearoff=0)
logds.config(menu=logdsu,direction='below')
logdsu.add_command(label="Add New Participant",command=newpart.dialog)

def buildmenus():
    opdsu.delete(0,END)
    logdsu.delete(0,END)
    l = participants.values()
    l.sort()
    for i in l:
       # if re.match(r'.*, delete,',i): continue
        m = re.match(r'[a-z0-9]+, [a-zA-Z ]+, ([a-z0-9]+)$',i)
        if m: opdsu.add_command(label=i, command=lambda n=i:(setoper(n)))
        logdsu.add_command(label=i, command=lambda n=i:(setlog(n)))
    opdsu.add_command(label="Add New Participant",command=newpart.dialog)
    logdsu.add_command(label="Add New Participant",command=newpart.dialog)

# power

def ckpowr():
    global power
    pwr = ival(pwrnt.get())
    if pwr < 0: pwr = "0"
    elif pwr > 1500: pwr = "1500"
    pwrnt.delete(0,END)
    pwrnt.insert(END,pwr)
    if natv.get(): pwr = "%sn"%pwr
    else: pwr = "%s"%pwr
    power = pwr
    print 'power',power
    return 1

def setpwr(p):
    global power
    pwr = ival(p)
    pwrnt.delete(0,END)
    pwrnt.insert(END,pwr)
    if p[-1:] == 'n': powcb.select()
    else: powcb.deselect()
    power = p

pwrmb = Menubutton(f1b,text="Power",font=fdfont,relief='raised',\
                   background='gray')
pwrmb.grid(row=0,column=6,sticky=NSEW)
pwrmu = Menu(pwrmb,tearoff=0)
pwrmb.config(menu=pwrmu,direction='below')
pwrmu.add_command(label='0 Watts',command=lambda:(setpwr('0')))
pwrmu.add_command(label='5 Watts',command=lambda:(setpwr('5')))
pwrmu.add_command(label='5W Natural',command=lambda:(setpwr('5n')))
pwrmu.add_command(label='50 Watts',command=lambda:(setpwr('50')))
pwrmu.add_command(label='50W Natural',command=lambda:(setpwr('50n')))
pwrmu.add_command(label='100 Watts',command=lambda:(setpwr('100')))
pwrmu.add_command(label='100W Natural',command=lambda:(setpwr('100n')))
pwrmu.add_command(label='150 Watts',command=lambda:(setpwr('150')))
pwrmu.add_command(label='150W Natural',command=lambda:(setpwr('150n')))
pwrmu.add_command(label='500 Watts',command=lambda:(setpwr('500')))
pwrmu.add_command(label='1000 Watts',command=lambda:(setpwr('1000')))
pwrmu.add_command(label='1500 Watts',command=lambda:(setpwr('1500')))

pwrnt = Entry(f1b,width=4,font=fdfont,validate='focusout',validatecommand=ckpowr)
pwrnt.grid(row=0,column=7,sticky=NSEW)

Label(f1b,text="W",font=fdfont).grid(row=0,column=8,sticky=NSEW)

natv = IntVar()
powcb = Checkbutton(f1b,text="Natural",variable=natv,command=ckpowr,\
                    font=fdfont,relief='raised',background='gray')
powcb.grid(row=0,column=9,sticky=NSEW)
setpwr(power)

f1b.grid(row=1,columnspan=2,sticky=NSEW)
                                                # log window
logw = Text(root,takefocus=0,height=11,width=80,font=fdmfont,\
            wrap=NONE,setgrid=1)
logw.configure(cursor='arrow')
scroll = Scrollbar(root,command=logw.yview)
logw.configure(yscrollcommand=scroll.set)
logw.grid(row=2,column=0,sticky=NSEW)
scroll.grid(row=2,column=1,sticky=NS)
root.grid_rowconfigure(2,weight=1)
root.grid_columnconfigure(0,weight=1)
                                                # command input window
text = Text(root,takefocus=1,height=10,width=80,font=fdmfont,\
            wrap=NONE,setgrid=1)
scrollt = Scrollbar(root,command=text.yview)
text.configure(yscrollcommand=scrollt.set)
text.grid(row=3,column=0,sticky=NSEW)
scrollt.grid(row=3,column=1,sticky=NS)
root.grid_rowconfigure(3,weight=1)

logw.tag_config("b",foreground="blue")
logw.insert(END,"Log Window\n",("b"))


# startup

contestlog(0)                   # define globals
buildmenus()

sms = syncmsg()                 # setup sync message service

qdb = qsodb()                   # init qso database
#qdb.loadfile()                  # read log file



net.start()                     # start threads

renew_title()

text.insert(END,"%s\n"%prog)
text.insert(END,"Set Operator, Logger, Power and Band/Mode!!\n")
text.insert(END,"Contacts on zero power or off band do not count!!\n? for help\n\nReady\n\n")

text.focus()


def showthiscall(call):
    "show the log entries for this call"
    p = call.split('/')
#    print p[0]
    findany = 0
    m,n,g = qdb.cleanlog()
#    print m.values()
    for i in m.values():
#        print i.call
        q = i.call.split('/')
        if p[0] == q[0]:
            if findany == 0: text.insert(END,"\n")
            text.insert(END,"%s\n"%i.prlogln())
            findany = 1
    return findany


# section data validation

secName = {} # index by handle, call area number, official abbreviation, and full state
#                       handle is official abbreviation or misspelled version
secPartial = {} # section partial indexed by partials of the correct names for partial matching

def readSections():
    #sectost,stcnt,r,e = {},{},[],[]
    # canum is call area number

    try:
        fd = file("arrl_sect.dat","r")  # read section data
        while 1:
            ln = fd.readline().strip()          # read a line and put in db
            if not ln: break
            #if ln == "": continue
            if ln[0] == '#': continue
            try:
                sec,st,canum,abbrev,name = string.split(ln,None,4)
                #r = abbrev + ' ' + desc
                #secName[sec] = abbrev
                secName[abbrev] = abbrev + ' ' + name + ' ' + canum
                for i in range(len(abbrev)-1):
                    p = abbrev[:-i-1]
##                    print abbrev,p
                    secPartial[p] = 1
                #sectost[sec] = st
                #stcnt[st] = 0
##                    print sec,st,desc
            except ValueError,e:
                print "rd arrl sec dat err, itm skpd: ",e
        fd.close()
    except IOError,e:
        print "read error during readSections", e

readSections()

## the difflib experiment was poor, it matched substrings with abbreviations
## building up multiple tables and separating the 2,3 from 4+ compares might
## make it work better. Removed 7/2016


def proc_key(ch):
    "process keystroke"
    global kbuf,suffix

    #print "kbuf '%s', ch '%s'"%(kbuf,ch)  # debug
    #print "  suffix store '%s'"%suffix

    if ch == '?' and (kbuf == "" or kbuf[:1] != '#'):    # ? for help, allow it in QSTs
        mhelp()

    elif ch == '\b':                # backspace erases char
        if kbuf != "":
            kbuf = kbuf[0:-1]
            text.delete('end - 2 chars')

    elif ch == '\x1b':              # escape quits this input line
        text.insert(END," ESC -aborted line-\n")
        kbuf = ""

    elif ch == '\r':                # return, may be QST, command or log entry

        if kbuf[:1] == '#':         # check for QST
            qdb.qst(kbuf[1:])
            kbuf = ""
            text.insert(END,'\n')

        elif kbuf[:1] == '.':       # check for (dot) commands
            proc_cmd()
            kbuf = ""
            text.insert(END,'\n')

        elif kbuf != '': proc_qso()

    else:                           # character for the buffer?

        buf = kbuf + ch             # echo & add legal char to kbd buf
        if len(buf) < 50:
            if buf[:1] == '.':      # dot command
                if re.match(r'[ a-zA-Z0-9.,/@-]{0,45}$',ch):
                    kbuf = buf
                    text.insert(END,ch)

            elif buf[:1] == '#':    # QST
                if re.match(r'#[ a-zA-Z0-9.,?/!@$;:+=%&()-]{0,40}$',buf):
                    kbuf = buf
                    text.insert(END,ch)

            else:                   # Q
                if ch == ' ': procQspace()
                else:
                    #stat,tm,pfx,sfx,call,xcall,rept = qdb.qparse(buf) # check for legal Q character
                    stat,tm,pfx,sfx,call,xcall,rept = qparse3(buf) # check for legal Q character
                    if stat > 0 and len(buf) < 50:   # accept new character (else ignore it)
                        kbuf = buf
                        text.insert(END,ch)


# stub to match old parse args
#
# stat,tm,pfx,sfx,call,xcall,rept = qdb.qparse(buf)
#
def qparse3(buf):
    c = parseFD()
    r = c.ooiParse(buf)  # it only returns an int here
    #print "  ",c.stat,c.prefix,c.suffix,c.call,c.xcall,c.rept
    #tm = '' # no time support (yet) (is there, need to integrate/test)

    return c.action,c.tm,c.prefix,c.suffix,c.call,c.xcall,c.rept

    # force callsign components to lowercase
    # except extended call? in gridsquares case matters
    # the following probably won't work properly, didn't test 6/2017
    # xcall contains mixed case and needs to for gridsquares
    # so implementing lowercase call forcing might have to be in the parser
    # don't want to mess with that just now
    #return c.action,c.tm,c.prefix.lower(),c.suffix.lower(),c.call.lower(),c.xcall,c.rept

# action or stat?

##def qparse4(buf):
##    c = parseFD()
##    r = c.ooiParse(buf)
##    return r

# FDLog Out Of Order Input QSO parser V4 June-July 2016

# handles time parsing for forcing time on log entries
# handles contest modes for VHF gridsquares and FD class and section
#  (based on contest global)

# Input fields can occur in any order but only once
# To solve the suffix/section confusion prepend ';' to mark the section if it
# preceeds the suffix, if the section follows the suffix the ';' is optional
#
# Loop, looking for input in this order, skip any already found field
# If one doesn't fit, try the next one
# Stop when the input is all parsed or when parsing stalls
# Stall indicates bad input
#   :date.time
#   ;section
#   prefix
#   suffix
#   class (FD only)
#   section (try only if suffix filled) (FD only)
#   gridsquare (VHF only)
#   comment (try only if all other fields filled)

# Use https://regex101.com/#python to test regexp

# New layering design in this code
#   top level breaks line into words
#   mid level analyzes each word
#   bottom level is set of recognizers for each word type

# Parser Return Values and Status (.action object variable)
#   0 BAD, parse failed
#   1 OK, partial, no action, continue
#   2 OK, suffix action
#   3 OK, prefix action
#   4 OK, callsign action
#   5 OK, complete Q info available

# Recognizer Return Values (return and .stat)
#   0 bad (implies last character not allowed)
#   1 ok, partial match but not complete valid word
#   2 complete valid word

class parseFD():

##    def __init__(self):
##        pass
    
    def ooiParse(self,buf):         # out of order parsing, Version 4
        "out of order input parser"
        self.buf = buf              # parse buffer
        self.lastCh = buf[-1:]      # last input character
        self.stat = 0               # status (see above)
        self.action = 0             # action, parser return

        self.aprefix = ''           # callsign ancillary prefix ve7/
        self.prefix = ''            # callsign prefix w6 wb6
        self.suffix = ''            # callsign suffix a ab abc
        self.postfix = ''           # callsign postfix /a /ab /abc
        self.call = ''              # callsign <prefix><suffix>
        self.xcall = ''             # extended call <everything>
        self.fdclass = ''           # field day class 2a 39f
        self.section = ''           # field day section eb stx
        self.comment = ''           # comment, whats left
        self.rept = ''              # report (sum of fdclass, section, grid, comment)

        self.tm = ''                # time (for forcing time)
        self.grid = ''              # gridsquare for VHF contest

        #print "parsing '%s'"%buf

        if buf == '': return 1

        #if self.lastCh == '\r': print "  return at end"

        # return is special in that it can override length limit
        if len(buf) > 40 and self.lastCh != '\r':   # length limit
            return 0
        
        r = self.parse(buf)
        if r == 1 and self.action == 0: self.action = 1
        if r == 2 and self.action == 0: self.action = 1

        if r == 0:
            #print "  parsing failed"
            self.action = 0
            self.stat = 0
            return 0
        
        if self.stat > 0 and self.call and \
           self.fdclass and self.section:
            self.rept = self.fdclass + ' ' + self.section
            if self.comment: self.rept += ' ' + self.comment
            self.action = 5           # full FD QSO info present

        if self.stat > 0 and self.call and self.grid:
            self.rept = self.grid
            if self.comment: self.rept += ' ' + self.comment
            self.action = 5           # full VHF QSO info present
            
        return self.action


   # may be some confusion here between self.stat and self.action
   # ooiParse returns action which has status incorporated into it
   # parse returns status
   # wparse returns status
   # recognizers return status

    def parse(self,buf):
        "parse partial or full input line, given buffer"

        lch = buf[-1:]                      # last char

        #print "'%s' %d"%(buf,ord(lch))

        if '  ' in buf: return 0            # avoid multispaces
        
        if lch == '\r':                     # if last is special
            buf = buf[:-1]                  # remove it
            lch = ' '                       # consider same as space

        if ord(lch) > 126 or ord(lch) < 32: # char must be printable ascii
            return 0
            
        if buf[:-1] == ' ':                 # don't want ending space
            return 0
        
        s = buf.split()                    # split into words
        
        for i in range(len(s)):             # analyze each word
     
            m = self.wparse(s[i])           # this word
            self.stat = m
            if m == 0: return 0             # fail if doesn't match

            #print "parse",m,len(s),i,s[i],self.stat
            
            # partial match allowed only at last word
            # and not if a space follows
            if m == 1 and (i != (len(s)-1) or lch == ' '):
                self.stat = 0               
                return 0
            
        return self.stat                    # return status of final word, look up action


    # Elements in Natural Order
    #   forced date,time (skipped this for now)
    #   prefix
    #   suffix
    #   class
    #   section
    #   comment

    # search order priority first
    # keep trying until something matches
    # or give up
    
    def wparse(self,buf):
        "parse a single word"

        self.action = 0             # these represent final result
        self.stat = 0               # reset for each word

        #print "wparse",buf
        
        if self.suffix == '' != self.prefix == '':
            return 0 # when we have just one of prefix/suffix we're done
        
        fch = buf[:1] # first character

        # force date time first
        if fch == ':' and self.tm == '':
            m = self.rdatime(buf)
            if m > 0: return m
        
        # extended call
        if fch == '"' and self.prefix == '' and self.suffix == '':
            m = self.rxcall(buf)
            if m > 0: return m

        # call, prefix, suffix, call with postfix
        if self.prefix == '' and self.suffix == '': 
            m = self.rcall(buf) # catches prefix, suffix or call with simple postfix
            if m > 0: return m

        if contest == "VHF":
            # gridsquare for VHF contest
            if self.grid == '':
                m = self.rgrid(buf)
##                if m > 0: print "  gridsq: '%s'"%buf,m
                if m > 0: return m

        if contest == "FD":
            # FD class
            if self.fdclass == '':
                m = self.rfdclass(buf)
                if m > 0: return m

            # FD section
            if self.section == '' and (fch == ';' or self.suffix != ''):
                m = self.rsection(buf)
                #if m > 0: print "  section: '%s'"%buf,m
                if m > 0: return m
            
        # comment .. if we have everything else
        if self.prefix != '' and self.suffix != '' and \
          (self.fdclass != '' and self.section != '') or self.grid != '':
            m = self.rcomment(buf)
            if m > 0: return m

        return 0
    

# library of word analyzers (recognizers) for ooiParser V4
#
# discard optional command prefix
# must match remaining input text
# match a fully formed result is 2, and set action if apropo
# match is partial result 1
# fail to match result 0
# set action here but only if full match

# pythex.org is the place to test regex for python

    def rxcall(self,buf): # complex call: extended callsign with " prefix

        # don't disable complex calls, they are used for processing the logfiles
        
        #return 0  # disable complex calls

        #if contest == "VHF": return 0

        # look for complex call override
        # triggered by doublequote

        # 4 cases - depending on number of slashes

        # ancillary prefix / call / postfix
        x = re.match(r'"(([a-zA-Z0-9]{1,6})[/](([a-zA-Z0-9]{1,4}[0-9])([a-zA-Z]{1,4}))[/]([a-zA-Z0-9]{1,4}))$',buf)
        if x:
            self.xcall = x.group(1)
            self.aprefix = x.group(2)
            self.call = x.group(3)
            self.prefix = x.group(4)
            self.suffix = x.group(5)
            self.postfix = x.group(6)
            self.action = 4
##                print "  call",self.xcall
            return 2

        # ancillary prefix / call
        x = re.match(r'"(([a-zA-Z0-9]{1,6})[/](([a-zA-Z0-9]{1,4}[0-9])([a-zA-Z]{1,4})))$',buf)
        if x:
            self.xcall = x.group(1)
            self.aprefix = x.group(2)
            self.call = x.group(3)
            self.prefix = x.group(4)
            self.suffix = x.group(5)
            self.action = 4
##                print "  call",self.xcall
            return 2

        # call / postfix
        x = re.match(r'"((([a-zA-Z0-9]{1,4}[0-9])([a-zA-Z]{1,4}))[/]([0-9a-zA-Z]{1,4}))$',buf)
        if x:
            self.xcall = x.group(1)
            self.call = x.group(2)
            self.prefix = x.group(3)
            self.suffix = x.group(4)
            self.postfix = x.group(5)
            self.action = 4
##                print "  call",self.xcall
            return 2

        # call only but allow multiple digits
        x = re.match(r'"((([a-zA-Z0-9]{1,4}[0-9])([a-zA-Z]{1,4})))$',buf)
        if x:
            self.xcall = x.group(1)
            self.call = x.group(2)
            self.prefix = x.group(3)
            self.suffix = x.group(4)
            self.action = 4
##                print "  call",self.xcall
            return 2

        #print "excall '%s' pfx '%s' sfx '%s' pst '%s'"%(self.xprefix,self.prefix,self.suffix,self.postfix)

        # now look for partial call
        # stuff / stuff <digit> stuff / stuff
        x = re.match(r'"[0-9a-zA-Z]{1,6}[/][0-9a-zA-Z]{2,5}[/][0-9a-zA-Z]{0,3}$',buf)
        if x: return 1
        x = re.match(r'"[0-9a-zA-Z]{1,6}[/][0-9a-zA-Z]{0,8}$',buf)
        if x: return 1
        x = re.match(r'"[0-9a-zA-Z]{0,8}$',buf)
        if x: return 1

        return 0
    

    def rcall(self,buf): # regular callsign and postfix recognizer
        "match prefix, suffix, whole callsign possibly with postfix"
        # match full call / postfix (three char)(four for VHF)
        x = re.match(r'((([a-zA-Z]{1,2}[0-9])([a-zA-Z]{1,3}))[/]([0-9a-zA-Z]{1,4}))$',buf)
        if contest == "VHF":
            x = re.match(r'((([a-zA-Z]{1,2}[0-9])([a-zA-Z]{1,3}))([/][rR]))$',buf)  # w6akb/r
        #print "rcall",buf
        if x:
            self.xcall = x.group(1)
            self.call = x.group(2)
            self.prefix = x.group(3)
            self.suffix = x.group(4)
            self.postfix = x.group(5)
            self.action = 4
##            print "  rcall",self.xcall
            return 2
        # match full call with / (partial wait for postfix)
        if contest == "VHF":
            x = re.match(r'[a-zA-Z]{1,2}[0-9][a-zA-Z]{1,3}[/][a-rA-R]{0,2}$',buf)
            if x: return 1 # call/ to call/CM
            x = re.match(r'[a-zA-Z]{1,2}[0-9][a-zA-Z]{1,3}[/]$',buf)  # w6akb/
            if x: return 1 
        if contest == "FD":
            x = re.match(r'(([a-zA-Z]{1,2}[0-9])([a-zA-Z]{1,3})[/])$',buf)  # wb6zqz/
            #print "rcall",buf
            if x: return 1 # call and slash
        # match full call, return 2 and call
        x = re.match(r'(([a-zA-Z]{1,2}[0-9])([a-zA-Z]{1,3}))$',buf)  # w6a w6ab w6akb
        #print "rcall",buf
        if x:
            self.xcall = x.group(1)
            self.call = x.group(1)
            self.prefix = x.group(2)
            self.suffix = x.group(3)
            self.action = 4
##            print "  rcall",self.xcall, self.call, self.prefix, self.suffix
            return 2
        # match prefix, return 2 and prefix
        x = re.match(r'([a-zA-Z]{1,2}[0-9])$',buf)
        if x:
            self.prefix = x.group(1)
            self.action = 3
##            print "  prefix",self.prefix
            return 2
        # match suffix, return 2 and suffix (note it might be early prefix)
        x = re.match(r'([a-zA-Z]{1,3})$',buf)
##        print "rcall suffix '%s'"%buf
        if x:
            self.suffix = x.group(1)
            self.action = 2
##            print "  suffix",self.suffix
            return 2
        # fail to match all, return 0
        return 0

    def rfdclass(self,buf): # field day class
        x = re.match(r'(([1-3][0-9][a-fA-F])$|([1-9][a-fA-F]))$',buf)
        #print "rclass '%s'"%buf
        if x:
            if x.group(2): val = x.group(2)
            elif x.group(3): val = x.group(3)
            self.fdclass = val
##            print "  class",val
            return 2

        x = re.match(r'([1-3][0-9]|[1-9])$',buf) # one or two digits partial
        if x:
            #print "  partial class match '%s'"%buf
            return 1
        return 0

    # validate section against partial and full lists
    def rsection(self,buf): # arrl section
        x = re.match(r'(;?([a-zA-Z]{0,3}))$',buf)
        #print "  rsection '%s'"%buf
        if x:
            val = x.group(2)
            if buf == ';': return 1
            #print "  rsection match val '%s'"%val
            if val.upper() in secName:  # validate with dictionary
            #if len(val) > 1:
                # if val not in sections and len == 2:
                #   return 1
                # else: return 0  # let it go to 3 chars before refusing
                self.section = val
##                print "  section '%s'"%val
                return 2
            if val.upper() in secPartial: # validate with dictionary
                #print '  in sectionpartial'
                return 1
        else:
            return 0

    # note that comment gets broken into words also
    def rcomment(self,buf): # comment (how long should it allow?)
        x = re.match(r'([- a-zA-Z0-9/;,.:]{0,20})$',buf)             
        if x:
            self.comment = ' '.join([self.comment,buf])  # collect value
##            print "  comment '%s'"%self.comment
            if len(self.comment) < 20:
                return 2
        return 0


    # force qso time with :dd.hhmm or :yymmdd.hhmm for entering paper logs later
    
    def rdatime(self,buf):  # date and time
##        return 0            # skip this

# not sure why but only two digit is acceptible here, the rest of the date is forced
# in somewhere else. Not going to fix that right now, this is enough for putting
# paper logs into the log within the same month as the contest occurs
##        x = re.match(r':([0-9]{2}[01][1-9][0-3][0-9][.][0-2][0-9][0-5][0-9])$',buf) # yymmdd.hhmm
##        if x:
##            self.tm = x.group(1)
##            return 2
        x = re.match(r':([0-3][0-9][.][0-2][0-9][0-5][0-9])$',buf)  # dd.hhmm
        if x:
            #tm2 = now()
            tm2 = ''
            self.tm = tm2[0:4]+x.group(1)                            # dd.hhmmss to yymmdd.hhmm
            return 2
##        x = re.match(r':[0-9]{6}[.][0-9]{0,3}$',buf)                # partial yymmdd.hhm
##        if x: return 1
        x = re.match(r':[0-9]{2}[.][0-9]{0,3}$',buf)                # partial dd.hhm
        if x: return 1
        x = re.match(r':[0-9]{0,2}$',buf)                           # partial dd
        if x: return 1
                        
    # Gridsquares (for vhf)
    #   4: [A-R]{2}[0-9]{2}
    #   6: [A-R]{2}[0-9]{2}[a-x]{2}

    def rgrid(self,buf): # grid square (four character only)
        x = re.match(r'([A-Ra-r]{2}[0-9]{2})$',buf)     # full match       
        if x:
            self.grid = x.group(1).upper()
            return 2
        x = re.match(r'([A-Ra-r]{1,2})$',buf)           # partial
        if x:
            return 1
        x = re.match(r'([A-Ra-r]{2}[0-9])$',buf)        # partial
        if x:
            return 1
        return 0
    

# end of V4 parser



qdb.loadfile()                  # read log file after defining parsing, yuck :)



print
print "Time Master: '%s'"%gd.getv('tmast')
# error, time master doesn't appear to be initialized yet?
# yes, loading logfile uses parsing which hasn't been defined yet, so
# it had to be moved down, so we will move this section down
print
if node == gd.getv('tmast'):
    print "This Node is the TIME MASTER!!"
    print "THIS COMPUTER'S CLOCK BETTER BE RIGHT (preferably GPS/NTP locked)"
    print "User should Insure that system time is within a second of the"
    print "  correct time and that the CORRECT TIMEZONE is selected (in the OS)"
    print
else:
    print "User should Insure that System Time is within a few seconds of the"
    print "  correct time and that the CORRECT TIMEZONE is selected (in the OS)"
print "To change system timezone, stop FDLog, change the setting, then restart"
print



def proc_cmd():  # process a command (starts with period)

        global kbuf,power,operator,logger,debug,band,node,suffix,tdwin,timeok

        if re.match(r'[.]h$',kbuf):      # help request

            m = """
    .band 160/80/40/20/15/10/6/2/220/440/900/1200/sat c/d/p
    .off               change band to off
    .pow <dddn>        power level in integer watts (suffix n for natural)

    .node <call-n>     set id of this log node
    .testq <n>         gen n test qsos use current band etc
    .tdwin <sec>       display node bcasts exceeding this time skew
    .st                this station status
    .re                summary band report
    .ba                station band report
    .pr                generate entry and log files
    .remip <n.n.n.n>   remote ip to join to (TCP) (0.0.0.0 off)
    .timeok n          declare system time good or not (1/0)

    .delete <node> <seq_num> <reason>    delete log entry
            """

            viewtextv(m,'Command Help')
            kbuf = ""
##            text.insert(END,'\n')
##            return

        pwr,s = testcmd(".pow",r"[0-9]{1,4}n?",power)
        if pwr != power: setpwr(pwr)

        netsync.rem_host,s = testcmd('.remip',r'([0-9]{1,3}[.]){3}[0-9]{1,3}',netsync.rem_host)
        if s: globDb.put('remip',netsync.rem_host)

##        v,s = testcmd('.remcli',r'[0-1]',netsync.rem_cli)
##        if s and v == 1:
##            pass # start client thread
##        v,s = testcmd('.remsrv',r'[0-1]',netsync.rem_srv)
##        if s and v == 1:
##            pass # start server thread

        v,s = testcmd(".timeok", r"[0-1]", str(timeok))
        timeok = int(v)

        v,s = testcmd(".debug", r"[0-9]+", str(debug))
        debug = int(v)

        v,s = testcmd(".tdwin", r"[0-9]{1,3}", str(tdwin))
        tdwin = int(v)

        v,s = testcmd(".testq", r"[0-9]{1,2}", str('0'))
        testq = int(v)
        if testq: testqgen(testq)

        v,s = testcmd(".gpsclock",r"[0-1]","2")
        if v != "2": mclock.gpsclockDebug(v)

        saveglob()
        renew_title()

        m = re.match(r"[.]set ([a-z0-9]{3,6}) (.*)$", kbuf)  # generic set
        if m:
            name,val = m.group(1,2)
            r = gd.setv(name,val,now())
            if r: text.insert(END,"\n%s\n"%r)
            else:
                text.insert(END,"\n")
                qdb.globalshare(name,val)   # global to db
            kbuf = ""
            renew_title()
##            return

        m = re.match(r"[.]band (((160|80|40|20|15|10|6|2|220|440|900|1200|sat)[cdp])|off)", kbuf)
        if m:
            print
            nb = m.group(1)
##            kbuf = ""
##            text.insert(END,"\n")
            bandset(nb)
##            return

        if re.match(r'[.]off$',kbuf):
            bandoff()
            kbuf = ""
##            text.insert(END,"\n")
##            return

        if re.match(r'[.]ba$',kbuf):
            qdb.bands()
            kbuf = ""
##            text.insert(END,"\n")
##            return

        if re.match(r'[.]pr$',kbuf):
            contestlog(1)
            text.insert(END," Entry/Log File Written")
            kbuf = ""
##            return

        p = r'[.]delete ([a-z0-9-]{1,9}) ([0-9]+) (.+)'
        if re.match(p,kbuf):
            m = re.match(p,kbuf)
            nod,seq,reason = m.group(1,2,3)
            qdb.delete(nod,seq,reason)
            kbuf = ""
##            text.insert(END,"\n")
##            return

        p = r'[.]edit ([a-z0-9]{1,6})'
        if re.match(p,kbuf):
            m = re.match(p,kbuf)
            call = m.group(1)
#            qdb.delete(nod,seq,reason)
            kbuf = ""
            text.insert(END," to edit use mouse click on log entry")
##            return

        if re.match(r'[.]node',kbuf):
            if band != 'off':
                text.insert(END,"\nSet band off before changing node id")
                kbuf = ""
                return
            node,s = testcmd(".node", r"[a-z0-9-]{1,8}",node)
            if s: renew_title()
            #text.insert(END,"\n")
##            return

        if re.match(r'[.]st$',kbuf):           # status  xx mv to gui
            print
            print
            print "FD Call   %s"%string.upper(gd.getv('fdcall'))
            print "GOTA Call %s"%string.upper(gd.getv('gcall'))
            print "FD Report %s %s"%(string.upper(gd.getv('class')),gd.getv('sect'))
            print "Band      %s"%band
            print "Power     %s"%power
            print "Operator  %s"%operator
            print "Logger    %s"%logger
            print "Node      %s"%node
            if authk != "" and node != "": print "Net       enabled"
            else: print "Net       disabled"
            print
            kbuf = ""
##            text.insert(END,"\n")
##            return

        if re.match(r'[.]re$',kbuf):           # report  xx mv to gui
            print
            print "  band  cw q   pwr dig q   pwr fon q   pwr"
            qpb,ppb,qpop,qplg,qpst,tq,score,maxp,cwq,digq,fonq,qpgop,gotaq,nat,sat = qdb.bandrpt()
            for b in (160,80,40,20,15,10,6,2,220,440,1200,'sat','gota'):
                print "%6s"%b,
                for m in 'cdp':
                    bm = "%s%s"%(b,m)
                    print "%5s %5s"%(qpb.get(bm,0),ppb.get(bm,0)),
                print
            print
            print "%s total Qs, %s QSO points,"%(tq,score),
            print maxp,"watts maximum power"
            kbuf = ""
##            text.insert(END,"\n")
##            return

        if kbuf and kbuf[0] == '.':                     # detect invalid command
            text.insert(END," <= Invalid Command\n")
            kbuf = ""
##            text.insert(END,"\n")
##           # return
##        return




def proc_qso():
            "check for valid contact"

            global kbuf

            if kbuf[-1:] == ' ':
                stat,ftm,pfx,sfx,call,xcall,rept = qparse3(kbuf)
            else:
                stat,ftm,pfx,sfx,call,xcall,rept = qparse3(kbuf+' ')
            #print "parse result %d '%s'"%(stat,kbuf)
            if stat == 5:                               # whole qso parsed
##                buf = ""
                if len(node) < 3:
                    text.insert(END," ERROR, set .node <node_id> before logging\n")
##                elif qdb.dupck(call, band):             # dup check
                elif qdb.dupck(call,band,rept[:4]):             # dup check
                    text.insert(END," DUP on band %s\n"%band)
                else:
                    text.insert(END," QSL")
                    em = ''
                    if band == "off": em += " Band "
                    if ival(power) < 1: em += " Power "
                    if len(operator) < 2: em += " Operator "
                    if len(logger) < 2: em += " Logger "
                    if em: text.insert(END,"- WARNING: ( %s ) NOT SET"%em)
                    text.insert(END,"\n")
                    tm = now()
                    if ftm:                             # force timestamp
                        tm = tm[0:4]+ftm[0:8]+tm[11:]   # yymmdd.hhmmss
                    qdb.qsl(tm,xcall,band,rept)
                kbuf = ""
            elif stat == 4:
                kbuf = ""
                if showthiscall(call) == 0:
                    text.insert(END," none found\n")


def procQspace():    # process space in Q entry

        global kbuf,suffix

#    if ch == ' ':               # space, check for prefix/suffix/call

        stat,tm,pfx,sfx,call,xcall,rept = qparse3(kbuf+' ')

        if stat == 2:           # suffix, dup check NOTE may have class ;section before suffix
            suffix = sfx
            #kbuf = ""
            r = qdb.sfx2call(suffix,band)
            if not r: r = 'None'
            text.insert(END,": %s on band '%s'\n"%(r,band))
            kbuf = kbuf[:-len(sfx)]
            text.insert(END,kbuf)
            return

        elif stat == 3:                 # prefix, combine w suffix
            stat,tm,pfx,sfx,call,xcall,rept = qparse3(kbuf+suffix+' ')
            if stat >= 4:               # whole call or more
                kbuf += suffix
                text.insert(END,suffix)    # fall into call dup ck

        if stat >= 4:           # whole call, dup chk
            #if qdb.dupck(xcall,band):
            if qdb.dupck(call,band,''):
                text.insert(END," DUP on band %s\n"%band)
                showthiscall(call)
                kbuf = ""
                return
            else:
##                kbuf += ' '
##                text.insert(END,' ')
                if stat == 4:
                    if showthiscall(call): # may want to make this optional due to speed issues
                        #text.insert(END,"%s "%xcall)
                        #text.insert(END,"%s "%kbuf)  # seems to have extra space
                        text.insert(END,"%s"%kbuf)

        if stat > 0:
            if kbuf[-1:] != ' ':
                kbuf += ' '
                text.insert(END,' ')



def kevent(event):
    "keyboard event handler"

##    print "event '%s' '%s' '%s'"%(event.type,event.keysym,event.keysym_num)

    k = event.keysym_num

    if k > 31 and k < 123:      # space to z
        proc_key(chr(event.keysym_num))
    elif k == 65288:            # backspace
        proc_key('\b')
    elif k == 65307:            # ESC
        proc_key('\x1b')
    elif k == 65293:            # return
        proc_key('\r')
    elif k == 65361:            # left arrow
        print "left"
    elif k == 65362:            # up arrow
        print "up"
    elif k == 65363:            # right arrow
        print "right"
    elif k == 65364:            # down arrow
        print "down"
    elif k == 65505:            # shift key, ignore
        pass
    else:                       # display key code for unrecognized key
        print "ignored key",k

    text.see(END)               # insure that it stays in view

    return "break"              # prevent further processing on kbd events

def focevent(e):
    text.mark_set('insert',END)
    return "break"

class Edit_Dialog(Toplevel):
    'edit log entry dialog'
    def __init__(self,parent,node,seq):
        s = '%s.%s'%(node,seq)
        self.node,self.seq = node,seq
        if qdb.byid[s].band[0] == '*': return
        top = self.top = Toplevel(parent)
        #Toplevel.__init__(self,parent)
        #self.transient(parent)     # avoid showing as separate item
        tl = Label(top,text='Edit Log Entry',font=fdbfont,bg='gray',relief=RAISED)
        tl.grid(row=0,columnspan=2,sticky=EW)
        tl.grid_columnconfigure(0,weight=1)
        Label(top,text='Date',font=fdbfont).grid(row=1,sticky=W)
        #Label(top,text='Time',font=fdbfont).grid(row=2,sticky=W)
        Label(top,text='Band',font=fdbfont).grid(row=3,sticky=W)
        #Label(top,text='Mode',font=fdbfont).grid(row=4,sticky=W)
        Label(top,text='Call',font=fdbfont).grid(row=5,sticky=W)
        Label(top,text='Report',font=fdbfont).grid(row=6,sticky=W)
        Label(top,text='Power',font=fdbfont).grid(row=7,sticky=W)
        #Label(top,text='Natural',font=fdbfont).grid(row=8,sticky=W)
        Label(top,text='Operator',font=fdbfont).grid(row=9,sticky=W)
        Label(top,text='Logger',font=fdbfont).grid(row=10,sticky=W)
        self.de = Entry(top,width=13,font=fdbfont)
        self.de.grid(row=1,column=1,sticky=W,padx=3,pady=2)
        self.de.insert(0,qdb.byid[s].date)
        #self.de.insert(0,qdb.byid[s].date[:6])
##             self.src,self.seq,
##             self.date,self.band,self.call,self.rept,
##             self.powr,self.oper,self.logr
##        self.te = Entry(top,width=6,font=fdbfont)
##        self.te.grid(row=2,column=1,sticky=W,padx=3,pady=2)
##        self.te.insert(0,qdb.byid[s].date[-6:])
        self.be = Entry(top,width=5,font=fdbfont)
        self.be.grid(row=3,column=1,sticky=W,padx=3,pady=2)
        #self.be.configure(bg='yellow') #test yes works
        self.be.insert(0,qdb.byid[s].band)
##        self.me = Entry(top,width=1,font=fdbfont)
##        self.me.grid(row=4,column=1,sticky=W,padx=3,pady=2)
##        self.me.insert(0,qdb.byid[s].band[-1])
        self.ce = Entry(top,width=11,font=fdbfont)
        self.ce.grid(row=5,column=1,sticky=W,padx=3,pady=2)
        self.ce.insert(0,qdb.byid[s].call)
        self.re = Entry(top,width=24,font=fdbfont)
        self.re.grid(row=6,column=1,sticky=W,padx=3,pady=2)
        self.re.insert(0,qdb.byid[s].rept)
        self.pe = Entry(top,width=5,font=fdbfont)
        self.pe.grid(row=7,column=1,sticky=W,padx=3,pady=2)
        self.pe.insert(0,qdb.byid[s].powr)
##        self.ne = Entry(top,width=1,font=fdbfont)
##        self.ne.grid(row=8,column=1,sticky=W,padx=3,pady=2)
##        self.ne.insert(0,'n')
        self.oe = Entry(top,width=3,font=fdbfont)
        self.oe.grid(row=9,column=1,sticky=W,padx=3,pady=2)
        self.oe.insert(0,qdb.byid[s].oper)
        self.le = Entry(top,width=3,font=fdbfont)
        self.le.grid(row=10,column=1,sticky=W,padx=3,pady=2)
        self.le.insert(0,qdb.byid[s].logr)
        bf = Frame(top)
        bf.grid(row=11,columnspan=2,sticky=EW,pady=2)
        bf.grid_columnconfigure((0,1,2),weight=1)
        db = Button(bf,text=' Delete ',font=fdbfont,command=self.dele)
        db.grid(row=1,sticky=EW,padx=3)
        sb = Button(bf,text=' Save ',font=fdbfont,command=self.submit)
        sb.grid(row=1,column=1,sticky=EW,padx=3)
        qb = Button(bf,text=' Quit ',font=fdbfont,command=self.quitb)
        qb.grid(row=1,column=2,sticky=EW,padx=3)
        #self.wait_window(top)
    def submit(self):
        print 'submit edits'
        error = 0
        t = self.de.get().strip()               # date time
        print t
        self.de.configure(bg='white')
        m = re.match(r'[0-9]{6}\.[0-9]{4,6}$',t)
        if m:
            newdate = t + '00'[:13-len(t)]
            print newdate
        else:
            self.de.configure(bg='yellow')
            error += 1
        t = self.be.get().strip()               # band mode
        self.be.configure(bg='white')
        newband = ''
        if contest == "FD":
            m = re.match(r'(160|80|40|20|15|10|6|2|220|440|900|1200|sat)[cdp]$',t)  # should unify the band string
            if m:
                newband = t
                print newband
        elif contest == "VHF":
            if t[:-1] in bandToScore:
                newband = t
                print newband
        if newband == '':
            self.be.configure(bg='yellow')
            error += 1
        t = self.ce.get().strip()               # call
        self.ce.configure(bg='white')
        m = re.match(r'[a-z0-9/]{3,11}$',t)
        if m:
            newcall = t
            print newcall
        else:
            self.ce.configure(bg='yellow')
            error += 1
        t = self.re.get().strip()               # report
        self.re.configure(bg='white')
        m = re.match(r'.{4,24}$',t)
        if m:
            newrept = t
            print newrept
        else:
            self.re.configure(bg='yellow')
            error += 1
        t = self.pe.get().strip().lower()       # power
        self.pe.configure(bg='white')
        m = re.match(r'[0-9]{1,4}n{0,1}$',t)
        if m:
            newpowr = t
            print newpowr
        else:
            self.pe.configure(bg='yellow')
            error += 1
        t = self.oe.get().strip().lower()       # operator
        self.oe.configure(bg='white')
        if participants.has_key(t):
            newopr = t
            print newopr
        else:
            self.oe.configure(bg='yellow')
            error += 1
        t = self.le.get().strip().lower()       # logger
        self.le.configure(bg='white')
        if participants.has_key(t):
            newlogr = t
            print newlogr
        else:
            self.le.configure(bg='yellow')
            error += 1
        if error == 0:
            # delete and enter new data
            print 'no errors, enter data'
            reason = 'edited'
            qdb.delete(self.node,self.seq,reason)
            qdb.postnew(newdate,newcall,newband,newrept,newopr,newlogr,newpowr)
            self.top.destroy()
            text.insert(END," EDIT Successful\n")
    def dele(self):
        print 'delete entry'
        reason = 'deleteclick'
        qdb.delete(self.node,self.seq,reason)
        self.top.destroy()
    def quitb(self):
        print 'quit - edit aborted'
        self.top.destroy()

def edit_dialog(node,seq):
    'edit log entry'
    # validate, make sure entry is not already edited,
    # and that it is a proper entry to edit at all
    ed = Edit_Dialog(root,node,seq)
    #ed.wait_window(ed)
    #wait for it

def log_select(e):
    'process mouse left-click on log window'
##    print e.x,e.y
    t = logw.index("@%d,%d"%(e.x,e.y))
##    print t
    line,col = t.split('.')
    line = int(line)
##    print line
    logtext = logw.get('%d.0'%line,'%d.82'%line)
##    print logtext
    seq = logtext[65:69].strip()
    if len(seq) == 0: return 'break'
    seq = int(seq)
    stn = logtext[69:].strip()
    if len(stn) == 0: return 'break'
    print 'edit',stn,seq
    if stn == node:             # only edit my own Q's
        edit_dialog(stn,seq)
    else: print "Cannot Edit other node's Q"
    return 'break'

updatect = 0

def update():
    "timed updater"
    global updatect

    root.after(1000,update)         # reschedule early for reliability

    sms.prout()                     # 1 hz items
    updatebb()
    net.si.age_data()
    mclock.adjust()

    if mclock.level == 0:           # time master broadcasts time more frequently
        net.bcast_time()

    updatect += 1

   # if (updatect % 5) == 0:         # 5 sec
       # net.bcast_now()

    if (updatect %10) == 0:         # 10 sec
        updateqct()   # this updates rcv packet fail
        renew_title() # this sends status broadcast

    if (updatect %30) == 0:         # 30 sec
        mclock.update()

    if updatect > 59:               # 60 sec
        updatect = 0

root.bind('<ButtonRelease-1>',focevent)
text.bind('<KeyPress>',kevent)
logw.bind('<KeyPress>',kevent)      # use del key for?xx
logw.bind('<Button-1>',log_select)  # start of log edit

root.after(1000,update)             # 1 hz activity

root.mainloop()                     # gui up, returns on exit

print "\nShutting down"

band = 'off'                        # gui down, xmt band off, preparing to quit
net.bcast_now()                     # push band out
time.sleep(0.2)
saveglob()                          # save globals
print "  globals saved"
time.sleep(0.2)
net.close_all()                     # close ports
time.sleep(0.2)
print "  ports closed"

print "\n\nFDLog is shut down, you should close this console window now"
time.sleep(0.5)

os._exit(0)                         # kill the process


# this is the end of code, only comments or parked code below here


# test procedure (draft)

# test against old standard version (UDP)
# test against self version (UDP and TCP)

# test operator, logger, power, natural, band set, seeing other band
# test qsos
# test editing a qso
# test filling using .testq 10 on each machine (note does bcasts so may need to shut down FDLog, do testq, start up FDLog to get fill testing)
# test generating a report

# test time sync
#   .set tmast <node>




# Suggestions

# FD 2005 pre-meeting
#
#  thought - make the RCVP button bring up a description of the errors there
#  and the other buttons above that similar - bring up descriptions of what
#  they mean..
#
# FD 2004 notes
#   used version 1.125 on FD04.
#   version 1.126 is the same with comments/bugs/etc added
#
# question - where are operator/station scores? make easier to see??
#
# feature request - vhf contest version (Kit) DONE,
#   or general contests (Frank)
#   have a .set contest variable DONE
#
# feature request - editing previous input functionality ***** DONE
#
# feature request - editing current input (out of order input)
#   cursor keys left, right, char->insert, delete
#   tab to cycle words?
#   refrain from syntax checking while editing?
#
# feature request - generate port number w/o field? what happens if port is
#   already in use? dynamic port searching?? done.
#
# suggestion - better frequency chart. (Cal)
#
# issue - probably does not handle the 1d-1d contacts properly?
#
# consider band timeout - 30 minutes w/o contact releases band?
#
# old idea - Eric - balloon popup on band shows who is there


# Short List
#
# add node list display after db read during startup?
#
# raise GUI to front during startup (tried, don't know how)
#
# someday should make any attempt to log q with callsign that is in the
# operator list come up a dup without including them in the dup sheet!

# thoughts 7/30/2002
#
# mv info files to info dir
# set up autodiscovery to build menus
# do same for manuals
# actually, let's move most of the doc stuff out
# to a web tree under the program, and take it
# completely out of the program proper

##ToDo, Brainstorming List
##
##  add phonetic alphabet display
##
##  .st to popup
##
##  limit call width in log display (done?)
##  stop log processing every 10 seconds to get score. do less. count.
##  dupcheck on 0 power not working. ok?
##
##  document .set system better
##
##  Weo suggested making Control-C text copy/paste work.
##  Eric suggested show stations on band with bubble dialog
##    (also q count etc)
##  do better job of reporting net status & info
##  gui
##    sta/oper/logr/pwr/q dsply in lower rt?
##    delete log entry dialog box???
##    more reports
##  add natural power comment section to entry
##  code cleanup
##  greplog .grep <match>

# wa6nhc 5/2013 suggests precluding site operators from being logged as Q's

# some foreign callsigns not supported properly (really a feature request)
#   8a8xx
#   need to change the way this works
#   define a suffix as trailing letters
#   prefix as anything ending in digits
#   bring down a previous suffix with a character such as ' or .

# 2014 suggestions
#
# add a comparison to previous year group scores


# 2016 suggestions
#
# see Rick's Google Doc for more from RickB, GlennT, TomJ
#
# Alan Suggestions
#
# make contacts with power over 1500W drop out of scoring
# or just limit to 1500w?
#
# initial startup GUI:
# come on to dialog box for startup
# then shut down this startup gui and continue
# node id
# checkbox or radio button for test / operate
# database / authentication code radio choice button
#   tst / ... (remembered code)
# serial GPS clock status
# helpful information / help button(s)
# START LOGGING button (or RETURN activates)
# QUIT button (ESCAPE activates)
# station name ?
# database / authentication code
# remote ip?
# time offset?
# time?
# 

# Code Parking

### temporary testing for the future (moved from the top)
### may want to use JSON for transport later on
##
##import json
##
##msg = {}
##msg['S'] = 'akb-2'
##msg['N'] = '202'
##msg['T'] = 'Q'
##msg['q'] = 'w1aw'
##msg['d'] = '20130621:0034'
##msg['b'] = '40'
##msg['m'] = 'P'
##
##msg2 = {}
##msg2['T'] = 's'
##msg2['S'] = 'akb-2'
##
##print json.dumps((msg,msg2),separators=(',',':'))
##
##raise"quit"

# eof   (5708 lines 6/2016) (6626 7/2016) (6064 7/20/2016)
