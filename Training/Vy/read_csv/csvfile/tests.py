from django.test import TestCase
from django.shortcuts import render, get_object_or_404
# Create your tests here.
def upload_file(request):
    return render(request, 'file_upload_csv.html',)