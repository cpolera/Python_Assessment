import unittest
import requests
import json
import datetime

class Test_API(unittest.TestCase):
    http = "https://"
    page = "imagequix-qa-interview2"
    domain = ".herokuapp.com"
    url = http + page + domain
    blog_posts = "/blog-posts"
    authors = "/authors"
    authorPostDict = {"firstName": "", "lastName": ""}
    blogPostDict = {"title":"", "body":"", "authorId":"", "publishDate":""}

    ##BLOGS
    ##test get all
    def test_GET_All_Blogs(self):
        None

    ##test get one id
    def test_GET_Blog_ID(self):
        expectedId =1000
        testJson = self.GET_Wrapper(self.url + self.blog_posts + "/" + str(expectedId))
        print(testJson["id"])
        self.assertEqual(testJson["id"], expectedId, "Id: " + str(testJson["id"]) + " did not match expected ID: "+ str(expectedId))

    ##test post blog
    def test_POST_Blog(self):
        blogParams = ["Some title", "Polera", 1, datetime.datetime.now().isoformat()]
        statusCode = self.POST_Blog(blogParams)
        self.assertEqual(str(statusCode), "<Response [201]>", "The POST resulted in code: " + str(statusCode))

    ##test put blog
    def test_PUT_Blog(self):
        blogParams = ["PUT BLOG", "Polera", 1, datetime.datetime.now().isoformat()]
        resp = self.POST_Blog(blogParams)
        testJson = json.loads(resp.content)
        id = testJson["id"]
        blogPutParam = {"title":"PUT BLOG_P"}
        respPut  = self.PUT_Blog(blogPutParam, id)
        testJson = self.GET_Wrapper(self.url+self.blog_posts + "/" + str(id))
        self.assertEqual(testJson["title"], blogPutParam["title"], "Title was not updated")

    ##test delete blog
    def test_DELETE_Blog(self):
        blogParams = ["DEL BLOG", "Polera", 1, datetime.datetime.now().isoformat()]
        resp = self.POST_Blog(blogParams)
        testJson = json.loads(resp.content)
        id = testJson["id"]
        self.DELETE_Wrapper(self.url + self.blog_posts + "/" + str(id))
        respDel = requests.get(self.url + self.blog_posts + "/" + str(id))
        self.assertTrue(respDel.status_code != "<Response [200]", "Code was not 200")


    ##AUTHORS
    ##test get all authors

    ##test get one author
    def test_GET_Author_ID(self):
        expectedId =1
        testJson = self.GET_Wrapper(self.url + self.authors + "/" + str(expectedId))
        print("Author Id: " + str(testJson["id"]))
        self.assertEqual(testJson["id"], expectedId, "Id: " + str(testJson["id"]) + " did not match expected ID: "+ str(expectedId))

    ##test post author
    def test_POST_Author(self):
        author = ["Cody", "Polera"]
        statusCode = self.POST_Author(author)
        self.assertEqual(str(statusCode), "<Response [201]>", "The POST resulted in code: " + str(statusCode))

    ##test put author
    def test_PUT_Author(self):
        authorParams = ["PUT Author", "Polera"]
        resp = self.POST_Author(authorParams)
        testJson = json.loads(resp.content)
        id = testJson["id"]
        authorPutParams = {"firstName":"PUT Author_P"}
        respPut = self.PUT_Author(authorPutParams, id)
        testJson = self.GET_Wrapper(self.url+self.authors + "/" + str(id))
        self.assertEqual(testJson["firstName"], authorPutParams["firstName"], "First name was not updated")

    ##test delete author
    def test_DELETE_Author(self):
        authorParams = ["DEL Author", "Polera"]
        resp = self.POST_Author(authorParams)
        testJson = json.loads(resp.content)
        id = testJson["id"]
        self.DELETE_Wrapper(self.url + self.authors + "/" + str(id))
        respDel = requests.get(self.url + self.authors + "/" + str(id))
        self.assertTrue(respDel.status_code != "<Response [200]", "Code was not 200")

    ##BEFORE TEST
    @classmethod
    def setUp(self):
        print("=======================")
        print("Begin test")
        print("=======================")


##=========================================================================
    ##HELPER METHODS
    def POST_Author(self, author):
        newDict = self.authorPostDict.copy()
        for param in newDict:
            newDict[param] = author.pop(0)
        return self.POST_Wrapper(Test_API.url + self.authors, newDict)

    def POST_Blog(self, blog):
        newDict = self.blogPostDict.copy()
        for param in newDict:
            newDict[param] = blog.pop(0)
        return self.POST_Wrapper(Test_API.url + self.blog_posts, newDict)

    def PUT_Blog(self, params, id):
        return self.PUT_Wrapper(Test_API.url + self.blog_posts + "/" + str(id), params)

    def PUT_Author(self, params, id):
        return self.PUT_Wrapper(Test_API.url + self.authors + "/" + str(id), params)

    def POST_Wrapper(self, url, dict):
        resp = requests.post(url, json=dict)
        print(resp.content)
        return resp

    def GET_Wrapper(self, url):
        resp = requests.get(url)
        return json.loads(resp.content)

    def PUT_Wrapper(self, url, dict):
        return requests.put(url, dict)

    def DELETE_Wrapper(self, url):
        return requests.delete(url)

if __name__ == "__main__":
    unittest.main()


