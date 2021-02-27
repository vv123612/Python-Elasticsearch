from elasticsearch import Elasticsearch
from pprint import pprint
import json

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connected')
    else:
        print('Awww it could not connect!')
    return _es


def store_record(elastic_object, index_name, record, id):
    is_stored = True
    try:
        # outcome = elastic_object.index(index=index_name, doc_type='salads', body=record)
        outcome = elastic_object.index(index=index_name, body=record, id=id)
        print(outcome)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))
        is_stored = False
    finally:
        return is_stored


def load_personal():
    store_record(es, 'personal', {'name':'Petr Petrov','salary':10000}, 1)
    store_record(es, 'personal', {'name':'Petr Ivanov','salary':12000}, 2)
    store_record(es, 'personal', {'name':'Ivan Ivanov','salary':15000}, 3)
    store_record(es, 'personal', {'name':'Ivan Ivanov Senior','salary':16000}, 4)
    store_record(es, 'personal', {'name':'Ivan Ivanov Junior','salary':17000}, 5)


def search(es_object, index_name, search):
    res = es_object.search(index=index_name, body=search)
    pprint(res)



es = connect_elasticsearch()
# load_personal()

# search_object = {'_source': ['title'], 'query': {'range': {'calories': {'gte': 20}}}}
search_object = {"query": {"match": {"name": "Petr Petrov"}}}
search(es, 'personal', json.dumps(search_object))


