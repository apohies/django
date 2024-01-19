from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from api.conection.pymongo import get_database
from api.models import User



class CodeSerlizer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)

    def validate(self, value):

        tamano = len(value['code'])
        if len(value['code']) > 3:
            raise serializers.ValidationError('El codigo es demaciado pequeño')
        return value 
        

@api_view(['GET'])
def mensaje(request):
    return Response({'msg':'hello pero desde otra vista'})


@api_view(['POST'])
def CrearSubjet(request):
    
    seria = CodeSerlizer(data=request.data)


    if not seria.is_valid():
        mensaje = seria.errors
        return Response({'msg': mensaje}, status=400)

    # Realiza acciones si la validación es exitosa
    return Response({'msg': 'Datos validados correctamente'})

@api_view(['GET'])
def getSubjets(request):
    db = get_database()
    subjets = db['users'].find()
    mensaje =list(subjets)

    usuario = User(**mensaje[0])
    return Response({'msg': usuario.username})