import socket
import re
import multiprocessing
'''实现简单web服务器，用多进程'''


def service_client(new_socket):
    """为一个客户端进行服务，进行数据的接收与响应"""
    # 1 接收浏览器发过来的请求，即 GET / HTTP/1.1 ...
    request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    # print("")
    # print(">"*20)
    # print(request_lines)
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"
    # 2 返回http格式数据，给浏览器
    try:
        print("./html" + file_name)
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "*******  file not found  *********"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据  header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # 2.1 准备发送给浏览器的数据  body
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)
    # 关闭套接字
    new_socket.close()


def main():
    """总体控制 """
    # 1 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2 绑定
    tcp_server_socket.bind(("", 7890))
    # 3 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4 等待新客户端的连接(得到套接字，得到客户端地址)
        new_socket, client_addr = tcp_server_socket.accept()
        # 5 为这个客户端进行服务
        srv_client = multiprocessing.Process(target=service_client, args=(new_socket,))
        srv_client.start()
        new_socket.close()
    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()