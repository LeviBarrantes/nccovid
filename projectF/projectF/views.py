from main.models import *

def save_covid_info(request):


    new_info.save()
    return JsonResponse({"Success": "true"})

def show(request):


    return render(request=request,
                  template_name='main/show.html',
                  context={"all_info": all_info})


def get_stat_from_zip(request):
    zip = request.GET['zip_value']



    return JsonResponse({"Zip": zip,
                         "City": city})

