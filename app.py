# from website import create_app

# if __name__ == '__main__':
#     app.run(debug=True)

# # import time

# # import redis
# from flask import Flask

# app = create_app()
# # cache = redis.Redis(host='redis', port=6379)


# @app.route('/')
# def hello():
#     # count = get_hit_count()
#     return 'Hello World!'

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)