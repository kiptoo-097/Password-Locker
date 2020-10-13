class Credential:
    """
    Class that generates instances of credential
    """

    credential_list =[]


    def __init__(self, account, acnt_username, acnt_password):
        self.account = account
        self.acnt_username = acnt_username
        self.acnt_password = acnt_password

    def save_credential(self):
        '''
        save user objects into credential
        ''' 
        Credential.credential_list.append(self)   

    def delete_credential(self):
        '''
        deleteletes saved contact
        '''
        Credential.credential_list.remove(self)
