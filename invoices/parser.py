import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

from invoices.models import *


def parseInvoiceHeader(element):
    invoice_header = InvoiceHeaderType()
    for children in element._children:
        if children.tag == 'InvoiceNumber':
            invoice_header.InvoiceNumber = children.text
        elif children.tag == 'InvoiceSeriesCode':
            invoice_header.InvoiceSeriesCode = children.text
        elif children.tag == 'InvoiceDocumentType':
            invoice_header.InvoiceDocumentType = children.text
        elif children.tag == 'InvoiceClass':
            invoice_header.InvoiceClass = children.text
    invoice_header.save()
    return invoice_header


def parseInvoiceIssueData(element):
    pass


def parseTaxesOutputs(element):
    pass


def parseTaxesWithheld(element):
    pass


def parseInvoiceTotals(element):
    pass


def parseItems(element):
    items = []
    item = ItemsType()
    for children in element._children:
        invoice_line = InvoiceLineType()
        for children_line in children.__children:
            if children_line.tag == 'IssuerContractReference':
                invoice_line.IssuerContractReference = children_line.text
            elif children_line.tag == 'IssuerContractDate':
                invoice_line.IssuerContractDate = children_line.text
            elif children_line.tag == 'IssuerTransactionReference':
                invoice_line.IssuerContractReference = children_line.text
            elif children_line.tag == 'IssuerTransactionDate':
                invoice_line.IssuerTransactionDate = children_line.text
            elif children_line.tag == 'ReceiverContractReference':
                invoice_line.ReceiverContractReference = children_line.text


def PaymentDetails(element):
    pass


class Parser(object):
    def __init__(self):
        self.efactura = EFactura()

    def parseFileHeader(self, element):
        file_header = FileHeaderType()
        for children in element._children:
            if children.tag == 'SchemaVersion':
                file_header.SchemaVersion = children.text
            elif children.tag == 'Modality':
                file_header.Modality = children.text
            elif children.tag == 'InvoiceIssuerType':
                file_header.InvoiceIssuerType = children.text
            elif children.tag == 'Batch':
                batch = BatchType()
                for subchildren in children._children:
                    if subchildren.tag == 'BatchIdentifier':
                        batch.BatchIdentifier = subchildren.text
                    elif subchildren.tag == 'InvoicesCount':
                        batch.InvoicesCount = subchildren.text
                    elif subchildren.tag == 'TotalInvoicesAmount':
                        total_invoices_amount = AmountType()
                        for amount_element in subchildren._children:
                            if amount_element.tag == 'TotalAmount':
                                total_invoices_amount.TotalAmount = amount_element.text
                        total_invoices_amount.save()
                        batch.TotalInvoicesAmount = total_invoices_amount
                    elif subchildren.tag == 'TotalOutstandingAmount':
                        total_outstanding_amount = AmountType()
                        for amount_element in subchildren._children:
                            if amount_element.tag == 'TotalAmount':
                                total_outstanding_amount.TotalAmount = amount_element.text
                        total_outstanding_amount.save()
                        batch.TotalOutstandingAmount = total_outstanding_amount
                    elif subchildren.tag == 'TotalExecutableAmount':
                        total_executable_amount = AmountType()
                        for amount_element in subchildren._children:
                            if amount_element.tag == 'TotalAmount':
                                total_executable_amount.TotalAmount = amount_element.text
                        total_executable_amount.save()
                        batch.TotalExecutableAmount = total_executable_amount
                    elif subchildren.tag == 'InvoiceCurrencyCode':
                        batch.InvoiceCurrencyCode = subchildren.text
                batch.save()
                file_header.Batch = batch
        file_header.save()
        self.efactura.FileHeader = file_header

    def parseParties(self, element):
        pass

    def parseInvoices(self, element):
        pass

    def parseFacturaE(self, stringValue):
        try:
            xml_parsed = ET.fromstring(stringValue)
            for children in xml_parsed._children:
                if children.tag == 'FileHeader':
                    self.parseFileHeader(children)
                elif children.tag == 'Parties':
                    self.parseParties(children)
                elif children.tag == 'Invoices':
                    self.parseInvoices(children)
            return True
        except ParseError:
            return False
