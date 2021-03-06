#!/usr/bin/env python

#
# Generated Thu Oct 12 01:57:52 2017 by generateDS.py version 2.28b.
# Python 2.7.9 (default, Jun 29 2016, 13:08:31)  [GCC 4.9.2]
#
# Command line options:
#   ('--silence', '')
#   ('--external-encoding', 'utf-8')
#   ('-o', '../dsr-xml-validation/dsoh.py')
#   ('-s', '../dsr-xml-validation/dsohsubs.py')
#
# Command line arguments:
#   ../dsr-xml-validation/Dealer Stock On Hand.xsd
#
# Command line:
#   generateDS.py --silence --external-encoding="utf-8" -o "../dsr-xml-validation/dsoh.py" -s "../dsr-xml-validation/dsohsubs.py" ../dsr-xml-validation/Dealer Stock On Hand.xsd
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


class PART_STOCKSub(supermod.PART_STOCK):
    def __init__(self, PART_STOCK_HEADER=None, PART_STOCK_DETAIL=None, PART_STOCK_CONTROL=None):
        super(PART_STOCKSub, self).__init__(PART_STOCK_HEADER, PART_STOCK_DETAIL, PART_STOCK_CONTROL, )
supermod.PART_STOCK.subclass = PART_STOCKSub
# end class PART_STOCKSub


class PART_STOCK_DETAILSub(supermod.PART_STOCK_DETAIL):
    def __init__(self, SUPP_CODE=None, DEALER_BRANCH_ID=None, PART_NO=None, QTY=None, UNIT_RRP=None, UNIT_AVG_COSTS=None):
        super(PART_STOCK_DETAILSub, self).__init__(SUPP_CODE, DEALER_BRANCH_ID, PART_NO, QTY, UNIT_RRP, UNIT_AVG_COSTS, )
supermod.PART_STOCK_DETAIL.subclass = PART_STOCK_DETAILSub
# end class PART_STOCK_DETAILSub


class PART_STOCK_HEADERSub(supermod.PART_STOCK_HEADER):
    def __init__(self, SESSION_ID=None, DEALER_ID=None, DATA_DATE=None, DEALER_SYSTEM=None, EXTRACTION_DATE=None):
        super(PART_STOCK_HEADERSub, self).__init__(SESSION_ID, DEALER_ID, DATA_DATE, DEALER_SYSTEM, EXTRACTION_DATE, )
supermod.PART_STOCK_HEADER.subclass = PART_STOCK_HEADERSub
# end class PART_STOCK_HEADERSub


class PART_STOCK_CONTROLSub(supermod.PART_STOCK_CONTROL):
    def __init__(self, TOTAL_RECORDS=None, TOTAL_QTY=None, TOTAL_SOH_VALUE=None):
        super(PART_STOCK_CONTROLSub, self).__init__(TOTAL_RECORDS, TOTAL_QTY, TOTAL_SOH_VALUE, )
supermod.PART_STOCK_CONTROL.subclass = PART_STOCK_CONTROLSub
# end class PART_STOCK_CONTROLSub


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
