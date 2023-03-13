from .models import Job
from .serializer import Jobserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def joblistapi(request):
    all_jobs = Job.objects.all()
    data = Jobserializers(all_jobs, many=True).data
    return Response({"data":data})
