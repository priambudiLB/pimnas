from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.

response={}
def index(request):
	return render(request, 'index.html', response)

def signin(request):
	return render(request, 'signin.html', response)

def data_daerah(request):
	return render(request, 'datadaerah.html', response)

def sponsor_departemen(request):
	return render(request, 'sponsor2.html', response)

def sponsor_perusahaan(request):
	return render(request, 'sponsor.html', response)

def dokumen_proposal(request):
	return render(request, 'proposal.html', response)

def dokumen_lpj(request):
	return render(request, 'lpj.html', response)

def dokumen_lpjpublik(request):
	return render(request, 'lpj2.html', response)