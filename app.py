"""
Copyright 2021-2022 Derailed.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os

from apiflask import APIFlask
from dotenv import load_dotenv

from derailedapi import ratelimiter
from derailedapi.json import ORJSONDecoder, ORJSONEncoder
from derailedapi.users import routes
from derailedapi.users.routes import users

load_dotenv()
routes.AUTH_KEY = os.getenv('AUTH_KEY')
ratelimiter.AUTH_KEY = routes.AUTH_KEY

from derailedapi.database import connect, sync_tables

connect()
sync_tables()

app = APIFlask(
    __name__,
    title='Derailed API',
    version='v0',
    spec_path='/openapi.json',
    docs_ui='elements',
    docs_path='/',
)
ratelimiter.limiter.init_app(app=app)
app.config['INFO'] = {
    'description': 'The API for Derailed.',
    'termsOfService': 'https://derailed.one/terms',
    'contact': {'name': 'Support', 'email': 'support@derailed.one'},
    'license': {
        'name': 'Apache-2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0',
    },
}
app.config['SERVERS'] = [
    {'name': 'Production', 'url': 'https://api.derailed.one'},
]
app.config['TAGS'] = [{'name': 'users', 'description': 'Endpoints for Derailed Users'}]
app.json_encoder = ORJSONEncoder
app.json_decoder = ORJSONDecoder


# register blueprints
app.register_blueprint(users)


if __name__ == "__main__":
    app.run()