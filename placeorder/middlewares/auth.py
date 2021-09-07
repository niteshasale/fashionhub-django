from django.shortcuts import redirect

def auth_middleware(get_response):
    
    def middleware(request):
        if not request.session.get('user_id'):
            return redirect('/account/login')

        response = get_response(request)

        
        return response

    return middleware