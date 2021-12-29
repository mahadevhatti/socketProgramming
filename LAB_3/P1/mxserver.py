import dns.resolver
from distlib.compat import raw_input

domain = raw_input('Enter the Domain name : ')

# example domain = 'nitk.edu.in'

for x in dns.resolver.resolve(domain, 'MX'):
    print('MX Server : ', (x.to_text()).split(' ', 1)[1])


# A MX record also called mail exchanger record is a resource record in the Domain Name System that specifies a mail
# server responsible for accepting email messages on behalf of a recipient's domain.