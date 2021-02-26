
// GET search?q=name:salads/_doc/

POST recipes/_search
{
  "query": {
    "match": {
      "phrase": {
        "query" : "Salad"
      }
    }
  }
}


POST recipes/_search
