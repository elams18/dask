from pandas import Series
def _raise_if_object_series(funcname):
    """
    Utility function to raise an error if an object column does not support
    a certain operation like `mean`.
    """
    if isinstance(Series) and hasattr("dtype") and x.dtype == object:
        raise ValueError("`%s` not supported with object series" % funcname)
_raise_if_object_series("mode")