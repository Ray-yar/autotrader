from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Vehicle

# Create your views here.
class VehicleView(generic.ListView):
    model = Vehicle
    object = Vehicle.objects.filter(status=1).order_by('created_at')
    template_name = "index.html"
    paginate_by = 8


class VehicleDetail(View):

    def get(self, request, id, *args, **keyargs):
        queryset = Vehicle.objects.filter(status=1)
        vehicle = get_object_or_404(queryset, id=id)

        return render(
            request, 
            'vehicle_details.html', 
            {
                'vehicle' : vehicle,
            },
        )