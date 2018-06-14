#This is a test code that shall be used to extract phone numbers for certain people

def extract(x):
    contacts = {
        'Collo': '0778404576',
        'Frank': '0788421618',
        'Mum': '0776939990',
        'Airtel': '0751939990',
        'Collo A': '0704893955',
        'Dad': '0772340595',
        'Sis': '0772885512',
    }
    for a in  contacts:
        if x == a:
            print (contacts[a])
        else:
            print ('Contact not found')

extract(input('Enter contact name: '))
