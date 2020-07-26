#!/usr/bin/env/python3
import nfc

import binascii
import logging
import os

class CardReader(object):
    def on_connect(self, tag):
        self.idm = binascii.hexlify(tag._nfcid)
    
    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr{'on-connect':self.on_connect})
        finally:
            clf.close()

if __name__ == '__main__':
    card_reader = CardReader()

    while True:
        card_reader.read_id()