#-*- coding:utf-8 -*-
from django.http import Http404, HttpResponse
from django.shortcuts import render,render_to_response
from library.models import *
from django.template import Context

def start(request):
    return render(request, 'start.html') 

def create(request):
	if request.POST:
		authorid = request.POST["Author"]
		author = ''
		try:
			author = Author.objects.get(AuthorID=authorid)
		except:
			pass
		if author:
			book = Book(ISBN = request.POST["ISBN"],Title = request.POST["Title"] , AuthorID = author , Publisher = request.POST["Publisher"],PublishDate = request.POST["PublishDate"],Price = request.POST["Price"])
			book.save()
		else:
			newauthor = Author(AuthorID = request.POST["AuthorID"] , Name = request.POST["Name"],Age = request.POST["Age"],Country = request.POST["Country"])
			newauthor.save()
			book = Book(ISBN = request.POST["ISBN"],Title = request.POST["Title"] , AuthorID = authorid , Publisher = request.POST["Publisher"],PublishDate = request.POST["PublishDate"],Price = request.POST["Price"])
			book.save()
	
	return render(request, 'create.html')
	
def search(request):
	return render(request, 'search.html')
	
def result(request):
	if request.POST:
		authors = Author.objects.filter(AuthorID = request.POST["AuthorID"])
		book = Book.objects.filter(AuthorID = request.POST["AuthorID"])
		L=[authors,book]
		c=Context({"L":L})
	return render(request, 'result.html',c)
	
	
		
def dele(request):
	if request.POST:
		post = request.POST
		print post["de"]
		Book.objects.get(ISBN = post["de"]).delete()
	return render(request, "delete.html")

	
def updat(request):
	if request.POST:
		post = request.POST
		print post["de"]
		Book.objects.get(ISBN = post["de"]).delete()
	return render(request, "update.html")
		
