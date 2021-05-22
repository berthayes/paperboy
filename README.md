# paperboy
Use ```ebook-convert``` from [Calibre](https://calibre-ebook.com/) to download your favorite newspaper(s) &amp; use [rmapy](https://github.com/subutux/rmapy) to upload to my.remarkable.com.  Set with cron and have the newspaper delivered daily as a PDF to your [reMarkable](https://remarkable.com/) tablet!

### To Run:
  - Make sure you register your "device" - the API client - to get an auth token.  http://rmapi.subutux.be/quickstart.html#registering-the-api-client
  - You'll want to either edit the ```fetch_paper.sh``` script or create a ```~/newspapers``` directory; this is where downloaded PDF newspapers are written.

### To Run for Daily Delivery
If you have Calibre installed in Linux, you can edit ```fetch_paper.sh``` accordingly and run from Cron.

If you have Calibre installed in MacOS, cron is deprecated in favor of [launchd](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html) . 
  - Use this very short [article](https://medium.com/@chetcorcos/a-simple-launchd-tutorial-9fecfcf2dbb3) and the included ```com.paperboy.daemon.plist``` file to get daily delivery.  
  - Edit the ```com.paperboy.daemon.plist``` file to replace "bert" with your username.
  - This will download your dailies at 06:00 local time every morning.

### To Help:
  - SUPPORT LOCAL JOURNALISM!