from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.response import Response

from complaint.models import Category, Complaint, Image

from complaint.serializers import CategoryListSerializer
from complaint.serializers import ComplaintSerializer
from complaint.serializers import ImageSerializer

# Create your views here.

# Categories are read-only so only get method implemented
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ComplaintListView(mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def get(self, request, sorting=None, format=None):
        if 'cat' in request.GET:
            cat = request.GET["cat"].lower().capitalize()
        else:
            cat = None

        if sorting:
            if sorting == 'hot':
                if cat:
                    qs = Complaint.objects.filter(category__name=cat).order_by('-upvote')
                else:
                    qs = Complaint.objects.order_by('-upvote')
            if sorting == 'new':
                if cat:
                    qs = Complaint.objects.filter(category__name=cat).order_by('-id')
                else:
                    qs = Complaint.objects.order_by('-id')
        else:
            qs = Complaint.objects.all()

        serializer = ComplaintSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ComplaintDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

# GET, POST ve DELETE methodlari ayni id'yi aliyor gibi
# gozukse de calisirken farkli amaclar icin kullaniyor
class ImageView(generics.GenericAPIView):
    serializer_class = ImageSerializer

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            images = Image.objects.filter(complaint__id=pk)
        except Image.DoesNotExist:
            raise Http404

        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        try:
            complaint = Complaint.objects.get(pk=pk)
        except:
            raise Http404

        serializer = ImageSerializer(data=request.DATA)
        if serializer.is_valid(): # TODO complaint eklenecek
            serializer.save()
            return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def pre_save(self, obj):
        obj.uploader = self.request.user
