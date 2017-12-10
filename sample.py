# sample.py
import falcon
import json


ALLOWED_ORIGINS = ['http://localhost:3000'] # Or load this from a config file

class CorsMiddleware(object):

    def process_request(self, request, response):
        origin = request.get_header('Origin')
        if origin in ALLOWED_ORIGINS:
            response.set_header('Access-Control-Allow-Origin', origin)
            response.set_header('Access-Control-Allow-Headers','*') 
class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }

        resp.body = json.dumps(quote)
    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
            print(req.params)
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Error',
                ex.message)
 
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
            print(result_json)
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Malformed JSON',
                'Could not decode the request body. The '
                'JSON was incorrect.')
 
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='utf-8')
api = falcon.API(middleware=[CorsMiddleware()])
api.add_route('/quote', QuoteResource())
