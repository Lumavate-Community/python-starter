from lumavate_service_util import lumavate_route, SecurityType, RequestType
from flask import render_template, g
from behavior import ServiceBehavior

# Renders defualt Lumavate service icon
@lumavate_route('/', ['GET'], RequestType.page, [SecurityType.jwt])
def root():
  return render_template('home.html', logo='/{}/{}/discover/icons/microservice.png'.format(g.integration_cloud, g.widget_type))

@lumavate_route('/discover/properties', ['GET'], RequestType.system, [SecurityType.jwt])
def properties():
  return ServiceBehavior().get_properties()

@lumavate_route('/hello-world', ['GET'], RequestType.api, [SecurityType.jwt])
def read():
  return ServiceBehavior().hello_world()
