from django.shortcuts import render, redirect
from .models import Equivalent
from .forms import NewShortUrlForm
import random
import string

# import requests # in order to validate the given URL by the user


def home(request):
   # if user submit the form
   if request.method == 'POST':
      form = NewShortUrlForm(request.POST)
      # check if the form is valid
      if form.is_valid():
         # check if that url already has a short alias into our database
         url = form.cleaned_data.get("original")
         result = Equivalent.objects.filter(original = url)

         '''
         # check if the given url exists on the internet
         response = requests.get(url)
         try:
            if response.status_code == 200:
               print("URL exists")
         except Exception:
            pass
         '''          

         # if already exists
         if result:
            # render the homepage sending the result and the form again because we always want the form to be displayed
            data = {'result_exists': result[0],
                    'form' : NewShortUrlForm()}
            # ************** case 1 **************
            return render(request, 'maker/home.html', data)
         # if that url isn't in our db yet
         else:
            # in the next 5 lines of code we are getting a random alias of 5 characteres, and will repeat the step if that alias already exist for another url within our database
            exists = True
            while exists:
               alias = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(5))
               # if new alias is not equal with any other alias from db
               if not Equivalent.objects.filter(alias=alias):
                  exists = False
            # create new instance (save it into the db)
            result = Equivalent.objects.create(alias=alias, original=url)
            # render the homepage sending the result and the form
            data = {'result_not_exists': result,
                    'form' : NewShortUrlForm()}
            # ************** case 2 **************                   
            return render(request, 'maker/home.html', data)
   #if the user didn't submit the form
   else:
      #render the homepage with the form
      data = {'form': NewShortUrlForm()}
      # ************** case 3 **************
      return render(request, 'maker/home.html', data)


def redirect_to_original(request, alias):
   result = Equivalent.objects.filter(alias=alias)
   return redirect(result[0].original)
