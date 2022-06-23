from utils.common import read_json_time_series

def interpolation(data, config):
    if config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data


def linear_interpolation(data ,config):
    data = read_json_time_series(data, config)
    data = interpolation(data, config)
    data = data.to_json()
    return data


