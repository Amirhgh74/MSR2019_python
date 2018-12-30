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

    # line_count_origin = origin.count('\n')
    # # line_count_edit = edit.count('\n')

    # metric_origin = LineMetric(origin , line_count_origin)
    # # metric_edit = LineMetric(edit , line_count_edit)

    # avg_line_length_origin = metric_origin.avg_line_length()
    # # avg_line_length_edit = metric_edit.avg_line_length()

    # max_line_len_origin = metric_origin.max_line_len()
    # # max_line_len_edit = metric_edit.max_line_len()

    # max_identifier_length_origin = metric_origin.max_identifier_length()
    # # max_identifier_length_edit = metric_edit.max_identifier_length()

    # avg_blank_lines_origin = metric_origin.avg_blank_lines()
    # # avg_blank_lines_edit = metric_edit.avg_blank_lines()

    # avg_indentation_origin = metric_origin.indentaion()
    # # avg_indentation_edit = metric_edit.indentaion()

    # max_indentations_origin = metric_origin.max_indentations()
    # # max_indentations_edit = metric_edit.max_indentations()

    # res = os.system("java -jar readability.jar")
    # time.sleep(1)
    # print("res = " + res)
    # os.system(origin)

    # call(["java", "-jar", "readability.jar", origin, "###"])
    # result = subprocess.run(['java', '-jar', 'readability.jar', '\n', origin, '\n', '###'], stdout=subprocess.PIPE)
    subprocess.call((
        'java', 
        '-jar',  
        'readability.jar',
        '\n',
        origin,
        '\n',
        '###',
    ))
    # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    # print('res = ' + str(result.stdout))




    

    return HttpResponse(json.dumps({'token': '', 'success': True}))