# ping-log
A python-based pinger for collecting network response time data and associated R code for analysing it.

# The problem
We often see internet response time problems at home and these usually lead to debates about what exactly is broken. It has to be said that our internet contect is 'challenging'. We live in rural East Anglia (UK), our nearest PSTN Exchange is at least a couple of miles away and we are the penultimate phone number on the line. We're pretty sure the line is split, possibly several times, upstream of our property. Internally we live in a rambling barn conversion and the master phone socket is at one end - well away from where we want the wifi. We also have [http://www.exbtengineers.com/wifi-problems/](celotex in the roof and foil-backed plasterboard) in (some of) the walls. We've tried wifi replicators, power line and running the ADSL down a phone extension to the middle of the house. None have proved particularly successful. But we decided we needed some data to inform the next steps. In particular, was our broadband service rubbish or was our internal distribution system the culprit? Or was it a bit of both at different times?

Did I mention that we are a family of six (2 + 4) with seemingly countless IP devices? It might be relevant... one hunch was that the default settings and usage habits of teenagers-with-iPads might be a contributing factor.

# The solution (well, the research that comes before the solution...)
Since 2/6 of the family are nerdy data/stats/coding types we wrote a script to use ping on any unix-type OS (OS X & Debian being our weapons of choice) to collect response time data for:

* our base wifi router (which is also our ADSL modem) - this happens to be a BT HomeHub v3 but this is probably not relevant (?)
* www.google.co.uk - we assumed this to be reliably online so we could test external (out-of-home) connectivity

We run the pinger on as many devices as possible on our home network and collate the data. Mostly this means running ssh to various OS X boxes and some Raspberry Pis. One Pi is permanently connected to the ADSL modem/base router while the rest 'float' across whichever internal networking method we are trying this week although we try to keep a few constant as a baseline in known fixed locations. 

We've been using [tmux](https://tmux.github.io/) to launch the script remotely and leave it running even if the ssh network connection dies. Which is symptomatic of the problems we face.
