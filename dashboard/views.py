from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login as auth_login,
	logout,
)
from .forms import UserLoginForm,TestimonialForm,BlogForm,PhotoGalleryForm,MediaGalleryForm
from .models import OurGallery,PhotoGallery,MediaGallery,Testimonial,Blog,FreeCounselling

# Create your views here.



def login_view(request):
	print(request.user.is_authenticated())
	log1 = "Login using Django authentication"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user2 = form.cleaned_data.get("username")
		pass2 = form.cleaned_data.get("password")
		user = authenticate(username=user2,password=pass2)
		auth_login(request, user)
		return HttpResponseRedirect("/dashboard/")



	context={
		"log":log1,
 		"form":form,
	}



	return render(request,"login.html",context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/dashboard/login/")


def dashboard_view(request):
    if request.user.is_authenticated():

        return render(request,"dashboard.html")
    else:
        raise Http404
def counselling_view(request):
    all=FreeCounselling.objects.all().order_by("-id")
    context={
        "all":all
    }
    return render(request,"counselling.html",context)

def media_view(request):
    if request.user.is_authenticated():

        form = MediaGalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            form = MediaGalleryForm()
        all = MediaGallery.objects.all().order_by("-id")
        context={
            "form":form,
            "all":all
        }
        return render(request,"mediagallery.html",context)
    else:
        raise Http404
def ourgallery_view(request):
    if request.user.is_authenticated():

        if request.POST:
            category=request.POST['id']
            image = request.FILES.get('file1')
            instance=OurGallery()
            instance.category=category
            instance.image=image
            instance.save()
        all = OurGallery.objects.all().order_by("-id")
        context={
            "all":all,
        }
        return render(request,"ourgallery.html",context)
    else:
        raise Http404

def testimonial_view(request):
    if request.user.is_authenticated():

        form1 = TestimonialForm(request.POST or None)
        if form1.is_valid():
            form1.save(commit=False)
            form1.save()
            form1 = TestimonialForm()

        log='saket'
        all =Testimonial.objects.all().order_by("-id")
        context = {
            "form1" : form1,
            "log":log,
            "all":all
        }

        return render(request,"testimonial.html",context)
    else:
        raise Http404
def blog_view(request):
    if request.user.is_authenticated():

        form=BlogForm(request.POST or None, request.FILES or  None)
        if form.is_valid():
            form.save()
            form=BlogForm()
        all = Blog.objects.all().order_by("-id")
        context={
            "form":form,
            "all":all
        }
        return render(request,"blog.html",context)
    else:
        raise Http404
def addphoto_view(request):
    if request.user.is_authenticated():

        form = PhotoGalleryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        all = PhotoGallery.objects.all().order_by("-id")
        context={
            "form":form,
            "all":all
        }
        return render(request,"photogallery.html",context)
    else:
        raise Http404
def delete_ourgallery_view(request,string1):
    if request.user.is_authenticated():

        instance =  get_object_or_404(OurGallery,id=string1)
        instance.delete()
        return HttpResponseRedirect("/dashboard/ourgallery/")
    else:
        raise Http404
def delete_photogallery_view(request,string1):
    if request.user.is_authenticated():

        instance =  get_object_or_404(PhotoGallery,id=string1)
        instance.delete()
        return HttpResponseRedirect("/dashboard/photogallery/")
    else:
        raise Http404
def delete_mediagallery_view(request,string1):
    if request.user.is_authenticated():

        instance =  get_object_or_404(MediaGallery,id=string1)
        instance.delete()
        return HttpResponseRedirect("/dashboard/mediagallery/")
    else:
        raise Http404

def delete_blog_view(request,string1):
    if request.user.is_authenticated():

        instance =  get_object_or_404(Blog,id=string1)
        instance.delete()
        return HttpResponseRedirect("/dashboard/blog/")
    else:
        raise Http404