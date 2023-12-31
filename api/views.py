from  rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from api.models import UserDTO

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer



@api_view(['GET'])

def lefdepart(request):
    if request.method == 'GET':
        return Response({'msg':'hello world'})
    
@api_view(['POST'])
def CrearUsuario(request):
    if request.method == 'POST':

        serrializer = UserDTO(**request.data)
        Programmer.objects.create(fullname=serrializer.nombre,nickname=serrializer.apellido,age=1 ,is_active=True)
        return Response({'msg':'Usuario Creado'})
    
