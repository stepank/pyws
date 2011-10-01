from lxml import etree as et

from pyws.functions import args
from pyws.protocols.soap import xsd
from pyws.protocols.soap.utils import *


class WsdlGenerator(object):

    def __init__(self,
            server, context,
            service_name, tns, location, headers_schema, encoding):

        self.server = server
        self.context = context
        self.service_name = service_name
        self.tns = tns
        self.location = location
        self.headers_schema = headers_schema
        self.encoding = encoding

        self.build_wsdl()

    def _add_part(self, element, arg_name, arg_type, use_element=False):
        part_type = xsd.TypeFactory(arg_type, self.types_ns, self.namespaces)
        part_type.get_types(self.types, use_element=use_element)
        kw = use_element and 'element' or 'type'
        kwargs = {kw: qname(*(part_type.name + (self.namespaces, )))}
        et.SubElement(element, wsdl_name('part'), name=arg_name, **kwargs)

    def _add_functions(self):

        if self.headers_schema:
            input = et.SubElement(
                self.definitions, wsdl_name('message'), name='headers')
            self._add_part(
                input, 'headers', self.headers_schema, use_element=True)

        input = et.SubElement(
            self.definitions, wsdl_name('message'), name='error')
        self._add_part(input, 'fault', args.DictOf('Error'), use_element=True)

        for function in self.server.get_functions(self.context):

            input_name = function.name
            input = et.SubElement(
                self.definitions, wsdl_name('message'), name=input_name)

            for arg in function.args.fields:
                self._add_part(input, arg.name, arg.type)

            output_name = function.name + '_response'
            output = et.SubElement(
                self.definitions, wsdl_name('message'), name=output_name)

            self._add_part(output, 'result', function.return_type)

            operation = et.SubElement(
                self.port_type, wsdl_name('operation'), name=function.name)
            et.SubElement(
                operation, wsdl_name('input'),
                name=input_name, message='tns:%s' % input_name)
            et.SubElement(
                operation, wsdl_name('output'),
                name=output_name, message='tns:%s' % output_name)
            et.SubElement(
                operation, wsdl_name('fault'),
                name='error', message='tns:error')

            operation = et.SubElement(
                self.binding, wsdl_name('operation'), name=function.name)
            et.SubElement(
                operation, soap_name('operation'),
                soapAction=self.tns + function.name)
            input = et.SubElement(operation, wsdl_name('input'))
            if function.needs_context:
                et.SubElement(
                    input, soap_name('header'),
                    message='tns:headers', part='headers', use='literal')
            et.SubElement(
                input, soap_name('body'), use='literal', namespace=self.tns)
            output = et.SubElement(operation, wsdl_name('output'))
            et.SubElement(
                output, soap_name('body'),
                use='literal', namespace=self.tns)
            fault = et.SubElement(
                operation, wsdl_name('fault'), name='error')
            et.SubElement(
                fault, soap_name('fault'), name='error', use='literal')

    def build_wsdl(self):

        self.wsdl = None

        tns = self.tns
        #noinspection PyUnboundLocalVariable
        self.types_ns = types_ns(tns)

        self.namespaces = {
            'tns': tns,
            'xsd': XSD_NS,
            'soap': SOAP_NS,
            'types': self.types_ns,
        }

        self.types = {}

        self.definitions = et.Element(
            wsdl_name('definitions'), name=self.service_name,
            targetNamespace=tns, nsmap=self.namespaces)

        types = et.SubElement(self.definitions, wsdl_name('types'))
        self.schema_types = et.SubElement(
            types, xsd_name('schema'), targetNamespace=self.types_ns)

        self.schema_base = et.SubElement(
            types, xsd_name('schema'), targetNamespace=self.tns)
        et.SubElement(
            self.schema_base, xsd_name('import'), namespace=self.types_ns)

        port_type_name = '%sPortType' % self.service_name
        self.port_type = et.Element(wsdl_name('portType'), name=port_type_name)

        binding_name = '%sBinding' % self.service_name
        self.binding = et.Element(
            wsdl_name('binding'),
            name=binding_name, type='tns:%s' % port_type_name)
        et.SubElement(
            self.binding, soap_name('binding'),
            style='rpc', transport='http://schemas.xmlsoap.org/soap/http')

        self.service = et.Element(
            wsdl_name('service'), name='%sService' % self.service_name)
        self.port = et.SubElement(
            self.service, wsdl_name('port'),
            binding='tns:%s' % binding_name, name='%sPort' % self.service_name)
        et.SubElement(self.port, soap_name('address'), location=self.location)

        self._add_functions()

        for type in self.types.itervalues():
            self.schema_types.append(type)

        self.definitions.append(self.port_type)
        self.definitions.append(self.binding)
        self.definitions.append(self.service)

        self.wsdl = et.tostring(
            self.definitions, encoding=self.encoding,
            pretty_print=True, xml_declaration=True)

    def get_wsdl(self):
        return self.wsdl
