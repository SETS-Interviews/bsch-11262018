import sys
import dns.resolver
import subprocess
import re

def main():
    #Check the input to make sure that a parameter was passed
    try:
        print sys.argv[1]
        sys.exit(0)
    except IndexError as e:
        print "IndexError: {}".format(e)
        sys.exit(1)

    #Check the input URL to confirm that it is well formed

    #Make an http request to the website to confirm that it is available

    #If unavailable, print message that it's unavailable

    #If available, check DNS records for all A record IPs and NS records
    #in order to return website IPs as well as Name Servers (including count)

    #Also if available, check the number of hops to the website utilizing
    #pythons subprocess module

    #Print this information to the console and exit the utility

if __name__ == "__main__":
    main()
