# core/views.py
from django.db.models import query
from rest_framework import viewsets


from .models import Branch, Product, Department
from .serializers import BranchSerializer, ProductSerializer, DepartmentSerializer
from .permissions import IsCreatorOrReadOnly



class BranchViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` for branch model.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsCreatorOrReadOnly,]


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


    
class DepartmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` for department model.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsCreatorOrReadOnly,]

    def perform_create(self, serializer):
	    serializer.save(created_by=self.request.user)


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` for product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsCreatorOrReadOnly,]
    

    def perform_create(self, serializer):
	    serializer.save(created_by=self.request.user)