from mewpy.stenography import writeImage
from mewpy.stenography import readImage

import tweepy as tw
import json

import os

class Database():
    def __init__( self, name="JoseRam04272499", schema_path="schemas.json"):

        self.API_KEY = 'r4q9ZTdev9x5rEvve82NGDo1g'
        self.API_SECRET_KEY = '9EXv8SrRjgShdysinMwTweNAPry7dIPWspPgxHhRJ541CeF8sR'

        self.ACCESS_TOKEN = '1249434535269294080-4uq2LmIKWjyTz38mCPcbBndFvIgnQq'
        self.ACCESS_TOKEN_SECRET = 'mN2oScFkVjQefSr52ntC7uyyvqe1XOPonVZO6cmtSxmz4'
        self.DATABASE_NAME = name

        self.SCHEMA_PATH = schema_path
        self.TABLES_SCHEMAS = []

    def Auth( self ):
        auth = tw.OAuthHandler( self.API_KEY, self.API_SECRET_KEY )
        auth.set_access_token( self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET )
        self.api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def Set_tables( self ):
        with open(self.SCHEMA_PATH) as json_schemas:
            data = json.load( json_schemas )
            self.TABLES_SCHEMAS = data

        for i,sch in enumerate( self.TABLES_SCHEMAS['tables'] ):
            if sch['id'] == 0:
                msg = str(sch['name'])+": "+ json.dumps(sch['schema'])
                data = self.api.update_status( msg )
                self.TABLES_SCHEMAS['tables'][i]['id'] = data._json['id']
                print ' [*] Nueva tabla agregada [{}]'.format( sch['name'] )

        with open(self.SCHEMA_PATH, 'w') as json_schemas:
            json.dump( self.TABLES_SCHEMAS, json_schemas, indent = 2 )
        print ' [*] Conexion con la base de datos lista.'

    def Query( type,var,argument ):
        pass

    def Commit( self, type, data ):
        data = json.dumps(data, indent=2)
        writeImage.Hide('test.jpg','out.png',data)
        id_table = self.TABLES_SCHEMAS['tables'][0]['id']
        with open('out.png') as file:
            img_id = self.api.media_upload('out.png')
            img_id = img_id.media_id
            self.api.update_status(media_ids=[img_id],in_reply_to_status_id=id_table)


user_data = {
    "username" : "jo_ramirez",
    "password" : "password"
}

db = Database( name="JoseRam04272499" )
db.Auth()
db.Set_tables()
db.Commit('users', user_data )
