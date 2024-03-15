from django.shortcuts import render,redirect
from rest_framework import status
from .forms import MessageForm
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import ReminderSerializer
from.models import Message
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'innn/index.html') 
    else:
        form = MessageForm()
    return render(request, 'innn/index.html', {'form': form})

#create datas with API
class ReminderAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
#view the datas
class DataList(APIView):
     def get(self,request):
          books=Message.objects.all()
          print(books)
          serializer=ReminderSerializer(books,many=True)

          return Response(serializer.data)