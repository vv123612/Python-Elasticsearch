
// все рецепты
GET personal/_search


// DELETE personal

// http://localhost:9200/personal


GET /_search
{
  "query": {
    "match": {
      "name": {
        "query": "Petr Petrov",
        "operator": "and"
      }
    }
  }
}