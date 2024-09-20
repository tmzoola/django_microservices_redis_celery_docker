from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProductListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        products = [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}]
        return Response(products)
