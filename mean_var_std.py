import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    array_np = np.array(list)
    array3 = array_np.reshape((3,3))

    def calculation(a: np.array, func_np) -> list:
        axis0 = func_np(a, axis= 0).tolist()
        axis1 = func_np(a, axis= 1).tolist()
        flat = func_np(a)

        return [axis0, axis1, flat]

    calculated = {
        'mean': calculation(array3, func_np= np.mean)
        ,'variance': calculation(array3, func_np= np.var)
        ,'standard deviation': calculation(array3, func_np= np.std)
        ,'max': calculation(array3, func_np= np.max)
        ,'min': calculation(array3, func_np= np.min)
        ,'sum': calculation(array3, func_np= np.sum)
    }
    return calculated
