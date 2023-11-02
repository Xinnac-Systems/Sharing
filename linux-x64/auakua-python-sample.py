import sys
import xml.etree.ElementTree as ET

from pythonnet import load
load("coreclr", runtime_config="runtimeconfig.json")

from datetime import datetime
import clr
import os
clr.AddReference('Syntizen.Aadhaar.AuaKua')

from Syntizen.Aadhaar.AuaKua import Authentication
from Syntizen.Aadhaar.AuaKua import AUAKUAParameters
from Syntizen.Aadhaar.AuaKua import AUAKUAResponse
from Syntizen.Aadhaar.AuaKua import Environment

import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from enum import Enum

import enum
global SettingsFile 
SettingsFile= "C:\\Projects\\Python\\aua-kua-python\\auakua-python-middleware\\auakuasettings.json"

class CallSDK:
    """
    This class is used to call the SDK for Aadhaar authentication.
    It includes methods for KYC, OTP generation, and demographic authentication.
    """
    def __init__(self):
        self.LicKey = "MBDXG-EFSAY-RUTJO-CCHIU"
        self.environment = Environment.PreProduction

    def do_kyc(self, aadhaarno):
        errCode = "1"
        errInfo = "NA"
        dc = ""
        mi = ""
        mc = ""
        dpId = ""
        rdsId = ""
        rdsVer = ""
        SKEY = ""
        Data = ""
        Hmac = ""
        ci = ""
        SrnoValue = ""
        objauth = Authentication(SettingsFile)
        resp = AUAKUAResponse()
        parms = AUAKUAParameters()
        
        objauth.SystemEnvironment = self.environment
        parms.LAT = "17.494568"
        parms.LONG = "78.392056"
        parms.DEVMACID = "11:22:33:44:55"
        parms.DEVID = "efsgrgrd"
        parms.SRNO = "2040444"
        parms.CONSENT = "Y"
        parms.SHRC = "Y"
        parms.LANG = "N"
        parms.PFR = "N"
        parms.VER = "2.5"
        parms.SERTYPE = "04"
        parms.ENV = "2"
        parms.AADHAARID = aadhaarno
        parms.SLK = self.LicKey
        parms.RRN = datetime.now().strftime("%Y%m%d%H%M%S%f")
        # xmldoc = ET.parse('PIDXML.xml')
        # root = xmldoc.getroot()
        # print("1234",root)
        # print(root.itertext)
        # PIDXML = "".join(root.itertext())
        # with open("PIDXML.xml", "r") as file:
        #     xml_content = file.read()

        # if len(xml_content) > 0:
        #     tree = ET.parse("PIDXML.xml")
        #     PIDResponseXML = tree.getroot()

        #     # Find the 'Resp' element and extract 'errInfo' and 'errCode' attributes
        #     resp_element = PIDResponseXML.find("Resp")
        #     if resp_element is not None:
        #         errInfo = resp_element.get("errInfo")
        #         errCode = resp_element.get("errCode")
        #     if errCode == "0":  # Success


        try:
            # pid_xml_path = os.path.join(os.environ['ProgramData'], 'PIDXML.xml')
            # with open(pid_xml_path, 'r') as pid_file:
            #     PIDXML = pid_file.read()

            # if PIDXML:
            #     PIDResponseXML = ET.fromstring(PIDXML)
            #     errInfo = PIDResponseXML.find('.//Resp').get('errInfo')
            #     errCode = PIDResponseXML.find('.//Resp').get('errCode')
            #     if errCode == "0":  # Success

            xmldoc = ET.parse('PIDXML.xml')
            root = xmldoc.getroot()
            print("1234",root)
            print(root.itertext)
            PIDXML = "".join(root.itertext())
            with open("PIDXML.xml", "r") as file:
                xml_content = file.read()

            if len(xml_content) > 0:
                tree = ET.parse("PIDXML.xml")
                PIDResponseXML = tree.getroot()

                # Find the 'Resp' element and extract 'errInfo' and 'errCode' attributes
                resp_element = PIDResponseXML.find("Resp")
                if resp_element is not None:
                    errInfo = resp_element.get("errInfo")
                    errCode = resp_element.get("errCode")
                if errCode == "0":  # Success
                    XmlDeviceInfoNode = PIDResponseXML.find('.//DeviceInfo')
                    rdsVer = XmlDeviceInfoNode.get('rdsVer')
                    dpId = XmlDeviceInfoNode.get('dpId')
                    rdsId = XmlDeviceInfoNode.get('rdsId')
                    mc = XmlDeviceInfoNode.get('mc')
                    mi = XmlDeviceInfoNode.get('mi')
                    dc = XmlDeviceInfoNode.get('dc')
                    srno = XmlDeviceInfoNode.get('srno')

                    if srno is None:
                        Xmladditionalinfo = PIDResponseXML.find('.//additional_info')
                        Params = Xmladditionalinfo[0].findall('.//Param')
                        if len(Params) > 1:
                            SrnoValue = Params[0].get('value')
                        srno = SrnoValue
                    else:
                        SrnoValue = srno

                    XmlSkeyNode = PIDResponseXML.find('.//Skey')
                    ci = XmlSkeyNode.get('ci')
                    SKEY = XmlSkeyNode.text
                    Hmac = PIDResponseXML.find('.//Hmac').text
                    Data = PIDResponseXML.find('.//Data').text

            parms.DC = dc
            parms.MC = mc
            parms.MI = mi
            parms.DPID = dpId
            parms.RDSID = rdsId
            parms.RDSVER = rdsVer
            parms.CI = ci
            parms.DATA = Data
            parms.SKEY = SKEY
            parms.HMAC = Hmac
            resp = objauth.DoKYC(parms)

            print("################################# Start Response ############################################")
            print(resp.ToString())
            print("################################# End Response ############################################")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def do_auth(self,aadhaarno):
        errCode = "1"
        errInfo = "NA"
        dc = ""
        mi = ""
        mc = ""
        dpId = ""
        rdsId = ""
        rdsVer = ""
        SKEY = ""
        Data = ""
        Hmac = ""
        ci = ""
        SrnoValue = ""

        # Create objects
        objauth = Authentication(SettingsFile)
        resp = AUAKUAResponse()
        parms = AUAKUAParameters()
        
        objauth.SystemEnvironment = self.environment
        parms.LAT = "17.11111"
        parms.LONG = "78.22222"
        parms.DEVMACID = "11:22:33:44:55"
        parms.DEVID = "F0178BF2AA61380FBFF0"
        parms.SRNO = "2040444"
        parms.CONSENT = "Y"
        parms.SHRC = "Y"
        parms.VER = "2.5"
        parms.SERTYPE = "02"
        parms.ENV = "2"
        parms.AADHAARID = aadhaarno
        parms.SLK = self.LicKey
        parms.RRN = datetime.now().strftime("%Y%m%d%H%M%S%f")
        parms.REF = "FROMSAMPLE"

     
        xmldoc = ET.parse('PIDXML.xml')
        root = xmldoc.getroot()
        print("1234",root)
        print(root.itertext)
        PIDXML = "".join(root.itertext())
        with open("PIDXML.xml", "r") as file:
            xml_content = file.read()

        if len(xml_content) > 0:
            tree = ET.parse("PIDXML.xml")
            PIDResponseXML = tree.getroot()

            # Find the 'Resp' element and extract 'errInfo' and 'errCode' attributes
            resp_element = PIDResponseXML.find("Resp")
            if resp_element is not None:
                errInfo = resp_element.get("errInfo")
                errCode = resp_element.get("errCode")
            if errCode == "0":  # Success
                XmlDeviceInfoNode = PIDResponseXML.find(".//DeviceInfo")
                rdsVer = XmlDeviceInfoNode.get("rdsVer")
                dpId = XmlDeviceInfoNode.get("dpId")
                rdsId = XmlDeviceInfoNode.get("rdsId")
                mc = XmlDeviceInfoNode.get("mc")
                mi = XmlDeviceInfoNode.get("mi")
                dc = XmlDeviceInfoNode.get("dc")

                if "srno" in XmlDeviceInfoNode.attrib:
                    srno = XmlDeviceInfoNode.get("srno")
                    SrnoValue = XmlDeviceInfoNode.get("srno")
                else:
                    Xmladditionalinfo = PIDResponseXML.findall(".//additional_info")
                    Params = Xmladditionalinfo[0].findall(".//Params")
                    
                    if len(Params) > 1:
                        SrnoValue = Params[0].get("value")
                    srno = SrnoValue

                XmlSkeyNode = PIDResponseXML.find(".//Skey")
                ci = XmlSkeyNode.get("ci")
                SKEY = PIDResponseXML.find(".//Skey").text
                Hmac = PIDResponseXML.find(".//Hmac").text
                Data = PIDResponseXML.find(".//Data").text

        parms.DC = dc
        parms.MC = mc
        parms.MI = mi
        parms.DPID = dpId
        parms.RDSID = rdsId
        parms.RDSVER = rdsVer
        parms.CI = ci
        parms.DATA = Data
        parms.SKEY = SKEY
        parms.HMAC = Hmac
        parms.UDC = "MFS1002040444"
        
        resp = objauth.DoAUTH(parms)

        print("################################# Start Response ############################################")
        print(resp.ToString())
        print("################################# End Response ############################################")

    

    def generate_OTP(self, aadhaarno, svctype):
        
        objauth = Authentication(SettingsFile)
        parms = AUAKUAParameters()
        resp = AUAKUAResponse()

        # print("objauth.SystemEnvironment:",objauth.SystemEnvironment)
        # print("objauth.SystemEnvironment:",type(objauth.SystemEnvironment))
        # print(" self.environment):",self.environment)
        # print("type(self.environment):",type(self.environment))
        # print("respsde",type(resp))

        # env=objauth.SystemEnvironment
        
        # print("env",env,type(env))

        parms.LAT = "17.494568"
        parms.LONG = "78.392056"
        parms.DEVMACID = "11:22:33:44:55"
        parms.CONSENT = "Y"
        parms.SHRC = "Y"
        parms.VER = "2.5"
        parms.SERTYPE = svctype
        parms.ENV = "2"
        parms.CH = "1"
        parms.AADHAARID = aadhaarno
        parms.SLK = self.LicKey
        parms.RRN = datetime.now().strftime("%Y%m%d%H%M%S%f")
        parms.REF = "FROMSAMPLE"
        parms.UDC = "MFS1002040444"

        resp = objauth.GenerateOTP(parms)

        print("################################# Start Response ################################")
        print(resp.ToString())
        print("################################# End Response ##################################")

        return resp.Response

    def KYC_with_OTP(self, aadhaarno, OTPValue, TxnID):
        objauth = Authentication(SettingsFile)
        parms = AUAKUAParameters()
        resp = AUAKUAResponse()

        objauth.SystemEnvironment = self.environment
        parms.LAT = "17.494568"
        parms.LONG = "78.392056"
        parms.DEVMACID = "11:22:33:44:55"
        parms.DEVID = "F0178BF2AA61380FBFF0"
        parms.CONSENT = "Y"
        parms.SHRC = "Y"
        parms.VER = "2.5"
        parms.SERTYPE = "05"
        parms.LANG = "N"
        parms.PFR = "N"
        parms.ENV = "2"
        parms.OTP = OTPValue
        parms.AADHAARID = aadhaarno
        parms.SLK = self.LicKey
        parms.RRN = datetime.now().strftime("%Y%m%d%H%M%S%f")
        parms.REF = "FROMSAMPLE"
        parms.TXN = TxnID
        parms.UDC = "MFS1002040444"

        resp = objauth.DoKYC(parms)

        print("######################## Start Response ########################")
        print(resp.ToString())
        print("######################## End Response ##########################")

        return resp.Response

    def auth_with_OTP(self, aadhaarno, OTPValue, TxnID):

        objauth = Authentication(SettingsFile)
        parms = AUAKUAParameters()
        resp = AUAKUAResponse()

        objauth.SystemEnvironment = self.environment
        parms.LAT = "17.494568"
        parms.LONG = "78.392056"
        parms.DEVMACID = "11:22:33:44:55"
        parms.DEVID = "F0178BF2AA61380FBFF0"
        parms.CONSENT = "Y"
        parms.SHRC = "Y"
        parms.VER = "2.5"
        parms.SERTYPE = "02"
        parms.ENV = "2"
        parms.OTP = OTPValue
        parms.AADHAARID = aadhaarno
        parms.SLK = self.LicKey
        parms.RRN = datetime.now().strftime("%Y%m%d%H%M%S%f")
        parms.REF = "FROMSAMPLE"
        parms.TXN = TxnID
        parms.UDC = "MFS1002040444"

        resp = objauth.DoAUTH(parms)

        print("################################# Start Response ################################")
        print(resp.ToString())
        print("################################# End Response ##################################")

        return resp.Response

    def do_demo_auth(self, aadhaarno):
        objauth = Authentication(SettingsFile)
        parms = AUAKUAParameters()
        resp = AUAKUAResponse()

        objauth.SystemEnvironment = self.environment
        parms.LAT = "17.494568"
        parms.LONG = "78.392056"
        parms.DEVMACID = "11:22:33:44:55"
        parms.DEVID = "F0178BF2AA61380FBFF0"
        parms.CONSENT = "Y"
        parms.SHRC = "Y"
        parms.VER = "2.5"
        parms.SERTYPE = "07"
        parms.ENV = "2"
        parms.AADHAARID = aadhaarno
        parms.SLK = self.LicKey
        parms.RRN = datetime.now().strftime("%Y%m%d%H%M%S%f")
        parms.REF = "FROMSAMPLE"
        parms.ISPA = True
        parms.ISPFA = False
        parms.ISPI = False
        parms.PAMS = True
        parms.PAHOUSE = "12-695"
        parms.PIGENDER = "F"
        parms.NAME = "Bayyapu Reddy Jyoshna"
        parms.UDC = "MFS1002040444"
        parms.PIMS = "P"
        parms.PIMV = "20"
        parms.PIGENDER = "F"
        # parms.PIEMAIL = "bayyapureddyjyoshna@gmail.com"
        parms.PAPC = "504208"

        resp = objauth.DoDemoAUTH(parms)

        print("################################# Start Response ################################")
        print(resp.ToString())
        print("################################# End Response ##################################")

        return resp.Response

def main():
    LicKey = ""
    environment = Environment.PreProduction

    req = "Y"

    call_sdk = CallSDK()    
    while req == "Y" or req == 'y':
        print("Enter the Following Option")
        print("1 for OTP for AUTH")
        print("2 for OTP for KYC")
        print("3 for AUTH")
        print("4 for KYC")
        print("5 for Demographic : ")
        req = input()
        if req == "1":
            adhrno = input("Please Enter your Aadhaar No : ")
            otp = call_sdk.generate_OTP(adhrno, "09")
            OTPValue = input("Please Enter received OTP : ")
            if OTPValue != "0":
                TxnID = input("Please Enter received TxnID : ")
                call_sdk.auth_with_OTP(adhrno, OTPValue, TxnID)
        elif req == "2":
            adhrno = input("Please Enter your Aadhaar No : ")
            otp = call_sdk.generate_OTP(adhrno, "10")
            OTPValue = input("Please Enter received OTP : ")
            if OTPValue != "0":
                TxnID = input("Please Enter received TxnID : ")
                call_sdk.KYC_with_OTP(adhrno, OTPValue, TxnID)
        elif req == "3":
            adhrno = input("Please Enter your Aadhaar No : ")
            call_sdk.do_auth(adhrno)
        elif req == "4":
            adhrno = input("Please Enter your Aadhaar No : ")
            call_sdk.do_kyc(adhrno)
        elif req == "5":
            adhrno = input("Please Enter your Aadhaar No : ")
            call_sdk.do_demo_auth(adhrno)
        else:
            print("Invalid Option, Please Enter a valid Option")

        print("Do you want to continue with another transaction Y/N : ")
        req = input()
if __name__ == "__main__":
    main()

