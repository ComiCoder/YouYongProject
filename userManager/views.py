from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from userManager.models import UserInfo
from rest_framework.response import Response
from userManager.serializers import UserInfoSerializer


def queryUserByPhone(phoneNum):
    userInfoSet = UserInfo.objects.filter(phoneNum=phoneNum)
    if userInfoSet == None or userInfoSet.count() == 0:
        return None
    else:
        return userInfoSet[0]

def get_object(pk):
    userInfo =  UserInfo.objects.get(pk=pk)
    if userInfo == None:
        return None
    else:
        return userInfo

# Create your views here.
@api_view(['POST'])
def register(request):
    """
        register the UserInfo
    """
    if request.method == 'POST':
        #get the reg type firstly
        regType = request.POST["regType"]
        if regType == None:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        
        regType = int(regType)
        
        if regType == UserInfo.REG_TYPE_PHONE:
            phoneNum = request.POST['phoneNum']
            password = request.POST['password']
            
            if phoneNum==None or password==None:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            
            phoneNum = phoneNum.encode('utf-8')
            password = password.encode('utf-8')
            
            userInfoSet = queryUserByPhone(phoneNum)
            if userInfoSet == None or userInfoSet.count()==0:
                userInfo = UserInfo()
                userInfo.phoneNum = phoneNum
                userInfo.password = password
                userInfo.save()
                
                userInfoSerializer = UserInfoSerializer(userInfo)
                return Response(userInfoSerializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(userInfoSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET'])
def logon(request):
    sessionUserID = request.session['userID']
    if sessionUserID!=None:
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)

    phoneNum=request.POST['phoneNum']
    tempUserInfo = queryUserByPhone(phoneNum=phoneNum)
    
    if tempUserInfo == None or tempUserInfo.count()==0:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    else:
        if tempUserInfo.password == request.POST['password']:
            request.session['user_id'] = tempUserInfo.id
            userInfoSerializer = UserInfoSerializer(tempUserInfo)
            return Response(userInfoSerializer.data,status=status.HTTP_202_ACCEPTED)
    
    