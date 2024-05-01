import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    array_np = np.array(list)
    array3 = array_np.reshape((3,3))

    def calc_mean(a: np.array) -> list:
        axis0 = np.mean(a, axis= 0).tolist()
        axis1 = np.mean(a, axis= 1).tolist()
        flat = np.mean(a)

        return [axis0, axis1, flat]

    def calc_var(a: np.array) -> list:
        axis0 = np.var(a, axis= 0).tolist()
        axis1 = np.var(a, axis= 1).tolist()
        flat = np.var(a)

        return [axis0, axis1, flat]

    def calc_std(a: np.array) -> list:
        axis0 = np.std(a, axis= 0).tolist()
        axis1 = np.std(a, axis= 1).tolist()
        flat = np.std(a)

        return [axis0, axis1, flat]

    def calc_max(a: np.array) -> list:
        axis0 = np.max(a, axis= 0).tolist()
        axis1 = np.max(a, axis= 1).tolist()
        flat = np.max(a)

        return [axis0, axis1, flat]

    def calc_min(a: np.array) -> list:
        axis0 = np.min(a, axis= 0).tolist()
        axis1 = np.min(a, axis= 1).tolist()
        flat = np.min(a)

        return [axis0, axis1, flat]

    def calc_sum(a: np.array) -> list:
        axis0 = np.sum(a, axis= 0).tolist()
        axis1 = np.sum(a, axis= 1).tolist()
        flat = np.sum(a)

        return [axis0, axis1, flat]

    calculation = {
        'mean': calc_mean(array3)
        ,'variance': calc_var(array3)
        ,'standard deviation': calc_std(array3)
        ,'max': calc_max(array3)
        ,'min': calc_min(array3)
        ,'sum': calc_sum(array3)
    }
    return calculation
