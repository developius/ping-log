# ping-log
A python-based pinger for collecting network response time data plus R markdown code for analysing the data & preducing a report.

## The problem
We often see internet response time problems at home and these usually lead to debates about what exactly is broken. 

It has to be said that our internet context is 'challenging'. We live in rural East Anglia (UK), our nearest PSTN Exchange is at least a couple of miles away and we are the penultimate phone number on the line. We're pretty sure the line is split, possibly several times, upstream of our property. Internally we live in a rambling barn conversion and the master phone socket is at one end - well away from where we want the wifi. We also have [celotex in the roof and foil-backed plasterboard](http://www.exbtengineers.com/wifi-problems/) in (some of) the walls. 

We've tried wifi replicators, power line and running the ADSL down a phone extension to the middle of the house. None have proved particularly successful. But we decided we needed some data to inform the next steps. In particular, was our broadband service rubbish or was our internal distribution system the culprit? Or was it a bit of both at different times?

Did we mention that we are a family of six (2 + 4) with seemingly countless IP devices? It might be relevant... one hunch was that the default settings and usage habits of teenagers-with-iPads might be a contributing factor.

## The solution (well, the research that comes before the solution...)
Since 2/6 of the family are nerdy data/stats/coding types we wrote a script to use ping on any unix-type OS (OS X & Debian being our weapons of choice) to collect response time data for:

* our base wifi router (which is also our ADSL modem) - this happens to be a BT HomeHub v3 but this is probably not relevant (?)
* www.google.co.uk - we assumed this to be reliably online so we could test external (out-of-home) connectivity

Command line parameters:
 
* file to save results to (.csv format in 'results' folder in current directory with start date/time appended)
* n minutes to run for (hint: 1440 = 1 day :-)
* n seconds between pings

The pinger sets off a ping every n seconds and records the result. When ping returns something meaningfull the millisecond response time is recorded against the date/time the ping started and the error colum will have "OK". An example:

    timestamp,host,milliseconds, error
    2016-04-28 10:53:56,www.google.co.uk,83.548, OK
    2016-04-28 10:53:57,router,121.820, OK
    2016-04-28 10:54:07,www.google.co.uk,71.019, OK
    2016-04-28 10:54:07,router,9.875, OK

Understood ping errors will be copied verbatim to the error column of the results. Mostly. Well, sometimes. See below.

## Our experiments

 We run the pinger on as many devices as possible on our home network and collate the data. Mostly this means running ssh to various OS X boxes and some Raspberry Pis. One Pi is permanently connected to the ADSL modem/base router while the rest 'float' across whichever internal networking method we are trying this week although we try to keep a few constant as a baseline in known fixed locations. We usually run the pinger for up to 24 hours collecting ping data every 10 seconds or so. We've been using [tmux](https://tmux.github.io/) to launch the script remotely and leave it running even if the ssh network connection dies. Which is symptomatic of the problems we face.

We use sftp to collect the data every few hours - or every few minutes if we are testing different configurations. At some point we will automate this process. 

Having collated the data we run the R markdown code using RStudio to generate a report. 

After all that we argue about what the result show and what to do about it.

## Code warnings
It isn't big and it isn't clever:
 * the pinger deals dis-gracefully with ICMP time outs and other ping errors. Some of these are currently caught by the R code but some aren't. For example you well get an 'OK' and an empty value in the milliseconds field even if the ping can't see your internal router - e.g. if you run the vanilla pinger outside your home network. We're working on it.
 * the R script records quite a few data read warnings that we have not really investigated
 * inevitably [#YMMV](https://en.wiktionary.org/wiki/YMMV)

