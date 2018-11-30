from webavail import *
import sys

#Check Input URL
bad_url_1 = 'reddit'
assert check_input_url(bad_url_1) == 1
bad_url_2 = 'reddit.com'
assert check_input_url(bad_url_1) == 1
bad_url_3 = 'google.notarealdomain'
assert check_input_url(bad_url_3) == 1

good_url_1 = "http://www.google.com"
assert check_input_url(good_url_1) == 0
good_url_2 = "http://api.reddit.com"
assert check_input_url(good_url_1) == 0
good_url_3 = "https://www.google.com"
assert check_input_url(good_url_3) == 0
good_url_4 = 'https://www.reddit.com/r/programming/'
assert check_input_url(good_url_4) == 0

#Check Result of URL
url_check_1 = "madeupnonsense"
assert check_result_of_url(url_check_1)[0] == 1
url_check_2 = "http://www.google.com/doesnotresolve"
assert check_result_of_url(url_check_2)[0] == 1
url_check_3 = "http://google.com"
assert check_result_of_url(url_check_3)[0] == 0
assert check_result_of_url(url_check_3)[1] == 200
url_check_4 = "http://www.google"
assert check_result_of_url(url_check_4)[0] == 1

#Check DNS Records
dns_check_1 = "http://www.reddit.com/"
assert sorted(dns_check_1['NS_records'])[0] == 'ns-1029.awsdns-00.org.'
assert sorted(dns_check_1['NS_records'])[-1] == 'ns-557.awsdns-05.net.'
assert sorted(dns_check_1['A_records'])[0] == '151.101.1.140'

dns_check_2 = "https://hub.docker.com"
assert sorted(dns_check_1['NS_records'])[0] == 'ns-1289.awsdns-33.org.'
assert sorted(dns_check_1['NS_records'])[-1] == 'ns-568.awsdns-07.net.'
assert sorted(dns_check_1['A_records'])[0] == '34.232.230.241'



print "All Tests Passed!"
