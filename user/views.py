from rest_auth.views import LoginView, LogoutView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import AdvancedUser
from .serializers import UserRegistrationSerializer


class UserRegistration(APIView):

    def get(self, request,  *args):
        serializer = UserRegistrationSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        phone       = request.data.get('phone', False)
        password    = request.data.get('password', False)
        first_name  = request.data.get('first_name', False)
        surname     = request.data.get('surname', False)

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



        else:
            return Response({
                'status': False,
                'display': 'Phone or password miss'
                })



class UserTokenView(APIView):
    pass


class UserLoginView(LoginView):
    pass


class UserLogoutView(LogoutView):
    pass


class UserResetPasword(APIView):
    pass


class UserVerifyTPO(APIView):
    pass
