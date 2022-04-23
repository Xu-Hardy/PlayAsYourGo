import psutil
from rest_framework.decorators import api_view
from rest_framework.response import Response


def cpu():
    cpuTimes = psutil.cpu_times()
    # 获取CPU信息中的内存信息
    def memoryInfo(memory):
        print(memory)
        return {
            '总内存(total)': str(round((float(memory.total) / 1024 / 1024 / 1024), 2)) + "G",
            '已使用(used)': str(round((float(memory.used) / 1024 / 1024 / 1024), 2)) + "G",
            '空闲(free)': str(round((float(memory.free) / 1024 / 1024 / 1024), 2)) + "G",
            '使用率(percent)': str(memory.percent) + '%',
            '可用(available)': (memory.available) if hasattr(memory, 'available') else '',
            '活跃(active)': (memory.active) if hasattr(memory, 'active') else '',
            '非活跃(inactive)': (memory.inactive) if hasattr(memory, 'inactive') else '',
            '内核使用(wired)': (memory.wired) if hasattr(memory, 'wired') else ''
        }
    return {
        '物理CPU个数': psutil.cpu_count(logical=False),
        '逻辑CPU个数': psutil.cpu_count(),
        'CPU使用情况': psutil.cpu_percent(percpu=True),
        '虚拟内存': memoryInfo(psutil.virtual_memory()),
        '交换内存': memoryInfo(psutil.swap_memory()),
        '系统启动到当前时刻': {
            pro: getattr(cpuTimes, pro) for pro in dir(cpuTimes) if pro[0:1] != '_' and pro not in ('index', 'count')
        },
    }


def disk():
    disk_info = {

    }
    return disk_info


def meomory():
    meomory_info = {

    }
    return meomory_info

@api_view(['GET'])
def pc(request):
    pc_info = {
        'cpu': cpu(),
        'disk': disk(),
        'meomory': meomory()
    }
    return Response(pc_info)