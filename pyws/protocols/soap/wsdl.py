from lxml import etree as et

import xsd

from utils import * #@UnusedWildImport


class WsdlGenerator(object):

    def __init__(self, server, service_name, tns_prefix, encoding):

        self.server = server
        self.service_name = service_name
        self.tns_prefix = tns_prefix
        self.encoding = encoding

        self.build_wsdl()

    def _add_part(self, element, function, arg_name, arg_type):
        part_type = xsd.TypeFactory(arg_type, self.types_ns, self.namespaces)
        part_type.get_types(self.types)
        et.SubElement(element, wsdl_name('part'),
            name=arg_name, type=qname(*(part_type.name + (self.namespaces, ))))

    def _add_functions(self):

        for function in self.server.get_functions():

            input_name = function.name
            input = et.SubElement(self.definitions,
                wsdl_name('message'), name=input_name)

            for arg in function.args.fields:
                self._add_part(input, function, arg.name, arg.type)

            output_name = function.name + '_response'
            output = et.SubElement(self.definitions,
                wsdl_name('message'), name=output_name)

            self._add_part(output, function, 'result', function.return_type)

            operation = et.SubElement(self.port_type,
                wsdl_name('operation'), name=function.name)
            et.SubElement(operation, wsdl_name('input'),
                name=input_name, message='tns:%s' % input_name)
            et.SubElement(operation, wsdl_name('output'),
                name=output_name, message='tns:%s' % output_name)

            operation = et.SubElement(self.binding,
                wsdl_name('operation'), name=function.name)
            et.SubElement(operation, soap_name('operation'),
                soapAction=self.tns_prefix + function.name)
            input = et.SubElement(operation, wsdl_name('input'))
            et.SubElement(input, soap_name('body'),
                use='literal', namespace=self.tns_prefix)
            output = et.SubElement(operation, wsdl_name('output'))
            et.SubElement(output, soap_name('body'),
                use='literal', namespace=self.tns_prefix)

    def build_wsdl(self):

        self.wsdl = None

        tns = self.tns_prefix
        self.types_ns = tns + 'types/'

        self.namespaces = {
            'tns': tns,
            'xsd': XSD_NS,
            'soap': SOAP_NS,
            'types': self.types_ns,
        }

        self.types = {}

        self.definitions = et.Element(wsdl_name('definitions'),
            name=self.service_name, targetNamespace=tns, nsmap=self.namespaces)

        types = et.SubElement(self.definitions, wsdl_name('types'))
        self.schema_types = et.SubElement(types,
            xsd_name('schema'), targetNamespace=self.types_ns)

        port_type_name = '%sPortType' % self.service_name
        self.port_type = et.Element(wsdl_name('portType'), name=port_type_name)

        binding_name = '%sBinding' % self.service_name
        self.binding = et.Element(wsdl_name('binding'),
            name=binding_name, type='tns:%s' % port_type_name)
        et.SubElement(self.binding, soap_name('binding'),
            style='rpc', transport='http://schemas.xmlsoap.org/soap/http')

        self.service = et.Element(
            wsdl_name('service'), name='%sService' % self.service_name)
        self.port = et.SubElement(self.service, wsdl_name('port'),
            binding='tns:%s' % binding_name, name='%sPort' % self.service_name)
        et.SubElement(self.port,
            soap_name('address'), location=self.server.location)

        self._add_functions()

        for type in self.types.itervalues():
            self.schema_types.append(type)

        self.definitions.append(self.port_type)
        self.definitions.append(self.binding)
        self.definitions.append(self.service)

        self.wsdl = et.tostring(self.definitions,
            encoding=self.encoding, pretty_print=True, xml_declaration=True)

    def get_wsdl(self):
        return self.wsdl