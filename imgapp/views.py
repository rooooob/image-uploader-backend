from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import ImageSerializer
from .models import Image


@api_view(['GET'])
def image_list(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def image_detail(request, pk):
    image = Image.objects.get(id=pk)
    serializer = ImageSerializer(image, many=False)

    return Response(serializer.data)

 
@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def image_create(request):
    serializer = ImageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    print(f'ASD : {serializer.data}')
    return Response(serializer.data)


@api_view(['DELETE'])
def image_delete(request, pk):
    image = Image.objects.get(id=pk)
    image.delete()

    serializer = ImageSerializer(Image.objects.all(), many=True)

    return Response(serializer.data)