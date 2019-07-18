import requests


def Test_SendEmail():
    '''
    Test for SendEmail in Email.views
    '''
    r = requests.post('http://localhost:8000/api/SendEmail',
                      {'Email': 'client@gmail.com',
                       'Subject': 'Test Email', 'Body': 'Test Body Text'})
    if r.json()['response'] == 1:
        return True
    return False
