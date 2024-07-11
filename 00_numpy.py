import numpy as np
import logging 
logging.basicConfig(filename="00_logging.log",level=logging.DEBUG)
# one diamensional array
myarr=np.array([4,56,57,34,97,34], np.int64)
logging.info(myarr)
logging.info("TYPE:{}".format(myarr.dtype))
logging.info(type(myarr))
#two diamensional array
myarr1=np.array([[1,2,3,4,5]])
logging.info(myarr1[0])
logging.info(myarr1.shape)
logging.info(myarr1[0,1])
