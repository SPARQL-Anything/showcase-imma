import csv
from PIL import Image, UnidentifiedImageError 
import requests
from io import BytesIO
import mimetypes
from os.path import exists

def downloadFile(imageID, url):
    try:
        file_exists = exists('./images/{0}.jpg'.format(imageID))
        if(file_exists):
            return
        print("Doing", imageID,"from", url)
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type)
        print("Saving", imageID, extension)
        img.save('./images/{0}{1}'.format(imageID,extension))
    except UnidentifiedImageError:
        return

with open('images.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for row in reader:
        downloadFile(row[0].replace("https://w3id.org/spice/imma/documentation/",""), row[1])