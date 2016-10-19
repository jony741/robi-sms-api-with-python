class sms:
    def __init__(self):
        """
        Here import some module
        request module for curl handle
        """
        import requests

        self.requests = requests

        # Set default limit for sms send & get query
        self.sms_limit = 400
        # Set default vendor
        self.sms_vendor = 'ROBI'
        # Set default current credit
        self.current_credit = 0
        self.url = False
        if (self.sms_vendor == 'ROBI'):
            # Define Robi Base URL for communication
            end_point = 'https://bmpws.robi.com.bd/ApacheGearWS/'
            # Rabi Credential
            self.username = 'yourname'
            self.password = 'yourPassword'
            self.telcom_from = 'yourTelecomeNumber'
            # Robi end points
            self.single_end_point = end_point + 'SendTextMessage'
            self.multi_end_point = end_point + 'SendTextMultiMessage'
            self.status_end_point = end_point + 'GetMessageStatus'
        elif (self.sms_vendor == 'GP'):
            # Define GP Base URL for communication
            end_point = 'https://cmp.grameenphone.com/gpcmpapi/messageplatform/controller.home'

            # GP Credential
            self.username = 'YourName'
            self.password = ''
            self.telcom_from = ''
            # GP end point
            self.single_end_point = ''
            self.multi_end_point = ''
            self.status_end_point = ''

    # sms send function, this is mother function for send sms and get status
    def send(self):

        # Single sms send method
        self.__SendTextMessage()

        # try to get sms status
        self.__GetMessageStatus()


    # single sms send method
    def __SendTextMessage(self):
        params ={'Username': self.username, 'Password': self.password, 'From': self.telcom_from}
        params['Message'] = 'your sms text'
        params['To'] = '8801820193313'
        self.url = self.single_end_point
        output = self.__curl_response(params)
        if output == False:
            msg = self.sms_vendor + 'Gateway Error'
            print(msg)
            return False
        else:
            print(output)

    # Get sms Status

    def __GetMessageStatus(self):

        params = {'Username': self.username, 'Password': self.password}
        params['MessageId'] = 'Your Message ID'
        self.url = self.status_end_point
        output = self.__curl_response(params)
        print(output)

    # sms send using request module
    def __curl_response(self, data):
        if self.url == False:
            return 'Url not defined'
        else:
            r = self.requests.get(self.url, params=data)
            if r.status_code == 200:
                output = r.text
            else:
                output = False

            return output




myobj = sms()
print(myobj.send())
