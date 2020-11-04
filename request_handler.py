from http.server import BaseHTTPRequestHandler, HTTPServer

from models import ParsedUrl

from categories import get_all_categories, create_category, delete_category, update_category
from tags import get_all_tags, create_tag, delete_tag, update_tag
from comments import get_all_comments
import json
from posts import create_post, get_all_posts, get_single_post, update_post

class HandleRequests(BaseHTTPRequestHandler):

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


    def do_GET(self):
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)
        
        if parsed.resource == "categories":
                response = get_all_categories()
        elif parsed.resource == "comments":
            if parsed.id is not None:
                response = get_single_comment(parsed.id)
            else:
                response = get_all_comments()
        elif parsed.resource == "tags":
                response = get_all_tags()
        elif parsed.resource == "posts":
            if parsed.id is not None:
                response = get_single_post(parsed.id)
            else:
                response = get_all_posts()
    
        elif parsed.resource == "login":
            content_len = int(self.headers.get('content-length', 0))
            post_body = self.rfile.read(content_len)
            post_body = json.loads(post_body)

            validate_user_login(post_body)
                
                
        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        parsed = self.parse_url(self.path)
        
        new_object = None

        if parsed.resource == "categories":
            new_object = create_category(post_body)
        elif parsed.resource == "comments":
            new_object = create_comment(post_body)
        elif parsed.resource == "posts":
            new_object = create_post(post_body)
        elif parsed.resource == "tags":
            new_object = create_tag(post_body)
        
        self.wfile.write(f"{new_object}".encode())

    def do_DELETE(self):
        self._set_headers(204)

        parsed = self.parse_url(self.path)

        if parsed.resource == "categories":
            delete_category(parsed.id)
        elif parsed.resource == "comments":
            delete_comments(parsed.id)
        elif parsed.resource == "posts":
            delete_post(parsed.id)
        elif parsed.resource == "tags":
            delete_tag(parsed.id)

        self.wfile.write("".encode())
    
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        parsed = self.parse_url(self.path)

        success = False
        
        if parsed.resource == "categories":
            success = update_category(parsed.id, post_body)
        elif parsed.resource == "comments":
            success = update_comment(parsed.id, post_body)
        elif parsed.resource == "posts":
            success = update_post(parsed.id, post_body)
        elif parsed.resource == "tags":
            success = update_tag(parsed.id, post_body)
        
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())
    
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        query = {}
        id = ""
        id_int = None
        try:
            id = path_params[2]
        except IndexError:
            pass

        if "?" in resource:
            param = resource.split("?")[1]
            resource = resource.split("?")[0]
            query = self.parse_query(param)
        
        if "?" in id:
            param = id.split("?")[1]
            id_int = int(id.split("?")[0])
            query = self.parse_query(param)

        else:
            try:
                id_int = int(id)
            except IndexError:
                pass
            except ValueError:
                pass
            
        return ParsedUrl(resource, id_int, query)

    def parse_query(self, query_string):
        pairs = query_string.split("&")
        query = {}

        for pair in pairs:
            (key, value) = tuple(pair.split('='))
            if key in query:
                query[key].append(value)
            else:
                query[key] = [value]
        return query

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-Width, content-type')
        self.end_headers()

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
