from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(serializer)
        print(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({ 
            'token': token.key, 
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })