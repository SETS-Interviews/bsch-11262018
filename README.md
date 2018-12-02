# bsch-11262018 - Website Availability Script
## Overview
Python Command Line Utility to Check the Status of a Website.
Takes One Parameter (Website) and returns the website availability,
IP address of the host, Name Servers and total hops to reach
the host.

## Requirements
- Python 2.7
- Linux Based Platform
- Ping (executable from command line)

Python 3rd Party Libraries Required:
- dnspython>=1.15.0
- validators>=0.11.0

## Quick Start
To run, download this script from github using the following
command:
> git clone https://github.com/SETS-Interviews/bsch-11262018.git

Then download the required libraries, if not already installed.
Once completed run the following command in the Linux shell.
> python webavail.py http://www.google.com

URL must be fully qualified and include the protocol in the command. The result will then print out in the terminal.

## Utility Output

The utility will return the following information:

- HTTP Code of the response (if successful)
- IPs of the URL
- The Name Servers of the URL
- The Number of hops to the host IP
