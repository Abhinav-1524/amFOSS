import re 
file = open('/home/abhinav/py_tasks/ch_9/mad_libs.py', 'r') 
content = file.read() 
mad_lib_words = list(content.split()) 
file.close() 

adjective = re.compile(r'ADJECTIVE') 
noun = re.compile(r'NOUN') 
adverb = re.compile(r'ADVERB') 
verb = re.compile(r'VERB') 


adj_input=input("enter a adjective: ") 
noun_input=input("enter a noun :") 
verb_input=input("enter a verb: ") 
adverb_input=input("enter a adverb: ") 


result_file = open('/home/abhinav/py_tasks/ch_9/mad_libs.py', 'w') 
result_string = ""
for word in mad_lib_words:
    if adjective.match(word): 
        word = adjective.sub(adj_input, word) 
    elif noun.match(word): 
        word = noun.sub(noun_input, word) 
    elif verb.match(word): 
        word = verb.sub(verb_input, word) 
    elif adverb.match(word): 
            word = adverb.sub(adverb_input, word) 
result_string += word + " " 
result_file.write(word + " ") 
print(result_string) 
result_file.close() 