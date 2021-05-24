from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)
from .models import ElasticDemo, Url
PUBLISHER_INDEX = Index('url')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)




@PUBLISHER_INDEX.doc_type
class UrlDocument(Document):
    
    id = fields.IntegerField(attr='id')
    fielddata=True
    url = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    label = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
   

    class Django(object):
        model = Url