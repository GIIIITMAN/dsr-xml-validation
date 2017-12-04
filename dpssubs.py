#!/usr/bin/env python

#
# Generated Thu Oct 12 01:57:30 2017 by generateDS.py version 2.28b.
# Python 2.7.9 (default, Jun 29 2016, 13:08:31)  [GCC 4.9.2]
#
# Command line options:
#   ('--silence', '')
#   ('--external-encoding', 'utf-8')
#   ('-o', '../dsr-xml-validation/dps.py')
#   ('-s', '../dsr-xml-validation/dpssubs.py')
#
# Command line arguments:
#   ../dsr-xml-validation/Dealer Part Sale.xsd
#
# Command line:
#   generateDS.py --silence --external-encoding="utf-8" -o "../dsr-xml-validation/dps.py" -s "../dsr-xml-validation/dpssubs.py" ../dsr-xml-validation/Dealer Part Sale.xsd
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


class PART_SALESub(supermod.PART_SALE):
    def __init__(self, PART_SALE_HEADER=None, PART_SALE_DETAIL=None, PART_SALE_CONTROL=None):
        super(PART_SALESub, self).__init__(PART_SALE_HEADER, PART_SALE_DETAIL, PART_SALE_CONTROL, )
supermod.PART_SALE.subclass = PART_SALESub
# end class PART_SALESub


class PART_SALE_CONTROLSub(supermod.PART_SALE_CONTROL):
    def __init__(self, TOTAL_RECORDS=None, TOTAL_QTY=None, TOTAL_SALES_VALUE=None):
        super(PART_SALE_CONTROLSub, self).__init__(TOTAL_RECORDS, TOTAL_QTY, TOTAL_SALES_VALUE, )
supermod.PART_SALE_CONTROL.subclass = PART_SALE_CONTROLSub
# end class PART_SALE_CONTROLSub


class PART_SALE_DETAILSub(supermod.PART_SALE_DETAIL):
    def __init__(self, DEALER_BRANCH_ID=None, PART_NO=None, PART_DESCRIPTION=None, SUPP_CODE=None, SUPP_DESCRIPTION=None, TMC_PART_NO=None, CUST_CAT=None, CUST_ID=None, CUST_NAME=None, CUST_ADDRESS=None, CUST_SUBURB=None, CUST_STATE=None, CUST_POSTCODE=None, CUST_PHONE=None, INVOICE_NO=None, RO_NO=None, QTY=None, UNIT_RRP=None, UNIT_AVG_COSTS=None, ACT_SALES_PRICE=None):
        super(PART_SALE_DETAILSub, self).__init__(DEALER_BRANCH_ID, PART_NO, PART_DESCRIPTION, SUPP_CODE, SUPP_DESCRIPTION, TMC_PART_NO, CUST_CAT, CUST_ID, CUST_NAME, CUST_ADDRESS, CUST_SUBURB, CUST_STATE, CUST_POSTCODE, CUST_PHONE, INVOICE_NO, RO_NO, QTY, UNIT_RRP, UNIT_AVG_COSTS, ACT_SALES_PRICE, )
supermod.PART_SALE_DETAIL.subclass = PART_SALE_DETAILSub
# end class PART_SALE_DETAILSub


class PART_SALE_HEADERSub(supermod.PART_SALE_HEADER):
    def __init__(self, SESSION_ID=None, DEALER_ID=None, DATA_DATE=None, DEALER_SYSTEM=None, EXTRACTION_DATE=None):
        super(PART_SALE_HEADERSub, self).__init__(SESSION_ID, DEALER_ID, DATA_DATE, DEALER_SYSTEM, EXTRACTION_DATE, )
supermod.PART_SALE_HEADER.subclass = PART_SALE_HEADERSub
# end class PART_SALE_HEADERSub


class SALES_DATESub(supermod.SALES_DATE):
    def __init__(self):
        super(SALES_DATESub, self).__init__()
supermod.SALES_DATE.subclass = SALES_DATESub
# end class SALES_DATESub


class TMC_PART_NOSub(supermod.TMC_PART_NO):
    def __init__(self):
        super(TMC_PART_NOSub, self).__init__()
supermod.TMC_PART_NO.subclass = TMC_PART_NOSub
# end class TMC_PART_NOSub


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
