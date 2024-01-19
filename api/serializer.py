from rest_framework import serializers
from .models import Programmer
from .models import Subjet


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'

class CodeSerlizer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)

    def validate(self, code):
        if len(code) < 3:
            raise serializers.ValidationError('El codigo es demaciado pequeño')
        return code
        