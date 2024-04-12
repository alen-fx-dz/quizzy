import datetime

def get_time_now(request):
    now = datetime.datetime.now()
    return {'time_now':now}
