#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 19:23
# @Author  : debugfeng
# @Site    : 
# @File    : scheduler.py
# @Software: PyCharm


from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class Scheduler:
    scheduler: AsyncIOScheduler = None

    @classmethod
    def init(cls, scheduler):
        cls.scheduler = scheduler

    @classmethod
    def start(cls):
        cls.scheduler.start()

    @classmethod
    def remove(cls, plan_id: str):
        cls.scheduler.remove_job(str(plan_id))

    @classmethod
    def add_test_plan(cls, func, plan_id, plan_name, cron):
        return cls.scheduler.add_job(
            func=func, args=(plan_id,), name=plan_name, id=str(plan_id), trigger=CronTrigger.from_crontab(cron)
        )

    @classmethod
    def edit_test_plan(cls, func, plan_id, plan_name, cron):
        job = cls.scheduler.get_job(str(plan_id))
        if job is None:
            return cls.add_test_plan(func, plan_id, plan_name, cron)

        cls.scheduler.modify_job(job_id=str(plan_id), trigger=CronTrigger.from_crontab(cron), name=plan_name)
        cls.scheduler.pause_job(str(plan_id))
        cls.scheduler.resume_job(str(plan_id))


if __name__ == '__main__':
    print(CronTrigger.from_crontab('0 0 1-15 5 *'))
