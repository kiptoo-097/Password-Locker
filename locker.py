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

    def test_save_credential(self):
        pass

    @classmethod
    def find_by_acnt_username(cls, acnt_username):
        for credential in cls.credential_list:
            if credential.acnt_username == acnt_username:
                return credential

    @classmethod
    def display_credentials(cls):
        return cls.credential_list

    @classmethod
    def display_all_credentials(cls):
        return cls.credential_list