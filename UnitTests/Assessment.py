import unittest
import requests
import json

class Assessment(unittest.TestCase):

    http = "https://"
    page = "imagequix-qa-interview2"
    domain = ".herokuapp.com"
    url = http + page + domain
    blog_posts = "/blog-posts"
    authors = "/authors"

    def testSum_ConfirmTestWorks(self):
        assert sum([1,2,3]) ==6, "blahhhh"
        print(str(sum([1,2,3])) + ' was correct')

    def test_response(self):
        resp = requests.get(self.url + self.blog_posts)
        testJson = json.loads(resp.content)
        print(resp.content)
        print(testJson[0]["id"])

    def test_response_Author(self):
        resp = requests.get(self.url + self.authors)
        testJson = json.loads(resp.content)
        print(resp.content)
        for author in testJson:
            print(author["id"])
            for val in author:
                print(val + ":  " + str(author[val]))

    def test_response_AuthorViaID(self):
        resp = requests.get(self.url + self.authors + "/1")
        testJson = json.loads(resp.content)
        print(resp.content)
        for val in testJson:
            print(val + ":  " + str(testJson[val]))

    @classmethod
    def setUp(self):
        print("Begin test")

if __name__ == "__main__":
    unittest.main()
    # a = Assessment()
    # a.testSum_ConfirmTestWorks()
    # a.test_response()
    # a.test_response_Author()