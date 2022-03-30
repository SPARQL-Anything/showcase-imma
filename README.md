# Building a knowledge graph of artists and artworks scraping the IMMA museum website

In what follows, `fx` refers to the following command
```
java -jar sparql-anything-0.5.0-SNAPSHOT.jar  
```

## Process
Extract the list of artists from the Web page and build an XML result set with ?artistNickname and ?artistUrl.
```
fx -q queries/imma-artists.sparql -o imma-artists.xml -f xml
```

Extract data from the artists' Web page and build one JSON-LD file each (create folder 'artists' first).
```
fx -q queries/imma-artist.sparql -i imma-artists.xml -p "artists/?artistNickname.jsonld" -f json
```
Extract the list of artworks' Web pages from the JSON-LD files of the artists.
```
fx -q queries/imma-artworks.sparql -l artists/ -o imma-artworks.xml -f xml
```
Extract data from the artworks' Web pages and build one JSON-LD file each (create folder 'artworks' first).
```
fx -q queries/imma-artwork.sparql -i imma-artworks.xml -p "artworks/?artworkNickname.jsonld" -f json
```
Load into your favourite triple store.

## Extract single entries

Extract data from a specific artist Web page:
```
fx -q queries/imma-artist.sparql -v artistNickname=lambert-gene -v artistUrl=https://imma.ie/artists/gene-lambert/ -p "artists/?artistNickname.jsonld" -f json
```
Extract data from a specific artwork Web page:
```
fx -q queries/imma-artwork.sparql  -v artworkNickname=naturaleza-desde-la-ventana -v artworkUrl=https://imma.ie/collection/naturaleza-desde-la-ventana/ -p "artworks/?artworkNickname.jsonld" -f json
fx -q queries/imma-artwork.sparql  -v artworkNickname=berry-dress -v artworkUrl=https://imma.ie/collection/berry-dress/ -p "artworks/?artworkNickname.jsonld" -f json
```
