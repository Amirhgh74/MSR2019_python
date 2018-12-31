from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import re 
from LineMetric import LineMetric
import os
import time
import subprocess

@csrf_exempt
def qu(request):
    origin = ""
    edit = ""
    try:
        js = json.loads(request.body)

    except Exception as a:
        print ("No JSON found!")
        return HttpResponse(json.dumps({'token': '', 'success': False}))

    try:
        origin = js['origin']
        edit = js['edit']

        print(origin)

    except Exception as b:
        print ("No origin and edit found!")
        return HttpResponse(json.dumps({'token': '', 'success': False}))

    line_count_origin = origin.count('\n')
    line_count_edit = edit.count('\n')

    metric_origin = LineMetric(origin , line_count_origin)
    metric_edit = LineMetric(edit , line_count_edit)

    avg_line_length_origin = metric_origin.avg_line_length()
    avg_line_length_edit = metric_edit.avg_line_length()

    max_line_len_origin = metric_origin.max_line_len()
    max_line_len_edit = metric_edit.max_line_len()

    max_identifier_length_origin = metric_origin.max_identifier_length()
    max_identifier_length_edit = metric_edit.max_identifier_length()

    max_identifier_origin = metric_origin.max_identifier()
    max_identifier_edit = metric_edit.max_identifier()

    avg_blank_lines_origin = metric_origin.avg_blank_lines()
    avg_blank_lines_edit = metric_edit.avg_blank_lines()

    avg_indentation_origin = metric_origin.indentaion()
    avg_indentation_edit = metric_edit.indentaion()

    max_indentations_origin = metric_origin.max_indentations()
    max_indentations_edit = metric_edit.max_indentations()

    avg_comment_origin = metric_origin.num_comment()
    avg_comment_edit = metric_edit.num_comment()

    # send request to java and get the result : 

    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:8080/quality/', data = json.dumps({'origin':origin , 'edit': edit}) , headers = headers )
    
    resultJson = json.load(r.json())

    originScore = resultJson["originScore"]
    editScore = resultJson["editScore"]

    jsonData = {}
    origin_metric = {}
    edit_metric = {}


    origin_metric["score"] = originScore
    origin_metric["lineCount"] = line_count_origin
    origin_metric["avgLineLength"] = avg_line_length_origin
    origin_metric["maxLineLength"] = max_line_len_origin
    origin_metric["manxIdentifierLength"] =max_identifier_length_origin
    origin_metric["maxIdentifier"] = max_identifier_origin
    origin_metric["avgBlankLine"] = avg_blank_lines_origin
    origin_metric["avgIndentation"] = avg_indentation_origin
    origin_metric["maxIndentation"] = max_indentations_origin
    origin_metric["avgComment"] = avg_comment_origin

    jsonData["origin"] = origin_metric

    edit_metric["score"] = editScore
    edit_metric["lineCount"] = line_count_edit
    edit_metric["avgLineLength"] = avg_line_length_edit
    edit_metric["maxLineLength"] = max_line_len_edit
    edit_metric["manxIdentifierLength"] =max_identifier_length_edit
    edit_metric["maxIdentifier"] = max_identifier_edit
    edit_metric["avgBlankLine"] = avg_blank_lines_edit
    edit_metric["avgIndentation"] = avg_indentation_edit
    edit_metric["maxIndentation"] = max_indentations_edit
    edit_metric["avgComment"] = avg_comment_edit

    jsonData["edit"] = edit_metric

    return HttpResponse(json.dumps({'data': jsonData, 'success': False}))