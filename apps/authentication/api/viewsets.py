from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.api.serializers import RegisterRequestSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)
