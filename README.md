
Automatically download each tweet in a ThreadReaderApp-archived Twitter thread.
This will also download all the media in each of the tweets using [TWMD](https://github.com/mmpx12/twitter-media-downloader)

# How to use it:
To use this docker container:

`docker run -v <dir_on_hostOS_for_downloads>/:/workdir -it sa7ori/threadreader_downloader` 

it will launch right into the downloader asking for a URL.
![](readme_assets/threadreader_downloader_howto.png)

Then after everything has run, you'll get a directory like this:

![](readme_assets/threadreader_downloader_howto2.png)

Note: `<dir_on_hostOS_for_downloads>` is the fully qualified path of the directory
that will be shared into the docker container. The container will download and
log everything into that shared directory so it is available on the host.

Example:
 
`docker run -v /home/s7ephen/great_twitterthread/:/workdir -it sa7ori/threadreader_downloader`

# Link to the Dockerhub:
https://hub.docker.com/r/sa7ori/threadreader_downloader

# Using tools within the container:
To use the tools inside the container like m3u8_download to download
media from a m3u8 link, use:

`docker run -v <dir_on_hostOS_for_downloads>/:/workdir -it sa7ori/threadreader_downloader bash`

To use m3u8_download:

`m3u8_download https://urltosome/file/hosted/somwhere/v5dpHSFzJ33kY-QQ.m3u8 tweet_20.mp4`

This will use ffmpeg to parse and follow/download all the m3u8 interlinked files and download (and reassemble) the media fragments and save to tweet_20.mp4 or whatever filename you give it.

# Downloading Twitter Videos with m3u8_download:

You can use this to download videos directly from twitter also. To do this:
- Turn on your browser's "Developer Tools"
- Load (or reload) the tweet URL in your browser.
- In the "Network" tab, enter `m3u8` into the "filter"
- If you see no results, refresh the page.
- When a result appears (usually the first one) right clip and "Copy URL"
- Paste that full URL into m3u8_download.

Example:
fetching the m3u8
![](readme_assets/m3u8_download_howto.png)
running m3u8_download
```
m3u8_download 'https://video.twimg.com/ext_tw_video/1763235266049777665/pu/pl/2fbRnL9S1NDv6Wcw.m3u8?variant_version=1&tag=12&container=cmaf' video.mp4
```  
![](readme_assets/m3u8_download_howto2.png)

# Extra Note: Downloading Multiple Twitter Threads
This whole repo was just a quick-hack so it isnt polished up to take command-line,
arguments or have features like reading URLs from a file (as input).

I dont know who would find this useful (I make similar notes like this for
myself, like I'm writing to a dumber future-self), but here is a simple mod 
to download multiple Twitter threads using what's here...with minimal asspain.

So to download multiple Twitter threads. Put all the URLs in a text file (one per line) then:
`while read in; do ./download_threadreaderapp_thread.py "$in"; done < threads_to_download.txt`
![](readme_assets/quick_mod_to_download_multiple_threads.png)
then you'll have a directry like this:
![](readme_assets/quick_mod_to_download_multiple_threads2.png)

