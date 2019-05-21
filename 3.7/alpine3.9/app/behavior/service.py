from lumavate_service_util import RestBehavior
from flask import g, jsonify

class ServiceBehavior(RestBehavior):
  def __init__(self):
    super().__init__(None)

  def get_properties(self):
    return []

  def hello_world(self):
    return jsonify("Hello")
