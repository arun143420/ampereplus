from django.shortcuts import render
from django.shortcuts import get_object_or_404
from services.models import Service


def service_detail_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    context = {
        'service':service
    }
    return render(request, 'services/service_detail.html', context)

