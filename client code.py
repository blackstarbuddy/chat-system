#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'client.py', "import socket\nimport random\nimport json\nhostname = socket.gethostname()\nclcon = socket.socket() #connect hostname\nclcon.connect((hostname, 1234))\n\n\ndef client():\n    mssg_store = open('mdata.txt','a')\n    ser = input('Enter message\\t')\n    cl = ['bye','talk to you later','good night']\n    \n    clcon.send(ser.encode())\n    if ser in cl:\n        clcon.close()\n    else:\n        recv_in = clcon.recv(1024)\n        dec = recv_in.decode()\n        mssg_store.write(f'\\t\\t\\t Server: {dec}\\n')\n        mssg_store.close()\n        print(dec)\n        if dec == 'bye':\n            clcon.close()\n        else:\n            client()\n\n\nclient()")


# In[ ]:




