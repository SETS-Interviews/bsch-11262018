import sys
import urllib2
import dns.resolver
import subprocess
import re

def check_input_url(input_url):
    '''
    Checks the input url that it conforms to the standard format of
    <subdomain>.<domain>.<top-level domain> standard.

    Returns 0 if well-formed.
    Returns 1 if ill-formed.
    '''

    return 0

def main():
    #Check the input to make sure that a parameter was passed
    try:
        input_url = sys.argv[1]
    except IndexError:
        print "No url parameter passed. Please provide a url."
        sys.exit(1)

    #Check the input URL to confirm that it is well formed
    if check_input_url(input_url):
        print "URL is not well formed. Please provide a well formed url."
        sys.exit(1)

    #Make an http request to the website to confirm that it is available
    #If unavailable, print message that it's unavailable
    try:
        response = urllib2.urlopen(input_url)
    except urllib2.URLError:
        print "URL does not resolve to an IP."
        exit(1)
    except urllib2.HTTPError as e:
        if e.code == 404:
            print "Website is Unavailable. Error Code: {}.".format(e.code)
            exit(1)
        else:
            print "Website is Unavailable"
            raise

    #If available, check DNS records for all A record IPs and NS records
    #in order to return website IPs as well as Name Servers (including count)

    #Also if available, check the number of hops to the website utilizing
    #pythons subprocess module

    #Print this information to the console and exit the utility

    print "URL: {}".format(input_url)
    print "Response Code: {}".format(response.code)
    print "The Website is currently available."

if __name__ == "__main__":
    main()
