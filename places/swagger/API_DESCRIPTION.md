API 에 대한 안내 문서입니다. 현재 목표버전은 1.0 이며, 진행 상황에 따라 일부 API 가 변경될 수 있습니다.

## API 키 발급

API 를 사용할 수 있는 `CLIENT_ID` 와 `CLIENT_SECRET` 을 발급받아 사용할 수
있습니다. 키 발급은  관리페이지의 **클라이언트 관리**
메뉴에서 가능합니다. 운영자에게 문의해주시기 바랍니다.

### 인증

OAuth2.0 의 `implicit` 방식과 `resource owner` 방식의 인증을
제공합니다.

**Auth: Resource Owner**

```
{{OAUTH_AUTHORIZE_URL}}?grant_type=password&cleint_id=CLIENT_ID&client_secret=CLIENT_SECRET&username=USERNAME&password=PASSWORD&scope=email
```

`ACCESS_TOKEN` 획득 URL에 아래 필수 데이터를 `GET` 또는 `POST`로 전달하면 됩니다.

- grant_type: password
- client_id: `CLIENT_ID`
- client_secret: `CLIENT_SECRET`
- username: 로그인할 사용자의 email
- password: 로그인할 사용자의 password
- scope: 기본 스코프 (`email`)

서버의 response는 아래와 같습니다.

```
{
  "access_token": "THE_ACCESS_TOKEN",
  "refresh_token": "THE_REFRESH_TOKEN",
  "type": "Bearer",
  "expire_at": "2016-07-30 00:00:00"
}
```

**Auth: Implicit**

웹서비스에서 사용 예정입니다.

## 리소스 호출

획득한 `ACCESS_TOKEN`을 이용하여 웹서비스를 호출합니다.

```
GET /v1/users/self HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Bearer THE_ACCESS_TOKEN
Connection: keep-alive
Host: localhost:5000
User-Agent: HTTPie/0.9.3



HTTP/1.0 200 OK
Content-Length: 42
Content-Type: application/json
Date: Thu, 19 May 2016 07:10:10 GMT
Server: Werkzeug/0.10.4 Python/2.7.11

{
    ......
}
```

## 응답 구조

### Envelope

모든 응답은 미리 지정한 envelope 형식을 따릅니다. 아래와 같은 구조입니다.

```
{
  "meta": {
    "code": 200
  },
  "data": {
    ...
  },
  "pagination": {
    ...
  }
}
```

### META
### DATA
### PAGINATION
