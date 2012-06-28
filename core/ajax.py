from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.template import Context, RequestContext, loader
from dajax.core import Dajax
from core.forms import *
from events.models import Event
from django.contrib.auth.models import User
from users.models import UserProfile

@dajaxice_register
def updateSummary(request):
    dajax = Dajax()
    dajax.assign("#summary",'innerHTML',"<table border='1'><thead><tr><th>S.No</th><th>Event Name</th><th>Coords</th></tr></thead><tbody id='event'>")
    event=Event.objects.order_by('id').all()
    for e in event:
        dajax.append("#event",'innerHTML',"<tr><td>"+str(e.id)+"</td><td onclick=\'displayevent("+str(e.id)+");\' class='grps' id="+e.title+"><a href=#>"+e.title+"</a></td><td id="+str(e.id)+"></td></tr>")
        coords=UserProfile.objects.filter(is_coord_of__title=e.title)
        for c in coords:
            dajax.append("#"+str(e.id),'innerHTML',"<li onclick=\'displayCoord("+str(c.user.id)+");\' class='coords' id="+str(c.user.username)+"><a href=#>"+str(c.user)+"</a>")
    return dajax.json()

@dajaxice_register
def add_edit_event(request,form="",id=0):
    dajax = Dajax()
    if form == "" :
        if id:
            template = loader.get_template('ajax/core/editevent.html')
            event_form = AddEventForm(instance=Event.objects.get(id=id))
            html=template.render(RequestContext(request,locals()))
        else:
            template = loader.get_template('ajax/core/addevent.html')
            event_form = AddEventForm()
            html=template.render(RequestContext(request,locals()))
        dajax.assign('#space', 'innerHTML', html)
        return dajax.json()
    if id:
        event_form = AddEventForm(form, instance=Event.objects.get(id=id))
    else:
        event_form = AddEventForm(form)
    if event_form.is_valid():
        event_form.save()
    dajax.assign("#space",'innerHTML',"")
    dajax.script("updateSummary();")
    return dajax.json()

@dajaxice_register
def del_event(request,id):
    dajax = Dajax()
    event=Event.objects.get(id=id)
    event.delete()
    dajax.assign('#space', 'innerHTML', "")
    dajax.script("updateSummary();")
    return dajax.json()

@dajaxice_register
def add_edit_coord(request,form="",id=0):
    dajax = Dajax()
    if form == "" :
        if id:
            template = loader.get_template('ajax/core/editcoord.html')
            coord=User.objects.get(id=id)
            coord_form = AddCoordForm(instance=coord,initial={'event':coord.get_profile().is_coord_of_id,})
            html=template.render(RequestContext(request,locals()))
        else:
            template = loader.get_template('ajax/core/addcoord.html')
            coord_form = AddCoordForm()
            html=template.render(RequestContext(request,locals()))
        dajax.assign('#space', 'innerHTML', html)
        return dajax.json()
    if id:
        coord_form = AddCoordForm(form, instance=User.objects.get(id=id))
        if coord_form.is_valid():
            coord=coord_form.save()
            coord_profile=coord.get_profile()
            coord_profile.is_coord_of_id=form['event']
            coord_profile.save()
            dajax.assign("#space",'innerHTML',"")
        else:
            template = loader.get_template('ajax/core/editcoord.html')
            html=template.render(RequestContext(request,locals()))
            dajax.assign("#space",'innerHTML',html)
    else:
        coord_form = AddCoordForm(form)
        if coord_form.is_valid():
            coord=coord_form.save()
            coord.set_password("default")
            coord.groups.add(request.user.groups.get_query_set()[1])
            coord.save()
            coord_profile = UserProfile(user=coord, is_coord_of_id=form['event'])
            coord_profile.save()
            dajax.assign("#space",'innerHTML',"")
        else:
            template = loader.get_template('ajax/core/addcoord.html')
            html=template.render(RequestContext(request,locals()))
            dajax.assign("#space",'innerHTML',html)
    dajax.script("updateSummary();")
    return dajax.json()

@dajaxice_register
def del_coord(request,id):
    dajax = Dajax()
    coord=User.objects.get(id=id)
    coord.delete()
    dajax.assign('#space', 'innerHTML', "")
    dajax.script("updateSummary();")
    return dajax.json()

