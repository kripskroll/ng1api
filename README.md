# ng1api
Python Wrapper for nGeniusONE RESTFul API

# Usage / Example :
from ng1_api import NG1APIObject

# Create ng1 instance to manipulate REST API
ng1 = NG1APIObject("localhost", "8080", "USER", "PASS")from ng1_api import NG1APIObject

# Open Session
session = ng1.session.opensession()

# Manage Applications. Create object applications 
apps = ng1.applications

  # Now delete an application
  apps.delApplication("MyApp")
  
  # Create an application
  apps.addApplications("myFileDefnition.xml")
