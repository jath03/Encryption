from pprint import pprint
from changebase import changebase

def encrypt(message, wantedbase):
   final_message = list()
   for x in range(0, len(message)):
      encrypted_message = changebase(ord(message[x]), 10, wantedbase)
      final_message.append(encrypted_message)
   return ', '.join(final_message)
