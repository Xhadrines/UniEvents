from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseCRUDView(APIView):
    # View generic pentru operatii CRUD simple
    service = None
    serializer_class = None

    def get_serializer_context(self, request):
        return {"request": request}

    def get(self, request, pk=None):
        if pk:
            obj = self.service.get_by_id(pk)

            if not obj:
                return Response(
                    {"error": "Object not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = self.serializer_class(
                obj,
                context=self.get_serializer_context(request),
            )
            return Response(serializer.data)

        objs = self.service.get_all()
        serializer = self.serializer_class(
            objs,
            many=True,
            context=self.get_serializer_context(request),
        )
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = self.serializer_class(
            data=request.data,
            context=self.get_serializer_context(request),
        )

        if serializer.is_valid():
            obj = serializer.save()

            return Response(
                self.serializer_class(
                    obj,
                    context=self.get_serializer_context(request),
                ).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response(
                {"error": "ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        obj = self.service.get_by_id(pk)

        if not obj:
            return Response(
                {"error": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(
            obj,
            data=request.data,
            context=self.get_serializer_context(request),
        )

        if serializer.is_valid():
            obj = serializer.save()
            return Response(
                self.serializer_class(
                    obj,
                    context=self.get_serializer_context(request),
                ).data
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if pk is None:
            return Response(
                {"error": "ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        obj = self.service.get_by_id(pk)

        if not obj:
            return Response(
                {"error": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(
            obj,
            data=request.data,
            partial=True,
            context=self.get_serializer_context(request),
        )

        if serializer.is_valid():
            obj = serializer.save()
            return Response(
                self.serializer_class(
                    obj,
                    context=self.get_serializer_context(request),
                ).data
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response(
                {"error": "ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        deleted = self.service.delete(pk)

        if not deleted:
            return Response(
                {"error": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
