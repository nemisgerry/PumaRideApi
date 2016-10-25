from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Point
from .serializers import PointSerializer
from .models import Line
from .serializers import LineSerializer
"""
class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
"""
@api_view(['GET','POST'])
def points_list(request):
	if request.method=='GET':
		print "GEEET"
		points=Point.objects.all()
		serializer=PointSerializer(points,many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer=PointSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def lines_list(request,p_ori,p_des):
	if request.method=='GET':

		#p_or=request.query_params.get('p_origen')
		#p_des=request.query_params.get('p_destino')
		#lines=Line.objects.filter(p_origen=p_or,p_destino=p_des)
		lines=Line.objects.filter(p_origen=p_ori,p_destino=p_des)
		serializer=LineSerializer(lines,many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer=LineSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def line(request):
	if request.method=='GET':
		print "GEEET"
		Lines=Line.objects.all()
		serializer=LineSerializer(Lines,many=True)
		return Response(serializer.data)
	"""elif request.method=='POST':
		serializer=LineSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""
