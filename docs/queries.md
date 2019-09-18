### SPARQL Queries

#### Check number of tuples

```
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
PREFIX datacite:<http://purl.org/spar/datacite/>
PREFIX d1node:<https://cn.dataone.org/cn/v1/node/>
PREFIX d1dataset:<http://dataone.org/dataset/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX prov:<http://www.w3.org/ns/prov#>
PREFIX geolink:<http://schema.geolink.org/1.0/base/main#>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX d1person:<http://dataone.org/person/>
PREFIX d1org:<http://dataone.org/organization/>
PREFIX dcterms:<http://purl.org/dc/terms/>
SELECT count(DISTINCT ?s)  as ?count
FROM <geolink>
WHERE 
{ 
    ?s ?p ?o
}
```

#### Check number of DataONE Datasets

```
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
PREFIX datacite:<http://purl.org/spar/datacite/>
PREFIX d1node:<https://cn.dataone.org/cn/v1/node/>
PREFIX d1dataset:<http://dataone.org/dataset/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX prov:<http://www.w3.org/ns/prov#>
PREFIX geolink:<http://schema.geolink.org/1.0/base/main#>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX d1person:<http://dataone.org/person/>
PREFIX d1org:<http://dataone.org/organization/>
PREFIX dcterms:<http://purl.org/dc/terms/>
SELECT count(DISTINCT ?s)  as ?count
FROM <geolink>
WHERE 
{ 
    ?s rdf:type geolink:Dataset
}
```

#### Getting tuples for a given dataset

```
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
PREFIX datacite:<http://purl.org/spar/datacite/>
PREFIX d1node:<https://cn.dataone.org/cn/v1/node/>
PREFIX d1dataset:<http://dataone.org/dataset/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX prov:<http://www.w3.org/ns/prov#>
PREFIX geolink:<http://schema.geolink.org/1.0/base/main#>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX d1person:<http://dataone.org/person/>
PREFIX d1org:<http://dataone.org/organization/>
PREFIX dcterms:<http://purl.org/dc/terms/>
SELECT *
WHERE {
  <http://dataone.org/dataset/doi:10.6067:XCV8MP519B_meta$v=1242317684150> ?p ?o .
}
LIMIT 10
```

#### Performing keyword/s search in Virtuoso

```
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
PREFIX datacite:<http://purl.org/spar/datacite/>
PREFIX d1node:<https://cn.dataone.org/cn/v1/node/>
PREFIX d1dataset:<http://dataone.org/dataset/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX prov:<http://www.w3.org/ns/prov#>
PREFIX geolink:<http://schema.geolink.org/1.0/base/main#>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX d1person:<http://dataone.org/person/>
PREFIX d1org:<http://dataone.org/organization/>
PREFIX dcterms:<http://purl.org/dc/terms/>
SELECT *
where 
{  
?s a  <http://schema.geolink.org/1.0/base/main#Dataset> . 
?s rdfs:label ?label .  FILTER (REGEX(?label,"Macrofossil Characteristics of Soil from Shark River Slough","i"))   
}  limit 1000
```
