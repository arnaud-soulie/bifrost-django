import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','bifrost_project.settings')

import django
django.setup()

from django.core.files import File
from bifrost_app.models import Volume


def populate(N=5,path="D:\covers"):
    print("Path: "+path)
    print("N:"+N)

    for num in range(1,int(N)+1):
        print("Opening "+os.path.join(path,str(num)+".txt"))
        with open(os.path.join(path,str(num)+".txt"),'r',encoding='utf8') as fsum:
            sum=fsum.read()
            print("Summary: "+sum)
        #Creates the new volume entry
        vol = Volume.objects.get_or_create(summary=sum,number=num,)[0]
        #vol.cover = File(open(os.path.join(path,str(num)+".jpg")), 'rb')
        #vol.save()

        print("Cover: ")
        print(vol.cover)

if __name__ == '__main__':
    print('Populating script!')
    populate(N=sys.argv[1],path=sys.argv[2])
    print('populating complete!')
