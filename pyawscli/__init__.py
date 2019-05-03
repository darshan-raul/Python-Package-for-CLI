
from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2

from pyfiglet import Figlet
f = Figlet(font='big')

mainquestions = [
    {
        'type': 'list',
        'name': 'service',
        'message': 'Which AWS service you want to use ?',
        'choices': [
            Separator('---------Compute Services---------'),
            'EC2',
            'Lambda',
            Separator('---------Storage Services---------'),
            'S3',
            'RDS',
            Separator('---------Network Services---------'),
            'Route53',
            'VPC',
            Separator('---------Management Services---------'),
            'IAM',
            'Cloudwatch',
            'Exit'

        ]
    },
    
  
]


def joke():
    return (u'works')

def main():
    print (f.renderText('AWS CLI'))
    print('A small little CLI to interact with AWS Services')
    print('Made with <3 by Darshan Raul \n')   

    mainanswers = prompt(mainquestions, style=custom_style_2) # initialize questions

    pprint(mainanswers) # print questions    


if __name__ == '__main__':
    main()