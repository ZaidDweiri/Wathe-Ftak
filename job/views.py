from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from .models import job
# Create your views here.
def jobList (request):
    # Now You gonna get all the jobs in DataBase
    jobList = job.objects.all()
    # The Context the first one is what you want to display in Front End and the second one is the real one in DataBase
    context = {'Jobs ': jobList,}
    # Every View should return three things ( 1.Request , 2. The Redirect Page , 3. The Context
    return render(request, 'jobList.html', context)

def jobDetail(request , id):
    # If you want to search for multiable jobs you going to use 'Filter' but if you want to search for a spaicfic job ypu need to use 'Get'!
    jobDetail = job.objects.get(id = id)
    return render(request , 'jobDetail.html' , {'Job' : jobDetail})