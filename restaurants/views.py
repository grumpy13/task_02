from django.shortcuts import render

# Create your views here.

def hello(request):
	context = {
		"msg":"Hello World!"

	}
	return render(request, 'hello.html',context)
