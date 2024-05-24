#!/usr/bin/env python
# 
# This downloads the text and media from all tweets
# in a threadreaderapp twitter thread.
# 
# Twitter has made it difficult to screen-scrape tweets
# and threadreaderapp only displays tweet-threads from
# currently active twitter users, so this tool can be used
# to archive twitter threads ideally before they (or the user) disappears.
# ============
# install prerequisites with:
# apt-get -y install python-requests
# apt-get -y install python-lxml
# apt-get -y install ffmpeg
#
# Get Twmd:
# https://github.com/mmpx12/twitter-media-downloader/releases/
#
# Videos download from TWMD is as m3u8 files and not the video files themselves
# These videos can be downloaded using /root/m3u8_download.sh which uses
# ffmeg to parse the m3u8 seed file and follow all the embedded links to
# download and reassemble all the segments of the mp4
#
# EXAMPLE USAGE: 
#    m3u8_download.sh ./v5dpHSFzJ33kY-QQ.m3u8 tweet_20.mp4
#  
from lxml import html
from lxml import etree
import requests, os
# url = "https://threadreaderapp.com/thread/1715789046943740102.html"
url = raw_input("Enter the threadreaderapp URL> ")
page = requests.get(url)
tree = html.fromstring(page.content)
elements = tree.xpath('/html/body/div[4]/div')
#tweet_elements = tree.findall('tweet_') #The element that contains the tweet
                                         #text on the threadreaderapp page is
                                         #has names like "tweet_1", "tweet_2", etc
#col12 = tree.find_class("col-12 hide-mentions") # the "div" where the tweets
                          # are found is called "col-12 hide-mentions"
tweets = tree.find_class("content-tweet allow-preview") # the "class" of each tweet
                          # is "content-tweet allow-preview" 
#import pdb;pdb.set_trace()

threadid = url.split('/')[-1].split('.')[0] #get the number from .html part of url
if len(tweets) == 0:
    print "No tweets found on that page."
    import sys;sys.exit(1)
print "Looks like there are %d tweets thread '%s'." % (len(tweets), threadid)
i = 1
print "Creating output directory: ",threadid
os.mkdir(threadid)
os.chdir(threadid)
with open("raw_threadreaderapp_response.txt", "w") as threadreader_f:
    threadreader_f.write(page.content)
    print "\t[+] wrote to: raw_threadreaderapp_response.txt"
    threadreader_f.close()
for element in tweets:
    print "----------- TWEET #%d ------------" % i
    print "\n\t=== USER ==="
    print "tweeter: ", element.get("data-screenname")
    print "\n\t=== TWEET ID ==="
    print "id: ", element.get("data-tweet")
    tweet_order = element.get("id")
    print "\n\t=== TWEET ORDER ==="
    print "tweet_order: ", tweet_order
    print "Changing to dir '%s' for output." % (tweet_order)
    os.mkdir(tweet_order);os.chdir(tweet_order)
    print "\n\t=== TEXT OF TWEET ==="
    print "Tweet text: "
    print element.text.encode('utf-8')
    with open("tweet.txt", "w") as tweet_f:
        tweet_f.write(element.text.encode('utf-8'))
        print "\t[+] wrote to: tweet.txt"
        tweet_f.close()
    print "\n\t=== RAW TEXT ==="
    with open("tweet_raw.txt", "w") as tweet_raw_f:
        tweet_raw_f.write(etree.tostring(element, pretty_print=True))
        print "\t[+] Wrote to: tweet_raw.txt"
        tweet_raw_f.close()
    #print etree.tostring(element, pretty_print=True) #print the xml in treeform
    #import pdb;pdb.set_trace()
    print "\n\t=== RUNNING TWMD ==="
    cmd = "/root/twitter-media-downloader -t %s" % element.get("data-tweet")
    print cmd
    os.system(cmd)
    print "-------------------------------------"
    
    print "Changing back to the tweet thread directory."
    os.chdir('..')
    i+=1
