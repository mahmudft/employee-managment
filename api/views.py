from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.reverse import reverse
from api.models import Employee, Team, TeamLeader, WorkTime
from api.serializers import EmployeeSerializer, TeamLeaderSerializer, TeamSerializer, WorkTimeSerializer

#teams route


@swagger_auto_schema(method='get', responses={200: TeamSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=TeamSerializer)
@api_view(['GET', 'POST'])
def teams_view(request):
    """
    Retrieve, create team(s)

    @Post Request 
    Request Body 

    {
        "team_name": String,
        "team_leader": Int  // Must be id of team leader record or can be null
    }

    """

    teams = Team.objects.all()

    if request.method == 'GET':
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        team_data = request.data

        if team_data.get('team_leader'):
            try:
                team_leader = TeamLeaderSerializer(
                    TeamLeader.objects.get(id=team_data.get('team_leader'))).data
            except TeamLeader.DoesNotExist:
              team_leader = None
        else:
            team_leader = None

        team_data['team_leader'] = team_leader
        serializer = TeamSerializer(data=team_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@swagger_auto_schema(method='get', responses={200: TeamSerializer(many=True)})
@swagger_auto_schema(method='delete', responses={200: []})
@swagger_auto_schema(method='PUT', responses={200: TeamSerializer()})
@api_view(['GET', 'DELETE', 'PUT'])
def team_view_detail(request, pk):
     """
     * Accepts id of single Team object as param

     Retrieve, Update, Delete single team object

     @GET request will return single team object or []
 
     @PUT will update exsisting team object

     Request Body

     Put the fields which are going to be updated

     {
         "team_name": String,
         "team_leader": Int  // Must be id of team leader record or can be null
     }


     @DELETE will delete signle record

     Send empty request     
     """
     
     try:
        team_by_id = Team.objects.get(id=pk)
     except Team.DoesNotExist:
        return Response([])
     if request.method == 'GET':
        return Response(TeamSerializer(team_by_id).data)

     elif request.method == 'DELETE':
        team_by_id.delete()
        return Response([])

     elif request.method == 'PUT':
        serializer = TeamSerializer(
            team_by_id, data=request.data, partial=True)
        if request.data.get('team_leader'):
            new_team_leader_record = TeamLeader.objects.get(
                id=request.data.get('team_leader'))
            request.data['team_leader'] = TeamLeaderSerializer(
                new_team_leader_record).data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# employee route


@swagger_auto_schema(method='get', responses={200: EmployeeSerializer(many=True)})
@swagger_auto_schema(method='post', responses={200: EmployeeSerializer()})
@api_view(['GET', 'POST'])
def employee_view(request):
    """
    Retrieve, create employee(s)

    @GET request will return Employees or []

    @POST will create new employee object

    Request Body

    {
        "name": String
        "team": Int //id of object Team
        "hourly_rate": Int
        "worktime": Int  // id of object in WorkTime 
    }

    """
    employees = Employee.objects.all()

    if request.method == 'GET':
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        team_data = request.data

        if team_data.get('team'):
            try:
                team = TeamSerializer(
                    Team.objects.get(id=team_data.get('team'))).data
            except Team.DoesNotExist:
              team = None
        else:
            team = None

        if team_data.get('worktime'):
            try:
                worktime = WorkTimeSerializer(
                    WorkTime.objects.get(id=team_data.get('worktime'))).data
            except WorkTime.DoesNotExist:
              worktime = None
        else:
            worktime = None

        team_data['team'] = team
        team_data['worktime'] = worktime
        serializer = EmployeeSerializer(data=team_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@swagger_auto_schema(method='get', responses={200: EmployeeSerializer(many=True)})
@swagger_auto_schema(method='delete', responses={200: []})
@swagger_auto_schema(method='put', responses={200: EmployeeSerializer()})
@api_view(['GET', 'DELETE', 'PUT'])
def employee_view_detail(request, pk):
    """
    * Accepts id of single Employee object as param

    Retrieve, Update, Delete single employee object

    @GET request will return single employee object or []

    @PUT will update exsisting employee object

    Request Body

    Put the fields which are going to be updated

    {
        "name": String
        "team": Int //id of object Team
        "hourly_rate": Int
        "worktime": Int  // id of object in WorkTime 
    }


    @DELETE will delete signle record

    Send empty request
    """
    try:
        employee_by_id = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return Response([])

    if request.method == 'GET':
        return Response(EmployeeSerializer(employee_by_id).data)

    elif request.method == 'DELETE':
        employee_by_id.delete()
        return Response([])

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(
            employee_by_id, data=request.data, partial=True)
        if request.data.get('team'):
            new_team_record = Team.objects.get(
                id=request.data.get('team'))
            request.data['team'] = TeamSerializer(
                new_team_record).data

        if request.data.get('worktime'):
            new_worktime_record = WorkTime.objects.get(
                id=request.data.get('worktime'))
            request.data['worktime'] = WorkTimeSerializer(
                new_worktime_record).data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# worktime
@api_view(['GET', 'POST'])
def worktime_view(request):
    """
    Retrieve, create worktime(s)

    @GET will return objects of Worktime table or []

    @POST will create new object in WorkTime table

    Request body

    {
        "type": String  // accepts type of work either full-time or part-time
        "hours": Int  // accepts work hours per week for full-time 40 hrs/week 
    }

    """
    teams = WorkTime.objects.all()


    if request.method == 'GET':
        serializer = WorkTimeSerializer(teams, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = WorkTimeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def worktime_view_detail(request, pk):
     """
     Retrieve, create worktime(s)

     *Accept id of worktime object id as param

     @GET will return single object from Worktime table or []

     @PUT will update exsisiting object in WorkTime table

     Request body

     {
         "type": String  // accepts type of work either full-time or part-time
         "hours": Int  // accepts work hours per week for full-time 40 hrs/week 
     }

     """
     try:
        worktime = WorkTime.objects.get(id=pk)
     except WorkTime.DoesNotExist:
        return Response([])
     if request.method == 'GET':
        return Response(WorkTimeSerializer(worktime).data)
     
     elif request.method == 'DELETE':
        worktime.delete()
        return Response([])
    
     elif request.method == 'PUT':
        serializer = WorkTimeSerializer(
            worktime, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# teamleader 
@api_view(['GET', 'POST'])
def teamleader_view(request):
    """
    Retrieve, create teamleader(s)

    @GET will return objects of Worktime table or []

    @POST will create new object in WorkTime table

    Request body

    {
        "team_leader_name": String
        "hourly_rate": Int
        "worktime": Int // id of record in Worktime table
    }

    """

    teamleaders = TeamLeader.objects.all()


    if request.method == 'GET':
        serializer = TeamLeaderSerializer(teamleaders, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        team_leader_data = request.data

        if team_leader_data.get('worktime'):
            try:
                worktime = WorkTimeSerializer(WorkTime.objects.get(id=team_leader_data.get('worktime'))).data
            except WorkTime.DoesNotExist:
              worktime = None
        else:
            worktime = None
        

        team_leader_data['worktime'] = worktime
        serializer = TeamLeaderSerializer(data=team_leader_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def teamleader_view_detail(request, pk):
     """
     Retrieve, create teamleader(s)

     @GET will return single object from Worktime table or []

     @PUT will update exsisting object in WorkTime table

     Request body

     {
         "team_leader_name": String
         "hourly_rate": Int
         "worktime": Int // id of record in Worktime table
     }
     """
     try:
        team_leader_by_id = TeamLeader.objects.get(id=pk)
     except TeamLeader.DoesNotExist:
        return Response([])
     if request.method == 'GET':
        return Response(TeamLeaderSerializer(team_leader_by_id).data)
     
     elif request.method == 'DELETE':
        team_leader_by_id.delete()
        return Response([])
    
     elif request.method == 'PUT':
        serializer = TeamLeaderSerializer(
            team_leader_by_id, data=request.data, partial=True)
        if request.data.get('worktime'):
            new_team_leader_record = WorkTime.objects.get(
                id=request.data.get('worktime'))
            request.data['worktime'] = WorkTimeSerializer(new_team_leader_record).data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class ApiRoot(generics.GenericAPIView):
    """
    Root Api view with clickable links to main endpoints
    """
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'teams': reverse('teams', request=request),
            'worktime': reverse("worktime", request=request),
            'teamleaders': reverse("teamleader", request=request),
            'employees': reverse("employees", request=request),
            'swagger': reverse("swagger-schema", request=request)
        })
