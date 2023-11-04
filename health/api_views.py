from rest_framework import viewsets
from . import models
from . import serializers

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'
    filterset_fields = ('id','user' )
    extra_kwargs = {'url': {'lookup_field':'user'}}














# This is a viewset for the Patient model in the Django project using the Django REST Framework.
# The queryset variable specifies the set of objects that this viewset will work with, which in this case
# is all Patient objects in the database.
# The serializer_class variable specifies the serializer that will be used to serialize and deserialize 
# the Patient objects between their Python representation and their JSON representation that will be 
# returned by the API.
# The lookup_field and lookup_url_kwarg variables specify the name of the field to use for the unique 
# identifier of the Patient objects. In this case, it is set to 'user', which means that the URL 
# parameter used to retrieve a specific Patient object will be named user.
# The filterset_fields variable specifies the list of fields that can be used to filter the queryset. 
# In this case, it allows filtering by id and user.
# The extra_kwargs variable allows specifying additional options for the URL configuration. In this case,
#  it sets the lookup_field attribute of the url option to 'user'.