import asyncio


def iscoroutinefunction(func):
    return asyncio.iscoroutinefunction(func)


def markcoroutinefunction(func):
    return func


def sync_to_async(func, **kwargs):
    async def wrapper(*args, **kwds):
        return func(*args, **kwds)

    return wrapper


def async_to_sync(func, **kwargs):
    def wrapper(*args, **kwds):
        result = func(*args, **kwds)
        if asyncio.iscoroutine(result):
            return asyncio.run(result)
        return result

    return wrapper


class ThreadSensitiveContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False
