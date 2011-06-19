WSDL_NS     = 'http://schemas.xmlsoap.org/wsdl/'
SOAP_NS     = 'http://schemas.xmlsoap.org/wsdl/soap/'
SOAP_ENV_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
XSD_NS      = 'http://www.w3.org/2001/XMLSchema'

def qname(name, ns=None, namespaces=None):
    if not ns:
        return name
    if not namespaces:
        return '{%s}%s' % (ns, name)
    prefix = filter(lambda x: x[1] == ns, namespaces.iteritems())[0][0]
    return '%s:%s' % (prefix, name)

def wsdl_name(name):
    return qname(name, WSDL_NS)

def soap_name(name):
    return qname(name, SOAP_NS)

def soap_env_name(name):
    return qname(name, SOAP_ENV_NS)

def xsd_name(name):
    return qname(name, XSD_NS)

def types_ns(prefix):
    return prefix + 'types/'