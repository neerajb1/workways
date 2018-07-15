from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.permissions import IsAuthenticated , IsAdminUser

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse

from .models import  Profile



User= get_user_model()

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)
	class Meta:
		model = Profile
		fields = [
			"Salary",
			"user",
			'dob',
			'name',
            "mobile",
            "empid",
		]




class ProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication, ]
    permission_classes = [ IsAuthenticated,]
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get_queryset(self):
	    if self.request.user.is_staff:
		    return Profile.objects.all()
	    else:
		    return Profile.objects.filter(user= self.request.user)
