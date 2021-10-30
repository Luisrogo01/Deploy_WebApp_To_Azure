import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'QLg7Q~bbQMyqS7mkdEDtG1TtQRQCA7q9uRVtS'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'project1storageacc'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '59FUme5vmKZ+j4YWTub5+E8FHC7maYyxZb6ZJK/4WDXNxGxB4kfPqiM97FAOhZV1DozeH7awl/n94pLpxVvThA==Y'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'project1container'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'project1depoloyserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'project1_db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'luis'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Dbpass01'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "QLg7Q~bbQMyqS7mkdEDtG1TtQRQCA7q9uRVtS"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "1103a736-4faa-4a99-9d7e-a9c286d67436"

    REDIRECT_PATH = "https://project1webapp.azurewebsites.net/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session