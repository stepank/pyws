import re

from StringIO import StringIO

from lxml import etree as et

from pyws.errors import BadRequest
from pyws.response import Response

from base import Protocol

SOAP_ENV_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
TAG_NAME_RE = re.compile('{(.*?)}(.*)')

def get_element_name(el):
    name = el.tag
    mo = TAG_NAME_RE.search(name)
    if mo:
      return mo.group(1), mo.group(2)
    return None, name

def xml2obj(xml):
    children = xml.getchildren()
    if not children:
        return xml.text
    result = {}
    for child in children:
        name = get_element_name(child)[1]
        obj = xml2obj(child)
        if name not in result:
            result[name] = obj
        else:
            if not isinstance(result[name], list):
                result[name] = [result[name]]
            result[name].append(obj)
    return result

def obj2xml(name, obj, namespace=None):
    if isinstance(obj, (list, tuple)):
        return [obj2xml(name, v) for v in obj]
    kwargs = namespace and {'namespace': namespace} or {}
    el = et.Element(name, **kwargs)
    if not isinstance(obj, dict):
        el.text = str(obj)
    else:
        for k, v in obj.iteritems():
            children = obj2xml(k, v)
            if not isinstance(children, (tuple, list)):
                el.append(children)
            else:
                for child in children:
                    el.append(child)
    return el


class SoapProtocol(Protocol):

    namespaces = {'se': SOAP_ENV_NS}
    encoding = 'utf-8'

    def get_function(self, request):

        if request.tail == 'wsdl':
            return self.get_wsdl

        xml = et.parse(StringIO(request.text.encode(self.encoding)))
        env = xml.xpath('/se:Envelope', namespaces=self.namespaces)

        if len(env) != 1:
            raise BadRequest('No {%s}Envelope element.' % SOAP_ENV_NS)
        env = env[0]

        body = env.xpath('./se:Body', namespaces=self.namespaces)

        if len(body) != 1:
            raise BadRequest('No {%s}Body element.' % SOAP_ENV_NS)
        body = body[0]

        func = body.getchildren()
        if len(env) != 1:
            raise BadRequest('{%s}Envelope element has more than one child element.' % SOAP_ENV_NS)
        func = func[0]

        func_name = get_element_name(func)[1]
        if func_name.endswith('_request'):
            func_name = func_name[:-8]

        params = xml2obj(func)

        return func_name, params

    def get_response(self, name, result):

        result = obj2xml(name + '_response', {'result': result}, namespace='hello')

        body = et.Element('{%s}Body' % SOAP_ENV_NS, nsmap=self.namespaces)
        body.append(result)

        xml = et.Element('{%s}Envelope' % SOAP_ENV_NS, nsmap=self.namespaces)
        xml.append(body)

        return Response(et.tostring(xml, encoding=self.encoding, pretty_print=True, xml_declaration=True))

    def get_error_response(self, error):

        error = self.get_error(error)

        fault = et.Element('{%s}Fault' % SOAP_ENV_NS, nsmap=self.namespaces)
        faultcode = et.SubElement(fault, 'faultcode')
        faultcode.text = 'se:%s' % error['type']
        faultstring = et.SubElement(fault, 'faultstring')
        faultstring.text = error['message']
        fault.append(obj2xml('detail', error))

        body = et.Element('{%s}Body' % SOAP_ENV_NS, nsmap=self.namespaces)
        body.append(fault)

        xml = et.Element('{%s}Envelope' % SOAP_ENV_NS, nsmap=self.namespaces)
        xml.append(body)

        return Response(et.tostring(xml, encoding=self.encoding, pretty_print=True, xml_declaration=True))

    def get_wsdl(self, request):
        return Response('wsdl')
