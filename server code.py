#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_cell_magic('writefile', 'server.py', "import socket\nimport json\n\ncon = socket.socket() #connection\nhostname = socket.gethostname()\ncon.bind((hostname,1234))\ncon.listen()\ncl_con,cl_ad = con.accept()\n\ndef server():\n    mssg_store = open('mdata.txt','a')\n    mssg = cl_con.recv(1024) # client s recieve and store in mssg var\n    dec = mssg.decode()\n    mssg_store.write(f'Client: {dec}\\n')\n    mssg_store.close()\n    print(dec)\n    cl = ['bye','talk to you later','good night']\n    if dec in cl:\n        con.close()\n    else :\n    \n        dat = input('Enter Message')\n        cl_con.send(dat.encode())\n        if dat == 'bye':\n            con.close()\n        else:\n            server()\n            \n\nserver()")


# In[ ]:




