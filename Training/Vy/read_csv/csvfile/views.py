from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import pandas as pd
import pandas as pd
from vncorenlp import VnCoreNLP
import re
import numpy as np

import re

from rest_framework.response import Response
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import json
import xlwt
from .tag_cloud import nlp_tokenize, stop_word
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Multi_Post, Newsfeed
from .tag_cloud import VnCoreNLP
def upload_file(request):
    return render(request, 'form_csv.html')
def read_data(request):
    count_word = {}
    if request.method == 'POST':
        if Newsfeed.objects.filter().count() > 0 :
            Newsfeed.objects.all().delete()
        path = request.POST['name_file']
        url = 'data_csv/'+path
        keywords, data  = nlp_tokenize(url)
        for id, content, post_ower in zip(data['ID'], data['Content'], data['ID người đăng']):
            feed = Newsfeed(id_post =str(id),
                            content= content,
                            post_ower = str(post_ower))
            feed.save()
        count_word = stop_word(keywords)
        response_data = []
        for word, frequently in zip(count_word['word'][0:50], count_word['frequently'][0:50]) :
            # feed = Multi_Post(keyword = word, frequently = frequently)
            # feed.save()
            response_data.append({'word': word, 'frequently': frequently})
            # response_data['id_post'] = feed.keyword
            # response_data['content'] = feed.frequently

        # html = render_to_string('form_csv.html', {'response_data': response_data})
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse("Request method is not a GET")

def newfeeds(request):
    response_data = []
    if request.is_ajax() and request.method == 'POST':
        tag_words = request.POST['tag_words']
        keywords = tag_words
        path = request.POST['name_file']
        path_file = path
        url = 'data_csv/'+path
        data = pd.read_excel(url)
        # print(data)
        data = data.dropna()
        data = data[['Content', 'ID người đăng']]
        data = data[data["Content"].str.contains(keywords, regex=True, case=False)]
        # response_data = "<a href= show_post(request'" > + str(data) + "</a>"
        response_data = []
        for user, post in zip(data['ID người đăng'], data['Content']):
            # feed = Multi_Post(keyword = word, frequently = frequently)
            # feed.save()
            response_data.append({'user': user, 'post': post})

        return render(request, 'showfeed.html', {'response_data':response_data})


def newsfeed(request,tag_words):
    newsfeed = Newsfeed.objects.all()
    response_data = []
    for i in newsfeed:
        if tag_words in i.content:
            case = {'post_owner': i.post_ower, 'feed': i.content, 'id_feed': i.id_post}

            response_data.append(case)

    return render(request,'showfeed.html',{'response_data':response_data})

from io import StringIO

def register_profile(request):
    return render(request, 'login.html')

def export_page(request,tag_words):
    response_data = []
    newsfeed = Newsfeed.objects.all()
    for i in newsfeed:
        if tag_words in i.content:
            case = {'post_owner': i.post_ower, 'feed': i.content, 'id_feed': i.id_post}
            response_data.append(case)
    out_path = "data_csv/data_output/"+tag_words+".xlsx"
    data = pd.DataFrame(response_data)
    data.to_excel(out_path, sheet_name='Sheet_name_1')
    return HttpResponse('Please go to folder data_output to see the file')

