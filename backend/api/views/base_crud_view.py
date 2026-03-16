from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseCRUDView(APIView):

    service = None
    serializer_class = None

    def get(self, request, pk=None):

        if pk:
            obj = self.service.get_by_id(pk)
            serializer = self.serializer_class(obj)
            return Response(serializer.data)

        objs = self.service.get_all()
        serializer = self.serializer_class(objs, many=True)

        return Response(serializer.data)

    def post(self, request, pk=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            obj = self.service.create(serializer.validated_data)
            return Response(
                self.serializer_class(obj).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            obj = self.service.update(pk, serializer.validated_data)
            return Response(self.serializer_class(obj).data)

        return Response(serializer.errors)

    def patch(self, request, pk):

        serializer = self.serializer_class(data=request.data, partial=True)

        if serializer.is_valid():
            obj = self.service.partial_update(pk, serializer.validated_data)
            return Response(self.serializer_class(obj).data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        self.service.delete(pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
