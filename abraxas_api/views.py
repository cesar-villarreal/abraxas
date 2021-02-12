#from inspect import getsource

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from datetime import datetime

from django.core import serializers
#from rest_framework.renderers import JSONRenderer
#from rest_framework_xml.renderers import XMLRenderer



@api_view(['GET'])
def overview_api(request):
	urls_api = {
		'List all tasks' : '/task-list/',
		'Create a task' : '/task-create/',
		'Update a task' : '/task-update/',
		'Delete a task' : '/task-delete/<id>/',
		'List tasks by status' : '/task-status/<id>/',
		'Search task by word' : '/tasks/search?q=<foo>',
	}
	return Response(urls_api)


#@renderer_classes([XMLRenderer])
#renderer_classes([XMLRenderer])(Response(taskList)
#taskList = api_view(['GET'])(taskList)

def format_cond(tasks_, request_, serializers):
	if ("*/*" or "application/json") not in request_.headers['Accept']:
		response = serializers.serialize("json", tasks_)
	else:
		serializer0 = serializers.serialize("xml", tasks_)
		serializer1 = serializers.serialize("json", tasks_)
		response = [serializer0, serializer1]
	return response



@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	return Response(format_cond(tasks, request, serializers))



@api_view(['POST'])
def taskCreate(request):
	task_id_max = Task.objects.order_by('-task_id').first().task_id
	request.data['task_id'] = task_id_max + 1
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)



@api_view(['PUT'])
def taskUpdate(request, pk):
	task = Task.objects.get(task_id = pk)
	if task.status == 'completada':
		return Response('Task already completed')
	if 'status' in request.data.keys():
		task.timespan = (datetime.now() - task.updated_at.replace(tzinfo = None)).seconds/60
		print(task.timespan)
	print(task.timespan)
	serializer = TaskSerializer(instance = task, data = request.data, partial = True)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)



@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(task_id = pk)
	task.delete()
	return Response("Task %(pk)s deleted" %locals())



@api_view(['GET'])
def taskStatus(request, pk):
	tasks = Task.objects.filter(status = pk)
	#serializer = TaskSerializer(tasks, many = True)
	#return Response(serializer.data)
	return Response(format_cond(tasks, request, serializers))



@api_view(['GET'])
def tasks(request):
	query = request.GET["q"].strip()
	tasks  = Task.objects.filter(description__icontains=query).all()
	#serializer = TaskSerializer(tasks, many = True)
	#return Response(serializer.data)
	return Response(format_cond(tasks, request, serializers))
