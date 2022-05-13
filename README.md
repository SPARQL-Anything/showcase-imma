# Construct a knowledge graph of artists and artworks of the IMMA museum website
This showcase demonstrates the use of SPARQL Anything for constructing a Knowledge Graph from data encoded in HTML pages.

In what follows, `fx` refers to the following command line
```
java -jar sparql-anything-<version>-.jar  
```

## Knowledge graph construction pipeline

### Step 1: list artists from the catalogue

This query extracts the list of artists from the Web page and build an XML result set with ?artistNickname and ?artistUrl.
The SPARQL result set file will be used in the next query to iterate over each one of the artists' pages.


| Title | Step 1: list artists from the catalogue |
|:----------|:-------------|
| __Query__ | [queries/imma-artists.sparql](queries/imma-artists.sparql)
| __Input__ | [https://imma.ie/artists/](https://imma.ie/artists/)
| __Output__ | [imma-artists.xml](imma-artists.xml) |
| __Type__ | SELECT |
| __Options__ | `html.selector=#az-group` |
| __Formats__ | HTML
| __Level__ | Novice

Run the example as follows:

```
fx -q queries/imma-artists.sparql -o imma-artists.xml -f xml
```

### Step 2: iterate over artists' web pages and create a JSON-LD for each one of them

In this step we use a parametrized query that is able to query an artists' web page and extract relevant metadata.
The query is repeated for each value of the SPARQL result set file produced in the previous step.
The command generates a JSON-LD for each execution, using the artist nickname as file name (one of the values provided by the result set).
Crucially, the JSON-LD files produced will include web pages of the related artworks.

| Title | Step 2: iterate over artists' web pages and create a JSON-LD for each one of them |
|:----------|:-------------|
| __Query__ | [queries/imma-artist.sparql](queries/imma-artist.sparql)
| __Input__ |  [imma-artists.xml](imma-artists.xml), `?_artistUrl`
| __Output__ | [artists/](artists/)*.jsonld |
| __Type__ | CONSTRUCT |
| __Options__ |  |
| __Formats__ | HTML |
| __Level__ | Novice |

Run the example as follows:

```
fx -q queries/imma-artist.sparql -i imma-artists.xml -p "artists/?artistNickname.jsonld" -f json
```

### Step 3: Generate the list of artworks 

Next, we extract the list of artworks' Web pages from the JSON-LD files of the artists. This is easy as we can simply query the JSON-LD files, loading them in an in-memory dataset via the command-line option `-l`.

| Title | Step 3: Generate the list of artworks |
|:----------|:-------------|
| __Query__ | [queries/imma-artworks.sparql](queries/imma-artworks.sparql)
| __Input__ |  [artists/](artists/)
| __Output__ | [imma-artworks.xml](imma-artworks.xml) |
| __Type__ | SELECT |
| __Options__ | `-l` |
| __Formats__ | |
| __Level__ | Novice

Run the example as follows:

```
fx -q queries/imma-artworks.sparql -l artists/ -o imma-artworks.xml -f xml
```

### Step 4: Generate the list of artworks 

Next, we extract data from the artworks' Web pages and build one JSON-LD file each (create folder 'artworks' first).

| Title | Step 4: Generate the list of artworks  |
|:----------|:-------------|
| __Query__ | [queries/imma-artwork.sparql](queries/imma-artwork.sparql)
| __Input__ |   [imma-artworks.xml](imma-artworks.xml), `?_artworkUrl`
| __Output__ | [artworks/](artworks/)*.jsonld |
| __Type__ | CONSTRUCT |
| __Options__ | |
| __Formats__ | |
| __Level__ | Novice

```
fx -q queries/imma-artwork.sparql -i imma-artworks.xml -p "artworks/?artworkNickname.jsonld" -f json
```

Finally, we can load the files into our favourite triple store.

## Extract single artists / artworks

These queries can be used to execute only one specific artists/artwork. In addition, they showcase the CLI option `-v`, used to pass parameter values.

Extract data from a specific artist Web page:
```
fx -q imma-artist.sparql -v artistNickname=lambert-gene -v artistUrl=https://imma.ie/artists/gene-lambert/ -p "artists/?artistNickname.jsonld" -f json
```

Extract data from a specific artwork Web page:
```
fx -q imma-artwork.sparql  -v artworkNickname=naturaleza-desde-la-ventana -v artworkUrl=https://imma.ie/collection/naturaleza-desde-la-ventana/ -p "artworks/?artworkNickname.jsonld" -f json
```
