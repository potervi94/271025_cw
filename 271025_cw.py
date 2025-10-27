# -*- coding: utf-8 -*-
import redis

def main() -> None:
    # Підключення до локального Redis
    server = redis.Redis(host="localhost", port=6379, decode_responses=True)

    # Встановити значення
    server.set(name="name", value="Anton2")

    # Прочитати значення і вивести
    value = server.get("name")
    print(f"name={value}")

if __name__ == "__main__":
    main()
