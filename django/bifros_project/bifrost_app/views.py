from django.shortcuts import render
from bifrost_app.models import Volume
# Create your views here.
def index(request):
    """
    Main page
    """
    volumes_list = Volume.objects.order_by('number')
    volumes_dict = {"volumes":volumes_list}
    for key in volumes_dict.keys():
        print(volumes_dict[key][1].number)
    numbers=range(97,1,-1)
    return render(request,'bifrost_app/index.html',volumes_dict)
