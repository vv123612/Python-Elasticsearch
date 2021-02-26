
// GET search?q=name:salads/_doc/

POST recipes/_search
{
   "query": {
      "match_all": {}
   }
}

// все рецепты
GET recipes/_search

// все индексы
GET /_cat/indices


// все индексы
GET _aliases?pretty=true

// все индексы
GET _cat/indices?v