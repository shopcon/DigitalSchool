from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login as auth_login,
	logout,
)
from dashboard.models import FreeCounselling,Blog,OurGallery,PhotoGallery,MediaGallery
from dashboard.forms import FreeCounsellingForm

# Create your views here.



def index_view(request):
	form=FreeCounsellingForm()
	all = PhotoGallery.objects.order_by("-id")[0:6]
	blogs = Blog.objects.order_by("-id")[0:6]
	context={
		"form":form,
		"all":all,
		"blogs":blogs
	}
	return render(request,"index.html",context)



def mediagallery(request):
	media = MediaGallery.objects.all().order_by("-id")
	context={
		"media":media,
	}
	return render(request,"media-gallery.html",context)

def ourgallery(request):
	all = OurGallery.objects.all()
	context={
		"all":all
	}
	return render(request,"our-gallery.html",context)

def photogallery(request):
	photos = PhotoGallery.objects.all().order_by("-id")
	context={
		"photos" :photos
	}
	return render(request,"photo-gallery.html",context)

def theperson(request):
	return render(request,"the-person.html")

def theperson2(request):
	return render(request,"Digital-school-story.html")

def addfreecounselling(request):
	form = FreeCounsellingForm(request.POST or None)
	if form.is_valid():
		form.save()
	return HttpResponseRedirect("/")

def blog(request):
	all = Blog.objects.all().order_by("-id")
	lla = Blog.objects.all()

	context={
		"all":all,
		"lla" :lla,
	}
	return render(request,"w_blog.html",context)

def ind_blog(request,string1):
	post = Blog.objects.get(id=string1)
	post.views=post.views+1
	post.save()
	all = Blog.objects.all().order_by("-id")
	context = {
		"post":post,
		"all":all,
	}
	return render(request,"blogpostdetail.html",context)

def wesolutions(request):
	return render(request,"e-sol-detail.html")