print('Please enter the following:')
print()

adj = input('adjective: ')
animal = input('animal: ')
verb = input('verb: ')
exc = input('exclamation: ')
vb1 = input('verb: ')
vb2 = input('verb: ')
reply = input('Unknown question: Yes or No? ')

if reply.lower() == 'yes':
    reply = 'And you forgave me :)'
elif reply.lower() == 'no':
    reply = 'And you do not forgive me :('
else:
    reply = ''
    
output = f""" Your story is:

TITLE: THE {animal.upper()} AND I 

The other day, I was really in trouble. It all started when I saw a very\n{adj.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exc.capitalize()}!" I yelled. But all\nI could think to do was to {vb1.lower()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to drive\nright in front of my family.


Gotcha! This has been a word game so far and I just too your time :(
{reply}
"""

print(output)