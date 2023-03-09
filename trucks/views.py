from django.shortcuts import render
from django.views import View
from trucks.models import Truck, TruckModel


class MainView(View):
    def get(self, request):
        context = {
            'models': TruckModel.objects.all(),
            'prev_value': request.GET.get('featured'),
        }
        if request.GET.get('featured') and request.GET.get('featured') != 'all':
            context['trucks'] = Truck.objects.filter(truck_model=request.GET.get('featured'))
        else:
            context['trucks'] = Truck.objects.all()
        return render(request, "../templates/trucks/truck_list.html", context)