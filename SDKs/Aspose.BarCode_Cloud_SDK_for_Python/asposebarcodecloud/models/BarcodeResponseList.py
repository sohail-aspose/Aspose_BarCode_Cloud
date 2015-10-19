#!/usr/bin/env python

class BarcodeResponseList(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'Code': 'str',
            'Status': 'str',
            'Barcodes' : 'list[Barcode]'

        }

        self.attributeMap = {
            'Code': 'Code','Status': 'Status', 'Barcodes':'Barcodes'}       

        self.Code = None # str
        self.Status = None # str
        self.Barcodes = None
        
