from ..models.hello import Hello


def save_hello(name, ip):
    hello = Hello(name=name, ip=ip)
    return hello.create()


def get_hello_list():
    return Hello.query.all()
