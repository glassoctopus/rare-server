import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_posts, get_single_post, create_post
from urllib.parse import urlparse, parse_qs
from views import create_category, update_category, create_subscription, delete_subscription
from views import create_user, login_user, get_single_user, get_all_users
from views import get_single_comment,get_all_comments,create_comment
from views import get_single_posttags,get_all_posttags,create_posttag,delete_posttag
from views import get_all_categories,get_single_category,delete_category
from views import get_all_subscriptions,get_single_subscription


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def do_GET(self):
        """Handles GET request to the server"""
        self._set_headers(200)

        response = {}

        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            ( resource, id ) = self.parse_url()

            # It's an if..else statement
            if resource == "Comments":
                if id is not None:
                    response = get_single_comment(id)

                else:
                    response = get_all_comments()
                    
            if resource == "PostTags":
                if id is not None:
                    response= get_single_posttags(id)                    
                else:   
                    response= get_all_posttags()
            
            if resource == "Categories":
                if id is not None:
                    response= get_single_category(id)                
                else: 
                    response = get_all_categories()
            
            if resource == "Subscriptions":
                if id is not None:
                    response= get_single_subscription(id)
                else:
                    response= get_all_subscriptions()
            
            if resource == "Posts":
                if id is not None:
                    response= get_single_post(id)
                else:
                    response= get_all_posts()
                    
            if resource == "Users":
                if id is not None:
                    response = get_single_user(id)
                else:
                    response = get_all_users()


        self.wfile.write(json.dumps(response).encode())
        
    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                            'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                            'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url()

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'Posts':
            response = create_post(post_body)

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        pass

    def do_DELETE(self):
        """Handle DELETE Requests"""
        pass





def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
