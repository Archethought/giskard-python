"""
DataSource Class
"""
import os
import sys
import uuid
sys.path.append("../")

from Giskard import Giskard, S3

class DataSource(object):
    """
    DataSource Class
    """

    def __init__(self, bucket):
        self._bucket = S3.Bucket(bucket)

    @property
    def bucket(self):
        return self._bucket

    def put(self, local_filepath):
        filename = os.path.basename(local_filepath)
        self.bucket.upload_file(local_filepath, "%s-%s" % (str(uuid.uuid4()), filename))

if __name__ == "__main__":
    d = DataSource("dixon-demo-data")
    with open("/tmp/test-data.txt", "w") as f:
        f.write("12345")
        f.close()
    d.put("/tmp/test-data.txt")
