from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from linkedin import linkedin
from requests_oauthlib import OAuth2Session

from rest_framework.views import View
from oauthlib.oauth2 import WebApplicationClient
from django.conf import settings

class LinkedInLoginView(View):
    def get(self, request):
        client = WebApplicationClient(settings.LINKEDIN_CLIENT_ID)
        scope = ['r_liteprofile', 'r_emailaddress', 'w_member_social']
        state = 'random-state-string'

        uri = client.prepare_request_uri(
            'https://www.linkedin.com/oauth/v2/authorization',
            response_type='code',
            redirect_uri=settings.LINKEDIN_REDIRECT_URI,
            state=state,
            scope=scope
        )

        return redirect(uri)
class LinkedInCallbackView(View):
    def get(self, request):
        linkedin_token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
        params = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'redirect_uri': settings.LINKEDIN_REDIRECT_URI,
            'client_id': settings.LINKEDIN_CLIENT_ID,
            'client_secret': settings.LINKEDIN_CLIENT_SECRET,
        }
        oauth = OAuth2Session
