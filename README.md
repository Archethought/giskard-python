# Giskard Python SDK

Giskard SDK for Python 2 & 3 applications.

## Installation

```pip install git+https://github.com/Archethought/giskard-python.git```

## Usage

The current version of Giskard SDK requires AWS credentials with permission to write to Archethought's S3. (In the future, this will change to use Giskard API credentials).

The following environment variables need to be set:

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_DEFAULT_REGION
    
To use in an application, import specific modules from the Giskard library.

Example:

```python
from Giskard.DataSource import DataSource    

ds = DataSource('my-bucket')
ds.put('/path/to/a/file')
```
