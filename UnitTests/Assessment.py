import unittest
import requests
import json
import datetime

class Assessment(unittest.TestCase):
    http = "https://"
    page = "imagequix-qa-interview2"
    domain = ".herokuapp.com"
    url = http + page + domain
    blog_posts = "/blog-posts"
    authors = "/authors"
    authorPostDict = {"firstName": "", "lastName": ""}
    blogPostDict = {"title":"", "body":"", "authorId":"", "publishDate":""}

    def createAuthor(self):
        author = ["Cody", "Polera"]
        newDict = self.authorPostDict.copy()
        for param in newDict:
            newDict[param] = author.pop(0)
        resp = requests.post(Assessment.url+self.authors, newDict)
        print(resp.content)

    def createBlogPost(self):
        blog = ["Some title", "Polera", 2001, datetime.datetime.now().isoformat()
]
        newDict = self.blogPostDict.copy()
        for param in newDict:
            newDict[param] = blog.pop(0)
        resp = requests.post(Assessment.url + self.blog_posts, json=newDict)
        print(resp.content)

    def putBlog(self):
        blog = {"id":1000}

    def test_response(self):
        resp = requests.get(self.url + self.blog_posts)
        expectedId =939
        testJson = json.loads(resp.content)
        print(resp.content)
        print(testJson[0]["id"])
        self.assertEqual(testJson[0]["id"], expectedId, "Id: " + str(testJson[0]["id"]) + " did not match expected ID: "+ str(expectedId))


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
        print("=======================")
        print("Begin test")
        print("=======================")
        self.createBlogPost(self)


if __name__ == "__main__":
    unittest.main()


