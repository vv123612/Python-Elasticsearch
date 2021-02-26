
// GET search?q=name:salads/_doc/

POST recipes/_search
{
   "query": {
      "match_all": {}
   }
}

GET recipes/_search
