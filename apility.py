import requests
import tldextract
import ipaddress

class IPReputation(object):
    def __init__(self,header,ip):
        self.header = header
        try:
            ipaddress.ip_address(ip)
            self.url = "https://api.apility.net/v2.0/ip/{}".format(ip)
            self.req = requests.api.get(self.url, headers=self.header).json()
            self.listParse = self.req['fullip']
        except ValueError:
            return None

    @property
    def hostname(self):
        return self.listParse['geo']['hostname']

    @property
    def country(self):
        return self.listParse['geo']['country_names']['en']

    @property
    def descriptino(self):
        return self.listParse['whois']['network']['remarks'][0]['description']

    @property
    def baddomain(self):
        return self.listParse['baddomain']['domain']['blacklist']

    @property
    def blacklist(self):
        return self.listParse['badip']

    @property
    def json(self):
        return self.req

class DomainReputation(object):
    def __init__(self,header,domain):
        tld = tldextract.extract(domain)
        self.domain = tld.registered_domain
        if self.domain:
            self.header = header
            self.url = "https://api.apility.net/baddomain/{}".format(self.domain)
            self.req = requests.api.get(self.url,headers=self.header).json()
            self.listParse = self.req['response']['domain']
        else:
            return None

    @property
    def checkBlacklist(self):
        return self.listParse['blacklist']

    @property
    def checkDNSBlacklist(self):
        return self.listParse['blacklist_ns']

    @property
    def getDNS(self):
        return self.listParse['ns']

    @property
    def json(self):
        return self.req

class apility(object):
    def __init__(self, api_key):
        self.header = {'X-Auth-Token': api_key,'Accept':'application/json'}
        self.url = "https://api.apility.net/"

    def IPWhois(self,ip):

        return IPReputation(self.header,ip)

    def DomainWhois(self,domain):

        return DomainReputation(self.header,domain)

