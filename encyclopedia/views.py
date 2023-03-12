from django.shortcuts import render

from . import util

import markdown2
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert(title):
    page = util.get_entry(title)
    markdowner = Markdown()
    if page == None:
        return None
    else:
        return markdowner.convert(page)

def entry(request, title):
        entrypage = convert(title)
        if entrypage == 0:
            return render(request, "encyclopedia/bad.html")
        else:
            return render(request,"encyclopedia/entry.html", {
            "title":title,
            "entrypage": entrypage   
            })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        entry_result = convert(entry_search)
        if entry_result is not None:
            return render(request,"encyclopedia/entry.html", {
            "title":entry_search,
            "entrypage": entry_result   
            })
        else:
            list = util.list_entries()
            view_list=[]
            for entry in list:
                if entry_search.upper() in entry.upper():
                    view_list.append(entry)
            return render(request,"encyclopedia/list.html", {
                "view_list":view_list
            })

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_exist = util.get_entry(title)
        if title_exist is not None:
            return render(request,"encyclopedia/bad.html", {
                "message":"We already have this entry!"})
        else:
            util.save_entry(title,content)
            new_entry=convert(title)
            return render(request,"encyclopedia/entry.html",{
            "title":title,
            "content":new_entry    
            }) 

def edit(request):
    if request.method == "POST":
        title = request.POST['edit_title']
        content = util.get_entry(title)

    return render(request,"encyclopedia/edit.html",{
            "title":title,
            "content":content    
            })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        entrypage=convert(title)
        return render(request,"encyclopedia/entry.html",{
            "title": title,
            "content":entrypage    
            })

def random_entry(request):
    list = util.list_entries()
    random_page = random.choice(list)
    entrypage = convert(random_page)
    return render(request,"encyclopedia/entry.html",{
            "title": random_page,
            "content":entrypage    
            }) 