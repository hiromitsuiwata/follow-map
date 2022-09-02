import codecs
 
u_text = "\u0950"
text = codecs.decode(u_text.encode())
print(text)