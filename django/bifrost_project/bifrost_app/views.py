from django.shortcuts import render
from bifrost_app.models import Volume
from django.db.models import Q
from bifrost_app.forms import NewVolumeForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    """
    Main page
    """
    searching=""

    volumes_list = Volume.objects.order_by('-number')
    print(volumes_list)


    if (request.method == 'POST'):
        #Filter
        searching=(request.POST.get('search') or "")
        print("Valeur cherchée : "+searching)
        volumes_list=Volume.objects.filter(Q(summary__icontains=searching)).order_by('-number')
        #volumes_list=volumes_list.filter(guest__icontains=request.POST.get('search'))
        print(volumes_list)

    context = {"volumes":volumes_list,"searching":searching}
    print("passe dans index")
    return render(request,'bifrost_app/index.html',context)

def add_volume(request):
    """
    Form pour ajouter un nouveau volume en DB
    """
    form=NewVolumeForm()

    if request.method == "POST":
        form=NewVolumeForm(request.POST)
        print("Form valid..")
        print(request.FILES)
        if form.is_valid():

            # Check if they provided a profile picture
            if 'cover_pics' in request.FILES:

                print('found cover')
                # If yes, then grab it from the POST form reply
                form.cover_pics = request.FILES['cover_pics']

            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print("ERROR: Invalid form")
    print("passe dans add_volume")
    return render(request,'bifrost_app/add_volume.html',{'form':form})
