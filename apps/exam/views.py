# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from django.contrib import messages
from ..login_and_registration.models import User

# Create your views here.
def index(request):
    if not 'username' in request.session:#this is the authorization
        messages.error(request, 'PLEASE LOG IN FIRST TO ACCESS ITEMS')
        return redirect('/')
    item = Wish.objects.all()
    current_user = User.objects.get(id=request.session['user_id'])
    others_items = Wish.objects.all().exclude(creator=current_user).exclude(wishers=current_user)
    print item
    items_wished = Wish.objects.filter(creator=current_user, wishers=current_user),
    my_items = Wish.objects.all().filter(creator=current_user)
    context = {
        "items": item,
        "current_user": current_user,
        "items_wished": items_wished,
        "my_items": my_items,
        "others_items": others_items
    }

    return render(request, 'exam/index.html', context)

def new(request):
    return render(request, 'exam/new.html')

def create(request):
    errors = Wish.objects.wish_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        print errors
        return redirect('/exam/new')
    else:
        name = request.POST['name']        
        current_user = User.objects.get(id=request.session['user_id'])
        new_item = Wish.objects.create(name=name, creator=current_user)
        print new_item  
        return redirect('/exam/')

def show(request, id):
    wishers = Wish.objects.get(id=int(id)).wishers.all()
    item = Wish.objects.get(id=int(id))
    context = {
        "item": item,
        "wishers": wishers
    }
    return render(request, "exam/show.html", context)

def joined(request, id):
        current_user = User.objects.get(id=request.session['user_id'])
        item_wished = Wish.objects.get(id=id)
        item_wished.wishers.add(current_user)
        # item_wished.save()
        return redirect('/exam/')

def dropped(request, id):
        current_user = User.objects.get(id=request.session['user_id'])
        item_wished = Wish.objects.get(id=id)
        item_wished.wishers.remove(current_user)
        # trip_joined.save() #not really neccessary
        return redirect('/exam/')

def edit(request, id):
    item = Wish.objects.get(id=int(id))
    context = {
		"item": item
        }
    print item.creator.id
    print request.session['user_id']
    if  item.creator.id == request.session['user_id']:
        return render(request, "exam/edit.html", context)    
    else:
        messages.error(request, 'SORRY, ONLY THE CREATOR CAN REMOVE AN ITEM.')
        return redirect('/exam/')

def delete(request,id):
    # trip = Trip.objects.get(id=int(id))
    Wish.objects.get(id=int(id)).delete()
    # if  trip.creator.id == request.session['user_id']:
    #     messages.error(request, 'TRIP SUCCESSFULLY REMOVED.')
    #     return redirect('/belt/')    
    # else:
    #     messages.error(request, 'SORRY, ONLY THE CREATOR CAN REMOVE A TRIP.')
    return redirect('/exam/')
       

