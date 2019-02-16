from rest_framework import generics
from rest_framework import authentication, permissions, status
from ..serializers import UserSerializer, AuthorProfileSerializer
from rest_framework.response import Response


class AuthorProfileView(generics.GenericAPIView):
    serializer_class = AuthorProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = AuthorProfileSerializer(data=request.data, context={"request": self.request})

        if (serializer.is_valid(raise_exception=True)):
            httpStatus = status.HTTP_200_OK
            return Response(serializer.data, httpStatus)
        else:
            httpStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors, httpStatus)