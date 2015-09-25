from haystack import indexes
from models import SampleModel
class SampleModelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    search_name = indexes.EdgeNgramField(model_attr = 'name')

    def get_model(self):
        return SampleModel