import sklearn
from sklearn.preprocessing import OneHotEncoder

print("scikit-learn version:", sklearn.__version__)

encoder = OneHotEncoder(sparse=False)  # or sparse_output=False if version >= 1.2
