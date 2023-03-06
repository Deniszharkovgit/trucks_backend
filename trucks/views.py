from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from trucks.models import Truck, TruckModel


@csrf_exempt
def trucks_page(request):
    context = {
        'models': TruckModel.objects.all(),
        'trucks': Truck.objects.all()
    }
    if request.GET.get('featured') and request.GET.get('featured') != 'all':
        trucks = Truck.objects.filter(truck_model=request.GET.get('featured'))
        context['trucks'] = trucks
    else:
        context['trucks'] = Truck.objects.all()
    return render(request, "../templates/trucks/truck_list.html", context)
