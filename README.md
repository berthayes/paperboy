# paperboy
Use ```ebook-convert``` from [Calibre](https://calibre-ebook.com/) to download your favorite newspaper(s) &amp; use [rmapy](https://github.com/subutux/rmapy) to upload to my.remarkable.com.  Set with cron and have the newspaper delivered daily as a PDF to your [reMarkable](https://remarkable.com/) tablet!

### To Run:
  - Make sure you register your "device" - the API client - to get an auth token.  http://rmapi.subutux.be/quickstart.html#registering-the-api-client
  - You'll want to either edit the ```fetch_paper.sh``` script or create a ```~/newspapers``` directory; this is where downloaded PDF newspapers are written.