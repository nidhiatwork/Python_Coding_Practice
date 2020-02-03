'''Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. 
'''

def numUniqueEmails(emails):
    uniqueEmails = set()
    for email in emails:
        local,domain = email.split('@')
        local = "".join(local.split('+')[0].split('.'))
        email = local +'@' + domain
        uniqueEmails.add(email)
    return len(uniqueEmails)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))