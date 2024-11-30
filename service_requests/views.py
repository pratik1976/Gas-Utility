from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest, Customer
from .forms import ServiceRequestForm

def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'create_request.html', {'form': form})

def view_requests(request):
    requests = ServiceRequest.objects.filter(customer__email=request.user.email)
    return render(request, 'view_requests.html', {'requests': requests})

def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'track_request.html', {'service_request': service_request})
