from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Vehicle, Review
from .forms import ReviewForm

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
        reviews = vehicle.reviews.filter(approved=True)

        return render(
            request, 
            'vehicle_details.html', 
            {
                'vehicle' : vehicle,
                'commented' : False,
                'reviews' : reviews,
                'review_form' : ReviewForm()
            },
        )

    def post(self, request, id, *args, **keyargs):
        queryset = Vehicle.objects.filter(status=1)
        vehicle = get_object_or_404(queryset, id=id)

        review = ReviewForm(request.POST)

        if(review.is_valid()):
            review.instance.vcl = vehicle
            review.instance.user = request.user
            review.save()
        else:
            review = ReviewForm()

        return render(
            request, 
            'vehicle_details.html',
            {
                'vehicle' : vehicle,
                'commented' : True,
                'review_form' : ReviewForm()
            },
        )