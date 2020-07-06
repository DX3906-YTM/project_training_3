from django import http
from django.views import View
from django_redis import get_redis_connection
from ihome.libs.captcha.captcha import captcha


class ImageCodeView(View):
    """
    图形验证码:
    """
    @staticmethod
    def get(request):
        """
        调用工具 captcha 生成图片验证码
        请求参数: 参数名	必选	    类型	   说明
                 cur	true	str	  验证码编号
                 pre	false	str	  上一次验证码编号
        返回结果: image
        请求方式: GET
        :param request: 请求报文
        :return: image
        """
        # 获取 UUID:
        cur = request.GET.get('cur')
        # 校验 UUID:
        if not cur:
            return http.JsonResponse({'errno': 4002, 'errmsg': '无数据'})
        # 生成图片验证码:
        text, image = captcha.generate_captcha()
        # 将验证码保存到redis数据库中
        redis_cli = get_redis_connection('verify_code')
        redis_cli.setex('img_%s' % cur, 300, text)
        # 响应图形验证码:image/jpg
        return http.HttpResponse(image, content_type='image/jpg')









































































