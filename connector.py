import requests
import elasticsearch as es
from elasticsearch.helpers import bulk


class connector:
    def __init__(self, hostname, index_name=None):
        self.hostname = hostname
        self.index_name = index_name
        self.es = es.Elasticsearch(hosts=['http://localhost:9200'], timeout=5000)

    def set_index(self, index_name):
        self.index_name = index_name

    def search(self, querystring, num_articles=30):
        if self.index_name is None:
            print('No index name set')
            return
        payload = {'q':querystring}
        r = requests.get(self.hostname+'/'+self.index_name+'/_search',params=payload).json()
        return r['hits']['hits'][:num_articles]

    def get_article(self, article_id):
        return self.search('_id:'+article_id)


if __name__ == '__main__':
    hostname = 'http://localhost:9200'
    index = 'simple'
    c = connector(hostname, index_name=index)
    s = c.get_article('nu0_AmMBBvgUg82cJ2E0')
    print(s[0])
