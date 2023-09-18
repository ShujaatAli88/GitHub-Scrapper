from elasticsearch import Elasticsearch


def my_Connection():
    conn = Elasticsearch([{'host':'localhost','port':9200}])
    return conn

if(__name__=='__main__'):
    my_Connection()