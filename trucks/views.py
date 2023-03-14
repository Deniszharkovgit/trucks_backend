from django.shortcuts import render, get_object_or_404
from django.views import View
from trucks.models import Truck, TruckModel


class MainView(View):
    template_name = "../templates/trucks/truck_list.html"

    def get(self, request):
        featured = request.GET.get('featured')
        trucks = Truck.objects.all()
        models = TruckModel.objects.all()
        prev_value = featured or 'all'

        if featured and featured != 'all':
            truck_model = get_object_or_404(TruckModel, name=featured)
            trucks = Truck.objects.filter(truck_model=truck_model)

        context = {
            'models': models,
            'prev_value': prev_value,
            'trucks': trucks,
        }

        return render(request, self.template_name, context)