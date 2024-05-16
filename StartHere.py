import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of packages to install
packages = ['pandas', 'numpy', 'matplotlib', 'scikit-learn', 'seaborn', 'scipy', 'tensorflow']

for package in packages:
    try:
        dist = __import__(package)
        print("{} ({}) is installed".format(dist.__name__, dist.__version__))
    except ImportError:
        print('{} is NOT installed'.format(package))
        print('Installing...')
        install(package)
        print('{} has been installed'.format(package))