import requests
from datetime import datetime, timedelta


class AuthorizedRequest:
    access_token = None
    refresh_token = None
    token_creation_time = None

    def get(self, url, params=None, headers: dict=None, **kwargs):
        if self.access_token is None or self._access_token_has_expired():
            self.access_token, self.refresh_token, self.token_creation_time = _update_access_token()

        headers = self._add_token_header(headers)

        response = requests.get(url, params=params, headers=headers, **kwargs)

        return response.json()

    def _access_token_has_expired(self):
        return (datetime.now() - self.token_creation_time) > timedelta(hours=1)

    def _add_token_header(self, headers):
        token_header = {"Authorization": "Bearer {}".format(self.access_token)}
        if headers:
            headers.update(token_header)
        else:
            headers = token_header

        return headers


def _update_access_token():
    token_url = "https://auth-sandbox.test.vismaonline.com/eaccountingapi/oauth/token"
    request_body = {
        "refresh_token": "97dba257d2d74896b642ddcf6f44db6c",
        "grant_type": "refresh_token",
        "redirect_uri": "https://localhost:44300/callback"
    }

    headers = {'Authorization': "Basic dmlzbWFzdXBwb3J0OmtPNjJLSzFRajh1b0FQSkxYSnB0c3dYWGZPT05Ia1VpVWFwa1o2NUM4TFE="}

    response = requests.post(token_url, json=request_body, headers=headers)
    response = response.json()
    access_token = response["access_token"]
    refresh_token = response["refresh_token"]
    token_time_stamp = datetime.now()

    return access_token, refresh_token, token_time_stamp
