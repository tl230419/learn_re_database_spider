import socket

def request_handler(new_client_socket):
    req_data = new_client_socket.recv(4096)
    req_content = req_data.decode('utf-8')
    print("打印请求的内容：", req_data)

    resp_line_and_headers = """
        HTTP/1.1 200 OK
        Server: one new bility server
        Content-Type: text/html; charset=UTF-8
        Connection: keep-alive
        Accept-Ranges: bytes
    """

    resp_body = "<h1>这是来自html页面的数据</h1>"

    resp_content = resp_line_and_headers\
                    + "\r\n"\
                    + resp_body

    print("响应的内容：%s" % resp_content)
    new_client_socket.send(resp_content.encode("utf-8"))
    new_client_socket.close()

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("", 80))
tcp_server_socket.listen(128)
print("服务器启动啦！")
while True:
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("新客户端上线啦：", ip_port)

    try:
        request_handler(new_client_socket)
    except Exception as e:
        print("异常信息：", e)
    else:
        print("服务器响应成功")

print("服务器关闭！")
tcp_server_socket.close()

