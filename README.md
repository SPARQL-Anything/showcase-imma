# Building a knowledge graph of artists and artoworks of the IMMA museum website

In what follows, `fx` refers to the following command
```
java -jar sparql-anything-0.0.4-SNAPSHOT.jar  
```

## Process
Extract the list of artists from the Web page and build an XML result set with ?artistNickname and ?artistUrl.
```
fx -q imma-artists.sparql -o imma-artists.xml -f xml
```

Extract data from the artists' Web page and build one JSON-LD file each (create folder 'artists' first).
```
fx -q imma-artist.sparql -i imma-artists.xml -p "artists/?artistNickname.jsonld" -f json
```
Extract the list of artworks' Web pages from the JSON-LD files of the artists.
```
fx -q imma-artworks.sparql -l artists/ -o imma-artworks.xml -f xml
```
Extract data from the artworks' Web pages and build one JSON-LD file each (create folder 'artworks' first).
```
fx -q imma-artwork.sparql -i imma-artworks.xml -p "artworks/?artworkNickname.jsonld" -f json
```
