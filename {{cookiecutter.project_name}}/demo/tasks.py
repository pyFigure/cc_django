from celery import shared_task


@shared_task()
def long_time_task(x: int, y: int) -> int:
    """
    假如这是个长时间执行的任务
    @param x: 加数 x
    @param y: 加数 y
    @return:  相加结果
    """
    return x + y
