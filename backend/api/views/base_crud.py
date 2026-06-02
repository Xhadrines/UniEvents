from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseCRUDView(APIView):
    """
    View generic pentru operațiile CRUD simple.

    CRUD înseamnă:
    - Create  -> creare
    - Read    -> citire
    - Update  -> actualizare
    - Delete  -> ștergere

    Această clasă este reutilizată de toate view-urile
    care au nevoie de funcționalități CRUD standard.
    """

    # Service-ul care gestionează logica aplicației.
    #
    # Va fi suprascris în clasele copil.
    service = None

    # Serializer-ul folosit pentru validare și răspuns.
    #
    # Va fi suprascris în clasele copil.
    serializer_class = None

    def get_serializer_context(self, request):
        """
        Returnează contextul trimis către serializer.

        De obicei includem request-ul pentru:
        - URL-uri absolute,
        - informații despre utilizator,
        - acces la request în serializer.
        """

        return {"request": request}

    def get(self, request, pk=None):
        """
        GET:
        - fără pk -> returnează toate obiectele
        - cu pk   -> returnează un singur obiect
        """

        # Dacă există pk,
        # vrem un singur obiect.
        if pk:

            # Căutăm obiectul după ID.
            obj = self.service.get_by_id(pk)

            # Dacă obiectul nu există,
            # returnăm 404.
            if not obj:
                return Response(
                    {"error": "Object not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            # Serializăm obiectul.
            serializer = self.serializer_class(
                obj,
                context=self.get_serializer_context(request),
            )

            return Response(serializer.data)

        # Dacă nu există pk,
        # returnăm toate obiectele.
        objs = self.service.get_all()

        # many=True:
        # serializer-ul primește o listă de obiecte.
        serializer = self.serializer_class(
            objs,
            many=True,
            context=self.get_serializer_context(request),
        )

        return Response(serializer.data)

    def post(self, request, pk=None):
        """
        POST:
        Creează un obiect nou.
        """

        # Construim serializer-ul cu datele primite.
        serializer = self.serializer_class(
            data=request.data,
            context=self.get_serializer_context(request),
        )

        # Validăm datele.
        if serializer.is_valid():

            # Salvăm obiectul în baza de date.
            obj = serializer.save()

            # Returnăm obiectul creat.
            return Response(
                self.serializer_class(
                    obj,
                    context=self.get_serializer_context(request),
                ).data,
                status=status.HTTP_201_CREATED,
            )

        # Dacă datele sunt invalide,
        # returnăm erorile.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        PUT:
        Actualizare completă a unui obiect.

        Practic:
        toate câmpurile importante
        trebuie retrimise.
        """

        # Pentru update avem nevoie de ID.
        if pk is None:
            return Response(
                {"error": "ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Căutăm obiectul.
        obj = self.service.get_by_id(pk)

        # Dacă nu există -> 404.
        if not obj:
            return Response(
                {"error": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Construim serializer-ul pentru update.
        serializer = self.serializer_class(
            obj,
            data=request.data,
            context=self.get_serializer_context(request),
        )

        # Validăm datele.
        if serializer.is_valid():

            # Salvăm modificările.
            obj = serializer.save()

            # Returnăm obiectul actualizat.
            return Response(
                self.serializer_class(
                    obj,
                    context=self.get_serializer_context(request),
                ).data
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        PATCH:
        Actualizare parțială.

        Spre deosebire de PUT,
        trimitem doar câmpurile care trebuie modificate.
        """

        # Verificăm dacă avem ID.
        if pk is None:
            return Response(
                {"error": "ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Căutăm obiectul.
        obj = self.service.get_by_id(pk)

        # Dacă obiectul nu există.
        if not obj:
            return Response(
                {"error": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # partial=True:
        # permite actualizarea doar a câmpurilor trimise.
        serializer = self.serializer_class(
            obj,
            data=request.data,
            partial=True,
            context=self.get_serializer_context(request),
        )

        # Validăm datele.
        if serializer.is_valid():

            # Salvăm modificările.
            obj = serializer.save()

            # Returnăm obiectul actualizat.
            return Response(
                self.serializer_class(
                    obj,
                    context=self.get_serializer_context(request),
                ).data
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        DELETE:
        Șterge un obiect după ID.
        """

        # Pentru ștergere avem nevoie de ID.
        if pk is None:
            return Response(
                {"error": "ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Încercăm să ștergem obiectul.
        deleted = self.service.delete(pk)

        # Dacă obiectul nu există.
        if not deleted:
            return Response(
                {"error": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # 204 = ștergere reușită fără conținut returnat.
        return Response(status=status.HTTP_204_NO_CONTENT)
