from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from collections import OrderedDict
from .models import obj, sens, values_sens
from .forms import LogForm, Form
from .fusioncharts import FusionCharts
from .fusioncharts import FusionTable
from .fusioncharts import TimeSeries
import datetime, qsstats, requests

# Create your views here.
def index(request):
    form = LogForm
    context =  {'form' : form}
    return render(request, 'grr/index.html', context)

def lk(request):
    obj_list = obj.objects.all()
    sens_list = sens.objects.all()
    form = Form()
    context =  {'obj_list' : obj_list, 'sens_list' : sens_list, 'form' : form}
    return render(request, 'grr/lk.html', context)

@require_POST

def logg (request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    return redirect('lk')

def loggout (request):
    return redirect('index')

def grath(request, sensid):
    #time = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
    qwe = values_sens.objects.all()
    qwe = qwe.filter(sensfk = sensid)
    values_x = []
    values_y = []
    for qwe.test in qwe:
        #if qwe.test.dat.date() == time:
        #strftime('%Y-%m-%d %H:%M:%S')
        #values_x = {'year': qwe.test.dat.year()}
        #val = Vall()
        #ewq = qwe.test.dat.strftime('%Y-%m-%d %H:%M:%S')
        #qwe.test.dat.strptime(ewq, '%Y-%m-%d %H:%M:%S')
        #val = Vall()
        #val.vv = qwe.test.dat.strftime('%Y-%m-%d %H:%M:%S')
        #values_x.append(val.vv)
        #[{% for val in values_x %}'{{val}}',{% endfor %}]
        values_x.append(qwe.test.dat.strftime('%Y-%m-%d %H:%M:%S'))
        values_y.append(int(qwe.test.tem))
    #qwe = qwe.filter(dat = time)
    #qss = qsstats.QuerySetStats(qs, 'dat', aggregate=None)
    #print (datetime.date.today())
    #today = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d')
    #seven_days_ago = today - datetime.timedelta(days=1)
    #today = today + datetime.timedelta(days=1)
    #values = qss.time_series(seven_days_ago, today, interval = 'days')
    #values = [(test.dat, int(test.tem)) for test in qwe]
    context =  {'values_x' : values_x, 'values_y' : values_y}
    for val in values_x:
        print(val)
    return render(request, 'grr/googletemp.html', context)

def timech(request, sensid):
    form = Form()
    context =  {'form' : form, 'sensid' : sensid}
    return render(request, 'grr/timech.html', context)

def grathtime(request, sensid):
    time = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
    qwe = values_sens.objects.all()
    qwe = qwe.filter(sensfk = sensid)
    values = []
    for qwe.test in qwe:
        if qwe.test.dat.date() == time:
            values = values + [(qwe.test.dat, int(qwe.test.tem))]
    context =  {'values' : values}
    return render(request, 'grr/googletemp.html', context)

class Vall:
    vv = ''