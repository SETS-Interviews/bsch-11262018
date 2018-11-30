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

def check_result_of_url(input_url):
    '''
    Checks the url by calling url and retrieving the status code.
    returns (0, <status_code>) if available.
    returns (1, <message>, <error>) if not available.
    '''
    try:
        response = urllib2.urlopen(input_url)
    except urllib2.URLError as e:
        m = "URL does not resolve to an IP."
        return (1, m)
    except urllib2.HTTPError as e:
        if e.code == 404:
            m = "Website is Unavailable. Error Code: {}.".format(e.code)
        else:
            m = "Website is Unavailable."
        return (1, m)
    except ValueError as e:
        m = "Unknown URL Type."
        return (1, m)

    return (0, response.code)

def check_dns_records(input_url):
    '''
    Checks the DNS records of the input url.
    Returns the 'A' and 'NS' records for the url in dictionary object.
    '''
    #'http://' needs to be removed from the input_url
    #A records need to be checked using all available elements of url
    #NS records need to check the domain and top level domain only

    pass

def check_number_of_hops(input_url):
    '''
    Takes the input_url and calls 'ping' one time to calculate the ttl.
    Returns int of ttl to IP.
    '''

    pass

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

    result = check_result_of_url(input_url)

    if result[0]: #If result returns non-zero response
        print result[1]
        exit(1)

    http_status_code = result[1]

    #If available, check DNS records for all A record IPs and NS records
    #in order to return website IPs as well as Name Servers (including count)

    dns_records = check_dns_records(input_url)

    #Also if available, check the number of hops to the website utilizing
    #pythons subprocess module

    count_hops = check_number_of_hops(input_url)

    #Print this information to the console and exit the utility

    print "URL: {}".format(input_url)
    print "Response Code: {}".format(http_status_code)
    print "The Website is currently available."
    print "Currently Available IPs for this url: "
    #for a in dns_records['A_records']:
    #    print "- {}".format(a)
    #print "Count of Name Servers for this url: {}"\
    #        .format(len(dns_record['NS_records']))
    print "Currently available Name Servers for this url: "
    #for ns in dns_records['NS_records']:
    #    print "- {}".format(ns)
    print "Count of Hops to this url: {}".format(count_hops)

if __name__ == "__main__":
    main()
