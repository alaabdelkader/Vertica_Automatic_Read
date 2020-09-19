
# coding: utf-8

# In[1]:


import pyodbc


# In[2]:
	

cnxn = pyodbc.connect("DSN=vertica_ODBC", ansi=True)


# In[3]:


cursor = cnxn.cursor()


# In[4]:


cursor.execute("""

vertica query here

""")


# In[5]:


rows = cursor.fetchall()


# In[6]:


for row in rows:
    print(",".join(str(word) for word in row))


# In[7]:


cursor.close()
cnxn.close()

