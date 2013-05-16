from rest_framework import generics, mixins
from complaint.models import Category, Complaint

from complaint.serializers import CategoryListSerializer
from complaint.serializers import ComplaintListSerializer
from complaint.serializers import ComplaintDetailSerializer

# Create your views here.

# Categories are read-only so only get method implemented
class CategoryListView(mixins.ListModelMixin,
                      generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ComplaintListView(generics.ListCreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintListSerializer

class ComplaintDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintDetailSerializer
