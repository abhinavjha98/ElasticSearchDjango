import json
from .models import ElasticDemo, Url

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *
from .document import UrlDocument


class NewsDocumentSerializer(DocumentSerializer):

    class Meta(object):
        """Meta options."""
        model = ElasticDemo
        document = NewsDocument
        fields = (
            'title',
            'content',
        )
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}

class UrlDocumentSerializer(DocumentSerializer):

    class Meta(object):
        """Meta options."""
        model = Url
        document = UrlDocument
        fields = (
            'url',
            'label',
        )
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}