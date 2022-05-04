from django.shortcuts import render, redirect
from .models import Equivalent
from .forms import NewShortUrlForm
import random
import string
# from django.http import HttpResponseRedirect 

# Create your views here.

def home(request):
   if request.method == 'POST':
      form = NewShortUrlForm(request.POST)
      if form.is_valid():
         url = form.cleaned_data.get("original")
         print(f"url from form: {url}")
         result = Equivalent.objects.filter(original = url)
         print(f"result: {result}")
         if result:
            # redirect to the original
            return redirect('maker-redirect', alias=result.alias)
         else:
            # create alias
            alias = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
            print(f"alias: {alias}")
            result = Equivalent.objects.create(alias=alias, original=url)
            print(f"created object: {result}")
            data = {'result': result,
                    'form' : NewShortUrlForm()}
            return render(request, 'maker/home.html', data)
   else:
      form = NewShortUrlForm()
      data = {'form': form}
      return render(request, 'maker/home.html', data)


def redirect(request, alias):
   result = Equivalent.objects.filter(alias=alias)
   print("This result is inside redirect view")
   return redirect(result)
