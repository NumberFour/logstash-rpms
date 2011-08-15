#!/usr/bin/env python
""" Grabs all the sources for a given version number of logstash """

import urlgrabber
from optparse import OptionParser

parser = OptionParser()
(options,args) = parser.parse_args()
print "Getting Main Source for version %s " % args[0]
urlgrabber.urlgrab('http://semicomplete.com/files/logstash/logstash-%s-monolithic.jar' % args[0])
print "Getting logstash-monolithic"
