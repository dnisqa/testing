###################################################################################
#	Marvell GPL License
#	
#	If you received this File from Marvell, you may opt to use, redistribute and/or
#	modify this File in accordance with the terms and conditions of the General
#	Public License Version 2, June 1991 (the "GPL License"), a copy of which is
#	available along with the File in the license.txt file or by writing to the Free
#	Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 or
#	on the worldwide web at http://www.gnu.org/licenses/gpl.txt.
#	
#	THE FILE IS DISTRIBUTED AS-IS, WITHOUT WARRANTY OF ANY KIND, AND THE IMPLIED
#	WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE ARE EXPRESSLY
#	DISCLAIMED.  The GPL License provides additional details about this warranty
#	disclaimer.
###################################################################################

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
from builtins import *
try:
    from exceptions import Exception
except ImportError:
    pass


class TestFailedException(Exception):
    """
    this exception should be raised when failing the test
    """
    def __init__(self, message, errors=None):
        super(TestFailedException, self).__init__(message)
        self.errors = errors


class TestCrashedException(Exception):
    """
	this exception should be raised when failing the test
	"""
    def __init__(self , message , errors=None):
        super(TestCrashedException , self).__init__(message)
        self.errors = errors