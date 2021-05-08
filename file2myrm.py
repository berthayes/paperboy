# Takes a filename/path as an argument
# uploads that file to a folder in my.remarkable.com
# http://rmapi.subutux.be/#quick-start

# Make sure to register your "device" first.
# See: http://rmapi.subutux.be/quickstart.html#registering-the-api-client

from rmapy.api import Client
from rmapy.document import ZipDocument
from datetime import date
import sys

# The name of the Folder in "My Files" in the reMarkable app
remarkable_folder = "sunday_paper"

today = date.today()
datestamp = date.isoformat(today)

rmapy = Client()
rmapy.renew_token()
rm = Client()
rm.renew_token()

delivery = sys.argv[1]
rawDocument = ZipDocument(doc=delivery)

books = [i for i in rm.get_meta_items() if i.VissibleName == remarkable_folder][0]
rm.upload(rawDocument, books)
