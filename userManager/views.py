from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from userManager.models import UserInfo
from rest_framework.response import Response
from userManager.serializers import UserInfoSerializer

import logging


logger = logging.getLogger(__name__)

def queryUserByPhone(phoneNum):
    userInfoSet = UserInfo.objects.filter(phoneNum=phoneNum)
    if userInfoSet == None or userInfoSet.count() == 0:
        return None
    else:
        return userInfoSet[0]

def queryUserByID(userID):
    userInfo =  UserInfo.objects.get(pk=userID)
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
            
@api_view(['POST'])
def logon(request):
 
    try:
        sessionUserID = request.session.get('user_id')
    except:
        logger.debug('A new user logon')
    if sessionUserID!=None:
        return HttpResponse(status=status.HTTP_100_CONTINUE)

    phoneNum=request.POST.get('phoneNum')
    if phoneNum == None:
        return HttpResponse(content='need phone number',status=status.HTTP_400_BAD_REQUEST)
    tempUserInfo = queryUserByPhone(phoneNum=phoneNum)
    
    if tempUserInfo == None:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    else:
        if tempUserInfo.password == request.POST.get('password'):
            request.session['user_id'] = tempUserInfo.id
            userInfoSerializer = UserInfoSerializer(tempUserInfo)
            return Response(userInfoSerializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def logout(request):
    sessionUserID = request.session.get('user_id')
    
    if sessionUserID == None:
        return HttpResponse(content='Not Logon', status=status.HTTP_401_UNAUTHORIZED)
    
    tempUserInfo= queryUserByID(sessionUserID)
    if tempUserInfo==None:
        return HttpResponse(content='User not found', status=status.HTTP_401_UNAUTHORIZED)
    request.session.pop('user_id')
    return HttpResponse(status=status.HTTP_200_OK)

@api_view(['POST'])
def update_icon_image(request):
    sessionUserID = request.session.get('user_id')
    
    if sessionUserID == None:
        return HttpResponse(content='Not Logon', status=status.HTTP_401_UNAUTHORIZED)
    
    tempUserInfo= queryUserByID(sessionUserID)
    if tempUserInfo==None:
        return HttpResponse(content='User not found', status=status.HTTP_401_UNAUTHORIZED)
    
    if request.FILES['userIcons'] ==None:
        return HttpResponse(content="no image upload", status=status.HTTP_400_BAD_REQUEST)
    tempUserInfo.largeIconURL = request.FILES['userIcons']
    tempUserInfo.save()
    
    userInfoSerializer = UserInfoSerializer(tempUserInfo)
    return Response(userInfoSerializer.data,status=status.HTTP_200_OK)

    