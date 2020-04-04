# This file is used to test the functionaliy of the webpage itself created via python

from seleniumbase import BaseCase

class Index_Home_Page_Testing(BaseCase):

	#Define the tests here
		#then define the elements to be tested here
	
	def Test_BMI_Calculator(self):
    	# Check when the webpage loads if element exists
    	#self.assert_element_not_visible('label#BMI_Result')