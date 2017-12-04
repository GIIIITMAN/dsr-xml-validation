#!/usr/bin/env python

#
# Generated Thu Oct 26 03:53:33 2017 by generateDS.py version 2.28b.
# Python 2.7.9 (default, Jun 29 2016, 13:08:31)  [GCC 4.9.2]
#
# Command line options:
#   ('--silence', '')
#   ('--external-encoding', 'utf-8')
#   ('-o', '../dsr-xml-validation/dss.py')
#   ('-s', '../dsr-xml-validation/dsssubs.py')
#
# Command line arguments:
#   ../dsr-xml-validation/Dealer Service Sale.xsd
#
# Command line:
#   generateDS.py --silence --external-encoding="utf-8" -o "../dsr-xml-validation/dss.py" -s "../dsr-xml-validation/dsssubs.py" ../dsr-xml-validation/Dealer Service Sale.xsd
#
# Current working directory (os.getcwd()):
#   generateDS
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class SERVICE_SALESub(supermod.SERVICE_SALE):
    def __init__(self, SERVICE_SALE_HEADER=None, SERVICE_SALE_DETAIL=None, SERVICE_SALE_CONTROL=None):
        super(SERVICE_SALESub, self).__init__(SERVICE_SALE_HEADER, SERVICE_SALE_DETAIL, SERVICE_SALE_CONTROL, )
supermod.SERVICE_SALE.subclass = SERVICE_SALESub
# end class SERVICE_SALESub


class SERVICE_SALE_DETAILSub(supermod.SERVICE_SALE_DETAIL):
    def __init__(self, MARQUE=None, DEALER_BRANCH_ID=None, CUST_ID=None, CUST_NAME=None, CUST_ADDRESS=None, CUST_SUBURB=None, CUST_STATE=None, CUST_POSTCODE=None, CUST_PHONE=None, CUST_MOBILE=None, CUST_EMAIL=None, VIN=None, VEHICLE_MODEL=None, VEHICLE_DELIVERY_DATE=None, TRANSIENT_VEHICLE_CODE=None, RO_NO=None, SALES_DATE=None, VEHICLE_MILEAGE=None, SERVICE_EVENT=None, SERVICE_TYPE=None, SERVICE_DESCRIPTION=None, SERVICE_ADVISOR_FIRSTNAME=None, SERVICE_ADVISOR_LASTNAME=None, SERVICE_ADVISOR_BIRTHDATE=None, SERVICE_ADVISOR_STAFFCODE=None, PURCHASES_TO_DATE=None, LAB_HOURS_AVAILABLE=None, LAB_HOURS_CLOCKED_R=None, LAB_HOURS_CLOCKED_W=None, LAB_HOURS_CLOCKED_I=None, LAB_HOURS_SOLD_R=None, LAB_HOURS_SOLD_W=None, LAB_HOURS_SOLD_I=None, LAB_VALUE_SOLD_R=None, LAB_VALUE_SOLD_W=None, LAB_VALUE_SOLD_I=None, SUBLET_COUNT_R=None, SUBLET_COUNT_W=None, SUBLET_COUNT_I=None, SUBLET_VALUE_R=None, SUBLET_VALUE_W=None, SUBLET_VALUE_I=None, JOB_COUNT_R=None, JOB_COUNT_W=None, JOB_COUNT_I=None, PART_UNITS_R=None, PART_UNITS_W=None, PART_UNITS_I=None, PART_VALUE_R=None, PART_VALUE_W=None, PART_VALUE_I=None, CONSUMABLES_VALUE=None, OTHER_CHARGES=None, INVOICE_VALUE=None, TOTAL_JOB_COUNT=None, JOB=None):
        super(SERVICE_SALE_DETAILSub, self).__init__(MARQUE, DEALER_BRANCH_ID, CUST_ID, CUST_NAME, CUST_ADDRESS, CUST_SUBURB, CUST_STATE, CUST_POSTCODE, CUST_PHONE, CUST_MOBILE, CUST_EMAIL, VIN, VEHICLE_MODEL, VEHICLE_DELIVERY_DATE, TRANSIENT_VEHICLE_CODE, RO_NO, SALES_DATE, VEHICLE_MILEAGE, SERVICE_EVENT, SERVICE_TYPE, SERVICE_DESCRIPTION, SERVICE_ADVISOR_FIRSTNAME, SERVICE_ADVISOR_LASTNAME, SERVICE_ADVISOR_BIRTHDATE, SERVICE_ADVISOR_STAFFCODE, PURCHASES_TO_DATE, LAB_HOURS_AVAILABLE, LAB_HOURS_CLOCKED_R, LAB_HOURS_CLOCKED_W, LAB_HOURS_CLOCKED_I, LAB_HOURS_SOLD_R, LAB_HOURS_SOLD_W, LAB_HOURS_SOLD_I, LAB_VALUE_SOLD_R, LAB_VALUE_SOLD_W, LAB_VALUE_SOLD_I, SUBLET_COUNT_R, SUBLET_COUNT_W, SUBLET_COUNT_I, SUBLET_VALUE_R, SUBLET_VALUE_W, SUBLET_VALUE_I, JOB_COUNT_R, JOB_COUNT_W, JOB_COUNT_I, PART_UNITS_R, PART_UNITS_W, PART_UNITS_I, PART_VALUE_R, PART_VALUE_W, PART_VALUE_I, CONSUMABLES_VALUE, OTHER_CHARGES, INVOICE_VALUE, TOTAL_JOB_COUNT, JOB, )
supermod.SERVICE_SALE_DETAIL.subclass = SERVICE_SALE_DETAILSub
# end class SERVICE_SALE_DETAILSub


class SERVICE_SALE_CONTROLSub(supermod.SERVICE_SALE_CONTROL):
    def __init__(self, TOTAL_RECORDS=None, TOTAL_INVOICE_VALUE=None):
        super(SERVICE_SALE_CONTROLSub, self).__init__(TOTAL_RECORDS, TOTAL_INVOICE_VALUE, )
supermod.SERVICE_SALE_CONTROL.subclass = SERVICE_SALE_CONTROLSub
# end class SERVICE_SALE_CONTROLSub


class SERVICE_SALE_HEADERSub(supermod.SERVICE_SALE_HEADER):
    def __init__(self, SESSION_ID=None, DEALER_ID=None, DATA_DATE=None, DEALER_SYSTEM=None, EXTRACTION_DATE=None):
        super(SERVICE_SALE_HEADERSub, self).__init__(SESSION_ID, DEALER_ID, DATA_DATE, DEALER_SYSTEM, EXTRACTION_DATE, )
supermod.SERVICE_SALE_HEADER.subclass = SERVICE_SALE_HEADERSub
# end class SERVICE_SALE_HEADERSub


class JOBSub(supermod.JOB):
    def __init__(self, LINE_NO=None, JOB_TYPE=None, SERVICE_TYPE=None, SERVICE_DESCRIPTION=None):
        super(JOBSub, self).__init__(LINE_NO, JOB_TYPE, SERVICE_TYPE, SERVICE_DESCRIPTION, )
supermod.JOB.subclass = JOBSub
# end class JOBSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xsd_double'
        rootClass = supermod.xsd_double
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='',
##             pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xsd_double'
        rootClass = supermod.xsd_double
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
##     if not silence:
##         content = etree_.tostring(
##             rootElement, pretty_print=True,
##             xml_declaration=True, encoding="utf-8")
##         sys.stdout.write(content)
##         sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xsd_double'
        rootClass = supermod.xsd_double
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xsd_double'
        rootClass = supermod.xsd_double
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('#from ??? import *\n\n')
##         sys.stdout.write('import ??? as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
