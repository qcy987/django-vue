import random
import string

from django.test import TestCase

end = ''.join(random.sample(string.digits,8))
print(end)