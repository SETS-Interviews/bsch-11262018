import sys
import dns.resolver
import subprocess
import re

def main():
    try:
        print sys.argv[1]
        sys.exit(0)
    except IndexError as e:
        print "IndexError: {}".format(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
