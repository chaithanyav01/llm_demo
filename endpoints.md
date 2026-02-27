predict:
curl -X POST http://localhost:5000/2015-03-31/functions/function/invocations -d "{\"version\":\"2.0\",\"routeKey\":\"GET /predict\",\"rawPath\":\"/predict\",\"rawQueryString\":\"prompt=hello^&max_tokens=10\",\"headers\":{},\"requestContext\":{\"http\":{\"method\":\"GET\",\"path\":\"/predict\",\"sourceIp\":\"127.0.0.1\",\"userAgent\":\"curl\"}},\"isBase64Encoded\":false}"

root:
curl -X POST http://localhost:5000/2015-03-31/functions/function/invocations -d "{\"version\":\"2.0\",\"routeKey\":\"GET /\",\"rawPath\":\"/\",\"rawQueryString\":\"\",\"headers\":{},\"requestContext\":{\"http\":{\"method\":\"GET\",\"path\":\"/\",\"sourceIp\":\"127.0.0.1\",\"userAgent\":\"curl\"}},\"isBase64Encoded\":false}"


docker run -p 5000:8080 tinygpt-api


aws lambda:
https://tmo6ynjylf6ou6yv7hscf6if2e0paqqd.lambda-url.ap-south-1.on.aws/
https://tmo6ynjylf6ou6yv7hscf6if2e0paqqd.lambda-url.ap-south-1.on.aws/predict?prompt=hello&max_tokens=10