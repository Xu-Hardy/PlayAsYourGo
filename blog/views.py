from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
import requests
from django.http import StreamingHttpResponse
import os
from django.core.mail import send_mail

from urllib.parse import quote

@api_view(['GET'])
def client_ip(request):
    client_ip = request.META.get('REMOTE_ADDR')
    if client_ip is not None:
        return Response({'ip': client_ip})
    else:
        return Response({
            'error': 'not found ip'
        })

@api_view(['GET'])
def server_ip(request):
    try:
        # ip=3
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        # return Response({'server':ip})
    except Exception as e:
        print('8'*100)
        return Response({'err': e})
    finally:
        return Response({
            'a':1
        })
    # return

class FileUploadView(APIView):
    parser_classes = [FileUploadParser, ]

    def get(self, request, filename='ana1.pdf'):
            path = os.path.dirname(__file__)
            file_stream = open('C:/Users/Administrator/Desktop/ana.pdf', 'rb')
            # 生成迭代器对象
            # file_iter = iter(lambda: file_stream.read(4096), b'')
            # 建立流响应对象
            response = StreamingHttpResponse(file_stream)
            response['content-type'] = 'application/pdf'
            # 告诉浏览器怎么处理
            # inline 浏览器内联打开
            # attachment 附件的形式下载
            # filename = quote('ana.pdf')
            filename += '11111.pdf'

            response['content-disposition'] = f'attachment;filename="{filename}"'
            return response

    def put(self, request, filename='1.txt', format=None):
        file_obj = request.data['file']
        with open(filename, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return Response(f'{filename} uploaded',status=204)


@api_view(['GET'])
def t_mail(reuest):

    tm = TempMail()
    email = tm.get_email_address()
