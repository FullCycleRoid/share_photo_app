from django.db.models import Q
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, AuthTokenSerializer, UserSearchSerializer
from main.models import AdvancedUser


class UserRegistration(APIView):

    def get(self, request, *args):
        serializer = UserRegistrationSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        password = request.data.get('password', False)
        first_name = request.data.get('first_name', False)
        surname = request.data.get('surname', False)

        print(str(request.query_params))
        print(phone, password, first_name, surname)

        if phone and password and first_name and surname:

            temp_data = {
                'phone': phone,
                'first_name': first_name,
                'surname': surname,
                'password': password,
            }

            serializer = UserRegistrationSerializer(data=temp_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'display': 'Phone or password miss'
        })


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


@api_view(['GET', ])
def search_user_view(request):
    try:
        params = request.query_params.get('search').split(' ')
        data = {}
        data['users'] = []
        q = Q()
        for item in params:
            q |= (Q(first_name__icontains=item) |
                  Q(surname__icontains=item) |
                  Q(phone__icontains=item))
        qs = AdvancedUser.objects.filter(q)
        serializer = UserSearchSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AttributeError:
        return Response({"ERROR": "No query parameters"},
                        status=status.HTTP_204_NO_CONTENT)


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
