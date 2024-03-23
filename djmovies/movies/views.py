from django.core.paginator import Paginator
from django.views.generic import ListView
from rest_framework import viewsets

from . import models
from .models import MovieData
from .serialziers import MovieSerializer


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(movie_type='action')
    serializer_class = MovieSerializer


class MovieListView(ListView):
    model = models.MovieData
    template_name = 'list.html'
    context_object_name = 'item_list'
    paginate_by = 2  # Number of items per page

    def get_queryset(self):
        # Fetch the queryset
        queryset = super().get_queryset()

        # Create a Paginator object
        paginator = Paginator(queryset, self.paginate_by)

        # Get the current page number from the request
        page_number = self.request.GET.get('page')

        # Return the paginated queryset for the current page
        return paginator.get_page(page_number)
