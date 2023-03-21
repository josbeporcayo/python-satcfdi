import base64

import requests
from lxml.etree import Element
from lxml import etree
from requests.auth import HTTPBasicAuth

from . import PAC, Accept, Document, CancelReason, CancelationAcknowledgment, Environment, TaxpayerStatus, AcceptRejectAcknowledgment
from .. import ScalarMap
from .. import __version__, Signer
from ..cfdi import CFDI
from ..create.cancela import cancelacionretencion, cancelacion
from ..create.cancela.aceptacionrechazo import SolicitudAceptacionRechazo
from ..transform.helpers import simple_element


class RequestTransaction(ScalarMap):
    """

    :param requestor:
    :param transaction:
    :param country:
    :param entity:
    :param user:
    :param user_name:
    :param data1:
    :param data2:
    :param data3:
    """

    tag = '{http://www.fact.com.mx/schema/ws}RequestTransaction'

    def __init__(
            self,
            requestor: str = None,
            transaction: str = None,
            country: str = None,
            entity: str = None,
            user: str = None,
            user_name: str = None,
            data1: str = None,
            data2: str = None,
            data3: str = None,
    ):
        super().__init__({
            'Requestor': requestor,
            'Transaction': transaction,
            'Country': country,
            'Entity': entity,
            'User': user,
            'UserName': user_name,
            'Data1': data1,
            'Data2': data2,
            'Data3': data3,
        })


def request_transaction(data):
    self = Element('{%s}%s' % ('http://www.fact.com.mx/schema/ws', 'RequestTransaction'), nsmap={'ws': 'http://www.fact.com.mx/schema/ws'})
    el = data.get('Requestor')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}Requestor', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('Transaction')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}Transaction', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('Country')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}Country', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('Entity')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}Entity', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('User')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}User', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('UserName')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}UserName', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('Data1')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}Data1', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('Data2')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}Data2', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    el = data.get('Data3')
    self.append(simple_element('{http://www.fact.com.mx/schema/ws}Data3', nsmap={'ws': 'http://www.fact.com.mx/schema/ws'}, text=el))
    return self


def soap_envelope(payload):
    self = Element('{%s}%s' % ('http://schemas.xmlsoap.org/soap/envelope/', 'Envelope'), nsmap={'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'})
    self.append(etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Header', nsmap={'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'}))
    el = etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Body', nsmap={'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'})
    el.append(payload)
    self.append(el)
    return self


class MYSuite(PAC):
    """
    PAC de facturacion MYSuite

    Documentacion: https://soporte.mysuitemex.com/portal/es/kb/soporte-especializado
    """
    RFC = "MSE090205D9A"

    def __init__(self, user: str, password: str, contrato: str, environment=Environment.PRODUCTION):
        super().__init__(environment=environment)
        self.auth = HTTPBasicAuth(user, password)
        self.contrato = contrato

    def issue(self, cfdi: CFDI, accept: Accept = Accept.XML) -> Document:
        raise NotImplementedError()

    def stamp(self, cfdi: CFDI, accept: Accept = Accept.XML) -> Document:
        raw_cfdi = base64.b64encode(cfdi.xml_bytes()).decode()

        xml = soap_envelope(
            request_transaction(
                data=RequestTransaction(
                    requestor="0c320b03-d4f1-47bc-9fb4-77995f9bf33e",
                    transaction="TIMBRAR",
                    country="MX",
                    entity="JES900109Q90",
                    user="0c320b03-d4f1-47bc-9fb4-77995f9bf33e",
                    user_name="MX.JES900109Q90.Juan",
                    data1=raw_cfdi,
                    data2="",
                    data3=""
                )
            )
        )
        xml = etree.tostring(xml, xml_declaration=False, encoding="UTF-8", pretty_print=True)
        print(xml.decode())

        match self.environment:
            case Environment.PRODUCTION:
                host = "https://www.mysuitecfdi.com"
            case Environment.TEST:
                host = "https://www.mysuitetest.com"
            case _:
                raise NotImplementedError("Not Supported CFDI")

        r = requests.post(
            url=f"{host}/mx.com.fact.wsfront/FactWSFront.asmx",
            headers={
                "User-Agent": __version__.__user_agent__,
                "Content-Type": "text/xml; charset=utf-8",
                "SOAPAction": "http://www.fact.com.mx/schema/ws/RequestTransaction"
            },
            data=xml
        )
        print(r.status_code)
        print(r.text)

        return Document(
            document_id="1234",
            xml=b"aaa" if accept & Accept.XML else None,
            pdf=b"bbb" if accept & Accept.PDF else None
        )

    def cancel(self, cfdi: CFDI, reason: CancelReason, substitution_id: str = None, signer: Signer = None) -> CancelationAcknowledgment:
        raise NotImplementedError()

    def recover(self, document_id: str, accept: Accept = Accept.XML) -> Document:
        raise NotImplementedError()

    def rfc_valid(self, rfc: str | list[str]) -> bool | list[bool]:
        raise NotImplementedError()

    def status(self, cfdi: CFDI) -> dict:
        raise NotImplementedError()

    def validate(self, cfdi: CFDI):
        raise NotImplementedError()

    def cancel_comprobante(self, cancelation: cancelacion.Cancelacion) -> CancelationAcknowledgment:
        raise NotImplementedError()

    def cancel_retencion(self, cancelation: cancelacionretencion.Cancelacion) -> CancelationAcknowledgment:
        raise NotImplementedError()

    def accept_reject(self, request: SolicitudAceptacionRechazo) -> AcceptRejectAcknowledgment:
        raise NotImplementedError()

    def pending(self, rfc: str) -> list[str]:
        raise NotImplementedError()

    def list_69b(self, rfc: str) -> TaxpayerStatus | None:
        raise NotImplementedError()
