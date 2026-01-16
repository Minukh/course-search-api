import  spacy
from django.db.models import Q
from .models import Course, CachedQuery


class CourseSearchHelper:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def preprocess_query(self, text):
        doc = self.nlp(text)
        tokens= [
            token.lemma_.lower()
            for token in doc
            if not token.is_stop and not token.is_punct and  token.is_alpha
        ]
        return tokens
    def search_courses(self, query):
        tokens = self.preprocess_query(query)

        token_filter = Q()
        for token in tokens:
            token_filter |= Q(tags__name__icontains=token)
            token_filter |= Q(cached_tokens__token__icontains=token)
        return Course.objects.filter(token_filter).distinct()

    def update_cached_tokens(self,course):
        course.cached_tokens.all().delete()
        tokens = self.preprocess_query(course.name)

        for token in tokens:
            CachedQuery.objects.create(course=course, token=token)

