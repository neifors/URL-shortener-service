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
         result = Equivalent.objects.filter(original = url)
         if result:
            # redirect to the original url
            return redirect('maker-redirect', alias=result[0].alias)
         else:
            # create alias, save into db and display the new short url
            alias = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
            result = Equivalent.objects.create(alias=alias, original=url)
            data = {'result': result,
                    'form' : NewShortUrlForm()}
            return render(request, 'maker/home.html', data)
   else:
      form = NewShortUrlForm()
      data = {'form': form}
      return render(request, 'maker/home.html', data)


def redirect_to_original(request, alias):
   result = Equivalent.objects.filter(alias=alias)
   return redirect(result[0].original)
