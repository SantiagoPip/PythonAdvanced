class Api_fetch:
    def fetch(self):
        print("fetching data from APi")
class Database_fetch:
    def fetch(self):
        print("fetching data from database")
class S3_fetch:
    def fetch(self):
        print("fetching data from s3")
obj = Api_fetch()
obj.fetch()