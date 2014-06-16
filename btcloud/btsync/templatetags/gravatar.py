### gravatar.py ###############
### place inside a 'templatetags' directory inside the top level of a Django app (not project, must be inside an app)
### at the top of your page template include this:
### {% load gravatar %}
### and to use the url do this:
### <img src="{% gravatar_url 'someone@somewhere.com' %}">
### or
### <img src="{% gravatar_url sometemplatevariable %}">
### just make sure to update the "default" image path below
 
from django import template
import urllib, hashlib, re
 
register = template.Library()
 
class GravatarUrlNode(template.Node):
    def __init__(self, email, var_name=''):
        self.email = template.Variable(email)
        self.var_name = var_name
 
    def render(self, context):
        try:
            email = self.email.resolve(context)
        except template.VariableDoesNotExist:
            return ''
 
        default = "http://example.com/static/images/defaultavatar.jpg"
        size = 40
 
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
        
        if self.var_name:
            context[self.var_name] = gravatar_url
            return ''
        return gravatar_url
 
@register.tag
def gravatar_url(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
 
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    email, var_name = m.groups()
    
    return GravatarUrlNode(email, var_name)