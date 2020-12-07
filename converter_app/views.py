from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from xhtml2pdf import pisa 
from django.template import Context, Template
import pathlib
import re


def generate_PDF(request):

        data = {}
        template = get_template('page.html')
        html  = template.render(data)
        file = open('test.pdf', "w+b")
        pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')
        file.seek(0)
        pdf = file.read()
        file.close()            
        return HttpResponse(pdf, 'application/pdf')

def page(request):

        return render(request, 'page.html', {})

def generate_PDF_from_selected_section(request):

        html_file = open(str(pathlib.Path(__file__).parent.absolute()) + '/templates/page.html', 'r')
        html_file_string = html_file.read()
        html_file.close()
        result = re.search(r'(<div id="paragraph">[\S\s]*?</div>)', html_file_string)
        selected_section = result.group(1)
        template = Template(selected_section)
        data = Context({})
        html_template = template.render(data)
        file = open('test_001.pdf', "w+b")
        pisaStatus = pisa.CreatePDF(html_template.encode('utf-8'), dest=file, encoding='utf-8')
        file.seek(0)
        pdf = file.read()
        file.close()            
        return HttpResponse(pdf, 'application/pdf')

