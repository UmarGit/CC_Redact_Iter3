from django.shortcuts import redirect, render, get_object_or_404
from mortems.models import Mortem

def mortems(request):
    mortems = Mortem.objects.order_by('-pub_date')
    context = {'mortem':mortem}
    return render(request, 'alls/landings.html', context)

