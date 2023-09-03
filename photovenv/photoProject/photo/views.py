from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout, login as auth_login

from . models import Photo 

# home page
def home(request):

    return render(request,'home.html')

#sign up page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request)  
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


#login page
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('photo_sharing')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#Photo_sharing page
# def photo_sharing(request):

#     if request.method =='POST':
#         new_photo = Photo(file = request.FILES['img'])
#         new_photo.save()
#         return render(request,'photo.html',{'new_url':str(new_photo.file.url)})

#     else:
#         return render(request,'photo.html')



def photo_sharing(request):
    if request.method == 'POST':
        new_photos = request.FILES.getlist('img')  # Get a list of uploaded image files

        for img in new_photos:
            new_photo = Photo(file=img)
            new_photo.save()
        #photos = Photo.objects.all()  # Retrieve all photos from the database
        photos = Photo.objects.all().order_by('-id')  # Retrieve all photos and order them by ID in descending order
        return render(request, 'album.html', {'photos': photos})

    else:
        return render(request, 'photo.html')
    
def user_logout(request):
    logout(request)
    return redirect('/')

