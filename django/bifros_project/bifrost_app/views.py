from django.shortcuts import render
from bifrost_app.models import Volume
from django.db.models import Q

# Create your views here.
def index(request):
    """
    Main page
    """
    searching=""
    volumes_list = Volume.objects.order_by('-number')
    print(volumes_list)


    if request.method == 'POST':
        #Filter
        searching=request.POST.get('search')
        print("Valeur cherchée : "+searching)
        volumes_list=Volume.objects.filter(Q(guest__icontains=searching)).order_by('-number')
        #volumes_list=volumes_list.filter(guest__icontains=request.POST.get('search'))
        print(volumes_list)

    context = {"volumes":volumes_list,"searching":searching}

    return render(request,'bifrost_app/index.html',context)
