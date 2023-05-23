
from django.http import HttpResponse
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from .models import *
from .forms import ItemCreate
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    offer = Offer.objects.all()[:1]
    allbranch = Branch.objects.all()[:3]
    allnews = News.objects.all()[:3]
    allteam = Team.objects.all()[:3]
    allitem = Item.objects.all()[:6]
    context = {
        "offer": offer,
        "allbranch":allbranch,
        "allnews":allnews,
        "allteam":allteam,
        "allitem":allitem,
    }

    return render(request,'home.html',context)


def branch(request):
    allbranch = Branch.objects.all()
    page =Paginator(allbranch, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)


    context = {
        "allbranch": allbranch,
    }
    return render(request,'branch.html', context)

def news(request):
    allnews = News.objects.all()
    page =Paginator(allnews, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)


    context = {
        "allnews": allnews,
        'page':page,
    }
    return render(request,'news.html', context)

def team(request):
    allteam = Team.objects.all()
    page =Paginator(allteam, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        "allteam": allteam,
        'page':page,
    }

    return render(request,'team.html',context)


def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')

def googlemap(request):
    allbranch = Branch.objects.all()


    context = {
        "allbranch": allbranch,
    }
    return render(request,'googlemap.html', context)

def team(request):
    allteam = Team.objects.all()

    page =Paginator(allteam, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)


    context = {
        "allteam": allteam,
        'page':page,
    }
    return render(request,'team.html', context)



def gallery(request):
    allitem = Gallery.objects.all()

    page =Paginator(allitem, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        "allitem": allitem,
        'page':page,
    }

    return render(request,'gallery.html', context)

def item(request):
    allitem = Item.objects.all()

    page =Paginator(allitem, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        "allitem": allitem,
        'page':page,
    }
    return render(request,'item.html', context)




# crud for item
# def index(request):
#     shelf = Item.objects.all()
#     return render(request, 'admin/index.html', {'shelf': shelf})
# def upload(request):
#     upload = ItemCreate()
#     if request.method == 'POST':
#         upload = ItemCreate(request.POST, request.FILES)
#         if upload.is_valid():
#             upload.save()
#             return redirect('index')
#         else:
#             return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
#     else:
#         return render(request, 'admin/upload_form.html', {'upload_form':upload})

# def update_item(request, item_id):
#     item_id = int(item_id)
#     try:
#         item_sel = Item.objects.get(id = item_id)
#     except item.DoesNotExist:
#         return redirect('index')
#     item_form = ItemCreate(request.POST or None, instance = item_sel)
#     if item_form.is_valid():
#        item_form.save()
#        return redirect('index')
#     return render(request, 'admin/upload_form.html', {'upload_form':item_form})

# def delete_item(request, item_id):
#     item_id = int(item_id)
#     try:
#         item_sel = Item.objects.get(id = item_id)
#     except Item.DoesNotExist:
#         return redirect('index')
#     item_sel.delete()
#     return redirect('index')